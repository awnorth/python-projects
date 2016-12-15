ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Lets fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # Call pop on more_stuff
    print "Adding: ", next_one
    stuff.append(next_one)      # Call append with argument next_one
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()               # Call pop on stuff
print ' '.join(stuff)           # Call join with argument stuff
print '#'.join(stuff[3:5])      # Call join with argument stuff


master_list = "One Two Three Four who let the munchkin in through the door!?"
break_list = master_list.split(' ')     # Call split on master_list
end_list = break_list.pop()             # Call pop on break_list

print "Master list: ", master_list
print "Broken by a space: ", break_list
print "Use the 'pop' command to take the end of the list: ", end_list
