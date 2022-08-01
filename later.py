##from functools import reduce
#l=[1,2,3,4,5]
##key = lambda a,b:a+b
##res =  reduce(key,l)

##total=0
##res = [total := total+item for item in l]
##print(total)



s = "hi welcome to python programming programming"
longest=""
a=s.split()
for word in a:
    if len(word)>len(longest) and a.count(word)==1:
        longest = word

