#DREW KROEGER- CSC240- ASSIGNMENT 5- this programs takes a user input hieght and makes a pascal triangle of the user specified height


def make_new_row(old_row):#this takes a list(one row of a pascal triangle) and returns the next row of the pascal triangle
    """Requires:
       -- list old_row that begins and ends with a 1 and has zero or more
          integers in between (has to have at least [1,1])
       Returns:
       -- list beginning and ending with a 1 and each interior (non 1)
          integer is the sum of the corresponding old_row elements
          For example if old_row = [ 1,4,6,4,1], then new_row = [1,5,10,10,5,1],
          i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1 """
    
    new_row = [1]                                   #initalize the new row list, the list that gets returned


    if old_row == []:                               #handle the special empty case
        new_row = [1]
        #print("entered if",new_row)
        return new_row  
      
    elif old_row == [1]:                            #handle the single number case
        new_row = [1,1]
        #print("entered elif", new_row)
        return new_row
    else:                                           #not empty or single number we go here
        #print("entered else:", old_row)
        
        for i in range(len(old_row)-1):             #we do a for loop for the length of the old row and minue one so there is no out of bounds error
            #print("else for loop " ,i)
            element = old_row[i] + old_row[i+1]     #this takes the two  next two elements of the previous row, and makes a new sum element out of them
            new_row.append(element)                 #add that sum of the previous two elements to the new row
        new_row.append(1)                           #have to add the ending one to the list
        return new_row                      
    
    
def main():                                         #this is the main function/method
    height = int(input("Please enter height of Pascal's Triangle:"))        #ask user for the height of the pascal triangle 
    funny_list = []                                                         #create a list that to store and print the pascal triangle
    for i in range(height):                                                 #do each row gets one iteration in the loop
        #print("height iteration i:" ,i)
        #print("the entered funny list is:",funny_list)
        funny_list =  make_new_row(funny_list)                              #we make the new row calling the make_new_row function, and store it in funny list
        print(funny_list)                                                   #we print it for just that iteration
    print("last row is:", funny_list)                        #this will print only the last row of the pascal triangle, but the for loop will print the whole triangle