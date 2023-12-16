#Find-S algorithm - our algorithm

import pandas as pd

#Data importing and cleaning
def isUniform(itr):
    temp=itr[0]
    for i in itr:
        if temp!=i:
            return False
    return temp

dataset = pd.read_csv("EnjoySport.csv")

target = list(dataset['EnjoySport'])

pte=dataset[dataset['EnjoySport']=='Yes'] #Conditional indexing to return only the rows (training examples) where target is positive

pte=pte.iloc[:,:-1] #remove the target

h=[None]*len(pte.columns) #Initialize the most specific hypothesis

index=0
for label,column in pte.items():
    if isUniform(column):
        h[index]=isUniform(column)
    else:
        h[index]='?'
    index+=1
print("The most specific hypothesis which fits all the positive training examples is ",h)

