with open('topDomainInfo.csv') as f1, open('sampleParkedInfo.csv') as f2, open('dataFull.csv', 'w') as f3:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    f3.write(lines1[0])
    for i in range(1, min(len(lines1),len( lines2))):
        f3.write(lines1[i])
        f3.write(lines2[i])
    
