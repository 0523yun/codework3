count=0
lst="this is a test."
lst1=['!','?','.',',',' ']
for char in lst:
    if char in lst1:
        count+=1
print("这个句子中单词个数为：{:.0f}".format(count))
