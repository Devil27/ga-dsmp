# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

data = np.genfromtxt(path, delimiter=",",skip_header=1)

print(data)

census = np.concatenate((new_record,data))
print(census)


# --------------
#Code starts here
import numpy as np
age = np.array([census[:,0]], dtype=int)  # all row = :  and column = 0 
print(age)

max_age = age.max()
print(max_age)

min_age= age.min()
print(min_age)

age_mean= age.mean()
print(age_mean)

age_std= np.std(age)


# --------------
#Code starts here
# Subsetting from census data
# Seperating the values as Race has values between 2 - 4
race_0 = census[[census[:,2]==0]]  # all row = :  and column = 0 
race_1 = census[[census[:,2]==1]]
race_2 = census[[census[:,2]==2]]
race_3 = census[[census[:,2]==3]]
race_4 = census[[census[:,2]==4]]

print(race_0,race_1,race_2,race_3,race_4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

# minimum no.s of citizen

#Printing the length of the above created subsets
print('race_0:',len_0)
print('race_1:',len_1)
print('race_2:',len_2)
print('race_3:',len_3)
print('race_4:',len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here


# --------------
#Code starts here
#new subset
senior_citizens = census[[census[:,0] > 60]]
  
#sum all working hours
working_hours_sum= senior_citizens.sum(axis=0)[6]

print(working_hours_sum)

#find length of senior_citizens
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours =  working_hours_sum/senior_citizens_len

print(avg_working_hours)




# --------------
#Code starts here
high = census[[census[:,1]>10]]
low = census[[census[:,1]<=10]]

print(high)
print(low)

avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]

print(avg_pay_high)
print(avg_pay_low)

