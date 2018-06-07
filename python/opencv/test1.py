import datetime   
import time 
import calendar 
import re 
'''print (datetime.datetime.now())


a=datetime.date(2018,11,5)

b=datetime.time(23,59,34)
print(a,b)


start = datetime.datetime(2018,5,22,19,31,52,379112)
end = datetime.datetime(2018,5,22,19,31,55,379113)
 
end-start

print (datetime.timedelta(0,3,1)

start = datetime.datetime(2018,5,22,19,31,52,379112)
gap = datetime.timedelta(0,3,1)

start+gap

print (datetime.datetime(2018,5,22,19,31,55,379113)
 


localtime=time.localtime(time.time())
print("local current time:",localtime)

import calendar
print (calendar.month(2018,5))
cal = calendar.Calendar(firstweekday=3)  #set first weekday as 3
for x in cal.iterweekdays():
	print (x)

for i in calendar.Calendar().itermonthdates(2018,5):
	print(i)

print (calendar.HTMLCalendar().formatmonth(2018,5,withyear=True))

print("regular expressions concepts")


p= re.compile('a*')   # * is looking for a starting position 0 or any umber of times in match
print (p.match("aaaAabbb"))

p= re.compile('a+')   # + is looking for a  in starting position atleast one time in match
print (p.match("aaaAabbb"))  # matched 3 times 


p= re.compile('[abc]*')   # * is looking for a to z starting position 0 or any umber of times in match
print (p.match("bacaAabbb"))  # matched 3 times "))

p= re.compile('[a-z]+')   # + is looking for a to z in starting position atleast one time in match
print (p.match("1zebra"))  # matched 3 times 

p= re.compile('[a-zA-Z0-9]*')   # * is looking for all characters at starting position 0 or any umber of times in match
print (p.match("bac1aAaSb5bb"))  # matched 3 times "))

p= re.compile('[^a]*')   # * is looking for any character except a in starting position in match
print (p.match("1bCac1aAaSb5bb"))  # matched 3 times "))

p= re.compile('[^a-zA-Z0-9]')   # * is looking for no characters at starting position 0 or any umber of times in match
print (p.match("#bac1aAaSb5bb"))  # matched 3 times "))

p= re.compile('\d')   # * is looking for matches any digit; this is equalent to 0-9
print (p.match("aaaAabbb"))

p= re.compile('\D')   # * is looking for matches any character except to 0-9
print (p.match("aaaAabbb"))

p=re.compile('ab*')   # should start with a then b can be any number of times
print (p.match("ab23b4"))
print (p.match("23ab23b4",2))  #  start search at 2nd index for ab

p=re.compile('ab+')   # should start search for ab at starting position 
print (p.match("abbb23b4"))

p=re.compile('abc+')   #  start search at 3nd index for ab 
print (p.match("abbabc23b4",3))

p=re.compile('ab*')   # should search for ab in given string - it find the first occurance 
print (p.search("12saddeffabbb23b4"))

p=re.compile('ab+')   # should search for ab in given string - it find the first occurance 
print (p.search("1ab2sabddeffabbb23b4"))

print (p.search("1ab2sabddeffabbb23b4",10))
 
p=re.compile('ab*')   # should search for ab in given string - it find the first occurance 
print (p.finditer("1ab2sabddeffabbb23b4"))

for i in p.finditer("234sabcab"):
	print (i)

print (p.findall("1ab2sabddeffabbb23b4")) # it will give you the list

k=p.findall("1ab2sabddeffabbb23b4")
print (type(k))

p=re.compile("o[a-z]*")   # return the span if the full text matches the Reg EX
print (p.fullmatch("dog"))
print (p.fullmatch("ogre"))
print (p.fullmatch("dogxie",1,5))

p=re.compile("o[a-z][0-9]*")   # return the span if the full text matches the Reg EX
print (p.fullmatch("dog"))
print (p.fullmatch("og1re"))
print (p.fullmatch("dogxie",1,5))

j=p.fullmatch("dogxie",1,5)

print (j.group())
print (j.span())
print (j.start())
print (j.end())

s='<html><head><title>Title</title>'
print(re.match('<.*>',s).group())  # greedy behaviour
print(re.match('<.*?>',s).group())  # non-greedy behaviour

p= re.compile('\w')   # * is looking for matches any digit; this is equalent to 0-9
print (p.match("aaaAabbb"))

p= re.compile('\W')   # * is simlar to [^a-zA-Z0-9].
print (p.match("aaaAabbb"))
print (p.match("#aaaAabbb"))'''

p= re.compile('\s')   # * is for \t\b.....
print (p.match(" aa aAa	bbb"))

p= re.compile('\S')   # * is for \t\b.....
print (p.match("aa aAa	bbb"))









