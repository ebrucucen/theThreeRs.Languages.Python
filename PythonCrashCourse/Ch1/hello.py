#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fractions import Fraction
##
#$ python
#Python 2.7.10 (default, Jul 30 2016, 19:40:32)
#[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
#>>> exit()
#$ python3
#Python 3.6.0 (default, Dec 24 2016, 08:01:42)
#[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
#>>> exit()
##################################################################
print("hello mars!")

the_light_is_green=True
if the_light_is_green:
    print("go")
#nw:    print "2+2 :"  str(2+2)
    calc=(3**2) + (4**5)
    print (49*8)-3 #int
    print (3.0/4)
    print calc
#nw:    print _+2
    x= Fraction(-8,3) #fraction
    print x
    y=3j+2 #complex
    print y


##################################################################
#type: int, float, decimal, fraction, complex
#run commands
#$ python3 -c 'command' [args]    
#run/compile modules: 
#$ python3 -m py_compile "hello.py"
#run it
#python3 "hello.py"
#"hello mars!"
