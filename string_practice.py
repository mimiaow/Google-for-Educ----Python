import string 

n='edmalyn'
print n[1]              #d
print len(n)            #7
print n + ' pacanor'    #edmalyn pacanor
print 'isn\'t'          #isnt


pi = 3.14
#text= 'The value of pi is ' + pi       #not working
text= 'The value of pi is ' + str(pi)   #working!
print text

raw = r'this\t\n and that'
print raw     ## this\t\n and that
    
multi = """It was the best of times.
It was the worst of times."""
print multi

#single line comment
'''this is a
multi-line comment'''
"""another multi
line comment"""

#***String Methods***
q='  ed is learning python. '
print q.lower()                     #  ed is learning python. 
print q.upper()                     #  ED IS LEARNING PYTHON. 
print q.isalpha()                   #False
print q.isdigit()                   #False
print q.isspace()                   #False
print '19'.isdigit()                #True
print q.strip()                     #ed is learning python.

r='there\'s only 1 way 2 say, 3 words 4 u'
print r
print r.startswith('t')                 #True
print r.startswith('theres')            #False
print r.endswith('u')                   #True
print r.find('o') 		        #8
print r.find('\'')			#5 \' is counted as one
print string.replace(r, 'u', 'you')     #using the imported string module
print r.replace('u', 'you')             #same as prev code
print r.capitalize()                    #There\'s only 1 way 2 say, 3 words 4 u
print r.split()                         #seperates between spaces ["there's", 'only', '1', 'way', '2', 'say,', '3', 'words', '4', 'u']
print r.split('1')                      #["there's only ", ' way 2 say, 3 words 4 u']
print '---'.join(['aaa', 'bbb', 'ccc']) #aaa---bbb---ccc

g='Hello'
'''
  STRING SLICES
H    e   l   l   o
0    1   2   3   4
-5  -4  -3  -2  -1
'''

print g[1:4]        #ell
print g[1:]         #ello
print g[:]          #Hello
print g[:4]         #Hell

print g[-3]         #llo
print g[:-3]        #He

k=g[:2] + g[2:] 
print k     #Hello

# % operator
'''%d int, %s string, %f%g floating point
This code-across-lines technique works with the
various grouping constructs detailed below: ( ), [ ], { }'''
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print text


ustring = u'A unicode \u018e string \xf1'
ustring
u'A unicode \u018e string \xf1'
s = ustring.encode('utf-8')
s
'A unicode \xc6\x8e string \xc3\xb1'  ## bytes of utf-8 encoding
t = unicode(s, 'utf-8')             ## Convert bytes back to a unicode string
t == ustring                      ## It's the same as the original, yay!
True
print s

