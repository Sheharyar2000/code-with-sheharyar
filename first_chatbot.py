# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:03:04 2019

@author: home
"""

import aiml

kernel = aiml.Kernel()
kernel.learn("English_Language_Chat.aiml")


# Press CTRL-C to break this loop
while True:
    print (kernel.respond(input("Enter your message >> ")))