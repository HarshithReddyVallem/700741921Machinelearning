#creating a sisters tuple
sisters = ('satya','radha')
print('',type(sisters))

#creating a brothers tuple
brothers = ('rahul','rohit')
print('',type(brothers))

#Joining both tuples to siblings
siblings = sisters + brothers
print(siblings)

#getting number of siblings
print("number of siblings ",len(siblings))

#modifying tuple to list and assigning father and mother name to it
siblings_list = list(siblings)
print(siblings_list)
siblings_list.append('Prakash')
siblings_list.append('Pranitha')
print(siblings_list)

#changing  to tuple family_members
family_members = tuple(siblings_list)
print(family_members)
print('',type(family_members))
