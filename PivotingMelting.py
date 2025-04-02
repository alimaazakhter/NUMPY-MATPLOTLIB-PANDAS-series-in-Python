import pandas as pd

dict = {'Keys' : ['K1', 'K2', 'K1', 'K2'],
        'Names' : ['Jonh', 'Riya', 'Ali', 'Ben'],
        'House' : ['Red', 'Blue', 'Green', 'Yellow'],
        'Grade' : ['3rd', '4th', '5th', '6th']
}

df = pd.DataFrame(dict)
print(df)
print(pd.melt(df, id_vars=['Names'], value_vars=['House', 'Grade'],value_name='Value')) 

# df = pd.DataFrame(dict)
# print(df)   
# print(df.pivot(index='Keys', columns='Names', values=['House','Grade']))     
        