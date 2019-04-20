uniqueDomains = {}

def helper(fName):
    with open(fName) as f:
        for line in f:
            uniqueDomains[line.rstrip()] = True
helper('domainsByNewID.txt')
helper('domainsByOldID.txt')
helper('domainByTokenAndOtherNS.txt')

with open('fullParkedDomains.txt', 'w') as f:
    for domain in uniqueDomains.keys():
        f.write(domain + '\n')
