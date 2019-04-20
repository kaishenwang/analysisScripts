with open('parkedInfo.csv') as rf, open('sampleParkedInfo.csv', 'w') as wf:
    rline = 0
    wline = 0
    for line in rf:
        rline += 1
        if rline % 2  == 1:
            wf.write(line)
            wline += 1
        if wline > 10000:
            break
