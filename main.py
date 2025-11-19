#main file / interface of a log analyzer of a system
#want to make a summarizer for a system's logs
#txt files contain example system logs
from analysis_functions import count_log_types
from analysis_functions import detect_threat

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
    counts = count_log_types(logs)
    threat_logs = detect_threat(logs)

    outfile = open(summary_file, "w")
    outfile.write("NUMBER OF LOGS PER TYPE\n")
    outfile.write(f"INFO: {counts[0]}\n")
    outfile.write(f"ERROR: {counts[1]}\n")
    outfile.write(f"WARNING: {counts[2]}\n\n")

    outfile.write("POTENTIAL THREATS DETECTED\n")
    if threat_logs == []:
        outfile.write("0 Threats Detected.")
    else:
        outfile.write("The following logs may signal potential threats: \n")
        for log in threat_logs:
            outfile.write(f"{log}\n")
    outfile.close()

def main():
    """Main function to run the analyzer and summarize logs"""
    print("\nSimple Log Analyzer\n")
    print("Please upload the system logs to analyze in the \"uploaded_logs.txt\" file.")
    is_valid = False
    while is_valid == False:
        ready = input("Ready to proceed? (Enter y or n): ").strip()
        if ready == "y" or ready == "Y":
            logs = read_log("uploaded_logs.txt")
            write_summary("summary.txt", logs)
            print("\nYour log summary has been completed.")
            print("Please proceed to and open the \"summary.txt\" file.")
            is_valid = True
        elif ready == "n" or ready == "N":
            print("\nPlease restart the program once your logs are uploaded to the \"uploaded_logs.txt\" file.")
            is_valid = True
        else:
            print("\nPlease enter a \'y\' or \'n\' character.")
    
if __name__ == "__main__":
    main()