
# Instructions

Welcome to the System Log Analyzer.

To use it effectively, please follow these 7 steps:

1. Have a list of system logs, each log in the exact format **[YYYY-MM-DD HH:MM:SS] INFOTYPE: MESSAGE**    
the program **will not work with logs or data of other formats**.   
For example: [2025-11-12 10:00:01] INFO: System started

2. Ensure your logs are in this format, **one log per line**.   
For example:   
[2025-11-12 10:00:01] INFO: System started  
[2025-11-12 10:00:05] WARNING: Unauthorized login  
[2025-11-12 10:00:08] ERROR: Unsuccessful port access

3. Ensure your logs are of one of these three types of logs:   
**INFO**  
**WARNING**  
**ERROR**  
    
    Otherwise, the program **won't count** the logs of other different types. For example:   
    Valid: [2025-11-12 10:00:01] **INFO**: System started    
    Invalid: [2025-11-12 10:00:01] **DATA**: System started 

4. Upload / copypaste your logs into the "**uploaded_logs.txt**" file.

5. Open the "**main.py**" file.

6. Run the program by typing "**python main.py**" in the bottom Terminal (or bash shell), or press **Run** button at the top-right corner.

7. Follow instructions carefully from the Terminal to see log analysis.

8. If you want to test the program s working correctly, follow instructions in the "**how_to_test.md**" file, then continue with tests from "**test_coverage.md**" file.