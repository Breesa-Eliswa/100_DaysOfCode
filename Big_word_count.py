#Program to find the word that has appeared the maximum no: of times.
counts = dict()
handle = input('Enter the file name: \n')
fopen = open(handle)
for line in fopen:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) +1
bigcount = None
bigword = None 
for word,count in counts.items():
    if bigcount is None or count> bigcount:
        bigword = word
        bigcount = count
print("Bigword :  ",bigword)
print("Bigcount:  ",bigcount)