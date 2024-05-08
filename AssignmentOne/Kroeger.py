
'''
Drew Kroeger- CSC240 - Assignment 1- This script takes THREE floating point numbers and sorts them using only if statements
'''

first_float = float(input("Please enter the first floating point number:"))
second_float = float(input("Please enter the second floating point number:"))
third_float = float(input("Please enter the third floating point number:"))
first_position, second_position, third_position = 0,0,0


#has 6 possible statements as the rubric says(them all equaling the same thing will filter out in the first if statement, which would make 7 possible statements)
if third_float >= second_float >= first_float:
    first_position,second_position,third_position = first_float,second_float,third_float

if third_float>= second_float <= first_float:
    if third_float> first_float:
        first_position, second_position, third_position = second_float,first_float,third_float
    
    elif third_float<= first_float:
        first_position, second_position, third_position = second_float,third_float,first_float

if third_float <= second_float <= first_float:
    first_position,second_position,third_position = third_float,second_float,first_float

if third_float <= second_float >= first_float:
    if third_float > first_float:
        first_position,second_position,third_position = first_float,third_float,second_float
    
    elif third_float <= first_float:
        first_position,second_position,third_position = third_float,first_float,second_float




print("Numbers in increasing order: ", first_position, " ", second_position, " ", third_position)