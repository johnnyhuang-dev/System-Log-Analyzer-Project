#main file / interface of a log analyzer of a system
#want to make a summarizer for a system's logs
#txt files contain example system logs
from analysis_functions import count_log_types

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

def write_summary(summary_file, logs):
    """Summarizes the system's logs into a txt file"""
    outfile = open(summary_file, "w")
    counts = count_log_types(logs)
    outfile.write(f"INFO: {counts[0]}\n")
    outfile.write(f"ERROR: {counts[1]}\n")
    outfile.write(f"WARNING: {counts[2]}\n")
    outfile.close()

def main():
    """Main function to run the analyzer and summarize logs"""
    
    logs = read_log("system_logs.txt")
    
    print(logs)

    write_summary("summary.txt", logs)

if __name__ == "__main__":
    main()