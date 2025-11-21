#File with all the program's analysis functions

def log_elements_list(log):
    """Takes in log line and splits it into its components/elements"""
    date_time = (log.split("]", 1)[0]).split()
    date = date_time[0].replace("[", "")
    time = date_time[1].strip()

    name_msg = (log.split("]", 1)[1]).split(":", 1)
    name = name_msg[0].strip()
    message = name_msg[1].strip()

    log_elements = [date, time, name, message]
    
    return log_elements

def count_log_types(logs):
    """Counts how many of each type of log were recorded"""
    info_count = 0
    error_count = 0
    warning_count = 0
    
    if logs == []:
        return [0,0,0]

    for line in logs:
        log_type = log_elements_list(line)[2]
        if log_type == "INFO":
            info_count += 1
        elif log_type == "ERROR":
            error_count += 1
        elif log_type == "WARNING":
            warning_count += 1
    
    counts = [info_count, error_count, warning_count]

    return counts

def detect_threat(logs):
    """Takes in list of logs and checks which logs contain potential 
    threats by performing threat keyword detection on each log,
    then returns array of logs signaling potential threats."""

    threat_keywords = ["error", "fail", "denied", "unauthorized", "malware", "attack"]
    threat_logs = []

    if logs == []:
        return threat_logs
    
    for log in logs:
        for word in threat_keywords:
            if word in log.lower():
                threat_logs.append(log)
                break
    
    print(threat_logs)

    return threat_logs