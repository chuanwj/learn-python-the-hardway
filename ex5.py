_name = 'Zed A. Shaw'
_age = 35 # not a lie
_height = 74 # inches
_weight = 180 # lbs
_eyes = 'Blue'
_teeth = 'White'
_hair = 'Brown'

# printf
# nedd use tuplet
print "Let's talk about %s." % _name
print "He's %d inches tall." % _height
print "He's %d pounds heavy." % _weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (_eyes, _hair)
print "His teeth are usually %s depending on the coffee." % _teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
_age, _height, _weight, _age + _height + _weight)