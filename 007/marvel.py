from collections import Counter, namedtuple

import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

DATA = 'marvel-wikia-data.csv'

Character = namedtuple('Character', 'pid name sid align sex appearances year')


def convert_csv_to_dict(data=DATA):
    '''write a function to parse marvel-wikia-data.csv, see
       https://docs.python.org/3.7/library/csv.html#csv.DictReader
       should return a list of OrderedDicts or a list of Character
       namedtuples (see Character namedtuple above')'''

    with open(data, newline='') as csvfile:  
        reader = csv.DictReader(csvfile)
        characters = [row for row in reader]        
    return characters


data = list(convert_csv_to_dict())

def most_popular_characters(n=5):
    '''get the most popular character by number of appearances
       accept an argument of n (int) of most popular characters
       to return (leave default of 5)'''

    characters = [(c['name'], c['APPEARANCES']) for c in data if c['APPEARANCES'].isdigit()]
    characters_by_apperances = sorted(characters, key=lambda x: int(x[1]), reverse=True)    

    return characters_by_apperances[:n]


def max_and_min_years_new_characters():
    '''Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)'''
    
    years = sorted([year['Year'] for year in data if year['Year']])
    counter = Counter(years)

    return (max(counter.items(), key=lambda x: x[1]), min(counter.items(), key=lambda x: x[1]))


def percentage_female():
    '''Get the percentage of female characters, only look at male and female
       for total, ignore the rest, return a percentage rounded to 2 digits'''

    female_characters = [f for f in data if f['SEX'] == 'Female Characters']    
    return round(len(female_characters)/len(data)*100, 2)


def good_vs_bad(sex):
    '''Return a dictionary of bad vs good vs neutral characters.
       This function receives an arg 'sex' and should be validated
       to only receive 'male' or 'female' as valid inputs (should
       be case insensitive, so could also pass it MALE)

       The expected result should be a the following dict. The values are
       rounded (int) percentages (values made up here):

       expected = {'Bad Characters': 33,
                   'Good Characters': 33,
                   'Neutral Characters': 33})
    '''
    
    sex = sex.title() + ' Characters'

    characters = [c['ALIGN'] for c in data if c['SEX'] == sex]
    counter = Counter(characters)

    results = {}
    results['Sex'] = sex
    for k,v in counter.items():
        results[k] = round(v / len(characters) * 100)

    return results

def plot_new_characters_by_year():
    years = sorted([year['Year'] for year in data if year['Year']])
    counter = Counter(years)

    years = [int(k) for k in counter.keys()]
    new_characters = [int(y) for y in counter.values()]

    print(years)
    print(new_characters)
    
    plt.plot(years, new_characters, 'ro')
    values = max_and_min_years_new_characters()

    #print(values)
    max_values = values[0]
    min_values = values[1]

    #plt.plot([1955, 1988, 1993, 2005], [100,200,300,40], 'ro')
    plt.axis([1930, 2017, min_values[1], max_values[1]])
    
    plt.show()

def pandas_plot():
    characters = pd.read_csv(DATA)

    print(characters.head())
    #characters['APPEARANCES'].plot(kind="bar")

    print(characters['APPEARANCES'].max())
    print(characters['APPEARANCES'].std())
    #ts = pd.Series(characters['APPEARANCES'])
    #ts.plot()

    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()

    plt.figure()    
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
    df.iloc[5].plot(kind='bar');
    plt.show()

    # generate bar graph of new characters by year


if __name__ == '__main__':
    print(most_popular_characters())
    print(max_and_min_years_new_characters())
    print("Percentage of Female Marvel characters " + str(percentage_female()))
    print(good_vs_bad('female'))
    print(good_vs_bad('male'))
    #plot_new_characters_by_year()
    pandas_plot()
    
