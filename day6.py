 #!/usr/bin/env python*


###Examples of bad variables##

bob=1
EIGHT=256 
charmander = 'c'
b0b=1
BOB=2
pi = pygame.Surface()
pI = pygame.Surface()
p_i = pygame.Surface()
p_img = pygame.Surface()

player_image=pygame.Surface()
ply_image=pygame.Surface()

##Make sure to name varibales appropriately

player_rect_for_collision = Rect()

##Make sure its descriptive but not too desciptive

##Its reasonable to have temporary varibales

##Make sure temporary variables relate when using the same combo of letters. Ex: t1 & t2

a=3
b=4
t1=2
t2='bob'


##All caps generally mean you-re dealing with a constant. Ex: BOB will always be Fred

BOB="Fred"


##If you're dealing with an object, your variables start with a capital letter

Player=5

longVariableNames #used in Java. long variable name while still easy to read
long_variable_names #used in Python. long variable name whiel still easy to read
longvariablesnames #DO NOT USE. HARD TO READ

__len__ #Defined by python. Special Meaning
_x #since python does not have the ability to make things private, use _x

#To comment use (#)
#If its a short comment stick it at the end of the line
#Long comments are right before what they are commenting on

#use triple " mark before and after multiline comment

"""
I am a multiline comment

"""

#Remember spacing to make things easier to read

t=x*3+y*3/2 #Not Good
t = x*3 + y*3/2 #Great
t = x*3 + (y*3)/2 #Better

#Spacing essential to readability

max(a, b) #Better
max(a,b) #Worse
