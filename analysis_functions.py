#File with all the program's analysis/logic functions

def log_elements_list(log):
    """Takes in log line and splits it into its components/elements"""
    #split "[<date> <time>]" from "<type>: <message>" in the log line, 
    #take the "<date> <time>" element of the new array and split it into ["<date>", "<time>"]
    date_time = (log.split("]", 1)[0]).split()
    #set date to the "<date>" element of the date_time array and replace "[" with blank
    date = date_time[0].replace("[", "")
    #set time to the "<time>" element of date_time array
    time = date_time[1].strip()

    #split "[<date> <time>]" from "<type>: <message>" in the log line, 
    #take the "<type>: <message>" element of the new array and split it into ["<type>", "<message>"]
    name_msg = (log.split("]", 1)[1]).split(":", 1)
    #set type to the "<type>" element of name_msg array
    name = name_msg[0].strip().upper() 
    #set message to the "<message>" element of name_msg array
    message = name_msg[1].strip()

    #make a new array with the log's elements in order
    log_elements = [date, time, name, message]
    
    return log_elements

def count_log_types(logs):
    """Counts how many of each type of log were recorded"""
    #set all counts of each type to 0
    info_count = 0
    error_count = 0
    warning_count = 0
    
    #if no logs available, return 0 amounts of each log type
    if logs == []:
        return [0,0,0]
    
    #find the log type of each line and add upp counts for each type
    for line in logs:
        log_type = log_elements_list(line)[2]
        if log_type == "INFO":
            info_count += 1
        elif log_type == "ERROR":
            error_count += 1
        elif log_type == "WARNING":
            warning_count += 1

    #return list with each type's count 
    counts = [info_count, error_count, warning_count]
    return counts

def detect_threat(logs):
    """Takes in list of logs and checks which logs contain potential 
    threats by performing threat keyword detection on each log,
    then returns array of logs signaling potential threats."""
    #threat keywords to detect
    threat_keywords = ["error", "fail", "denied", "unauthorized", "malware", "attack"]
    
    #list to gather threat logs
    threat_logs = []

    #if no logs available, return empty list
    if logs == []:
        return threat_logs
    
    #for each log, check if any threat keyword appears
    #if log has threat keyword, add log to list of threat logs
    for log in logs:
        for word in threat_keywords:
            if word in log.lower():
                threat_logs.append(log)
                break

    return threat_logs

def read_log(log_file):
    """Reads each log in the system's logs txt file and stores it in array"""
    #list of logs
    logs = []

    #read file of logs and add each non-empty line(log) to list of logs
    with open(log_file, "r") as infile:
        for log in infile:
            #remove trailing spaces from each line(log) 
            stripped_log = log.strip()
            if stripped_log != "":
                logs.append(stripped_log)
        infile.close()
    return logs

def write_summary(summary_file, logs):
    """Summarizes the system's logs into a txt file"""
    #retrieve counts for each type of log
    counts = count_log_types(logs)
    #retrieve list of threat logs
    threat_logs = detect_threat(logs)

    #open the output summary.txt file to write
    outfile = open(summary_file, "w")

    #Write out first part of summary (Type Counts)
    outfile.write("NUMBER OF LOGS PER TYPE\n")
    outfile.write(f"INFO: {counts[0]}\n")
    outfile.write(f"ERROR: {counts[1]}\n")
    outfile.write(f"WARNING: {counts[2]}\n\n")

    #Write out second part of summary (Threats)
    outfile.write("POTENTIAL THREATS DETECTED\n")

    #if no threat logs available, write '0 Threats Detected'
    if threat_logs == []:
        outfile.write("0 Threats Detected.\n")
    
    #else write each threat log one by one
    else:
        outfile.write("The following logs may signal potential threats:\n")
        for log in threat_logs:
            outfile.write(f"{log}\n")

    #confirm summary completion
    outfile.write("\nSummary Complete. Please restart the program once done.")
    #close summary.txt file
    outfile.close()