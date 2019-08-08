#!/usr/bin/python

import sys, getopt, re, json

def main(argv, stdin):
    skip = 0
    pretty = "false"
    delimiter = "\s+"
    try:
        opts, args = getopt.getopt(argv,"h:p:s:d:",["headers=","pretty=", "skip-lines=", "delimiter="])
    except getopt.GetoptError:
        sys.stdout.write('shell_to_json.py -h "<header>,<header>" -p true\n')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--headers"):
            headers = [x.strip() for x in arg.split(',')]
        elif opt in ("-p", "--pretty"):
            pretty = arg
        elif opt in ("-s", "--skip-lines"):
            skip = int(arg)
        elif opt in ("-d", "--delimiter"):
            delimiter = arg

    pattern = re.compile(delimiter)
    list = []
    for l, line in enumerate(stdin):
        if int(l + 1) <= skip: 
            continue
       
        line = line.strip()
        row = pattern.split(line)
        
        if len(row) == len(headers):
            obj = {} 
            for i, header in enumerate(headers):
                obj[header.lower()] = row[i]
            list.append(obj)
        
    if pretty == 'true':
        sys.stdout.write(json.dumps(list, indent=4) + '\n')
    else:
        sys.stdout.write(json.dumps(list) + '\n')

if __name__ == "__main__":
   main(sys.argv[1:], sys.stdin)

