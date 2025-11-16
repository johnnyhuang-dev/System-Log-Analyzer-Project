#main file / interface of a log analyzer of a system
#want to make a summarizer for a system's logs
#txt files contain example system logs

def read_log(log_file):
    """Reads each log in the system's logs txt file and stores it in array"""
    logs = []
    with open(log_file, "r") as infile:
        log = infile.readline().strip()
        while log != "":
            logs.append(log)
            log = infile.readline().strip()
        infile.close()
    return logs

def log_elements_list(log):
    """Takes in log line and splits it into its components/elements"""
    date_time = (log.split("] ")[0]).split()
    date = date_time[0].replace("[", "")
    time = date_time[1]

    name_msg = (log.split("] ")[1]).split(": ")
    name = name_msg[0]
    message = name_msg[1]

    log_elements = [date, time, name, message]
    
    print(log_elements)
    return log_elements

def write_summary(summary_file, logs):
    """Summarizes the system's logs into a txt file"""

    outfile = open(summary_file, "w")
    for line in logs:
        log_type = log_elements_list(line)[2]
        outfile.write(log_type)
        outfile.write("\n")
    outfile.close()

def main():
    """Main function to run the analyzer and summarize logs"""
    
    logs = read_log("system_logs.txt")
    
    print(logs)

    write_summary("summary.txt", logs)

if __name__ == "__main__":
    main()