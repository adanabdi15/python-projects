#!/usr/bin/env python3
import re

def test_regular_expression(regex, test_string) :
    pattern = re.compile(r'' + regex )
    match   = pattern.search(test_string)
    if match :
        try :
            return match.group(1)
        except :
            print('Match found but no substring returned')
            return ''
    else:
        print(regex, 'does not match', test_string)
        return ''

line_1 = 'Mar  xxxxx16xxxxxxx 11:58:13 xxxxxxxxxxxxxxx 65.96.149.57 port 60695    Wed'
line_2 = ' 205.236.184.32  09 Feb 2014:00:03:21 +0000 12_class_notes_it117.html HTTP/1.1" 200 56810323'

regex_1  = r'^([A-Z][a-z]{2})'
regex_2  = r'^.{3}\s+x{5}(\d{2})'
regex_3  = r'\s(\d{2}:\d{2}:\d{2})\s'
regex_4  = r'\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s'
regex_5  = r'port\s+(\d+)'
regex_6  = r'\s+([A-Z][a-z]{2})$'
regex_7  = r'\s(\d{2})\s[A-Z][a-z]{2}\s\d{4}:'
regex_8  = r'\s\d{2}\s([A-Z][a-z]{2})\s'
regex_9  = r'\s(\d{4}):'
regex_10 = r'\s([0-9A-Za-z_]+\.[0-9A-Za-z]+)\sHTTP'

print('regex_1',  regex_1, '\t returned ', test_regular_expression(regex_1, line_1))
print('regex_2',  regex_2, '\t returned ', test_regular_expression(regex_2, line_1))
print('regex_3',  regex_3, '\t returned ', test_regular_expression(regex_3, line_1))
print('regex_4',  regex_4, '\t returned ', test_regular_expression(regex_4, line_1))
print('regex_5',  regex_5, '\t returned ', test_regular_expression(regex_5, line_1))
print('regex_6',  regex_6, '\t returned ', test_regular_expression(regex_6, line_1))
print('regex_7',  regex_7, '\t returned ', test_regular_expression(regex_7, line_2))
print('regex_8',  regex_8, '\t returned ', test_regular_expression(regex_8, line_2))
print('regex_9',  regex_9, '\t returned ', test_regular_expression(regex_9, line_2))
print('regex_10', regex_10,'\t returned ', test_regular_expression(regex_10,line_2))
