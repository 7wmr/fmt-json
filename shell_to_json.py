#!/usr/bin/python

import sys, getopt, re, json

def main(argv, stdin):
    try:
        opts, args = getopt.getopt(argv,"h:p:",["headers=","pretty="])
    except getopt.GetoptError:
        print 'shell_to_json.py -h "<header>,<header>" -p true'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--headers"):
            headers = [x.strip() for x in arg.split(',')]
        elif opt in ("-p", "--pretty"):
            pretty = arg

    pattern = re.compile("\s+")
    list = []
    for line in stdin:
        line = line.strip()
        row = pattern.split(line)

        if len(row) == len(headers):
            obj = {} 
            for i, header in enumerate(headers):
                obj[header.lower()] = row[i]
            list.append(obj)
        
    if pretty == 'true':
        print json.dumps(list, indent=4)
    else:
        print json.dumps(list)

if __name__ == "__main__":
   main(sys.argv[1:], sys.stdin)

