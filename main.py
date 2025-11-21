#main file / interface of a log analyzer of a system
#want to make a summarizer for a system's logs
#txt files contain example system logs
from analysis_functions import read_log
from analysis_functions import write_summary

def main():
    """Main function to run the analyzer and summarize logs"""
    print("\nSimple Log Analyzer\n")
    print("Please upload the system logs to analyze in the \"uploaded_logs.txt\" file.")
    is_valid = False #temporary False value of input validity
    
    #loop until input validity is set to True
    while is_valid == False:
        #ask user if ready or not to get summary of logs
        ready = input("Ready to proceed? (Enter y or n): ").strip()

        #if respond y or Y, then ready to get summary, 
        #run program, confirm summary completion, then stop asking input
        if ready == "y" or ready == "Y":
            #read logs file and get list of logs
            logs = read_log("uploaded_logs.txt")
            #write summary of logs
            write_summary("summary.txt", logs)
            print("\nYour log summary has been completed.")
            print("Please proceed to and open the \"summary.txt\" file.")
            is_valid = True

        #else if respond n or N, then not ready to get summary, stop program
        elif ready == "n" or ready == "N":
            print("\nPlease restart the program once your logs are uploaded to the \"uploaded_logs.txt\" file.")
            is_valid = True

        #for all other responses, ask for valid input, don't stop program
        else:
            print("\nPlease enter a \'y\' or \'n\' character.")

if __name__ == "__main__":
    main()