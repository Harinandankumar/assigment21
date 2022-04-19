#!/usr/bin/env python
# coding: utf-8

# 1. Add the current date to the text file today.txt as a string.
# 
# 
# 
# Ans:-

# In[4]:


import datetime
# Code to Add current date to the today.txt file
file = open('today.txt','w')
file.write(datetime.datetime.now().strftime("%d-%m-%Y"))
file.close()
# Code to Read current date from today.txt file
file = open('today.txt','r')
print(file.read())
file.close()


# 2. Read the text file today.txt into the string today_string
# 
# 
# 
# Ans:-

# In[5]:


file = open('today.txt','r')
today_string = file.read()
print(today_string)


# 3. Parse the date from today_string.
# 
# 
# 
# Ans:-

# In[6]:


from datetime import datetime
parsed_data = datetime.strptime(today_string, '%d-%m-%Y')
print(parsed_data)


# 4. List the files in your current directory
# 
# 
# 
# Ans:-

# In[7]:


import os
for folders, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        print(file)


# 5. Create a list of all of the files in your parent directory (minimum five files should be available).
# 
# 
# 
# Ans:-

# In[8]:


import os 
os.listdir()


# 6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
# 
# 
# 
# 
# Ans:-

# In[9]:


import multiprocessing
import time 
import random
import datetime

def procOne():
    print(f'Proc_one_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Proc_one_Endtime -> {datetime.datetime.now()}')
    
def procTwo():
    print(f'Proc_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Proc_two_Endtime -> {datetime.datetime.now()}')

def procThree():
    print(f'Proc_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Proc_two_Endtime -> {datetime.datetime.now()}')
    
if __name__ == "__main__":    
    p1 = multiprocessing.Process(target=procOne)
    p2 = multiprocessing.Process(target=procTwo)
    p3 = multiprocessing.Process(target=procThree)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


#     Due to some unknown reason. the above did not print any results in the jupyter cell. so i copied the code to a python file.       executed it and pasted the ouput here
# 
#     Proc_two_Starttime -> 2022-04-19 08:41:04.382841
#     Proc_two_Endtime -> 2022-04-19 08:41:08.386952
#     Proc_one_Starttime -> 2022-04-19 08:41:04.382293
#     Proc_one_Endtime -> 2022-04-19 08:41:09.387375
#     Proc_two_Starttime -> 2022-04-19 08:41:04.382487
#     Proc_two_Endtime -> 2022-04-19 08:41:09.387591

# 7. Create a date object of your day of birth.
# 
# 
# 
# 
# Ans:-

# In[19]:


from datetime import datetime
my_dob = datetime.strptime('24/02/1998','%d/%m/%Y')
print(my_dob, type(my_dob))


# 8. What day of the week was your day of birth?
# 
# 
# 
# Ans:-

# In[20]:


from datetime import datetime
my_dob = datetime(1998,2,24)
my_dob.strftime("%A")


# 9. When will you be (or when were you) 10,000 days old?
# 
# 
# 
# Ans:-

# In[22]:


from datetime import datetime, timedelta
my_dob = datetime.strptime("24/02/1998",'%d/%m/%Y')
future_date = my_dob-timedelta(10000)
future_date

