import re
import os
from collections import defaultdict

def get_log_content(input_data: str) -> str:

    content = ''
    # check if input data is a stringio object;
    if hasattr(input_data, 'getvalue'):
        content = input_data.getvalue()
    else:
        with open(input_data) as logfile:
            content = logfile.readlines()
    
    if content == '\n':
        return []
    content = content.strip('\n')
    if content == '':
        return []
    else:
        return content.split('\n')

def parse_log_line(line: str) -> dict:
    pass



def logtolist(filename: str) -> dict:
    
    log_file_content_as_list = get_log_content(filename)
    if log_file_content_as_list == '':
        return []

    field_names = ("ip_address", "timestamp", "request")
    error_messages = {
        "ip_address": "No IP address found",
        "timestamp": "No timestamp found",
        "request": "No request found"
    }
    log_line_dict = defaultdict(list, 
                                { key: f"{error_messages[key]}" 
                                for key in field_names })
    log_list = []
    # for tests
    
    for line in log_file_content_as_list:

        log_line_pattern = r'''^(?P<ip_address>.*?)\s
                                        (.*?)\s
                                        (.*?)\s
                                        \[(?P<timestamp>.*?)\]\s
                                        "(?P<request>.*?)"\s
                                        (.*?)\s
                                        (.*?)\s
                                        "(.*?)"\s
                                        "(.*?)"'''
        compiled_log_line_pattern = re.compile(log_line_pattern)
        ip_log_pattern = r'\d+.\d+.\d+.\d+'
        compiled_ip_log_pattern = re.compile(ip_log_pattern)
        timestamp_log_pattern = r'\d+/\w+/\d+:\d+:\d+:\d+\s\+\d+'
        compiled_timestamp_log_pattern = re.compile(timestamp_log_pattern)
        request_log_pattern = r'"GET.*?"'
        compiled_request_log_pattern = re.compile(request_log_pattern)

        valid_log_line = re.search(compiled_log_line_pattern, line)
        new_log_line = log_line_dict

        if valid_log_line:
            new_log_line['ip_address'] = valid_log_line.group('ip_address')
            new_log_line['timestamp'] = valid_log_line.group('timestamp')
            new_log_line['request'] = valid_log_line.group('request')
            log_list.extend(new_log_line)
        else:
            ip_address = re.search(compiled_ip_log_pattern, line)
            if ip_address:
                ip_address = ip_address.group(0)
            else:
                ip_address = "No IP address found"
            
            timestamp = re.search(compiled_timestamp_log_pattern, line)
            if timestamp:
                timestamp = timestamp.group(0)
            else:
                timestamp = "No timestamp found"
            
            request = re.search(compiled_request_log_pattern, line)
            if request:
                request = request.group(0)[1:-1]
            else:
                request = "No request found"

            log_list.append({"ip_address": ip_address, 
                            "timestamp": timestamp, 
                            "request": request})
    return log_list