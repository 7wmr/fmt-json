#!/usr/bin/python

import sys, getopt, re, json

def main(argv, stdin):
    skip = 0
    pretty = False
    delimiter = "\s+"
    try:
        opts, args = getopt.getopt(argv,"h:Ps:d:",["headers=","pretty", "skip-lines=", "delimiter="])
    except getopt.GetoptError:
        sys.stdout.write('shell_to_json.py -h "<header>,<header>" -P\n')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--headers"):
            headers = [x.strip() for x in arg.split(',')]
        elif opt in ("-P", "--pretty"):
            pretty = True
        elif opt in ("-s", "--skip-lines"):
            skip = int(arg)
        elif opt in ("-d", "--delimiter"):
            delimiter = arg

    delimiter_match = re.compile(delimiter)
    list = []
    invalid_rows = []
    for l, line in enumerate(stdin):
        if int(l + 1) <= skip: 
            continue
       
        line = line.strip()
        row = delimiter_match.split(line)
        
        if len(row) == len(headers):
            obj = {} 
            for i, header in enumerate(headers):
                value = int(row[i]) if re.match("^\d+$", row[i]) else row[i]
                obj[header.lower()] = value
            list.append(obj)
        else:
            invalid_rows.append(row)
        
    if pretty:
        sys.stdout.write(json.dumps(list, indent=4) + '\n')
    else:
        sys.stdout.write(json.dumps(list) + '\n')

if __name__ == "__main__":
   main(sys.argv[1:], sys.stdin)

