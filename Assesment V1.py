"""
Filename: Assesment DT1.7 DT1.8 
Author: Lavanya Sahu 
Date: 6/07/22
Description: True and False Question 
"""
import random
def trueflase_quiz(question, correct_ans):
    if input(question) == correct_ans:
        return("correct")
    else:
        return("incorrect")
    #Question True and False 
quiz_2 = trueflase_quiz("God Save the King was New Zealand's national anthem up to and during WWII ", "T")
print("your answer is ", quiz_2)

quiz_3 = trueflase_quiz("Phar Lap was a New Zealand born horse who won the Melbourne Cup ", "F")
print("your answer is ", quiz_3)

quiz_4 = trueflase_quiz("Queen Victoria was the reigning monarch of England at the time of the Treaty ", "T")
print("your answer is ", quiz_4)

quiz_5 = trueflase_quiz("Te Rauparaha is credited with intellectual property rights of Kamate ", "T")
print("your answer is ", quiz_5)

quiz_6 = trueflase_quiz("The Treaty of Waitangi was signed in 1901", "F")
print("your answer is ", quiz_6)

quiz_7= trueflase_quiz("Is sign lanaguge the national langauge of New Zealand", "F")
print("your answer is ", quiz_7)

quiz_8 = trueflase_quiz("Jacinda used to work in the fish and chip shop", "T")
print("your answer is ", quiz_8)

quiz_9 = trueflase_quiz("Is Auckland the smallest city in NZ", "F")
print("your answer is ", quiz_9)

quiz_10 = trueflase_quiz("The first person who climbed MtEverest was it a kiwi?", "T")
print("your answer is ", quiz_10)

quiz_11= trueflase_quiz("Aotearoa commonly means Land of the Long White Cloud ", "T")
print("your answer is ", quiz_11)
