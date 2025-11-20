from main import read_log
from main import write_summary
from analysis_functions import log_elements_list
from analysis_functions import count_log_types
from analysis_functions import detect_threat
import pytest

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
    assert read_log("test_logs.txt") == logs