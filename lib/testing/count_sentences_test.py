#!/usr/bin/env python3


import io
import sys

class TestMyString:
    '''MyString in count_sentences.py'''

    def test_is_class(self):
        '''is a class with the name "MyString".'''
       
        

    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
      
        sys.stdout = sys.__stdout__
      
    def test_is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        
        

    def test_is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        

    def test_is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
      
    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
      
        
       
        