# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Code starts here

data=pd.read_csv(path)
data.head(5)

loan_status= data['Loan_Status'].value_counts()

loan_status.plot(kind='bar',figsize=(10,10))


# --------------
#Code starts here
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()

#property_and_loan.plot(kind='bar',stacked=False,figsize=(10,15))

plt.figure(figsize=[10,15])
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.title('Everyone needs money')
plt.plot(kind='bar',stacked=False)
plt.show()


# --------------
#Code starts here
education_and_loan= data.groupby(['Education', 'Loan_Status'])
education_and_loan= education_and_loan.size().unstack()
print(education_and_loan)
education_and_loan.plot(kind='bar', stacked=False)

plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here

#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']


#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education']=='Not Graduate']


#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')


#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')


#Code ends here

#For automatic legend display
plt.legend()


# --------------
fig ,(ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(10,15))
data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)
plt.title('Applicant Income')

data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
plt.title('Coapplicant Income')

data['TotalIncome']= data['ApplicantIncome'] + data['CoapplicantIncome']
plt.title('Total Income')

data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)
plt.title('Total Income')


