from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    # Let's define our first FST
    f1 = FST('soundex-generate')
    # Indicate that '1' is the initial state
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.add_state('7')
    f1.add_state('8')
    
    f1.initial_state = '1'

    # Set all the final states
    f1.set_final('2')
    f1.set_final('3')
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')
    f1.set_final('7')
    f1.set_final('8')
    
    set1 = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'h':1, 'w':1, 'y':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'H':1, 'W':1, 'Y':1}
    set2 = {'b':1,'f':1,'p':1,'v':1, 'B':1,'F':1,'P':1,'V':1}
    set3 = {'c':1,'g':1,'j':1,'k':1,'q':1,'s':1,'x':1,'z':1, 'C':1,'G':1,'J':1,'K':1,'Q':1,'S':1,'X':1, 'Z':1}
    set4 = {'d':1,'t':1, 'D':1,'T':1}
    set5 = {'l':1, 'L':1}
    set6 = {'m':1,'n':1, 'M':1,'N':1}
    set7 = {'r':1, 'R':1}
    
    # Add the rest of the arcs
    for letter in string.ascii_letters:
        if letter in set1:
            f1.add_arc('1', '2', (letter), (letter))
            f1.add_arc('2', '2', (letter), ())
            f1.add_arc('3', '2', (letter), ())
            f1.add_arc('4', '2', (letter), ())
            f1.add_arc('5', '2', (letter), ())
            f1.add_arc('6', '2', (letter), ())
            f1.add_arc('7', '2', (letter), ())
            f1.add_arc('8', '2', (letter), ())
        
        elif letter in set2:
            f1.add_arc('1', '3', (letter), (letter))
            f1.add_arc('2', '3', (letter), ('1'))
            f1.add_arc('3', '3', (letter), ())
            f1.add_arc('4', '3', (letter), ('1'))
            f1.add_arc('5', '3', (letter), ('1'))
            f1.add_arc('6', '3', (letter), ('1'))
            f1.add_arc('7', '3', (letter), ('1'))
            f1.add_arc('8', '3', (letter), ('1'))
        
        elif letter in set3:
            f1.add_arc('1', '4', (letter), (letter))
            f1.add_arc('2', '4', (letter), ('2'))
            f1.add_arc('3', '4', (letter), ('2'))
            f1.add_arc('4', '4', (letter), ())
            f1.add_arc('5', '4', (letter), ('2'))
            f1.add_arc('6', '4', (letter), ('2'))
            f1.add_arc('7', '4', (letter), ('2'))
            f1.add_arc('8', '4', (letter), ('2'))
           
        elif letter in set4:
            f1.add_arc('1', '5', (letter), (letter))
            f1.add_arc('2', '5', (letter), ('3'))
            f1.add_arc('3', '5', (letter), ('3'))
            f1.add_arc('4', '5', (letter), ('3'))
            f1.add_arc('5', '5', (letter), ())
            f1.add_arc('6', '5', (letter), ('3'))
            f1.add_arc('7', '5', (letter), ('3'))
            f1.add_arc('8', '5', (letter), ('3'))
            
        elif letter in set5:
            f1.add_arc('1', '6', (letter), (letter))
            f1.add_arc('2', '6', (letter), ('4'))
            f1.add_arc('3', '6', (letter), ('4'))
            f1.add_arc('4', '6', (letter), ('4'))
            f1.add_arc('5', '6', (letter), ('4'))
            f1.add_arc('6', '6', (letter), ())
            f1.add_arc('7', '6', (letter), ('4'))
            f1.add_arc('8', '6', (letter), ('4'))
            
        elif letter in set6:
            f1.add_arc('1', '7', (letter), (letter))
            f1.add_arc('2', '7', (letter), ('5'))
            f1.add_arc('3', '7', (letter), ('5'))
            f1.add_arc('4', '7', (letter), ('5'))
            f1.add_arc('5', '7', (letter), ('5'))
            f1.add_arc('6', '7', (letter), ('5'))
            f1.add_arc('8', '7', (letter), ('5'))
            
        elif letter in set7:
            f1.add_arc('1', '8', (letter), (letter))
            f1.add_arc('2', '8', (letter), ('6'))
            f1.add_arc('3', '8', (letter), ('6'))
            f1.add_arc('4', '8', (letter), ('6'))
            f1.add_arc('5', '8', (letter), ('6'))
            f1.add_arc('6', '8', (letter), ('6'))
            f1.add_arc('7', '8', (letter), ('6'))
            f1.add_arc('8', '8', (letter), ())
    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.initial_state = '1'
    f2.set_final('4')
    f2.set_final('3')
    f2.set_final('2')
    f2.set_final('1')
    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))

    for n in range(10):
        f2.add_arc('1', '2', (str(n)), (str(n)))
        f2.add_arc('2', '3', (str(n)), (str(n)))
        f2.add_arc('3', '4', (str(n)), (str(n)))
        f2.add_arc('4', '4', (str(n)), ())

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')
    
    f3.initial_state = '1'
    f3.set_final('2')
    
    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))
    
    f3.add_arc('1', '1a', (), ('0'))
    f3.add_arc('1a', '1b', (), ('0'))
    f3.add_arc('1b', '2', (), ('0'))
    
    for number in xrange(10):
        f3.add_arc('1', '1a', (str(number)), (str(number)))
        f3.add_arc('1a', '1b', (str(number)), (str(number)))
        f3.add_arc('1b', '2', (str(number)), (str(number)))
        
    
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
