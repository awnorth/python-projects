import random

print "\nrandom.random()"
print random.random(), '\n'
print "random.randint(0, 5)"
print random.randint(0, 5), "\n"
print "int(random.random() * 100)"
print int(random.random() * 100), "\n"
print "random.choice(['this', 'that', 'other'])"
print random.choice(['this', 'that', 'other']), '\n'

myList = ['one', 2, 'three', 4, 'five!']
print "myList:", myList
print "random.shuffle(myList)\nprint myList"
random.shuffle(myList)
print myList, '\n'
