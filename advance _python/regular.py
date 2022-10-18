'''import re
pattern=re.compile("ab")
match=pattern.finditer("abcabcabc")
count=0
for m in match:
    count+=1
    print(m.start(),"....",m.end(),"....",m.group())
print("no. of occourences:",count)'''

#character class
import re
match=re.finditer("[^a-zA-z0-9]","a7b@KAZ8Ij")
for m in match:
    print(m.start(),".....",m.group())