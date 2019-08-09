#!/usr/bin/python

import sys, getopt, re, json

def main(argv, stdin):
    def help():
        sys.stdout.write("""
        FMT-JSON
        ========

            Summary:

                Will parse the standard input passed to script and format as JSON string.

            Flags:
                
                -H,  --help       switch    help for script usage
                -h,  --headers    string    comma delimited list of header named (lowercase with underscores)
                -P,  --pretty     switch    to indent output for JSON data
                -K,  --key-value  switch    assume that input is a key value pair e.g. key=value
                -s,  --skip-lines number    number of lines to skip from start of input e.g. headers line
                -d,  --delimiter  regex     regular expression to split line on e.g. ","
        """ + "\n")
    
    skip = 0
    pretty = False
    key_value = False
    delimiter = "\s+"
    try:
        opts, args = getopt.getopt(argv,"Hh:PKs:d:",["help", "headers=","pretty", "key-value", "skip-lines=", "delimiter="])
    except getopt.GetoptError:
        sys.stdout.write("Incorrect usage: see help guide below.\n")
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-H", "--help"):
            help()
            sys.exit(0)
        elif opt in ("-h", "--headers"):
            headers = [x.strip() for x in arg.split(',')]
        elif opt in ("-P", "--pretty"):
            pretty = True
        elif opt in ("-s", "--skip-lines"):
            skip = int(arg)
        elif opt in ("-d", "--delimiter"):
            delimiter = arg
        elif opt in ("-K", "--key-value"):
            key_value = True

    delimiter_match = re.compile(delimiter)
    valid_rows = []
    invalid_rows = []
    for l, line in enumerate(stdin):
        if int(l + 1) <= skip: 
            continue
       
        line = line.strip()
        if key_value:
            # Split on first match only e.g. key=value
            row = delimiter_match.split(line, 1)
        else:
            # Split on all matches e.g. one,two,three
            row = delimiter_match.split(line)
        
        if len(row) <= len(headers):
            obj = {} 
            for i, header in enumerate(headers):
                if i >= len(row):
                    value = None
                else:
                    value = int(row[i]) if re.match("^\d+$", row[i]) else row[i]

                obj[header.lower()] = value
            valid_rows.append(obj)
        else:
            invalid_rows.append(row)

    response = {}
    response['data'] = valid_rows
    response['errors'] = invalid_rows
    response['status'] = 0 if len(invalid_rows) == 0 else 1 

    if pretty:
        sys.stdout.write(json.dumps(response, indent=4) + '\n')
    else:
        sys.stdout.write(json.dumps(response) + '\n')

if __name__ == "__main__":
   main(sys.argv[1:], sys.stdin)

