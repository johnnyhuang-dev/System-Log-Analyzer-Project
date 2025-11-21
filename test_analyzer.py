from analysis_functions import log_elements_list
from analysis_functions import count_log_types
from analysis_functions import detect_threat
from main import read_log
from main import write_summary
import pytest

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
    logs = []
    with open("test_logs.txt", "r") as infile:
        log = infile.readline().strip()
        while log != "":
            logs.append(log)
            log = infile.readline().strip()
        infile.close()
    assert read_log("test_logs.txt") == logs

def test_read_log_empty():
    """Test if program is reading empty txt file correctly."""
    logs = []
    assert read_log("test_empty_log.txt") == logs

