import re
import sys
import os

def filter_log_content(log_file_content: str) -> list:
    """clean log data"""
    if log_file_content == ['\n']:
        return []
    return log_file_content

def parse_log_line(line: str) -> dict:
        """parse log line and return new log line dictionary"""
        field_names = ("ip_address", "timestamp", "request")
        error_messages = {
            "ip_address": "No IP address found",
            "timestamp": "No timestamp found",
            "request": "No request found"
        }
        new_log_line = { key: f"{error_messages[key]}" for key in field_names }

        ip_log_pattern = r'.*?(?P<ip_address>\d+.\d+.\d+.\d+).*'
        timestamp_log_pattern = r'.*?(?P<timestamp>\d+/\w+/\d+:\d+:\d+:\d+\s\+\d+).*'
        request_log_pattern = r'.*?"(?P<request>GET.*?)".*'

        ip_address = re.search(ip_log_pattern, line)
        if ip_address:
            new_log_line['ip_address'] = ip_address.group('ip_address')
        
        timestamp = re.search(timestamp_log_pattern, line)
        if timestamp:
            new_log_line['timestamp'] = timestamp.group('timestamp')
        
        request = re.search(request_log_pattern, line)
        if request:
            new_log_line['request'] = request.group('request')

        return new_log_line

def logtolist(input_data: str) -> dict:
    """parse logfile and return list with log lines"""
    log_file_content = filter_log_content(input_data.readlines())
    position_index = 0
    for line in log_file_content:
        log_file_content[position_index] = parse_log_line(line)
        position_index += 1
    return log_file_content

if __name__ == '__main__':
    filename = sys.argv[1]
    script_path = os.path.dirname(__file__)
    full_file_path = os.path.join(script_path, filename)
    with open(full_file_path) as logfile:
        result = logtolist(logfile)
    print(result)