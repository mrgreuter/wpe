import re
import os

def logtolist(filename: str) -> dict:
    
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

    log_list = []
    # for tests
    content = filename.getvalue()
    content = content.strip('\n')
    file_content_list = (content).split('\n')
    
    for line in file_content_list:
        valid_log_line = re.search(compiled_log_line_pattern, line)
        if valid_log_line:
            log_list.append({
                "ip_address" : valid_log_line.group('ip_address'),
                "timestamp" : valid_log_line.group('timestamp'),
                "request" : valid_log_line.group('request'),
            })
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