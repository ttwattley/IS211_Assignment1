#!/usr/bin/env python
# coding: utf-8

# In[7]:


def listDivide (numbers, divide):
    #The function returns the number of elements in the numbers list that are divisible by divide.
    pass

class ListDivideException ():
    def testListDivide ():
        #test listdivide
        assert listDivide([1,2,3,4,5]) == 2
        assert listDivide([2,4,6,8,10]) == 5
        assert listDivide([30, 54, 63,98, 100], divide=10) == 2
        assert listDivide([]) == 0
        assert listDivide([1,2,3,4,5], 1) == 5
    

