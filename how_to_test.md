
# How to Test

This documents walks through how to verify that the system log analyzer works as expected. In order to properly test this System Log Analyzer, please follow every step below:   

---

1) Automated Tests (pytest)

The automated tests focus solely on the logic functions. The user interface is dealt with later using manual testing. These pytests make sure the important functions compute things correctly when given different inputs.   

Right now, I have pytest tests for the most of the main functions in my program:   

Functions tested with pytest:

* `read_log()`
* `parse_entry()`
* `count_log_types()`
* `detect_threat()`
* `write_summary()` (tested by checking output file content)
   
**What the automated tests check**:

**read_log()**

* Reads file correctly
* Returns the correct number of lines
* Handles empty files

**log_elements_list()**

* Separates valid log line into the 4 parts

**count_log_types()**

* Counts each log type correctly
* Returns an empty list if no logs

**detect_threat()**

* Detects threat logs correctly
* Returns an empty list when there are no threats
* Works even when some entries have similar keywords

**write_summary()**

* Creates and opens the output file
* Writes the correct counts
* Lists all threats correctly

---

2) Manual Tests (User Interface)

Manual testing checks how the program prints outputs and how it responds to different user inputs. Follow these steps below to check that the UI works and that the user experience makes sense.   

**Manual Test Cases**

**Test 1 – Normal Usage**

1. Run the main (main.py file) through Run button at top-right corner, or type in "python main.py" in the Terminal area on the bottom part of the screen
2. Enter either "y" or "Y" for the first input question on the terminal
3. Confirm the program prints messages in the Terminal that confirm the log summary's completion
4. Search for "summary.txt" file and confirm it was created with info inside

**Expected result:** summary file is created with correct data.

---

**Test 2 – Normal Usage (Cancelled)**

1. Run the main (main.py file) through Run button at top-right corner, or type in "python main.py" in the Terminal area on the bottom part of the screen
2. Enter either "n" or "N" for the first input question on the terminal
3. Confirm the program prints messages in the Terminal that ask you (user) to upload necessary info and restart the program

**Expected result:** program stops running for user to restart.

---

**Test 3 – Empty log file**

1. Find and open "uploaded_logs.txt" file
2. Delete all contents (if want to reset this txt file, save the previous default text elsewhere)
3. Run the program (main.py) same way as **Test 1**
4. Confirm on Terminal that it prints confirmation messages for the summary file
5. Confirm in the "summary.txt" file that all numerical values given are 0

**Expected result:** summary file should show zero counts and no threats.

---

What manual testing shows

* The user (you) sees clear output (Terminal and summary file)
* The summary file is created appropriately
* The UI works as expected 

---

3) Running Automated Tests

To run all automated logic tests, please write and enter on the Terminal:

```
pytest test_analyzer.py
```
Confirm that the terminal shows all pytests passed (green lines).  
This means that every logic functions works correctly with the preset test inputs.   

Your environment only needs Python and pytest installed.

