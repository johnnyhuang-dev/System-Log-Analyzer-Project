
# Test Coverage

This document shows additional testing I added to give full or almost full coverage of the program. To test almost everything that could be tested, both automated tests (pytest) and manual tests for the user interface will be used. With these tests, one can be confident that the program works the way it should with proper user inputs.

---

1) Additional Automated Tests (pytest).  

I increased the number of pytests so that every logic function is covered. By making these, not only normal scenarios are tested, but also all edge cases, invalid inputs, empty information, and possible situations with bugs.   

**Logic functions and their cases**:   

**read_log() –**

* Reads a normal file with many lines
* Reads an empty file
* Handles file with blank lines and normal lines
* Handles file with only blank lines

**log_elements_list() –**

* Correctly separates a valid log with 4 parts
* Handles logs with extra spaces
* Handles logs with long messages
* Handles logs with colons in their message
* Handles logs with brackets in their message
* Handles logs with lowercase type names

**count_log_types() –**

* Correctly counts multiple log types
* Works with repeated types
* Works with only one type
* Returns `[]` for empty input
* Handles multiple logs that don't include one type of log

**detect_threat() –**

* Detects multiple threat entries
* Detects a single threat entry
* Works with no threat entries
* Works when threat keywords in threat logs contain lower/uppercase
* Detects threat log with multiple threat keywords, but only returns this threat log one time
* Detects words similar to threat keywords

**write_summary() –**

* Correctly writes counts to file
* Correctly writes threat entries
* Works with no threats
* Works with empty logs
* Handles threat logs with different lower/upper cases
* Produces consistent summary formatting
* Overwrites existing files contents

For `write_summary()`, the tests read the file after the summary is complete and compare the actual text with the expected result.

---

2) Manual Test Cases (For the UI)

Please follow the following steps and confirm the user interface works correctly. These tests don't check logic, just how the program handles input, prints messages, errors, and creates files.

**Test Case 1 - Normal Usage**

1. Run the main program (main.py file) through Run button at top-right corner, or type in "python main.py" in the Terminal area on the bottom part of the screen
2. Enter either "y" or "Y" for the first input question on the terminal
3. Confirm the program prints messages in the Terminal that confirm the log summary's completion
4. Search for "summary.txt" file and confirm it was created with info inside

**Expected result:** summary file is created and terminal displays confirmation messages.

---

**Test Case 2 – Normal Usage (Cancelled)**

1. Run the main (main.py file) through Run button at top-right corner, or type in "python main.py" in the Terminal area on the bottom part of the screen
2. Enter either "n" or "N" for the first input question on the terminal
3. Confirm the program prints messages in the Terminal that ask you (user) to upload necessary info and restart the program

**Expected result:** program stops running for user to restart.

---

**Test Case 3 – Normal Usage (Invalid First Input)**

1. Run the main (main.py file) through Run button at top-right corner, or type in "python main.py" in the Terminal area on the bottom part of the screen
2. Enter any character or number that is **not** "y", "Y", "n", nor "N" for the first input question on the terminal
3. Confirm the program prints messages in the Terminal that ask you (user) to try again and enter a valid input
4. Enter another invalid input and confirm it keeps asking to re-enter a valid input
5. Enter a valid input "y", "Y", "n", or "N" and confirm the program runs as expected from Test Case 1 or Test Case 2

**Expected result:** program keeps running and asking for valid input until a valid input is entered for the first question in Terminal.

---

**Test Case 4 – Overwrite test**

1. Repeat all of **Test Case 1** steps
2. Confirm information summarized in the "summary.txt" file
3. Find and open "uploaded_logs.txt" file
4. Delete one or a couple lines/logs 
5. Repeat all of **Test Case 1** steps
6. Confirm the contents of the summary file changed and updated

**Expected:** summary file is overwritten without problems.

---

**Test Case 5 – Special characters**

1. Find and open "uploaded_logs.txt" file
2. Put odd or special symbols in one log entry while keeping appropriate formatting
3. Run the program (main.py) same way as **Test Case 1**
4. Confirm program handles odd logs without crashing as long as format is correct

**Expected:** UI handles it normally without crashing.

---

**Test Case 6 – Empty log file**

1. Find and open "uploaded_logs.txt" file
2. Delete all contents (if want to reset this txt file, save the previous default text elsewhere)
3. Run the program (main.py) same way as **Test 1**
4. Confirm on Terminal that it prints confirmation messages for the summary file
5. Confirm in the "summary.txt" file that all numerical values given are 0

**Expected result:** summary file should show zero counts and no threats.

---

**Test Case 7 – Log file with incorrectly formatted logs**

1. Find and open "uploaded_logs.txt" file
2. Change contents to one or more invalid logs (improper format)
3. Run the program (main.py) same way as **Test 1**
4. Confirm the program displays error messages in the Terminal and stops working

**Expected:** the program stops and displays automatic error messages to prompt user to change to correctly formatted logs.

---

4) How to Run All Automated Tests

To run all automated logic tests, please write and enter on the Terminal:

```
pytest test_analyzer.py
```

To run with more detailed output:

```
pytest --verbose test_analyzer.py
```

---

5) Coverage Achievements

With all these automated pytests and manual tests, the whole project is almost fully tested and I can confidently say it works as it should.

* **Automated tests:** check that the logic is always correct for valid inputs
* **Manual tests:** checks that the UI works as expected for real users, whether with valid or invalid inputs

High confidence is achieved in that the program will work almost all the time a user tries it out appropriately. Though the program was not built to take inputs with incorrect formatting, testing it and instructing users to only give valid inputs (logs) makes the program less complex and work more effectively. Thus, assumptions were made about users always inputting correctly formatted logs.