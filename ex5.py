name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair= 'Brown'

print("Let's talk about %r." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

height_in_metric = height * 2.54
weight_in_metric = weight * 0.453592

print("He's %(#)5d centimeters tall." % {"#" : height_in_metric})
print("He's %f kilograms heavy." % weight_in_metric)