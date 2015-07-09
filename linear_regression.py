import pandas as pd 
import matplotlib.pyplot as plt 

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate


cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength


cleanFicoRange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFicoRange = cleanFicoRange.map(lambda x: [int(num) for num in x])
loansData['FICO.Range'] = cleanFicoRange


# Create a New Column called FICO.Score: 
new_column = loansData['FICO.Range'].map(lambda x: x.pop(0))
loansData['FICO.Score'] = new_column


# PLOT: 
plt.figure()
#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()

