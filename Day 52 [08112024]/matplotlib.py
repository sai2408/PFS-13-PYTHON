# -*- coding: utf-8 -*-
"""Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18BPZGjT-hxpCyTLAiMRyjlk0wxuVmGEU

# Importing necessary packages
"""

pip install pandas

pip install numpy

pip install matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

"""### Line Plot"""

x = [1,2,3,4,5]
y = [10,14,8,16,12]

plt.plot(x,y, marker = 's', linestyle = '-.', color = 'r', label = 'Line')

plt.title('Line Plot Example')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.grid(True)
plt.show()

#Markers
'''
'o' : Circle
's' : Square
'^' : Triangle (up)
'v' : Triangle (down)
'<' : Triangle (left)
'>' : Triangle (right)
'p' : Pentagon
'*' : Star
'''
#Line styles
'''
'-' : Solid line
'--' : Dashed line
'-.' : Dash-dot line
':' : Dotted line
'''
#Colors
'''
'b' : Blue
'g' : Green
'r' : Red
'c' : Cyan
'm' : Magenta
'y' : Yellow
'k' : Black
'w' : White
'''

"""## Scatter Plot"""

x = [1,2,3,4,5]
y = [10,14,8,16,12]

plt.scatter(x,y, marker = 'o', color = 'r', label = 'Data Points')
plt.title('Scatter Plot Example')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.grid(True)
plt.show()

#Markers
'''
'o' : Circle
's' : Square
'^' : Triangle (up)
'v' : Triangle (down)
'<' : Triangle (left)
'>' : Triangle (right)
'p' : Pentagon
'*' : Star
'''
#Line styles
'''
'-' : Solid line
'--' : Dashed line
'-.' : Dash-dot line
':' : Dotted line
'''
#Colors
'''
'b' : Blue
'g' : Green
'r' : Red
'c' : Cyan
'm' : Magenta
'y' : Yellow
'k' : Black
'w' : White
'''

"""## Bar Plot"""

categories = ['A','B','C','D']
values = [15,8,12,10]

plt.bar(categories, values, color = 'r', alpha = 0.4) #alpha --> adjusts the transparency of the bars
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis = 'y')
plt.show()

#Colors
'''
'b' : Blue
'g' : Green
'r' : Red
'c' : Cyan
'm' : Magenta
'y' : Yellow
'k' : Black
'w' : White
'''

"""## Histogram"""

data = [1,2,2,3,3,3,4,4,5,5,5,5]

plt.hist(data, bins = 5, color='r', alpha=0.5)
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

#Colors
'''
'b' : Blue
'g' : Green
'r' : Red
'c' : Cyan
'm' : Magenta
'y' : Yellow
'k' : Black
'w' : White
'''

"""## Pie Chart"""

labels = ['A','B','C','D']
sizes = [20,15,25,40]

plt.pie(sizes,labels=labels, autopct = '%1.2f%%', startangle = 90, colors = ['gold','lightgreen','red','yellow'])
#autopct --> %1.1f%% --> displays the percentage of each category on the pie chart with one decimal place

plt.title('Pie Chart Example')
plt.axis('equal') # --> Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

"""## Line Plot"""

df = pd.read_csv('data2.csv')
df

plt.plot(df['Name'], df['Age'], marker = 'o', linestyle = '-', color = 'b')

#Markers
'''
'o' : Circle
's' : Square
'^' : Triangle (up)
'v' : Triangle (down)
'<' : Triangle (left)
'>' : Triangle (right)
'p' : Pentagon
'*' : Star
'''
#Line styles
'''
'-' : Solid line
'--' : Dashed line
'-.' : Dash-dot line
':' : Dotted line
'''
#Colors
'''
'b' : Blue
'g' : Green
'r' : Red
'c' : Cyan
'm' : Magenta
'y' : Yellow
'k' : Black
'w' : White
'''

plt.title('Line Plot - Age vs Name')
plt.xlabel('Name')
plt.ylabel('Age')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

"""## Scatter Plot"""

plt.scatter(df['Salary'], df['Rating'], marker = 'o', color = 'r', label = 'Data Points')

#Markers
'''
'o' : Circle
's' : Square
'^' : Triangle (up)
'v' : Triangle (down)
'<' : Triangle (left)
'>' : Triangle (right)
'p' : Pentagon
'*' : Star
'''
#Line styles
'''
'-' : Solid line
'--' : Dashed line
'-.' : Dash-dot line
':' : Dotted line
'''
#Colors
'''
'b' : Blue
'g' : Green
'r' : Red
'c' : Cyan
'm' : Magenta
'y' : Yellow
'k' : Black
'w' : White
'''

plt.title('Scatter Plot - Salary vs Rating')
plt.xlabel('Salary')
plt.ylabel('Rating')
plt.legend()
plt.grid(True)
plt.show()

"""## Bar Plot"""

plt.figure(figsize = (8,6))

plt.bar(df['Name'], df['Salary'], color = 'g', alpha = 0.6)

#Colors
'''
'b' : Blue
'g' : Green
'r' : Red
'c' : Cyan
'm' : Magenta
'y' : Yellow
'k' : Black
'w' : White
'''

plt.title('Bar Plot - Salary by Name')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

"""# Histogram"""

df

plt.figure(figsize = (8,4))

plt.hist(df['Age'], bins = 5, color='purple', alpha=0.7)

#Colors
'''
'b' : Blue
'g' : Green
'r' : Red
'c' : Cyan
'm' : Magenta
'y' : Yellow
'k' : Black
'w' : White
'''

plt.title('Histogram - Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

plt.figure(figsize = (6,6))

plt.pie(df['Salary'], labels=df['Name'], autopct = '%1.1f%%', startangle = 90)
plt.title('Pie Chart - Salary Distribution')
plt.axis('equal')
plt.tight_layout()
plt.show()