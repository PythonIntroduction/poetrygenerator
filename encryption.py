import string

LOOKUP_TABLE = string.ascii_letters + ".,!? \n"

def rotate_character(character):
    '''
    En- or decrypt a character using a ROT13-like encryption strategy and return the resulting character.
    '''
    current_position = LOOKUP_TABLE.index(character)
    rotate_by = len(LOOKUP_TABLE) // 2 #Floor division
    next_position = (current_position + rotate_by) % len(LOOKUP_TABLE)
    return LOOKUP_TABLE[next_position]

def rotate_string(string):
    '''
    En- or decrypt a string and return the result
    '''
    rotated_string = ""
    for character in string:
        rotated_string += rotate_character(character)
    return rotated_string