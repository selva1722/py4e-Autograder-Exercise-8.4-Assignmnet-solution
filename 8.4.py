fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    t1=line.split()
    for w in t1  : 
        if  w in  lst: continue 
            # there is no if w is not in lst
            # if w is not in lst() also wont work - lst() is a function call
        lst.append(w)
lst.sort()
print( lst)
