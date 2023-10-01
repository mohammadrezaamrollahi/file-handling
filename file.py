f = open("1.txt", 'r')
lines = f.readlines()
print(lines)
words = 0
chars = 0
for line in lines:
    words = words+len(line.split())
    chars = chars+len(line.strip())
print("**Result:===================================")
print("********** :"+ str(len(lines)) +"\t" "lines")
print("**********  :"+str(words) +"\twords")
print("**********  :"+ str(chars) +"\tcharacters")
print("============================================")
f.close()
