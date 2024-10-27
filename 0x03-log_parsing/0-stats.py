#!/usr/bin/python3
'''A script for parsing HTTP request logs and computing metrics.
'''
import re
import sys


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.

    Args:
        input_line (str): A single line from the log file.

    Returns:
        dict: Parsed data from the log line.
    '''
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\]\s*',
        r'\"(?P<request>GET \/projects\/260 HTTP\/1\.1)\"\s*',
        r'(?P<status_code>\d+)\s*',
        r'(?P<file_size>\d+)'
    )
    log_fmt = '{}\\-{}{}{}\\s*'.format(log_pattern[0], log_pattern[1], log_pattern[2], log_pattern[3], log_pattern[4])
    match = re.fullmatch(log_fmt, input_line)
    
    if match is not None:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size')),
        }
    return None


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total size of all files in the log.
        status_codes_stats (dict): A dictionary containing status codes and their counts.
    '''
    print(f'File size: {total_file_size}')
    for code in sorted(status_codes_stats):
        if status_codes_stats[code] > 0:
            print(f'{code}: {status_codes_stats[code]}')


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log line.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): A dictionary of status codes and their counts.

    Returns:
        int: The updated total file size.
    '''
    line_info = extract_input(line)
    
    if line_info is not None:
        status_code = line_info['status_code']
        file_size = line_info['file_size']
        if status_code in status_codes_stats:
            status_codes_stats[status_code] += 1
        total_file_size += file_size

    return total_file_size


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {code: 0 for code in ['200', '301', '400', '401', '403', '404', '405', '500']}
    
    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break

            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            line_num += 1

            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)

    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)
        sys.exit(0)


if __name__ == '__main__':
    run()
