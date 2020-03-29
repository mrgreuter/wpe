import re

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

        field_names = ("ip_address", "timestamp", "request")
        error_messages = {
            "ip_address": "No IP address found",
            "timestamp": "No timestamp found",
            "request": "No request found"
        }
        new_log_line = { key: f"{error_messages[key]}" for key in field_names }

        ip_log_pattern = r'\d+.\d+.\d+.\d+'
        timestamp_log_pattern = r'\d+/\w+/\d+:\d+:\d+:\d+\s\+\d+'
        request_log_pattern = r'"GET.*?"'

        ip_address = re.search(ip_log_pattern, line)
        if ip_address:
            new_log_line['ip_address'] = ip_address.group(0)
        
        timestamp = re.search(timestamp_log_pattern, line)
        if timestamp:
            new_log_line['timestamp'] = timestamp.group(0)
        
        request = re.search(request_log_pattern, line)
        if request:
            new_log_line['request'] = request.group(0)[1:-1]

        return new_log_line

def logtolist(filename: str) -> dict:
    
    log_file_content_as_list = get_log_content(filename)
    log_list = []
    for line in log_file_content_as_list:
        log_list.append(parse_log_line(line))
    return log_list