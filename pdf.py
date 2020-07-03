# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:01:01 2020

@author: RjkG
"""

# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('The_Living_World.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print(pdfReader.numPages) 

# creating a page object 
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i) 
    # extracting text from page 
    print(pageObj.extractText()) 


# closing the pdf file object 
pdfFileObj.close() 
