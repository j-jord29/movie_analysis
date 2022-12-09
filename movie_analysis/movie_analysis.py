# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:58:04 2022

@author: Jack
"""

import pandas as pd
from datetime import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

# Notes on the task:
#    Feel free to import any additional modules you may need.
#    If there are any sections you can't complete, feel free to write the theory/steps behind what you would do if you knew how to do it.
#    Please add comments to all of the code you write explaining how and why you have used it.
#

# 1. use pandas to load Netflix, Amazon Prime and Disney+ data into seperate dataframes (called netflix, amazon, disney)

netflix = pd.read_csv('netflix_titles.csv')
disney_plus = pd.read_csv('disney_plus_titles.csv')
amazon_prime = pd.read_csv('amazon_prime_titles.csv')

#print(netflix)
#print(disney_plus)
#print(amazon_prime)

# 2. when combining the two dataframes into one (called netflix_amazon), how many TV Shows/Movies appear in both the Netflix and Amazon Prime catalogue?

# Creates an array containing elements of netflix and amazon movies
netflix_amazon_frame = [netflix, amazon_prime]

# concatinates the dataframes together
netflix_amazon = pd.concat(netflix_amazon_frame)
#print(netflix_amazon[['show_id', 'title']])

#returns the total amount of rows ()
#print(netflix_amazon.shape[0])

# 3. create a new dataframe (called netflix_disney) that shows only the MOVIES that are in both the Netflix and DISNEY catalogues

# Creates an intersection on the 2 Dataframes Netflix and Disney Plus dependent on the title

netflix_disney = pd.merge(netflix, disney_plus, how = 'inner', on = ['title'])

def task_3():    
    # Outputs a CSV File displaying the intersection between the 2 Dataframes
    try:
        netflix_disney.to_csv('output.csv', encoding='utf-8')
        print("OUTPUT CREATED")
    except Exception as e:
        print("ERROR: " , e)    
    
    # Returns 43 shows that appear on both Disney Plus and Netflix
    print(netflix_disney)

# 4. create a function, or process, that checks a single row of the netflix_disney movie dataframe and prints the following info to the output console:
#       - Name of Movie
#       - Which of the two streaming services added the movie first?
#       - Is the duration of the movie listed the same in both netflix and disney?
#       - Which streaming service has given the movie the longest description, and how many characters is it?

# function that compares the dates
def compare_dates(netflix, disneyplus):    
    if (netflix == disneyplus):
        return 'Same Time'        
    elif (netflix < disneyplus):
        return 'Netflix'
    else:
        return 'Disney Plus'   

# function that compares running times
def are_runtimes_equal(netflix, disneyplus):
    if (netflix == disneyplus):
        return True
    else:
        return False

# function that compares the character length of the descriptions
def compare_descriptions(netflix, disneyplus):
    if (len(netflix) == len(disneyplus)):
        return "Same Length"
    elif (len(netflix) > len(disneyplus)):
        return "Netflix"
    else:
        return "Disney Plus"

# formats the output into a table
def format_to_table(title, first_to_add, same_run_length, longest_desc):
    print("{:<45}".format(str(title))+' '
          +"{:<20}".format(str(first_to_add))+' '
          +"{:<20}".format(str(same_run_length)+' '
          +"{:^50}".format(str(longest_desc)+' ')))
    
# Seperated Function for Task 4
def task_4(r_num):
    try:
        # variable definitions
        netflix_duration = netflix_disney['duration_x'][r_num]
        disneyplus_duration = netflix_disney['duration_y'][r_num]
        
        netflix_date = datetime.strptime(netflix_disney['date_added_x'][r_num], '%B %d, %Y')
        disneyplus_date = datetime.strptime(netflix_disney['date_added_y'][r_num], '%B %d, %Y')
        
        netflix_desc_len = netflix_disney['description_x'][r_num]
        disneyplus_desc_len = netflix_disney['description_y'][r_num]  
        
        print("Movie Title: " + netflix_disney['title'][r_num])         
        print("Who Added First?:", compare_dates(netflix_date, disneyplus_date))
        print("Netflix Date:", netflix_disney['date_added_x'][r_num])
        print("Disney Plus Date: ", netflix_disney['date_added_y'][r_num])
               
        print("Same Running Length?: ", are_runtimes_equal(netflix_duration, disneyplus_duration) )
        print("Netflix Run Time: ", netflix_duration )
        print("Disney Plus Run Time: ", disneyplus_duration)       
            
        print("Longest Description?: ", compare_descriptions(netflix_desc_len, disneyplus_desc_len))
        print("Netflix Description Length:", len(netflix_desc_len))
        print("Disney Plus Description Length:", len(disneyplus_desc_len))            
    except Exception as e:
        print("AN ERROR HAS OCCURED: ", e)
        
# Selects a Random Row from the dataset and outputs the details  
r = random.randint(0, netflix_disney.shape[0])
task_4(r)    
    
# Same as Task 4 but outputs the results into a table format for task 5
def movie_checker(r_num):
    # outputs an error without breaking the program    
    try:
        # variable definitions
        netflix_duration = netflix_disney['duration_x'][r_num]
        disneyplus_duration = netflix_disney['duration_y'][r_num]
        
        netflix_date = datetime.strptime(netflix_disney['date_added_x'][r_num], '%B %d, %Y')
        disneyplus_date = datetime.strptime(netflix_disney['date_added_y'][r_num], '%B %d, %Y')
        
        netflix_desc_len = netflix_disney['description_x'][r_num]
        disneyplus_desc_len = netflix_disney['description_y'][r_num]       
        
        format_to_table(netflix_disney['title'][r_num], 
                        compare_dates(netflix_date, disneyplus_date), 
                        are_runtimes_equal(netflix_duration, disneyplus_duration), 
                        compare_descriptions(netflix_desc_len, disneyplus_desc_len))
    except Exception as e:
        print("AN ERROR HAS OCCURED: ", e)

# 5. Use the function created in step 4 to loop through the dataframe and output the results for each of the movies present.

def task_5():
    print("{:<45}".format("Movie Title")+' '
          +"{:<20}".format("Who Added First?")+' '
          +"{:<20}".format("Same Running Length?")+' '
          +"{:<50}".format("Longest Description"))
    
    print("-----------------------------------------------------------------------------------------------------------------------")
    
    for i in range(netflix_disney.shape[0]):
        movie_checker(i)

task_5()
    
# BONUS TASKS:
# tip: feel free to use non-python tools or programs to complete any aspect of this task
# 6. Analyse the data and note any trends spotted in the following areas, including some kind of visualisation:
#    A - Has the average duration of movies changed over the last 20 years?
#    B - Which service adds movies the quickest after they are released?
#    C - Is there a trend between duration of movies and their country of origin?
"""
#merge all dataframes into one
all_csv = [netflix, disney_plus, amazon_prime]
all_dataframes = pd.concat(all_csv)

## A

#clean dataframes
remove_seasons = all_dataframes.loc[all_dataframes["duration"].str.contains("Season") == False ]
all_dataframes['duration'] = all_dataframes["duration"].str.replace("min", '')
#all_dataframes['duration'] = pd.to_numeric(all_dataframes['duration'])
sort_by_year = remove_seasons.sort_values(by = ['release_year'])
#sort_by_year['release_year'] = pd.to_datetime(sort_by_year.release_year)
sort_by_year['duration'] = sort_by_year['duration'].str.replace('min', '')
#print(sort_by_year)

x = [sort_by_year['duration'].min(), sort_by_year['duration'].max()]

sort_by_year.plot(kind='hist', x='duration', y='release_year')

"""

"""
Partial - the goal was to try and get the average times of the movies
          on the x axis and compare the duration times on the y axis
          by using a histogram to compare the years against the duration
"""


## B
"""

"""

## C
"""
Create a plot with the countries on the x axis and the duration of the films on the y axis
on the y axis to comapre the average lenght of the films.


all_dataframes.plot(kind = 'hist', x = 'country', y = 'duration')
"""