import re
from collections import defaultdict
import os

def logtolist(filename: str) -> dict:
    log_pattern = '^(?P<ip>.*?)\s(.*?)\s(.*?)\s\[(?P<timestamp>.*?)\]\s"(?P<request>.*?)"\s(?P<http_status_code>.*?)\s(?P<size>.*?)\s"(.*?)"\s"(?P<user_agent>.*?)"'
    compiled_log_pattern = re.compile(log_pattern)
    log_list = []
    # for tests
    if hasattr(filename, 'getvalue'):
        line_count = 0
        for line in filename.getvalue():
            line_count += 1
            line_match = re.search(compiled_log_pattern, line)
            if line_match:
                log_list.append({
                    "ip_address" : line_match.group('ip'),
                    "timestamp" : line_match.group('timestamp'),
                    "request" : line_match.group('request'),
                })
            else:
                log_list.append({})
    else:
        script_path = os.path.dirname(__file__)
        file_path = os.path.join(script_path, filename)
        with open(file_path) as log_file:
            line_count = 0
            for line in log_file:
                line_count += 1
                line_match = re.search(compiled_log_pattern, line)
                if line_match:
                    log_list.append({
                        "ip_address" : line_match.group('ip'),
                        "timestamp" : line_match.group('timestamp'),
                        "request" : line_match.group('request'),
                    })
                else:
                    print(f"\n!!! Log on line {line_count} not valid. Skipping line. !!!\n")
    return log_list