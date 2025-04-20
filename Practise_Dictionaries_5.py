name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic = dict()
for x in handle:
    if not x.startswith("From "): continue
    x  = x.split()
    x = x[5]
    x = x.split(":")
    x = x[0]
    dic[x] = dic.get(x,0)+1
print(dic)
lst = list()
for x,y in dic.items():
    tup = (x,y)
    lst.append(tup)
print(lst)
lsst = sorted(lst)
for l,t in lsst[:]:
    print(l,t)
