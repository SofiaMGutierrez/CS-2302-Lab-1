#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:19:50 2019
Course: CS 2302
Author: Sofia Gutierrez
Lab #1: Program created to receive a word from the user and print all the anagrams of that word.
Instructor: Olac Fuentes
T.A.: Anindita Nath
"""
import sys
import time

#loads file into a set 
#deletes any space and lines
words_set = {line.strip() for line in open(r'words_alpha.txt')}
user_word = input("Enter a word or empty string to finish: ")
if (len(user_word) < 1):
    print("Bye, thanks for using this program!")
    sys.exit()

start_time = time.time()
def scramble(r_letters, s_letters, permutations):
    """
    Output every possible combination of a word.
    Each recursive call moves a letter from
    r_letters (remaining letters) to
    s_letters (scrambled letters)
    """
    if len(r_letters) == 0:
        permutations.append(s_letters)
    else:
        # Recursive case: For each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(r_letters)):
            # The letter at index i will be scrambled
            scramble_letter = r_letters[i]
            
            # Remove letter to scramble from remaining letters list
            remaining_letters = r_letters[:i] + r_letters[i+1:]
            
            # Scramble letter
            scramble(remaining_letters, s_letters + scramble_letter, permutations)

permutations = [] #all the permutations of user's word
scramble(user_word, '', permutations)

#will check the list of permutations and only add the permutations 
#found within words_set to a new list of permutations
#this new list will still contain duplicates
def perms(permutations, new_perm_list): #
    for i in range(len(permutations)):
        true_false = permutations[i] in words_set
        if(true_false == True):
            new_perm_list.insert(i, permutations[i]) #inserts ith permutation at [i]

new_perm_list = []
perms(permutations, new_perm_list)

#will remove any duplicates found within the new set of permutations
def remove_dups(new_perm_list, final_anagrams):
    for i in new_perm_list: #iterates through list of words
        if i not in final_anagrams:
            final_anagrams.append(i)
    final_anagrams.remove(final_anagrams[0]) #removes user's word from list

final_anagrams = []
remove_dups(new_perm_list, final_anagrams)

final_anagrams.sort() #sorts list alphabetically
print("The word " + user_word + " has the following " + str(len(final_anagrams)) + " anagrams:")
for x in final_anagrams:
    print(x)
print("It took %s seconds to find the anagrams" % (time.time() - start_time))

#Part 2
start_time = time.time()
def prefix_set(user_word, prefix):
    for x in range(1, len(user_word)):
        prefix.add(user_word[:x])
    return prefix

prefix = set()
prefix_set(user_word, prefix)

#method returns 1 if chosen_word contains a duplicate element
#method returns 0 if chosen_word does not contain a duplicate element
def check_duplicate(word):
    for i in range(len(word)-1):
        for j in range(len(word)-1):
            if word[i] == word [j+1]:
                return True
        return False
True_or_False2 = check_duplicate(word)

user_word2 = input("Enter another word or empty string to finish: ")
if (len(user_word2) < 1):
    print("Bye, thanks for using this program!")
    sys.exit()
    
start_time = time.time()
def scramble2(r_letters, s_letters, permutations):
    """
    Output every possible combination of a word.
    Each recursive call moves a letter from
    r_letters (remaining letters) to
    s_letters (scrambled letters)
    """
    if len(r_letters) == 0:
        permutations.append(s_letters)
    else:
        # Recursive case: For each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(r_letters)):
            # The letter at index i will be scrambled
            scramble_letter = r_letters[i]
            
            # Remove letter to scramble from remaining letters list
            remaining_letters = r_letters[:i] + r_letters[i+1:]
            
            # Scramble letter
            scramble(remaining_letters, s_letters + scramble_letter, permutations)

permutations2 = [] #all the permutations of user's word
scramble2(user_word2, '', permutations2)

#will check the list of permutations and only add the permutations 
#found within words_set to a new list of permutations
#this new list will still contain duplicates
def perms2(permutations2, new_perm_list2): #
    for i in range(len(permutations2)):
        true_false = permutations2[i] in words_set
        if(true_false == True):
            new_perm_list2.insert(i, permutations2[i]) #inserts ith permutation at [i]

new_perm_list2 = []
perms2(permutations2, new_perm_list2)

def duplicates(new_perm_list2, final_anagrams2):
    for i in new_perm_list2: #iterates through list of words
        if i not in final_anagrams2:
            final_anagrams2.append(i)
    final_anagrams2.remove(final_anagrams2[0]) #removes user's word from list

final_anagrams2 = []
duplicates(new_perm_list2, final_anagrams2)

final_anagrams2.sort() #sorts list alphabetically
print("The word " + user_word2 + " has the following " + str(len(final_anagrams2)) + " anagrams:")
for x in final_anagrams:
    print(x)
print("It took %s seconds to find the anagrams" % (time.time() - start_time))