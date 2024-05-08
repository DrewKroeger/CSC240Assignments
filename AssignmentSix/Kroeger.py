#Drew Kroeger- CSC240- ASSIGNMENT 6- 5/1/24- THIS FILE HAS THREE FUNCTIONS: MAIN(driver), print_index, and compare files


def print_index(file_obj):
    '''function- this file takes in an open file object, and then takes the words from that file and puts them in a dictionary.
        it also will display the alphabetical order of the files, along with what lines that word appears on in the file
        the alphabetization is done with by closely dealing with the list
    requires 
        an already opened text file for reading
    returns 
        prints/returns a dictionary that is in alphabetical order(key)
        each value will be a set that contains the line numbers the key appears on'''
    
    book = {}
    sorted_list = []
    iteration = 0
    
    for line in file_obj:       #iterate through each line
        iteration += 1          #this is the line number actually used in the sets in the dictionary
        line = line.strip()
        
        for word in line.split():
            
            word = word.lower()
            word = word.strip()
            word = word.strip(",.;:")
            
            if word in book:    #when the word is already in the book we just need to add the extra line to the set of values of that word
                book[word].add(iteration)
                
            else:               #if the word is not in the book then we need to make a new set with that word, and add the line number the word was first on
                book[word] = set()
                book[word].add(iteration)
                sorted_list.append(word)  #this list will be used for making the display alphabetized, since we can sort list but not dictionaries
    
    #print(book)
    #print("\n\n\n",sorted_list, "\n")
    
    sorted_list.sort()                     #we sort the list
    print("This is the list of words in the first file input, in alphabetical order,\nalong with the lines each word appears on:\n")
    iteration = 0                           #this time it is used for displaying the word
    for element in sorted_list:             #here is tricky to think about, we are iterating through each element not in the dicitionary, but through the list, that is sorted
        print(sorted_list[iteration], sorted(book[element]))#we know the list contains same words as dictionary, we display that element of sorted list, and then the second part(value) - will display the values of that element in the dictionary, sorted
        iteration +=1

    return book
        
        
        


def compare_files(file_obj_one, file_obj_two):
    '''
    function: this file takes in two opened file objects and then will output the amount of words
    that are in both files(intersection), and then the amount of words that are in at least one of the files(union)
    requires:
        two opened text file objects
    returns:
        the number of common words that occured in both files(intersection),
        and total number of words that occured in general(intersection_'''
    
    set_one = set()                     #make two sets
    set_two = set()
    
    for line in file_obj_one:           #start reading from file
        line = line.strip()
        for word in line.split():           
            word = word.lower()
            word = word.strip()
            word = word.strip(",.;:")
            set_one.add(word)          #add individual words to the sets
            
    for line in file_obj_two:          #read file two this time, and add its words to the set two
        line = line.strip()
        for word in line.split():
            word = word.lower()
            word = word.strip()
            word = word.strip(",.;:")
            set_two.add(word)
            
    #print("WORDS PRESENT IN BOTH FILES:", sorted(set_one & set_two))
    #print("\n\n")
    #print("WORDS IN AT LEAST ONE OF THE FILES:" ,sorted(set_one | set_two))

    intersection_words_int = len(set_one & set_two)     #intersection the two sets
    union_words_int = len(set_one | set_two)            #union the two sets

    print("NUMBER OF WORDS IN BOTH FILES:",intersection_words_int)
    print("NUMBER OF WORDS IN AT LEAST IN ONE FILE:",union_words_int)

    #print("Set one:" , sorted(set_one))
    #print("set two:" , sorted(set_two))
    return intersection_words_int, union_words_int     #return the amount of words in union and intersection










def main():
    file_name = input("Enter the name of the input file you want to see dictionary of: ")
    file_obj = open(file_name, "r")         #we open this twice, once for each function call, it would not work if i opened it only once
    file_obj_one = open(file_name, "r")
    
    file_name_two = input("Enter the name of the OTHER input file: ") 
    file_obj_two = open(file_name_two, "r")
    
    big_book = {}
    big_book = print_index(file_obj)
    print()
    intersection, union = compare_files(file_obj_one, file_obj_two)
    #CLOSE FILE
    
    file_obj.close()
    file_obj_one.close()
    file_obj_two.close()


main()

