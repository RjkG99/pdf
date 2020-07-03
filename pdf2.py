# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:13:02 2020

@author: RjkG
"""
import fitz

pdf_document = "C:/Users/RjkG/Desktop/machine learning/The_Living_World.pdf"
doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)

for i in range(doc.pageCount):
    page1 = doc.loadPage(i)
    page1text = page1.getText("text")
    print(page1text)
