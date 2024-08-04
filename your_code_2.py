
# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?


# Чому дорівнює медіанна (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?


# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?


# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?


# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?


# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?



import pandas as pd

df = pd.read_csv('GoogleApps.csv')

print(df.info())
print(df.head(1))
# print(df.tail())
# print(df.describe())
# print(df[df["Rating"]>4.9]["Installs"].mean())


# # Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?
# df[df["Type"]=="Paid"]["Price"].min()

# print(df[df["Type"]=="Paid"]["Price"].min())

# print(df[df["Category"]=="ART_AND_DESIGN"]["Installs"].median())

# free = df[df['Type']=="Free"]["Reviews"].max()
# paid = df[df['Type']=="Paid"]["Reviews"].max()
# print(free-paid)





# print(df['Content Rating'].value_counts())

temp = df['Content Rating'].value_counts()
everyoneCount = temp['Everyone']
everyone_10Count = temp['Everyone 10+']
# print(round(everyoneCount/everyone_10Count, 2))

meanSizeForEveryAudience = df.groupby(by = 'Content Rating')['Size'].mean()
# print(meanSizeForEveryAudience)

print(df['Category'].value_counts())



temp = df['Content Rating'].value_counts()
print('Співвідношення:', round(temp['Teen'] / temp['Everyone 10+'], 2))

temp = df.groupby(by = 'Type')['Rating'].mean()
print(temp)

print(round(temp['Paid'] - temp['Free'], 2))

temp = df.groupby(by = 'Category')['Size'].agg([min, max])
# print(temp['Comix'])


temp = df.groupby(by = ['Type', 'Content Rating'])['Size'].agg(['min', 'max', 'mean'])
print(temp['min']['Free']['Teen'])
print(temp)


print(round(df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max']), 1))

print(df[df['Type'] == 'Paid'].groupby(by = 'Content Rating')['Price'].agg(['min', 'median', 'max']))

temp = df.pivot_table(index = 'Content Rating', columns = 'Category', values = 'Reviews', aggfunc = 'max')
print(temp[['EDUCATION', 'FAMILY', 'GAME']])

print(df[df['Type'] == 'Paid'].pivot_table(columns = 'Content Rating', index = 'Category', values = 'Reviews', aggfunc = 'max'))
