#Saad Bhuiyan
#SoftDev1 pd2
#K2 -- Get the name of a random student from a team (input) within a dictionary
#2019-09-10

KREWES = {
	'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse', 'Tiffany', 'Amanda', 'Junhee', 'Jackie ', 'Tyler', 'Emory', 'Ivan', 'Elizabeth', 'Pratham', 'Shaw', 'Eric', 'Yaru', 'Kelvin', 'Hong Wei', 'Michael', 'Kiran', 'Amanda', 'Joseph', 'Tanzim', 'David', 'Yevgeniy'],
	'rex': ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham', 'Michael', 'Matthew', 'Jionghao', 'Devin ', 'David', 'Jacob', 'Will', 'Hannah', 'Alex'],
	'endymion': ['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason', 'Tammy', 'Albert', 'Kazi', 'Derek', 'Brandon', 'Kenneth', 'Lauren', 'Biraj', 'Jeff', 'Jackson', 'Taejoon', 'Kevin', 'Jude', 'Sophie', 'Henry', 'Coby', 'Manfred', 'Leia', 'Ahmed', 'Winston']
}

'''
print (KREWES)

print (KREWES['orpheus'])
print (KREWES['rex'])
print (KREWES['endymion'])
'''

import random

'''
def randomStudent(team):
    teamMembers = KREWES[team]
    return teamMembers[random.randrange(len(teamMembers))]
'''

def randomStudent(team):
    return random.choice(KREWES[team])

print (randomStudent('orpheus'))

print (randomStudent('rex'))

print (randomStudent('endymion'))
