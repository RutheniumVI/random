# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:09:10 2018

@author: veerash palnichamy
"""
import random


passLen = random.randint(10,24)#choosing the lenght of the password randomly
choiceList = []
specialChar = ['-','|','@','.',',','?','/','!','~','#','%','^','&','*','(',')','{','}','[',']','=','*']
choiceList.append(chr(random.randint(65,90)))#one uppercase char 
choiceList.append(chr(random.randint(97,122)))#one lower case char
choiceList.append(chr(random.randint(48,57)))#one number
choiceList.append(random.choice(specialChar))#special char
for i in range(passLen-3):
    choiceList.append(chr(random.randint(33,126)))#filling the rest of the list with random chr
random.shuffle(choiceList)
password = "".join(i for i in choiceList)#make password form shuffled list
print(password)

