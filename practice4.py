myword="this is my word"
newword=myword.split(' ')
lenth=len(newword)
for i in range(lenth//2):
    newword[i],newword[lenth-i-1]=newword[lenth-i-1],newword[i]
print(' '.join(newword))