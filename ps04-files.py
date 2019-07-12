#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:28:05 2019

@author: yuting
"""

import os
d = os.getcwd()
print(d)
## use os.chdir() to change path
f = os.listdir(".") # current folder
print(f)
files = os.listdir('data')
#file = list(files)
print(files)

def freq_Table(words):
    word_frequency = dict()
    for word in words:
        if word != "":
            word = word.lower()
            if not word in word_frequency.keys():
                word_frequency[word] = 0
            word_frequency[word]+=1
    total = sum(word_frequency.values())
    freq_table = {k:v/total for k, v in word_frequency.items()}        
    return freq_table

def most_freq(d, length):
    pairlist = sorted(d.items(), key=lambda kv: kv[1], reverse=True) 
    #print(pairlist)
    return dict(pairlist[:length])  

dicts = dict()
small_dicts = dict()
mostFrequent = dict()
for fname in files:
    with open('data/'+fname) as f:   
        content = f.read()
        # print(content)
    words = [ word.strip('􏰇|©􏰆􏰄􏰅!@#$%^&*()-_=+,.;:?/<>\'\`􏰀􏰁[]') for word in content.split()]
    #print(words)
    short_words = [w for w in words if len(w)<=4]
    #print(short_words)
    dicts[fname] = freq_Table(words)
    small_dicts[fname] = freq_Table(short_words)
    mostFrequent[fname] = most_freq(small_dicts[fname], 10)

#print(mostFrequent)

def print_result(dicts):
    unknown = dicts.pop('unknown-lang.txt')
    known = dicts

    ###################
    total_difference = dict()
    min_difference = 1
    answer = unknown
    for f in dicts.keys():
        total_difference[f] = 0
        for k, v in known[f].items():
            total_difference[f] += abs(v - unknown.get(k, 0))
        if min_difference > total_difference[f]:
            min_difference = total_difference[f]
            answer = f
    
    print("language with smallest total di􏰂fference is", answer)

print_result(dicts)
'''   
unknown = mostFrequent.pop('unknown-lang.txt')
known = mostFrequent

###################
total_difference = dict()
min_difference = 1
answer = unknown
for f in mostFrequent.keys():
    total_difference[f] = 0
    for k, v in mostFrequent[f].items():
        total_difference[f] += abs(v - unknown.get(k, 0))
    if min_difference > total_difference[f]:
        min_difference = total_difference[f]
        answer = f

print("language with smallest total di􏰂erence is", answer)
'''