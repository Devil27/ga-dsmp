# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
# replace  '-' with str'Agender
data['Gender'].replace('-','Agender',inplace= True)

#no.s of gender type count
gender_count = data['Gender'].value_counts()
print(gender_count)
# plotting the data
plt.bar(gender_count.index, gender_count)  # x = index y = gender_count
plt.xlabel('Types of Gender')
plt.ylabel('No.s of SuperHeroes')
plt.title('Total Gender Type Of SuperHeroes')
plt.xticks(rotation=45)




# --------------
#Code starts here

alignment = data['Alignment'].value_counts()
print(alignment)

plt.scatter(alignment.index,alignment)
plt.title('Character Alignment')



# --------------
#Code starts here

#Subsetting the data with columns ['Strength', 'Combat']
sc_df = data[['Strength','Combat']].copy()

#Finding covariance between 'Strength' and 'Combat'
sc_covariance = sc_df.cov().iloc[0,1]

#Finding the standard deviation of 'Strength'
sc_strength = sc_df['Strength'].std()

#Finding the standard deviation of 'Combat'
sc_combat = sc_df['Combat'].std()

#Calculating the Pearson's correlation between 'Strength' and 'Combat'
sc_pearson = sc_covariance/(sc_combat*sc_strength)

print("Pearson's Correlation Coefficient between Strength and Combat : ", sc_pearson)


#Subsetting the data with columns ['Intelligence', 'Combat']
ic_df = data[['Intelligence','Combat']].copy()

#Finding covariance between 'Intelligence' and 'Combat'
ic_covariance = ic_df.cov().iloc[0,1]

#Finding the standard deviation of 'Intelligence'
ic_intelligence = ic_df['Intelligence'].std()

#Finding the standard deviation of 'Combat'
ic_combat = ic_df['Combat'].std()

#Calculating the Pearson's correlation between 'Intelligence' and 'Combat'
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)

print("Pearson's Correlation Coefficient between Intelligence and Combat : ", ic_pearson)

#Code ends here


# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)
print(total_high)

super_best = data[data['Total']>total_high]
print(super_best)

super_best_names= list(super_best['Name'])
print(super_best_names)




# --------------
#Code starts here

#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting box plot
ax_1.boxplot(super_best['Intelligence'])

#Setting the subplot axis title
ax_1.set(title='Intelligence')


#Plotting box plot
ax_2.boxplot(super_best['Speed'])

#Setting the subplot axis title
ax_2.set(title='Speed')


#Plotting box plot
ax_3.boxplot(super_best['Power'])

#Setting the subplot axis title
ax_3.set(title='Power')

#Code ends here   


