#Find-S algorithm

import pandas as pd

#Data importing and preparation
dataset = pd.read_csv("EnjoySport.csv")

target = list(dataset['EnjoySport'])

pte=dataset[dataset['EnjoySport']=='Yes'] #Conditional indexing to return only the rows (training examples) where target is positive

pte=pte.iloc[:,:-1] #remove the target

h=[None]*len(pte.columns) #Initialize the most specific hypothesis


for index,x in pte.iterrows():
    print('The hypothesis at the end of the',index,'iteration is',h)
    for index1, a in enumerate(h):
        if a == None:
            h[index1]=x[index1]
        #elif a == '?' or a==x[index1]: #? is most general constraint
            #pass
        elif a!=x[index1]:
            h[index1]='?'
    
print("The most specific hypothesis which fits all the positive training examples is ",h)

           
