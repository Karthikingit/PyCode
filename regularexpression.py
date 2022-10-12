'''regular expression is useful where validation or finding charecters 
 for ex. checking emails or passwords in proper format'''
import re 
a = "searching for this string in regular expression!"

print(re.search('this',a)) #also has lots of method in regular expression

#using pattern 
import re
pattern = re.compile('searching for this')
string = 'searching for this string in regular expression! using pattern'

a1 = pattern.match(string)
b = pattern.findall(string)
c = pattern.groups(string)
d = pattern.fullmatch(string)
print(a1)
print(b)
print(c)
print(d)
#watch real life practice of reg expression in part 4.