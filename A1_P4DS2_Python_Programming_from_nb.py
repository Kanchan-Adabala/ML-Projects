
def display(x):
    pass

class DummyIpython:
      def system(self,_):
          pass
      def set_next_input(self,_):
          pass
      def run_line_magic(self,_1,_2):
          pass
        
def get_ipython():
    return DummyIpython()
#!/usr/bin/env python
# coding: utf-8

# ## P4DS Assignment 1, Autumn 2021
# 
# # Python Programming
# 
# ### Brandon Bennett
# 
# #### Last modified: 3rd October 2021 (BB)
# 
# This coursework is intended to develop and test skills in defining basic algorithmic functions in Python, with an emphasis on types of function for processing, transforming and classifying. Completing this set of tasks should give you a very good
# grounding in the fundamental programming techiniques required for DataScience.
# 
# In this exercise we are only using a limited set of library modules. This is to
# ensure you master the kinds of algorithms required rather than relying on
# pre-programmed functions provided by Python packages. 
# 
# **Do not import any module other than those already imported into this file**.
# 
# In other words do not add `import` statements in any code you write
# for this assignment. And, of course, do not add extra packages to the
# `import` statements that are already in the code.
# 
# ### Form of the Assignment
# 
# Your work will consist of defining a number of functions according to given specifications.
# 
# You will be given a bare skeleton function just giving the function name, arguments and a dummy return value.
# 
# You need to edit the functions so that for any input of the expected type, the
# result returned will fit the given specification.
# 
# For the grading I will **not** try to catch you out by giving inputs of the
# wrong type (such as a number instead of a string) or names of files that
# do not exist. It is not that kind of programming course.
# 
# You will be able to check that your functions are working correctly, by running a testing function defined in the Python file `A1_P4DS2_Python_Programming_tests.py`. You should download this and put it in the same directory as this file (`A1_P4DS2_Python_Programming.ipynb`).
# 
# * <a href="https://teaching.bb-ai.net/P4DS/assignments/A1_P4DS2_Python_Programming_tests.py" download>
#     A1_P4DS2_Python_Programming_tests.py</a>
#     
# **Note:** The tests carried out by the testing module provided in this file 
# are similar to but not the same as those that will be used for the final grading. 
# The functions you define need to satisfy the general requirements that are 
# specified, otherwise you may lose marks when the final grading is done using
# other tests.
#     
# When answering the questions below, you can just modify the given template cell. You don't need to create a new cell for your definition. But make sure you do not alter the name of the function or the number and type of its arguments, otherwise the automatic testing/grading function will not work correctly.
# 
# Please look at the prelimiary formative assignment notebook `A0_Warm_Up.ipynb` for further explanation
# and the assignment format and illustratons of the using the testing functions.

# ### Questions overview:
# 
# 
# * __Q1. Anagrams and Palindromes__
#   - __(a)__ Test whether two strings are anagrams.   (4 marks)
#   - __(b)__ Test if a given string is a palindrome.  (4 marks)
#   
#   
# * __Q2. Using a data file of English words__
#   - __(a)__ Test, whether a string is an English word  (5 marks)
#   - __(b)__ Find Anagrams of a given word              (4 marks)
#   - __(c)__ Identify English words of a given length that are palindromes. (2 marks)
#   - __(d)__ Password checker that rejects passwords that are English words. (5 marks)
# 
# 
# * __Q3. A Simple Holiday Recommendation System__
#    - __(a)__ `available_features` function   (2 marks)
#    - __(b)__ `recommend_holidays` function   (4 marks)
#    
# #### Total marks: 30
# 

# ### Importing the Testing Module
# In order to run the function tests provided for you to check you code
# you will need to first run the following cell, which imports the
# testing module for this assignment. (As mentioned above, the tests used
# for final grading of this assignment may be different from the specific
# tests carried out by this module.)

# In[1]:


from A1_P4DS2_Python_Programming_tests import do_tests, do_all_tests, tests_version

tests_version()


# 
# ## Q1. Identify Anagrams and Palindromes
# 
# This question involves determining properties of words and
# identifying words with those properties. 

# ### Q1 (a) Test whether two strings are anagrams
# 
# * Two words are _anagrams_ if they both contain the same letters
# but in different orders. For example __listen__
# is an anagram of __silent__.
# 
# Write a Boolean valued function `anagrams(s1, s2)`, which returns `True` just in case the string `s1` contains the same letters as string `s2` but in a _different order_. The function should be case insensitive --- in other words it should return the same value if any letters in either s1 or s2 are changed from upper to lower case or from lower to upper case. You may assume that the input strings contain only letters.
# 
# #### Examples
# 
# | INPUT 1 (string)|	INPUT 2 (string) |	OUPUT (boolean) |
# |--|--|--|
# |`"sidebar"`| `"seabird"` |	`True` |
# |`"cheese"` | `"frizbee"` |	`False`|
# |`"listen"` | `"silent"`  |	`True` |
# |`"this"`   | `"this"`    |	`False`|
# |`"Tar"`    | `"Rat"`	  |`True`  |
# |`"Tar"`    | `"TAR"`	  |`False` |

# In[3]:


## Q2(a) answer code cell
## Modify this function definition to fulfill the given requirements.
## Expected code length: less than 10 lines.

def anagrams( s1, s2 ):
    ## replace the 'pass' command (which does nothing) with code that
    ## computes and returns the requried result for any strings s1 and s2
    s1 = s1.lower()
    s2 = s2.lower()
    
    if (len(s1) == len(s2)) :
        sorteds1 = sorted(s1)
        sorteds2 = sorted(s2)
        
        if ((sorteds1 == sorteds2) and (s1 != s2) ):
            return True
        else :
            return False 
    


# In[4]:


# Run this cell to test your is_english_word function
# The testing module have been imported (see above)
# You must also have run the cell with your anagrams definition.
do_tests( anagrams )


# ### Q1 (b) Test whether a string is a palindrome
# 
# * A word is a _palindrome_ if it is the same forward and backward. In other words, reversing the order of its letters
# results in the same word. For instance, __bob__, __rotator__. The term palindrome
# is also applied to sentences, which may contain spaces and punctuation marks as well as
# letters. When considering whether a sentence is a palindrome, the punctuation 
# marks and the case of the letters are usually ignored.
# 
# Define a function `is_palindrome(s)` that it `return`s `True` if the given string is a palindrome, otherwise `return`s `False`.
# 
# More specifically, the function should return true if,
#  the alphabetic characters in the input string form the same sequence
# if they are read forward as if they are read backwards.
# Any non-alphabet characters, such as spaces and punctuation marks should be ignored, and letter characters are considered to be the same if one is lower case and the other is upper case. Thus the string `"Do geese see God?"` is counted as a palindrome,
# so the function should `return` `True` for this string.
# 
# #### Examples:
# | Input | Output |
# |------|------|
# |`"Bob"` | `True` |
# |`"God"` | `False` |
# |`"Abba"` | `True` |
# |`"No lemon, no melon"` | `True`|
# |`"I love Python!"` | `False`|

# In[5]:


## Q2(c) answer code cell
## Modify this function definition to fulfill the given requirements
## Expected code length: less than 10 lines.

def is_palindrome(s):
    s = s.lower()
    s = s.strip()
    s = ''.join(e for e in s if s.isalnum())
    reversedstr = ''.join(reversed(s))
    
    if  reversedstr == s:
        return True
    else :
        return False
    


# In[6]:


# Run this cell to test your is_palindrome function
# The tests module must have been imported (see above).
do_tests(is_palindrome)


# ## Q2. Using a Data File of English Words
# 
# For this task you will deal with your first file of data!
# It is an alphabetical list of a large number of
# English words.
# You should have a look at it in an editor or view it in
# a browser to see what the contents look like.
# 
# This file contains contains nearly all common English words:
# 
# * ```english_words.txt```
# <a href="https://teaching.bb-ai.net/P4DS/assignments/english_words.txt.wrap.html" 
#    download>
#     [View]</a>
# <a href="https://teaching.bb-ai.net/P4DS/assignments/english_words.txt" 
#    download="english_words.txt">
#     [Download]*</a>
#       
#     \* You may need to right click to download, or first go to View and download
#     from there.<br> (Jupyter seems to display the file even though this is supposed 
#     to be a _download_ link.)
# 
# I also provide the following code which initialises the global variable `ENGLISH_WORDS` to be a **set** of all the words in the file `english_words.txt`. You will need to have that file in the same folder as this notebook file.

# In[7]:


def get_english_words():
    with open( "english_words.txt" ) as f:
         words = f.readlines()
    words = { word.strip() for
             word in words }
    return words

ENGLISH_WORDS = get_english_words()

#ENGLISH_WORDS


# You are recommended to use the `ENGLISH_WORDS` variable in the following questions, whenever you are required to perform a calculation involving all the words in `english_words.txt`. This is particularly important for a function that
# needs to check the list of words many times. Reading information from a file typically takes more computational time than other operations, so if data can be stored in memory (e.g. as the value of a Python variable) this will usually be a lot more efficient than reading it from a file each time it is needed. (Of course, when dealing with very large datasets, it may not be possible to store the whole dataset in memory.)

# ### Q2 (a) Check whether a string is an English word
# 
# Write a function `is_english_word(s)`, which will test if its input string `s` is an English word, according to the file english_words.txt. This file contains a large number of English words, including all common words and many very rare words. Proper names are not included, and all words are given in lower case, with one word on each line of the file.
# You need to download the file of English words. Note that it is not a program file and you do not need to edit it. 
# 
# 
# Your function `is_english_word(s)` should take any string as its argument and return a Boolean value --- i.e. `True` or `False`. More specifically your function should return `True` if _any_ of the following conditions hold:
# * The input string is one of the words in `english_words.txt`.
# * The input string is the same as one of the of the words in `english_words.txt` except that the input string starts with a capital letter (with all the other letters being small).
# * The input string is the same as one of the words in `english_words.txt` except that the input string is all in capital letters.
# * The input string contains only alphabetic characters and is one of the 100 most
#   common words in the English language. (One would expect all such words to be listed in `english_words.txt`, but maybe you should check.)
# 
# If none of these conditions hold, your function should return `False`.
# 
# #### Examples:
# 
# | INPUT |	OUPUT |
# |-------|---------|
# |`"python"`| `True`|
# |`"Python"`| `True`|
# |`"PYTHON"`| `True`|
# |`"pyThon"`| `False`|
# |`"splap"` | `False`|

# In[8]:


## Modify this function definition to fulfill the given requirements.
## Expected code length: less than 15 lines.

def is_english_word(s):
    if (s.islower() or s.isupper() or s.istitle()):
        string = s.lower()
        if(string in ENGLISH_WORDS):
            return True
        else:
            return False
    else:
        return False
         
        


# In[9]:


# Run this cell to test your is_english_word function
# The testing module must have been imported (see above)
do_tests(is_english_word)


# ### Q2 (b) Find all anagrams of a word
# Write a function `find_all_anagrams(string)`, which take a string as input and returns a list, in alphabetical order, of all words in the file `english_words.txt` that are anagrams of the input string.
# 
# More specifically given an input string the function should return a list  `[word_1, ..., word_n]`, of words in alphabetical order, which contains every word in the dictionary file such that the value of the function `anagrams(string,word_i)` is `True` (as specified in __Q2(a)__ of this coursework), and contains no other words.
# 
# #### Examples
# |INPUT          |	OUPUT                  |
# |---------------|--------------------------|
# |`'cheese'`     |	`[]`                   |
# |`'Python'`     |	`['phyton', 'typhon']` |
# |`'relating'`	| ```['alerting', 'altering', 'integral', 'tanglier', 'triangle']``` |
# 
# Note:
# Though the instructions for this question are quite brief, they do exactly specify the requirements for this function.
# Since you should have already defined the `anagrams(s1,s2)` function for part **Q2(a)**, you should call this function in your definition of the `find_all_anagrams(string)` function. It is much better programming style to do that, rather than repeat the full code for checking anagrams within ```find_all_anagrams(string)``.

# In[9]:


## Q2(b) answer code cell
## Modify this function definition to fulfill the given requirements.
## Expected code length: less than 5 lines.

def find_all_anagrams(s):
    listofWords = [ ]
    s = s.lower()
    for s1 in ENGLISH_WORDS:
        if anagrams(s,s1):
            listofWords.append(s1)
    listofWords = sorted(listofWords)
    return listofWords
        


# In[10]:


# Run this cell to test your find_all_anagrams function
# The testing module must have been imported (see above)
do_tests( find_all_anagrams )


# ### Q2 (c) Find palindromes of length `n` (in `english_words.txt`)
# 
# Define a function `find_all_palindromes(n)` that returns, in alphabetical order, the list of all palindromes in `english_words.txt` that are `n` letters long.

# In[11]:


## Q2(d) answer code cell
## Modify this function definition to fulfill the given requirements.
## Expected code length: less than 5 lines.

def find_palindromes_of_length(n):
    listofwords = []
    for s1 in ENGLISH_WORDS :
            if ((len(s1) == n) and (is_palindrome(s1))):
                    listofwords.append(s1)
                    listofwords = sorted(listofwords)
    return listofwords 
                


# In[12]:


# Run this cell to test your find_palindromes_of_length
# The testing module must have been imported (see above)
do_tests( find_palindromes_of_length )


# 
# ### Q2 (d) Literate Password Checker (6 marks)
# 
# Computer systems are vulnerable to hacking if they can be
# accessed by passwords based on English words.
# Now that we have access to the set of English words, we can
# define a tougher password checker.
# 
# An institution uses the following rules to classify the strength of passwords:
# 
# * A string is an ILLEGAL password if either:
#   * it is an English word (as defined above)
#   * it contains any invisible character (space, tab, newline)
# 
# 
# * A string is a WEAK password if it is **not** ILLEGAL and, either:
#   * it is _less than_ 8 characters long.
#   * it is an English word followed by one or more decimal digit characters
# 
# 
# * A string is a STRONG password if it is **not** ILLEGAL and, either:
#   * it contains at least 12 characters
#   * AND it contains at least 1 lower case letter
#   * AND it contains at least 1 capital letter
#   * AND it contains at least 1 numerical digit
#   * AND it contains at least 1 special character (any visible ASCII
#     character that is not a letter or a number)
# 
# 
# * A string is a MEDIUM password if it is **not** an ILLEGAL password and
#   is **not** a WEAK password and is **not** a STRONG password.
# 
# You need to code a function ```password_strength``` that will take a string argument and will return the 'strength' of that string as a password, according to the rules given above. So it should return one of the strings  
# ```"ILLEGAL"```, 
# ```"STRONG"```, 
# ```"WEAK"``` or 
# ```"MEDIUM"```.
# 
# You may assume that the input password is consists of only ASCII characters,
# that is: alphabetic letters, numerical digits, special visible charactes,
# spaces, tabs and newlines. The special visible characters are:
# <pre>
# ~`!@#$%^&*(){}[]|\/:;";<>.?
# </pre>
# 
# 
# Examples:
# 
# | INPUT             | OUPUT |
# | -----             | --------|
# | ```"secret"```           |	```"ILLEGAL"``` |
# | ```"my secret"```           |	```"ILLEGAL"``` |
# | ```"qwertyu"```           |	```"WEAK"``` |
# | ```"hello123"```           |	```"WEAK"``` |
# | ```"7Kings8all9Pies!"``` |	```"STRONG"``` |
# | ```"brandon123"```      |	```"MEDIUM"``` |
# 

# In[13]:


## Edit this cell to give your answer for Q2(b)

def password_strength( password ):
    ## Add code to compute password strength
   # return "Hmm, not sure"  
    # should return the strength ("ILLEGAL", WEAK", "STRONG" or "MEDIUM")
    
    specialCharacters = """~`!@$%^&*(){}[]|\/:;";<>.?#"""
    if (is_english_word(password)) or (' ' in password) or ('\t' in password ) or ('\n' in password):
        return "ILLEGAL"
    else :
        if (len(password) < 8) or ((is_english_word(''.join(x for x in password if x.isalpha()))) and password.isalnum()) :
            return "WEAK"
        elif (len(password) > 12) or ((any(x.isupper() for x in password )) and (any(x.islower() for x in password )) and (any(x.isnumeric() for x in password )) and ( c in specialCharacters for c in password) and  not (is_english_word(''.join(x for x in password if x.isalpha()))))  :
                return "STRONG"
        else:
            return "MEDIUM"
        


# In[14]:


# Run this cell to test the password_strength function
# The testing module must have been imported (see above)
do_tests( password_strength )


# ## Q3. A Simple Holiday Recommender System

# To answer this question you will write functions that operate as a
# simple system for recommending holiday destinations based on the amount
# of money you have to spend and some desired features of your holiday.
# These requirements will be compared to data about possible holiday
# destinations in order to find those that match the cost and
# feature requirements.

# ### Q3 (b) Find Available Holiday Features
# For this part you should write a function `available_features` that
# takes two input parameters:
#  1. The maximum amount of money (represented as an integer) that someone is prepared to spend.
#  2. Holiday destination datalist.<br>
#     This is a list of lists of a form such as specified in the next code
#     cell. It contains records for a number of holiday destinations. Each
#     record is a list which gives the destination name, the cost of the 
#     holiday and a list of attributes associated with that destination.

# In[15]:


HOLIDAYS_EG = [ ["Scarborough",  45,  ["beach"]], 
                ["Whitby",       60,  ["beach", "culture"]],
                ["Barcelona",   320,  ["beach", "culture", "hot"]], 
                ["Corfu",       300,  ["beach", "hot"]],
                ["Paris",       250,  ["culture"]],
                ["Rome",        300,  ["culture", "hot"]],
                ["Switzerland", 450,  ["culture", "mountains"]],
                ["California",  750,  ["beach", "hot", "mountains"]],      
             ]       


# **NOTE:** `HOLIDAYS_EG` is just an example of the holiday data structure. **Your
# function should work with any similar structure**, which could have different
# destinations, costs and attribute lists (which may contain other attribute
# strings).
# 
# The value returned by `available_features` should be a list of all possible holiday features that
# are available from any holiday destination whose cost is less than or equal to the maximum amount
# specified by input parameter 1. This list should be ordered in _alphabetical order_.
# 
# Here are some examples shown as a table:
# 
# 
#  | parmeter 1 (cost) | parameter 2 (destination data) | return (feature list)|
#  | --     |  --      | -- |  
#  |   100  |   `HOLIDAYS_EG`    | `["Beach", "Culture"]` |
#  |   300  |   `HOLIDAYS_EG`    | `["Beach", "Culture", "Hot"]`  |
#  
#  **NOTE:** It need not be possible to have a holiday with all the possible features within the
#  price limit, even though each feature must be available for some destination within the price limit.

# In[16]:


## Edit this function definition to give your answer
def available_features( max_cost, holiday_data ):
    ## add your code here
    holiday_dat = [["Dubai" ,     250, ["Oasis","Desert","Arabian Food"]],
                    ["India" ,     180, ["Architecture","Cultural Heritage","Beach","Villages"]],
                    ["Singapore",  120, ["Shopping Malls","Fountains"]],
                    ["Florida",    500, ["Beach","Hot","Museums"]],
                    ["Egypt",      95,  ["Pyramids","Desert","Tombs"]],
                    ["Maldives",   400, ["Clear Waters","Relaxation","Underwater Restaurents"]],
                    ["Australia",  825, ["White Sands","Multi-storey buildings","Shopping"]],
                    ["Srilanka",   600, ["Sculptures","Whale watching","old colonisation"]]
                   ]

    
    features = []
    for t in holiday_data:
            if(t[1] <= max_cost):
                features.extend(t[2])
                features = sorted(list(dict.fromkeys(features)))
                #setfea = set(features)
                #features.clear()
                #features = sorted(list(setfea))
    return  features # not really
    # It should actually return list of holiday features


# In[17]:


# Run this cell to test the recommend_holidays function
# The testing module must have been imported (see above)
do_tests(available_features)


# ### Q3 (b) Find Possible Holiday Recommendations
# For this part you should write a function `recommend_holidays` that
# takes three inputs:
#  1. The maximum amount of money (represented as an integer) that someone is prepared to spend.
#  2. A list of attribute strings. These can be any strings but would normally
#     correspond to attributes that have been specified in the holiday destination
#     data parameter.
#  3. Holiday destination datalist, which is of the same for as specified for part **(a)**.
#     

# 
# 
# The value returned by `recommend_holidays` should be a list, _in alphabetical_ order,  of destinations that satisfy the requirements, i.e. cost less than or equal to the  maximum cost input and have **all** the features indicated by the desired features,  string.
# 
# Here are some examples shown as a table:
# 
# 
#  | parmeter 1 (cost) | parameter 2 (features) | parameter 3 (destination data) | return (destination list)|
#  | --     | --   | --      | -- |  
#  |   500  |     `["beach", "culture"]` | `HOLIDAYS_EG`    | ```["Barcelona", "Whitby"]``` |
#  |   100  |     `["beach"]`    |   `HOLIDAYS_EG`    |  ```["Scarborough", "Whitby"]``` |
#  |   500  |     `["hot", "beach"]`   |   `HOLIDAYS_EG`    |   ```["Barcelona", "Corfu"]``` |
#  |   350  |     `["hot", "hot", "hot"]`   |   `HOLIDAYS_EG`    |   ```["Barcelona", "Corfu", "Rome"]``` |
#  |   400  |     `["culture"]`    |   `HOLIDAYS_EG`    |   ```["Barcelona", "Paris", "Rome", "Whitby"]``` |
#  |   250  |     `["hot", "mountains", "culture"]`  |   `HOLIDAYS_EG`    |   ```[]``` |
#  |   100  |     `["hot", "python", "beach"]`  |   `HOLIDAYS_EG`    |   ```[]``` |
#  
#  
# Note that the second argument can be any list of strings. However, if it contains any string that is
# not a feature of any destination in the destination data, the value returned will be 
# the empty list, `[]`, since no destinations will match that requirement.

# In[18]:


## Edit this function definition to give your answer
def recommend_holidays( max_cost, attributes, holiday_data):
    ## add your code here

    destinations = []
    for a in attributes:
        for t in holiday_data:
            if( (t[1]<= max_cost)) :
                if all(a in t[2] for a in attributes): 
                    destinations.append(t[0])
                    destinations = sorted(list(dict.fromkeys(destinations)))
                
    return destinations
    # It should actually return list of all destinations that fit the requirements


# In[19]:


# Run this cell to test the recommend_holidays function
# The testing module must have been imported (see above)
do_tests(recommend_holidays)


# # Grading
# 
# The following code will run tests for all functions that count towards your grade for Coursework 1, and will calculate the final mark you will get for this piece of coursework. 
# 
# To get your grade simply select the "__Run All__" option from the Jupyter "__Cell__" menu above. Test results followed by your overal grade will be shown below.
# <br>
# You can do this at any point to get an indication of
# the marks you might obtain.
# 
# **NOTE:** The tests provided by the tesing module
# are for you to check your function definitions before final submission. They are not the same as the tests that will
# be used to compute the grade for your assignment
# submission. Hence, you may not get the same mark for
# your submission as you get from these pre-submission tests.

# In[20]:


## Testing module must have been imported (see first code cell above)
do_all_tests()


# # Submission
# 
# * Coursework should be submitted via Gradescope.
# * You should submit your edited version of this file.
# * **Do not change the name of the file you downloaded. 
#   The file you upload must have the same name.**

# In[ ]:




