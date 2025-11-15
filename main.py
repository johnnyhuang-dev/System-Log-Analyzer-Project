#main file / interface of a log analyzer of a system
#want to make a summarizer for a system's logs
#txt files contain example system logs

def read_log(log_file):
    """Function to read each log and store it in a list"""
    logs = []
    with open(log_file, "r") as infile:
        log = infile.readline().strip()
        while log != "":
            logs.append(log)
            log = infile.readline().strip()
        infile.close()
    return logs

def get_log_type(log):
    no_date_log = (log.split("] "))[1]
    log_sections = no_date_log.split(":")
    log_type = log_sections[0]
    print(log_type)
    return log_type

def write_summary(summary_file, logs):
    """Function for summarizing the system's logs into a txt file"""

    outfile = open(summary_file, "w")
    for i in logs:
        log_type = get_log_type(i)
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