from sys import argv

script, person, place, thing = argv

date_of_birth = input("When was %s born? " % person)
location = input("Where is %s? " % place)
synonym = input("What is another word for %s? " % thing)

print("Did you know that %s was from %s and their favorite thing is %s?" % (person, place, thing))
print("I was born on %s in %s and I like %s" % (date_of_birth, location, synonym))