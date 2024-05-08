def get_and_strip_number(s):
    """Requires:
       -- string s consists of (the string representing) a non-negative integer n followed
          by a single space, and then n words, separated by a single space
       Returns:
       -- the leading integer n (as an int), and
       -- the "rest" of s, i.e., what is left after stripping off n and, if n>0,
          the space following it"""
    #WRITE CODE HERE- 
    space_index = s.find(' ')                                       #this finds the index of the first space, so we can take number before it and words after
    if space_index == -1:                                           #no space exists means number is 0, which is one char long, and no words after that
        the_number = int(s[0])
        the_words = s[2::]
    else:
        the_number = s[0:space_index]                               #this means a space exist, number may be two chars long(or more)
        the_number = int(the_number)                                #turn it into an int because docstring said to
        the_words = s[space_index+1::]                              #the words are what comes after the first space                                                                                   
    return the_number, the_words







def get_and_strip_word(s):
    """Requires:
       -- string s has no leading spaces, and is either empty or
          consists of one or more words, separated by a single space
       Returns:
       -- first word of s, and
       -- the "rest" of s, i.e. what is left after stripping off the word and, if
          there is one, the space following the word"""
    #WRITE CODE HERE
    length = len(s)                                                 #take the length of the string
    if length == 0:                                                 #if the string is empty than return other variables as empty
        first_index = ''
        string_index = ''
    else:                                                           #not an empty string means something inside of it
        split_list = s.split()                                      #split the string into a list, makes it easier to deal with
        first_index = split_list[0]                                 #first index of the list becomes first return variable
        string_index = ' '.join(split_list[1::])                    #this makes the rest of the list back into a string with the join function, space in between each word
    return first_index, string_index
   
    
    
    
    
    
def pad_words(s, num_words, final_len):
    """Requires:
       -- final_len > len(s)
       -- string s consists of num_words words, each separated by a single space
       Returns:
       -- string r, containing the words in s evenly padded with spaces to make
          len(r) == final_len"""
    if num_words <= 1:      # best we can do is fill out the line with spaces
        return s + ((final_len - len(s))*' ')

    # there are at least 2 words, so at least one pigeon hole to fill (with spaces)
    num_pigeon_holes = num_words - 1                        # the buckets (pigeon holes) are between words
    num_pigeons = final_len - (len(s) - num_pigeon_holes)   # my pigeons are spaces
    pad_num = num_pigeons // num_pigeon_holes
    extra_num = num_pigeons % num_pigeon_holes              # number of holes that get an extra pigeon
    working_str = ''
    
    # take care of the first num_pigeon_holes - extra_num holes
    for i in range(num_pigeon_holes - extra_num):
        word, s = get_and_strip_word(s)
        working_str += word + (pad_num * ' ')   # insert pad_num spaces

    # take care of the last extra_num holes
    for i in range(extra_num):
        word, s = get_and_strip_word(s)
        working_str += word + ((pad_num + 1) * ' ')

    working_str += s
    return working_str





def main():
    """Main program for testing some text formatting functions."""
    file_name = input("Enter the name of the input file: ")
    file_obj = open(file_name, "r")

    print("Line length should be as long as the longest line to print, or longer.") 
    line_len = int(input("Enter the desired line length: "))
    print()

    for line in file_obj:
        line = line.strip()                   # strip the trailing '\n'
        n, words = get_and_strip_number(line)
        print(pad_words(words, n, line_len))

    file_obj.close()