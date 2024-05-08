'''
CSC360- Assignment 3
Drew Kroeger
This assignment is a gibberish maker, where it takes syllables and insets them into a word, based on the vowels of that word, a wildcard * can also be used to insert the vowel being used
It also has syllable input validation, and asks the users if they want to do it again
'''
import string
print("This is a game where a word becomes gibberish by entering syllables into a normal word. \nI will have you enter two syllables and a word. \nYou can also enter * for a character. ")

vowels = "aeiouAEIOU" #these are used to for comparison, if the input word has any letters matching these
again_string = ''     #this is used to initalize a string that will be needed to repeat the function


    

def master():
    """This is used for most of this python script, it takes input for two syllables and a word, and makes the word gibberish with those syllables"""


    first_syllable = input("Enter the first syllable:")
    w=0
    while w < len(first_syllable):                                                                                          #this is input validation to make sure the first syllable only contains letters or *
        if first_syllable[w] not in string.ascii_letters and first_syllable[w] not in '*':                                  #if the letter in question is not ascii or * it comes here
            first_syllable = input("Syllable can only contain letters or '*':")                                             #ask user to re input the syllable
            #print(first_syllable)
            w = 0                                                                                                           #we reset to zero and check word they put in, will repeat whole while loop
        else:                                                                                                               #if letter in question is fine it will come here, if whole syllabe is fine it will go through this only
            w+=1
    w=0



    second_syllable = input("Enter the second syllable:")                                                                   #this is input validation to make sure the second syllable only contains letters or *
    while w < len(second_syllable):
        if second_syllable[w] not in string.ascii_letters and second_syllable[w] not in '*':                                
            second_syllable = input("Syllable can only contain letters or '*':")
            print(second_syllable)
            w = 0
        else:
            w+=1




    original_word = input("Enter the word you want to manipulate:")                                                         #no input validation for actual word
    i = 0                                                                                                                   #other variables that need to be used some point
    new_string = ''
    first_vowel_used = False
    previous_character = ' '





    for x in original_word:                                                                                                 #this is a long loop, goes through each character of the original input word
        new_string += x                                                                                                     #we add x to the new string which we will return
        previous_character_boolean = False                                                                                  #defualt boolean setting, used later on   
        #print("X is:", x, "I is", i, " Original word is ", original_word, " and new string is:" , new_string) 

        if i >=1:                                                                                                           #this is so we can check if there is two vowels next to each other, we keep track of what is in front of out current iteration
            previous_character = new_string[i-1]
        
        if x in vowels and previous_character in vowels:                                                                    #if both the letter we are on and the letter behind us are vowels, we make a boolean true, which is used for making sure we do use gibberish on simeutaneous vowels
            #print("Double vowel")
            previous_character_boolean = True



        if x in vowels and first_vowel_used == False and previous_character_boolean == False:                               #if we are on first vowel found, then we will come here, the second boolean might not be needed(previous_character_boolean), as it is redundant
            #print("YES: ", x)
            new_first_syllable= ""                                                                                          #this is used to store the asterisk, and transform it into a actual vowel
            if first_syllable[0] == '*':
                new_first_syllable =  x + first_syllable[1:]
            else:
                new_first_syllable = first_syllable
            
            new_string = new_string[:i] + new_first_syllable  + new_string[i:]                                              #we take the string we have so far and the first syllable and put them together for gibberish
            #print(new_string)
            i+=len(new_first_syllable)                                                                                      #we add this so we iterate correctly on the next go around, other wise splicing will be off
            first_vowel_used = True                                                                                         #if we go through this we make it true so we only use first syllable once and second syllable the rest

        elif x in vowels and first_vowel_used == True and previous_character_boolean == False:                              #if we find a second vowel that is not right after another vowel we come here, see if statements above comments for how this works
            #print("YES: ", x)                                                                                                                                                                                  
            new_second_syllable = ""
            if second_syllable[0] == '*':
                new_second_syllable = x + second_syllable[1:]
            else:
                new_second_syllable = second_syllable
            new_string = new_string[:i] + new_second_syllable  + new_string[i:]
            #print(new_string)
            i+=len(new_second_syllable)

        else:                                                                                                              #if its not a vowel, or is a double vowel, it will come here
            print("consanant or double vowel here, increasing...")


        i += 1                                                                                                              #implement i at the end of the for loop, for proper splicing
    #end of for loop

    print("New manipulated word is ", new_string)                                                                           #prints and returns the gibberish word
    return new_string
##end of first step method





returned_string = master()                                                                                                  #this calls the master method which is written above
again_string = input("Do you want to play again, y or n:")                                                                  #if we want to do master again we can with a simple y into the terminal, otherwise to leave you can input n
while again_string != 'n' and again_string != 'N':                                                                          #as long as answer is NOT no(n or N) we ask them something
    if again_string == 'y' or again_string == 'Y':                                                                          #while answer to play again is yes(y or Y), we play again
        returned_string = master()
        again_string =input("Do you want to play again? y or n: ")
    else:                                                                                                                   #no y/Y or n/N will result in asking them to input a y/Y or n/N until they do
        again_string = input("Please enter a y/Y or n/N to continue: ")
print("Thank you for playing!")                                                                                            #if n/N is input into wanting to play again, they will come here

#End of Kroeger.py- Assignment 3 gibberish word generator, with character and basic word input validation
