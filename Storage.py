# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:02:10 2020

@author: 18moh
"""

import pickle

def storeData(data, file):
    st = open(file, 'wb') 
    pickle.dump(data, st)                      
    st.close() 
  
def loadData(file):
    st = open(file, 'rb')
    ld=pickle.load(st)
    st.close
    return ld