import json
import sys
status_code = {}
status_code['miss'] = 0
with open('validDomains.txt', 'w') as wf, open(sys.argv[1]) as rf:
    for line in rf:
        if line[:4] == 'null':
            continue
        data = json.loads(line)
        try:
            code = data['data']['http']['response']['status_code']
            if code not in status_code:
                status_code[code] = 0
            status_code[code] += 1
            if (int(code) / 100 == 2):
                wf.write(data['domain']+ '\n')
        except:
            status_code['miss'] += 1
print(status_code)
