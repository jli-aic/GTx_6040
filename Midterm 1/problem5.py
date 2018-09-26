
# coding: utf-8

# # Problem 5: AirBnB-TX
# 
# In this problem, you will be analyzing house listing data from AirBnB in Texas using regex, lists, and dictionaries.
# 
# > This problem was inspired by a Kaggle problem: https://www.kaggle.com/PromptCloudHQ/airbnb-property-data-from-texas
# 
# You will work with a subset of the AirBnB data. Namely, you will focus on the price and the URL features of the dataset (the URL contains information on what city a customer searched for).
# 
# The goal for this problem is to see what search cities appear most in a given price range.
# 
# Please run the following code cell to set up the problem. The output shows the first 5 lines of the data you will be working with. The data is a list, available in a variable named `Master_list`. Each item of this list is an AirBnB listing, and more specifically holds the price and URL of that listing.
# 
# > This cell uses Pandas (Topic 7) to simplify reading in the data. However, you do not need Pandas to solve the problem, as this exam covers only Topics 1-5.

# In[1]:


import pandas as pd
import numpy as np
import re

# Extract data into tabular format using pandas (stay tuned for lab 7!)
AirBnB_Austin = pd.read_csv('../resource/asnlib/publicdata/Airbnb_Texas_Rentals.csv')
AirBnB_Austin = AirBnB_Austin.dropna()

# Price_list
price_raw = AirBnB_Austin['average_rate_per_night'].tolist()

# Url_list
url_list = AirBnB_Austin['url'].tolist()

# Combine Price and URL into one list
Master_list = [[price_raw[i], url_list[i]] for i in range(len(price_raw))]

# Output first five lines of Master_list
print("The first five lines of your data:")
Master_list[0:5]


# Note that the price is currently in the type of string. So first, lets convert the prices to integers.
# 
# **Exercise 0** (1 point). Write a function `convertint(prices)` that, given a list of prices (of type string), finds the number in the string and converts it into an integer.
# 
# For example, if
# 
# ```python
# prices = ['$27' , '$149' , '$59' , '$60' , '$75']
# ```
# 
# then your function should produce the output,
# 
# ```python
# convertint(prices) == [27 , 149 , 59 , 60 , 75]
# ```
# 
# You may assume all the prices are in the form `'$xx'` or `'$xxx'` and have no decimal part. 

# In[2]:


def convertint(prices):
    new_prices = []
    
    for i in prices:
        i = new_prices.append(int(re.sub('\$', '', i)))
    
    return new_prices


# In[3]:


## Exercise 0 Test Cell - convertint(prices) ##

test = convertint(['$27' , '$149' , '$59' , '$60' , '$75'])
print ("Your convertint result: {}".format(test),"->", "Expected result: {}".format([27,149,59,60,75]))
assert convertint(['$27' , '$149' , '$59' , '$60' , '$75']) == [27,149,59,60,75],'Your result does not match'
print("\n(Passed!)")


# Great job! Now let's see what the updated data looks like. Run the code cell below. It will replace all the string-based dollar amounts in `Master_list` with their numerical equivalents.

# In[4]:


prices = convertint(price_raw)
Master_list = [[prices[i], url_list[i]] for i in range(len(prices))]
print("The first five lines of your updated data, with prices all converted to integer:")
Master_list[0:5]


# Next, let's parse the URL strings to get the search cities.

# **Exercise 1** (3 points). Write a function `parseurls(urls)` that parses the names of the cities searched from each of the url strings in the data. Since we know all the data come from Texas, you can ignore the state as it appears in these URLs.
# 
# For example, if
# 
# ```python
# urls = ['https://www.airbnb.com/rooms/18520444?location=Cleveland%2C%20TX',
#         'https://www.airbnb.com/rooms/17481455?location=Cibolo%2C%20TX',
#         'https://www.airbnb.com/rooms/16926307?location=Beach%20City%2C%20TX',
#         'https://www.airbnb.com/rooms/11839729?location=College%20Station%2C%20TX']
# ```
# 
# then your function should produce the output shown below:
# 
# ```python
# parseurls(urls) == ['Cleveland','Cibolo','Beach City','College Station']
# ```
# 
# That is, you need to extract the city name from the raw URL, replace the special subsequences, `'%20'` with spaces, strip off the `'%2C%20TX'` suffixes.

# In[5]:


import re

def parseurl(urls):
    
    cities = []
    
    for i in urls:
        my_city = re.findall(r"\=(.*?)T", i)
        my_city = re.sub("\%2C\%20", '', my_city[0])
        my_city = re.sub("\%20", ' ', my_city)
        cities.append(my_city)
        
    return cities

urls = ['https://www.airbnb.com/rooms/18520444?location=Cleveland%2C%20TX',
        'https://www.airbnb.com/rooms/17481455?location=Cibolo%2C%20TX',
        'https://www.airbnb.com/rooms/16926307?location=Beach%20City%2C%20TX',
        'https://www.airbnb.com/rooms/11839729?location=College%20Station%2C%20TX']

parseurl(urls)


# In[6]:


## Exercise 1, Test Cell 1 - The One Word Cities (1 point) ##
result = parseurl(['https://www.airbnb.com/rooms/18520444?location=Cleveland%2C%20TX',
                  'https://www.airbnb.com/rooms/17481455?location=Cibolo%2C%20TX'])
t_result = ['Cleveland','Cibolo']
print ("Your parseurl result: {}".format(result),"->", "Expected result: {}".format(t_result))
assert result== t_result, 'Your result does not match'

print("\n(Passed!)")


# In[7]:


## Exercise 1, Test Cell 2 - One and Two Word Cities (2 point) ##

result = parseurl(['https://www.airbnb.com/rooms/18520444?location=Cleveland%2C%20TX',
                 'https://www.airbnb.com/rooms/17481455?location=Cibolo%2C%20TX',
                 'https://www.airbnb.com/rooms/16926307?location=Beach%20City%2C%20TX',
                 'https://www.airbnb.com/rooms/11839729?location=College%20Station%2C%20TX'])
t_result = ['Cleveland','Cibolo','Beach City','College Station']
print ("Your parseurl result: {}".format(result),"->", "\nExpected result: {}".format(t_result))
assert result == t_result,'Your result does not match'

print("\n(Passed!)")


# Great! Now we are ready to analyze the data. Run the cell below to see the cleaned data, which again overwrites `Master_list`.

# In[8]:


urls = parseurl(url_list)

Master_list = [[prices[i], urls[i]] for i in range(len(prices))]
print("The first five lines of your updated data, with prices and url cleaned:")
Master_list[0:5]


# Now, we will try to see what search cities appear most at certain price listings. To do this, we will first need a way to filter the data by price.

# **Exercise 2** (1 point) Create a function `filterdata(data, low, high)` that filters the data by a price range, given by the low and high values. For instance, `filterdata(data, 50, 100)` should output data for all the listings where the price is between 50 and 100 (inclusive of 50 and 100). Note the `data` input will be in the same form as `Master_list` in the code cell above. That is, it will be in the form:
# 
# ```python
# [[27, 'Cleveland'],
#  [149, 'Cibolo'],
#  [59, 'Beach City'],
#  [60, 'College Station'],
#  [75, 'Colleyville']]
# ```
# 
# When run on the data above, `filterdata(data, 50, 100)` would return `[[59, 'Beach City'], [60, 'College Station'], [75, 'Colleyville']]`.

# In[44]:


def filterdata(data, low, high):
    
    L = []
    
    for x_i in data:
        if x_i[0] >= low and x_i[0] <= high:
            L.append(x_i)
            
    return L

len(filterdata(Master_list, 50, 100))


# In[18]:


## Exercise 2, Test Cell 1 - Assert output lengths are correct (0.5 points) ##

assert len(filterdata(Master_list,50,100)) == 5436,'Length of your filtered data differ!'
assert len(filterdata(Master_list,1000,10000)) == 515, 'Length of your filtered data differ!'
assert len(filterdata(Master_list,0,200)) == 13538, 'Length of your filtered data differ!'
assert len(filterdata(Master_list,15,87)) == 7338, 'Length of your filtered data differ!'

print("\n(Passed!)")


# In[19]:


## Exercise 2, Test Cell 2 - Assert individual items in the list are correct (0.5 points) ##

def sortfilterdata(s):
    return sorted(s, key=lambda x:(x[0],x[1]))

test = sortfilterdata(filterdata(Master_list,0,200))

assert test[0:10] == [[10, 'Bellaire'], [10, 'Bertram'], [10, 'Big Bend National Park'],
                      [10, 'Castro County'], [10, 'Castroville'], 
                      [10, 'Castroville'], [10, 'Castroville'], 
                      [10, 'Castroville'], [11, 'Addison'], [11, 'Aubrey']], 'Result does not match!'

assert test[40:50] == [[16, 'Caldwell'],[16, 'College Station'],[16, 'Coupland'],
                       [17, 'Alvin'],[17, 'Alvin'],[17, 'Bastrop County'],
                       [17, 'Bell County'],[17, 'Belton'],
                       [17, 'Buda'],[17, 'Carrollton']],'Result does not match!'

assert test[13527:13537] == [[200, 'Corpus Christi'],[200, 'Corpus Christi'],
                             [200, 'Corpus Christi'],[200, 'Corpus Christi'],
                             [200, 'Corpus Christi'],[200, 'Corpus Christi'],
                             [200, 'Corpus Christi'],[200, 'Corpus Christi'],
                             [200, 'Coupland'],[200, 'Coupland']],'Result does not match!'

print("\n(Passed!)")


# Next, we need a way to count the number of occurances of each search city.

# **Exercise 3** (1 point) Create a function `findcount(s)` that generates a dictionary of the number of occurences of each unique string in a list. For example:
# 
# ```python
# findcount(['Cleveland','Austin','Dallas','Austin','Cleveland']) == {'Cleveland':2, 'Austin':2, 'Dallas':1}
# ```
# 
# Note that because the output is a dictionary, order does not matter, as long as all the keys and values are correct.
# 
# > **Hint:** You might find useful types or functions in the `collections` module.

# In[28]:


from collections import defaultdict

count_dict = defaultdict(int)

def findcount(s):
    for x_i in s:
        count_dict[x_i] += 1
        
    return dict(count_dict)
        
        
findcount(['Cleveland', 'Los Angeles'])
    
    


# In[29]:


## Exercise 3 Test Cell - Counts for Cities (1 point) ##

testdata = filterdata(Master_list,50,100)
citiestest = [i[1] for i in testdata]
test1 = findcount(citiestest)

assert type(test1) is dict, "Your result is of type `{}`, not `dict`.".format(type(test1))
assert test1['Allen'] == 117, 'Result does not match'
assert test1['Columbus'] == 10, 'Result does not match'
assert test1['College Station'] == 57, 'Result does not match'

print("\n(Passed!)")


# Finally, lets put everything together in order to find the most common search cities for each price range.

# **Exercise 4** (4 points) Generate a dictionary that shows the top 3 most common search cities in the following price ranges: 0-50, 51-100, 101-200, and 201-10000. The dictionary should be in the following form:
# 
# `{'Price 0-50':['city1','city2','city3'], etc..}`
# 
# Store your dictionary as the variable `TopCities`
# 
# Use the above functions, or functions of your own, to help you generate the dictionary.

# In[67]:


from collections import Counter

TopCities = {}

price_50 = filterdata(Master_list, 0, 50)
price_100 = filterdata(Master_list, 51, 100)
price_150 = filterdata(Master_list, 101, 200)
price_200 = filterdata(Master_list, 201, 10000)


price50_dict = defaultdict(int)
price100_dict = defaultdict(int)
price150_dict = defaultdict(int)
price200_dict = defaultdict(int)

for i in price_50:
    price50_dict[i[1]] += 1
    
for i in price_100:
    price100_dict[i[1]] += 1
    
for i in price_150:
    price150_dict[i[1]] += 1
    
for i in price_200:
    price200_dict[i[1]] += 1
    

price50_dict = Counter(price50_dict)
price100_dict = Counter(price100_dict)
price150_dict = Counter(price150_dict)
price200_dict = Counter(price200_dict)

L_50 = []
L_100 = []
L_150 = []
L_200 = []

for key, value in price50_dict.most_common(3):
    L_50.append(key)
    
for key, value in price100_dict.most_common(3):
    L_100.append(key)
    
for key, value in price150_dict.most_common(3):
    L_150.append(key)
    
for key, value in price200_dict.most_common(3):
    L_200.append(key)
    
TopCities['Price 0-50'] = L_50
TopCities['Price 51-100'] = L_100
TopCities['Price 101-200'] = L_150
TopCities['Price 201-10000'] = L_200
    
TopCities


# In[68]:


## Exercise 4 Test Cell - TopCities (4 points) ##

result1 = {'Price 0-50': ['Coppell', 'Colleyville', 'Carrollton'],
           'Price 101-200': ['Bayou Vista', 'Center Point', 'Aransas Pass'],
           'Price 51-100': ['Bellaire', 'Alvin', 'Alamo Heights'],
           'Price 201-10000': ['Baffin Bay', 'Burnet', 'Buchanan Dam']}

result2 = {'Price 0-50': ['Coppell', 'Colleyville', 'Carrollton'],
           'Price 51-100': ['Bellaire', 'Alvin', 'Alamo Heights'],
           'Price 101-200': ['Bayou Vista', 'Center Point', 'Corpus Christi'], 
           'Price 201-10000': ['Baffin Bay', 'Burnet', 'Buchanan Dam']}

assert TopCities == result1 or TopCities == result2,'TopCities does not match!'

print("\n(Passed!)")


# **Fin!** You've reached the end of this problem. Don't forget to restart the kernel and run the entire notebook from top-to-bottom to make sure you did everything correctly. If that is working, try submitting this problem. (Recall that you *must* submit and pass the autograder to get credit for your work!)
