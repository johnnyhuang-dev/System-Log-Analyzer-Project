from analysis_functions import log_elements_list
from analysis_functions import count_log_types
from analysis_functions import detect_threat
from main import read_log
from main import write_summary
import pytest
import os

# All Necessary Pytests for Every Function

def test_log_elements_list_valid_log():
    log = "[2025-11-12 10:00:01] INFO: System started"
    expected_elements = ['2025-11-12', '10:00:01', 'INFO', 'System started']
    assert log_elements_list(log) == expected_elements

def test_log_elements_list_valid_long_log():
    log = "[2025-10-01 09:00:00] WARNING: Disk space running low, affecting GPU speed"
    expected_elements = ['2025-10-01', '09:00:00', 'WARNING', 'Disk space running low, affecting GPU speed']
    assert log_elements_list(log) == expected_elements

def test_log_elements_list_valid_trailing_spaces():
    log = "     [2025-11-12     10:00:01]     INFO:     System started   "
    expected_elements = ['2025-11-12', '10:00:01', 'INFO', 'System started']
    assert log_elements_list(log) == expected_elements

def test_log_elements_list_valid_colon_in_message():
    log = "[2025-11-12 10:00:01] INFO: Download: Completed"
    expected_elements = ['2025-11-12', '10:00:01', 'INFO', 'Download: Completed']
    assert log_elements_list(log) == expected_elements

def test_log_elements_list_valid_bracket_in_message():
    log = "[2025-11-12 10:00:01] INFO: System status [Activated]"
    expected_elements = ['2025-11-12', '10:00:01', 'INFO', 'System status [Activated]']
    assert log_elements_list(log) == expected_elements

def test_log_elements_list_valid_lowercase_type_log():
    log = "[2025-11-12 10:00:01] info: System started"
    expected_elements = ['2025-11-12', '10:00:01', 'INFO', 'System started']
    assert log_elements_list(log) == expected_elements

# Not necessary to test for empty log input since this function
# is not called if log is empty.
# Not necessary to test for invalid input using pytests as program
# always assumes valid input with correct format from user.
# Manual tests can be done to test that it does not work with invalid input.

#------------------------------------------------------

def test_count_log_types_empty_list():
    assert count_log_types([]) == [0, 0, 0]

def test_count_log_types_single_info():
    logs = ["[2025-09-08 09:01:02] INFO: Something"]
    assert count_log_types(logs) == [1, 0, 0]

def test_count_log_types_single_error():
    logs = ["[2025-09-08 09:01:02] ERROR: Something bad"]
    assert count_log_types(logs) == [0, 1, 0]

def test_count_log_types_single_warning():
    logs = ["[2025-09-08 09:01:02] WARNING: Watch out"]
    assert count_log_types(logs) == [0, 0, 1]

def test_count_log_types_mixed():
    logs = [
        "[2025-09-08 09:01:02] INFO: ok",
        "[2025-09-08 09:01:03] ERROR: oops",
        "[2025-09-08 09:01:04] WARNING: careful",
        "[2025-09-08 09:01:05] INFO: again"
    ]
    assert count_log_types(logs) == [2, 1, 1]

def test_count_log_types_no_info():
    logs = [
        "[2025-09-08 09:01:02] ERROR: error",
        "[2025-09-08 09:01:03] WARNING: warn"
    ]
    assert count_log_types(logs) == [0, 1, 1]

def test_count_log_types_no_error():
    logs = [
        "[2025-09-08 09:01:02] INFO: a",
        "[2025-09-08 09:01:03] WARNING: b"
    ]
    assert count_log_types(logs) == [1, 0, 1]

def test_count_log_types_no_warning():
    logs = [
        "[2025-09-08 09:01:02] INFO: a",
        "[2025-09-08 09:01:03] ERROR: b"
    ]
    assert count_log_types(logs) == [1, 1, 0]

def test_count_log_types_many_info():
    logs = ["[2025-09-08 09:01:02] INFO: a"] * 50
    assert count_log_types(logs) == [50, 0, 0]

# As mentioned before, Manual Tests will be made for invalid input
# The program always assumes strict formatting of input logs

#------------------------------------------------------

def test_detect_threat_empty_list():
    assert detect_threat([]) == []

def test_detect_threat_no_threats():
    logs = ["[2024-09-08 09:01:02] INFO: System running normally"]
    assert detect_threat(logs) == []

def test_detect_threat_single_threat():
    logs = ["[2024-09-08 09:01:02] ERROR: Unauthorized access attempt"]
    assert detect_threat(logs) == logs

def test_detect_threat_multiple_mixed():
    logs = [
        "[2024-09-08 09:01:02] INFO: System is good",
        "[2024-09-08 09:01:02] WARNING: Disk fail imminent",
        "[2024-09-08 09:01:02] ERROR: Malware detected",
        "[2024-09-08 09:01:02] INFO: Normal activity",
    ]
    assert detect_threat(logs) == [
        "[2024-09-08 09:01:02] WARNING: Disk fail imminent",
        "[2024-09-08 09:01:02] ERROR: Malware detected",
    ]

def test_detect_threat_case_insensitive():
    logs = ["[2024-09-08 09:01:02] INFO: UNAUTHORIZED login detected"]
    assert detect_threat(logs) == logs

def test_detect_threat_multiple_keywords_one_log():
    logs = ["[2024-09-08 09:01:02] ERROR: Unauthorized malware attack detected"]
    assert detect_threat(logs) == logs

def test_detect_threat_similar_keyword():
    logs = ["[2024-09-08 09:01:02] ERROR: Login failed"]
    assert detect_threat(logs) == logs

# As mentioned before, Manual Tests will be made for invalid input
# The program always assumes strict formatting of input logs

#------------------------------------------------------

def test_read_log():
    """Test if program is reading the logs correctly, 
    assuming correctly formatted input from user."""
    expected = ["[2025-11-12 10:00:01] INFO: System started"]
    
    file = "test_file.txt"
    with open(file, 'w') as temp:
        temp.write(expected[0])
    
    assert read_log(file) == expected
    os.remove(file)

def test_read_log_empty():
    """Test if program is reading empty txt file correctly."""
    expected = []
    
    file = "test_file.txt"
    with open(file, 'w') as temp:
        temp.write("")
    
    assert read_log(file) == expected
    os.remove(file)

def test_read_log_with_blank_lines():
    """Tests file that contains blank lines that should not be included."""
    expected = ["[2025-11-12 10:00:01] INFO: System started", "[2025-11-12 10:00:01] INFO: System started"]
    
    file = "test_file.txt"
    with open(file, 'w') as temp:
        temp.write(
        "\n"
        "[2025-11-12 10:00:01] INFO: System started\n"
        "\n"
        "[2025-11-12 10:00:01] INFO: System started"
        "\n"
        )
    
    assert read_log(file) == expected
    os.remove(file)

def test_read_log_only_blank_lines():
    """Tests file that contains blank lines that should not be included."""
    expected = []
    
    file = "test_file.txt"
    with open(file, 'w') as temp:
        temp.write(
        "\n"
        "\n"
        "\n"
        )
    
    assert read_log(file) == expected
    os.remove(file)

def test_read_log_many_logs():
    """Test if program is reading the logs correctly, 
    assuming correctly formatted input from user."""
    expected = ["[2025-11-12 10:00:01] INFO: System started", 
                "2024-09-08 09:01:02] WARNING: UNAUTHORIZED login detected",
                "[2025-11-12 10:00:01] erRor: System started"
    ]
    
    file = "test_file.txt"
    with open(file, 'w') as temp:
        for i in expected:
            temp.write(i)
            temp.write("\n")
    
    assert read_log(file) == expected
    os.remove(file)

# As mentioned before, Manual Tests will be made for invalid input
# The program always assumes strict formatting of input logs

#------------------------------------------------------

def test_write_summary_no_threats():
    logs = [
        "[2025-11-12 10:00:01] INFO: System started",
        "[2025-10-01 09:00:00] WARNING: Disk space running low",
        "[2025-11-12 10:00:01] INFO: Download: Completed"
    ]

    outfile = "summary.txt"
    write_summary(outfile, logs)
    with open(outfile, 'r') as file:
        result = file.read().strip()

    expected = (
        "NUMBER OF LOGS PER TYPE\nINFO: 2\nERROR: 0\nWARNING: 1\n\nPOTENTIAL THREATS DETECTED\n0 Threats Detected.\n\nSummary Complete. Please restart the program once done."
    )

    assert result == expected

def test_write_summary_with_threats():
    logs = [
        "[2024-09-08 09:01:02] INFO: System is good",
        "[2024-09-08 09:01:02] WARNING: Disk fail imminent",
        "[2024-09-08 09:01:02] ERROR: Malware detected"
    ]

    outfile = "summary.txt"
    write_summary(outfile, logs)
    with open(outfile, 'r') as file:
        result = file.read().strip()

    expected = (
        "NUMBER OF LOGS PER TYPE\n"
        "INFO: 1\n"
        "ERROR: 1\n"
        "WARNING: 1\n\n"
        "POTENTIAL THREATS DETECTED\n"
        "The following logs may signal potential threats:\n"
        "[2024-09-08 09:01:02] WARNING: Disk fail imminent\n"
        "[2024-09-08 09:01:02] ERROR: Malware detected\n"
        "\n"
        "Summary Complete. Please restart the program once done."
    )

    assert result == expected

def test_write_summary_empty_logs():
    logs = []

    outfile = "summary.txt"
    write_summary(outfile, logs)
    with open(outfile, 'r') as file:
        result = file.read().strip()

    expected = (
        "NUMBER OF LOGS PER TYPE\n"
        "INFO: 0\n"
        "ERROR: 0\n"
        "WARNING: 0\n\n"
        "POTENTIAL THREATS DETECTED\n"
        "0 Threats Detected.\n"
        "\nSummary Complete. Please restart the program once done."
    )

    assert result == expected

def test_write_summary_mixed_case_threats():
    logs = [
        "[2024-09-08 09:01:02] WARNING: UNAUTHORIZED login detected",
        "[2025-11-12 10:00:01] erRor: System started"
    ]

    outfile = "summary.txt"
    write_summary(outfile, logs)
    with open(outfile, 'r') as file:
        result = file.read().strip()

    expected = (
        "NUMBER OF LOGS PER TYPE\n"
        "INFO: 0\n"
        "ERROR: 1\n"
        "WARNING: 1\n\n"
        "POTENTIAL THREATS DETECTED\n"
        "The following logs may signal potential threats:\n"
        "[2024-09-08 09:01:02] WARNING: UNAUTHORIZED login detected\n"
        "[2025-11-12 10:00:01] erRor: System started\n\n"
        "Summary Complete. Please restart the program once done."
    )

    assert result == expected

# As mentioned before, Manual Tests will be made for invalid input
# The program always assumes strict formatting of input logs