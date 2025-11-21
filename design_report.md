
# Design Report

1) **Introduction**:   
A system's log history is always too long for any human being to possibly analyze and/or summarize.   
People need software and programs that can read through all logs and summarize relevant information.   
The objective of this project is to build a system log analyzer that can fulfill these needs.

2) **Design**:   
I designed the software using small functions for each little thing that the program should compute or do. Instead of putting everything together in one big piece of code, I decided to make each function do a single job. It makes the program easier to understand, debug, and test.   
For example, I created some separate functions like:   
- read_log() – reads the log file and returns a list with each lines.  
- log_elements_list() – separates a single log entry into elements.  
- count_log_types() – counts how many of each log type occur.  
- detect_threat() – looks through logs to find threat logs.  
- write_summary() – writes the summary text file    
These functions are pure logic since they don't print anything or ask or user input. They just take in data and return data. This is separated from the code and functions that deal with the UI.   
The UI is only handled by the main() function in the main.py file.
All user input (like asking if they're ready or not for the summary) and prints (like telling the user the summary is done) are stored separate from the logic in the main.py file. This separation makes it easy to run pytests on the logic functions without manually typing anything.   
For example, the logic file called analysis_functions.py has the function:   
```python
    def read_log(log_file):
    """Reads each log in the system's logs txt file and stores it in array"""
    logs = []
    with open(log_file, "r") as infile:
        for log in infile:
            stripped_log = log.strip()
            if stripped_log != "":
                logs.append(stripped_log)
        infile.close()
    return logs
```  
Meanwhile, the UI file called main.py with function main() does things like:
```python
ready = input("Ready to proceed? (Enter y or n): ").strip()
```  
The logic functions only deal with actual operations and computations behind the screens, while the main UI function main() just deals with the inputs, prints, etc. that the user can interact with and see.


3) **Design Highlights**:   
One thing I am proud of is how  was able to organize the function quite well. Each function does only one job, which made the whole program feel much cleaner, smoother, and easier to read/edit. I also like that I separated the logic functions from the interface by making separate files for each. That made writing tests much simpler.   
An area of complexity that I had to overcome to get the program working well was in the log_elements_list() function. I had to find a way to separate a string with the correct log format into each of its components, returned as a list. To do that, I tried the split() function that we learned in class, did some online research, and discovered that I could use that method to split a log string into elements by splitting through the key separators. For example, one of those separators were "]" that separated the log's date-time section from the name-message section. From then on, I was able to figure out how to properly divide each log and return a list with the log's elements.   
This is how the code for the log_elements_list() function ended up looking when retrieving only the time and date from the log:
```python
    #split "[<date> <time>]" from "<type>: <message>" in the log line, 
    #take the "<date> <time>" element of the new array and split it into ["<date>", "<time>"]
    date_time = (log.split("]", 1)[0]).split()
    #set date to the "<date>" element of the date_time array and replace "[" with blank
    date = date_time[0].replace("[", "")
    #set time to the "<time>" element of date_time array
    time = date_time[1].strip()
```
It's my creative way of using split methods to strategically split a log's string into half and then re-splitting the first half into the date and time components. A similar process was followed for retrieving the type and message of a log, successfully solving this challenging problem of element separation.

4) **Areas for Improvement**:   
If I had more time, I would improve the program's flexibility in terms of its inputs and outputs. For now, the log format s very specific, so if a user uses a slightly different format, the program ight not work properly. I also want to improve the program's error handling. For example, if someone enters invalid logs into uploaded_logs.txt, the program could give users a chance to re-input their logs instead of creashing. Another thing I would like to add/change is a more detailed summary, such as sorting by log types or giving recommendations based on the threats detected.

5) **Lessons Learned**:   
Working on this small project taught me that if I organize things into small functions, it makes everything easier.   
In the beginning, it felt like a slow and tedious process. However, after a while it saves a lot of time because you   don’t get confused with your own code. I also learned about how important it was to separate logic from the user interface. Testing logic functions became much easier as it was all separated into pieces. If the logic functions were filled with print methods, writing pytests would have been challenging (maybe impossible).
I realized that it is essential to think about data formats, unexpected scenarios, and errors. Logs often have many different formats, so the program has to deal with that properly. Overall, I learned to plan better, organize my code, and write functions that make the project easier to maintain and test.