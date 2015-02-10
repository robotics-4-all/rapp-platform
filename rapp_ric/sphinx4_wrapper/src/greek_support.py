#!/usr/bin/env python
# -*- coding: utf-8 -*-

#MIT License (MIT)

#Copyright (c) <2014> <Rapp Project EU>

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

# Authors: Athanassios Kintsakis, Manos Tsardoulias
# contact: akintsakis@issel.ee.auth.gr, etsardou@iti.gr


import rospy
import sys
import rospkg
import mmap

from limited_vocabulary_creator import *

class GreekSupport:

  def __init__(self):
    
    self.generic_sphinx_configuration = {}
    self.limited_sphinx_configuration = {}

    self.vocabulary = LimitedVocabularyCreator()
    rospack = rospkg.RosPack()
    # TODO: Split the rapp_sphinx4_java_libraries package into libraries and
    # language models
    self.greek_dictionary = rospack.get_path('rapp_sphinx4_java_libraries')   
    # NOTE: This does not exist yet
    self.greek_dictionary = self.greek_dictionary + \
        "/englishPack/cmudict-en-us.dict"
    
    self.sphinx4_jars = rospack.get_path('rapp_sphinx4_java_libraries')   
    self.sphinx4_class_path = rospack.get_path('sphinx4_wrapper')   
    
    jar_path = ".:" + self.sphinx4_jars + "/sphinx4-core-1.0-SNAPSHOT.jar:" \
            + self.sphinx4_class_path + "/src"

    # Grammar is dummy here..
    # NOTE: Fix this according to the generic Greek model
    self.generic_sphinx_configuration = { \
      'jar_path' : jar_path, \
      'configuration_path' : self.sphinx4_jars+"/greekPack/default.config.xml", \
      'acoustic_model' : self.sphinx4_jars + "/englishPack/en-us/", \
      'grammar_name' : 'hello', \
      'grammar_folder' : self.sphinx4_jars+"/greekPack/", \
      'dictionary' : self.sphinx4_jars + "/englishPack/cmudict-en-us.dict", \
      'language_model' : self.sphinx4_jars + "/englishPack/en-us.lm.dmp", \
      'grammar_disabled' : True
      }
    
    # Open the generic english dictionary file
    # NOTE: Fix this according to the Greek generic dictionary
    #try:
      #self.english_dict_file = open(self.english_dictionary, 'r')
    #except IOError:
      #print "English dictionary could not be opened!"
    # Create a mapping of the file
    #self.english_dict_mapping = mmap.mmap(self.english_dict_file.fileno(), 0, \
        #access = mmap.ACCESS_READ)

    self.configureLetters()

  def configureLetters(self):

    self.capital_letters = {}
    self.capital_letters[(u'Α').encode('utf-8')] = (u'α').encode('utf-8')
    self.capital_letters[(u'Ά').encode('utf-8')] = (u'ά').encode('utf-8')
    self.capital_letters[(u'Β').encode('utf-8')] = (u'β').encode('utf-8')
    self.capital_letters[(u'Γ').encode('utf-8')] = (u'γ').encode('utf-8')
    self.capital_letters[(u'Δ').encode('utf-8')] = (u'δ').encode('utf-8')
    self.capital_letters[(u'Ε').encode('utf-8')] = (u'ε').encode('utf-8')
    self.capital_letters[(u'Έ').encode('utf-8')] = (u'έ').encode('utf-8')
    self.capital_letters[(u'Ζ').encode('utf-8')] = (u'ζ').encode('utf-8')
    self.capital_letters[(u'Η').encode('utf-8')] = (u'η').encode('utf-8')
    self.capital_letters[(u'Ή').encode('utf-8')] = (u'ή').encode('utf-8')
    self.capital_letters[(u'Θ').encode('utf-8')] = (u'θ').encode('utf-8')
    self.capital_letters[(u'Ι').encode('utf-8')] = (u'ι').encode('utf-8')
    self.capital_letters[(u'Ί').encode('utf-8')] = (u'ί').encode('utf-8')
    self.capital_letters[(u'Ϊ').encode('utf-8')] = (u'ϊ').encode('utf-8')
    self.capital_letters[(u'Κ').encode('utf-8')] = (u'κ').encode('utf-8')
    self.capital_letters[(u'Λ').encode('utf-8')] = (u'λ').encode('utf-8')
    self.capital_letters[(u'Μ').encode('utf-8')] = (u'μ').encode('utf-8')
    self.capital_letters[(u'Ν').encode('utf-8')] = (u'ν').encode('utf-8')
    self.capital_letters[(u'Ξ').encode('utf-8')] = (u'ξ').encode('utf-8')
    self.capital_letters[(u'Ο').encode('utf-8')] = (u'ο').encode('utf-8')
    self.capital_letters[(u'Ό').encode('utf-8')] = (u'ό').encode('utf-8')
    self.capital_letters[(u'Π').encode('utf-8')] = (u'π').encode('utf-8')
    self.capital_letters[(u'Ρ').encode('utf-8')] = (u'ρ').encode('utf-8')
    self.capital_letters[(u'Σ').encode('utf-8')] = (u'σ').encode('utf-8')
    self.capital_letters[(u'Τ').encode('utf-8')] = (u'τ').encode('utf-8')
    self.capital_letters[(u'Υ').encode('utf-8')] = (u'γ').encode('utf-8')
    self.capital_letters[(u'Ύ').encode('utf-8')] = (u'ύ').encode('utf-8')
    self.capital_letters[(u'Ϋ').encode('utf-8')] = (u'ϋ').encode('utf-8')
    self.capital_letters[(u'Φ').encode('utf-8')] = (u'φ').encode('utf-8')
    self.capital_letters[(u'Χ').encode('utf-8')] = (u'χ').encode('utf-8')
    self.capital_letters[(u'Ψ').encode('utf-8')] = (u'ψ').encode('utf-8')
    self.capital_letters[(u'Ω').encode('utf-8')] = (u'ω').encode('utf-8')
    self.capital_letters[(u'Ώ').encode('utf-8')] = (u'ώ').encode('utf-8')

    self.phonems = {}
    self.phonems[(u'ου').encode('utf-8')] = 'UW '
    self.phonems[(u'ού').encode('utf-8')] = 'UW '
    self.phonems[(u'μπ').encode('utf-8')] = 'B '
    self.phonems[(u'ντ').encode('utf-8')] = 'D '
    self.phonems[(u'γκ').encode('utf-8')] = 'G ' #?
    self.phonems[(u'γγ').encode('utf-8')] = 'G ' #?
    self.phonems[(u'τσ').encode('utf-8')] = 'CH ' #?
    self.phonems[(u'τζ').encode('utf-8')] = 'JH ' #?
    
    self.two_digit_letters = {}
    self.two_digit_letters[(u'αι').encode('utf-8')] = 'EH '
    self.two_digit_letters[(u'αί').encode('utf-8')] = 'EH '
    self.two_digit_letters[(u'ει').encode('utf-8')] = 'IH '
    self.two_digit_letters[(u'εί').encode('utf-8')] = 'IH '
    self.two_digit_letters[(u'οι').encode('utf-8')] = 'IH '
    self.two_digit_letters[(u'οί').encode('utf-8')] = 'IH '
    self.two_digit_letters[(u'υι').encode('utf-8')] = 'IH '
    self.two_digit_letters[(u'υί').encode('utf-8')] = 'IH '

    self.s_specific_rules = {}
    self.s_specific_rules[(u'σγ').encode('utf-8')] = 'Z W '
    self.s_specific_rules[(u'σβ').encode('utf-8')] = 'Z V '
    self.s_specific_rules[(u'σδ').encode('utf-8')] = 'Z DH '

    self.letters = {}
    self.letters[(u'α').encode('utf-8')] = 'AA ' # when AE?
    self.letters[(u'ά').encode('utf-8')] = 'AA '
    self.letters[(u'β').encode('utf-8')] = 'V '
    self.letters[(u'γ').encode('utf-8')] = 'W '
    self.letters[(u'δ').encode('utf-8')] = 'DH '
    self.letters[(u'ε').encode('utf-8')] = 'EH '
    self.letters[(u'έ').encode('utf-8')] = 'EH '
    self.letters[(u'ζ').encode('utf-8')] = 'Z '
    self.letters[(u'η').encode('utf-8')] = 'IH '
    self.letters[(u'ή').encode('utf-8')] = 'IH '
    self.letters[(u'θ').encode('utf-8')] = 'TH '
    self.letters[(u'ι').encode('utf-8')] = 'IH '
    self.letters[(u'ί').encode('utf-8')] = 'IH '
    self.letters[(u'ϊ').encode('utf-8')] = 'IH '
    self.letters[(u'ΐ').encode('utf-8')] = 'IH '
    self.letters[(u'κ').encode('utf-8')] = 'K '
    self.letters[(u'λ').encode('utf-8')] = 'L '
    self.letters[(u'μ').encode('utf-8')] = 'M '
    self.letters[(u'ν').encode('utf-8')] = 'N '
    self.letters[(u'ξ').encode('utf-8')] = 'K S '
    self.letters[(u'ο').encode('utf-8')] = 'OW '
    self.letters[(u'ό').encode('utf-8')] = 'OW '
    self.letters[(u'π').encode('utf-8')] = 'P '
    self.letters[(u'ρ').encode('utf-8')] = 'R '
    self.letters[(u'σ').encode('utf-8')] = 'S '
    self.letters[(u'τ').encode('utf-8')] = 'T '
    self.letters[(u'υ').encode('utf-8')] = 'IH '
    self.letters[(u'ύ').encode('utf-8')] = 'IH '
    self.letters[(u'ϋ').encode('utf-8')] = 'IH ' 
    self.letters[(u'ΰ').encode('utf-8')] = 'IH '
    self.letters[(u'φ').encode('utf-8')] = 'F '
    self.letters[(u'χ').encode('utf-8')] = 'HH '
    self.letters[(u'ψ').encode('utf-8')] = 'P S '
    self.letters[(u'ω').encode('utf-8')] = 'OW '
    self.letters[(u'ώ').encode('utf-8')] = 'OW '
    self.letters[(u'ς').encode('utf-8')] = 'S '

    self.literal_letters = {}
    self.literal_letters[(u'α').encode('utf-8')] = 'a' # when AE?
    self.literal_letters[(u'ά').encode('utf-8')] = 'a'
    self.literal_letters[(u'β').encode('utf-8')] = 'v'
    self.literal_letters[(u'γ').encode('utf-8')] = 'g'
    self.literal_letters[(u'δ').encode('utf-8')] = 'd'
    self.literal_letters[(u'ε').encode('utf-8')] = 'e'
    self.literal_letters[(u'έ').encode('utf-8')] = 'e'
    self.literal_letters[(u'ζ').encode('utf-8')] = 'z'
    self.literal_letters[(u'η').encode('utf-8')] = 'i'
    self.literal_letters[(u'ή').encode('utf-8')] = 'i'
    self.literal_letters[(u'θ').encode('utf-8')] = 'th'
    self.literal_letters[(u'ι').encode('utf-8')] = 'i'
    self.literal_letters[(u'ί').encode('utf-8')] = 'i'
    self.literal_letters[(u'ϊ').encode('utf-8')] = 'i'
    self.literal_letters[(u'ΐ').encode('utf-8')] = 'i'
    self.literal_letters[(u'κ').encode('utf-8')] = 'k'
    self.literal_letters[(u'λ').encode('utf-8')] = 'l'
    self.literal_letters[(u'μ').encode('utf-8')] = 'm'
    self.literal_letters[(u'ν').encode('utf-8')] = 'n'
    self.literal_letters[(u'ξ').encode('utf-8')] = 'ks'
    self.literal_letters[(u'ο').encode('utf-8')] = 'o'
    self.literal_letters[(u'ό').encode('utf-8')] = 'o'
    self.literal_letters[(u'π').encode('utf-8')] = 'p'
    self.literal_letters[(u'ρ').encode('utf-8')] = 'r'
    self.literal_letters[(u'σ').encode('utf-8')] = 's'
    self.literal_letters[(u'ς').encode('utf-8')] = 's'
    self.literal_letters[(u'τ').encode('utf-8')] = 't'
    self.literal_letters[(u'υ').encode('utf-8')] = 'u'
    self.literal_letters[(u'ύ').encode('utf-8')] = 'u'
    self.literal_letters[(u'ϋ').encode('utf-8')] = 'u' 
    self.literal_letters[(u'ΰ').encode('utf-8')] = 'u'
    self.literal_letters[(u'φ').encode('utf-8')] = 'f'
    self.literal_letters[(u'χ').encode('utf-8')] = 'x'
    self.literal_letters[(u'ψ').encode('utf-8')] = 'ps'
    self.literal_letters[(u'ω').encode('utf-8')] = 'o'
    self.literal_letters[(u'ώ').encode('utf-8')] = 'o'


  def transformWords(self, words):
    enhanced_words = {}
    englified_words = {}
    for word in words:
      initial_word = word
      # transform capital letters
      for cap in self.capital_letters:
        initial_word = initial_word.replace(cap, self.capital_letters[cap])
      # fix english version of letters
      eng_w = initial_word
      for lit in self.literal_letters:
        eng_w = eng_w.replace(lit, self.literal_letters[lit])
      englified_words[eng_w] = word
      # check phonems
      for ph in self.phonems:
        initial_word = initial_word.replace(ph, self.phonems[ph])
      # check two-digit letters
      for let in self.two_digit_letters:
        initial_word = initial_word.replace(let, self.two_digit_letters[let])
      # check specific rules
      for sr in self.s_specific_rules:
        initial_word = initial_word.replace(sr, self.s_specific_rules[sr])
      # check the rest of the letters
      for l in self.letters:
        initial_word = initial_word.replace(l, self.letters[l])
      
      enhanced_words[eng_w] = []
      temp = initial_word.split(' ')
      if len(temp) > 0:
        temp = temp[:-1]
      enhanced_words[eng_w] = temp
    
    return [enhanced_words, englified_words]

  def englify_words(self, words):
    englified_words = []
    for word in words:
      eng_w = word
      for lit in self.literal_letters:
        eng_w = eng_w.replace(lit, self.literal_letters[lit])
      englified_words.append(eng_w)
    return englified_words


  def getLimitedVocebularyConfiguration(self, words, grammar, sentences):
    enhanced_words = {}
    # NOTE: The following should work with the Greek generic dictionary
    #for word in words:
      #index = self.english_dict_mapping.find("\n" + word + " ") 
      #if  index == -1:
        #print "ERROR: Word " + word + " does not exist in the English Dictionary"
      #else:
        #self.english_dict_file.seek(index + 1) # +1 because of the extra \n
        #line = self.english_dict_file.readline()
        #line = line[:-1] # to erase the \n
        #split_line = line.split(" ")
        #enhanced_words[split_line[0]] = []
        #for i in range(1, len(split_line)):
          #enhanced_words[split_line[0]].append(split_line[i])

    [tr_words, englified] = self.transformWords(words)
    #for w in tr_words:
      #print w + " = "
      #for p in tr_words[w]:
        #print p + ' '
      #print "\n"
    #for en in englified:
      #print en + " " + englified[en] + '\n'
    englified_grammar = self.englify_words(grammar)    
    englified_sentences = self.englify_words(sentences)    
    self.limited_sphinx_configuration = \
        self.vocabulary.createConfigurationFiles(tr_words, englified_grammar , \
        englified_sentences)
    return self.limited_sphinx_configuration
  
  def getGenericConfiguration(self):
    return self.generic_sphinx_configuration