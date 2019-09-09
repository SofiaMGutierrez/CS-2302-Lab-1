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

my_set = {line.strip() for line in open('words_alpha.txt')} #loads file into a new set and gets rid of any space and new-lines
chosen_word = input("Enter a word or empty string to finish: ")

if (chosen_word in my_set) == False: #checks if user input is found within the file
    print("Word not found")
    sys.exit()
else:
    start_time = time.time()
    def create_anagram(r_letters, s_letters):
        if len(r_letters) == 0:
            # Base case: All letters used
                print(s_letters)
        else:
            # Recursive case: For each call to scramble()
            # move a letter from remaining to scrambled
            for i in range(len(r_letters)):
                # The letter at index i will be scrambled
                scramble_letter = r_letters[i]

                # Remove letter to scramble from remaining letters list
                remaining_letters = r_letters[:i] + r_letters[i+1:]

                # Scramble letter
                create_anagram(remaining_letters, s_letters + scramble_letter)

    #method returns True if chosen_word contains a duplicate element
    #method returns False if chosen_word contains a duplicate element
    def check_duplicate(chosen_word):
        if len(chosen_word) == 1:
            return False
        else:
            r_letters = chosen_word[1:]
            if chosen_word[0] == r_letters:
                return True
            else:
                return check_duplicate(chosen_word[1:])
    
    #attempts to create a second set of the word's prefixes
    def prefix_set(my_set):
        for i in my_set:
            split_word = str.split(i)[0]
            second_set = {}
            print(split_word[0])

    create_anagram(chosen_word, '')
    print("It took %s seconds to find the anagrams" % (time.time() - start_time))
    check_duplicate(chosen_word)
    #prefix_set(my_set)