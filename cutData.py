with open('dataFull.csv') as f1, open ('data.csv','w') as f2:
    for line in f1:
        parts = line.split(',')
        for i in range(7):
            f2.write(parts[i]+',')
        f2.write(parts[7] + '\n')
