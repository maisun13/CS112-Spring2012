 #!/usr/bin/env python

names=[ 'bob', 'fred']

letters = ['a','d','f']
letters += ['b','c']
print letters
print letters[-1]
letters2 = letters[:]
letters[0] = 'huh'
print letters2
