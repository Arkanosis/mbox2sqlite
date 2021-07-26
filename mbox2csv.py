#! /usr/bin/env python3

import sys

print(f'size\tbehalf\tsender\tlist\tsubject')

with open('/tmp/gmail.mbox') as mbox:
    start = 0
    line = mbox.readline()
    while True:
        headers = {}
        while True:
            line = mbox.readline()
            if not line:
                sys.exit(0)
            if line == '\n':
                break
            if ': ' in line:
                header = line.rstrip().split(': ', 1)
                value = ''
                if len(header) == 2:
                    value = header[1]
                headers[header[0].lower()] = value.lower()
            else:
                # TODO FIXME, append to the value of the previous line
                pass
        prev_line = '\n'
        content = ''
        while True:
            line = mbox.readline()
            if not line:
                sys.exit(0)
            if prev_line == '\n' and line.startswith('From '):
                break
            content += prev_line
            prev_line = line
        pos = mbox.tell()
        size = pos - start
        for header in ['from', 'sender', 'list-id']:
            if header in headers and headers[header]:
                value =  headers[header]
                lcpos = value.find('<')
                if lcpos != -1:
                    rcpos = value.find('>')
                    if rcpos > lcpos:
                        value = value[lcpos+1:rcpos]
                value = value.replace('"', '')
                headers[header] = value
            else:
                headers[header] = '?'
        if 'subject' in headers:
            headers['subject'] = headers['subject'].replace('"', "''")
        else:
            headers['subject'] = '?'
        print(f'{size}\t{headers["from"]}\t{headers["sender"]}\t{headers["list-id"]}\t"{headers["subject"]}"')
        start = pos
