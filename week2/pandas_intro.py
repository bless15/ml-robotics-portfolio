'''import pandas as pd
scores = pd.Series([90, 85, 100, 70])

print(scores)'''


"""import pandas as pd
data = {
    "Name": ["John", "Mary", "Love"],
    "Score": [90,85, 100],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)
print(df)"""


'''import pandas as pd
data = {
    "Name": ["John", "Mary", "Love"],
    "Score": [90,85, 100],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)

print(df[["Name", "Score"]])
print(df.iloc[1])'''


'''import pandas as pd
data = {
    "Name": ["John", "Mary", "Love"],
    "Score": [90,85, 100],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)

print(df.loc[1, "Name"])'''



"""import pandas as pd
data = {
    "Name": ["John", "Mary", "Love"],
    "Score": [90,85, 100],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)


print(df.describe())"""


import pandas as pd
data = {
    "Name": ["John", "Mary", "Love", "Peter", "Jane"],
    "Score": [90, 75, 100, 65, 85],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

print(df)
print(df["Score"])
print(df[df["Score"] > 80 ])
print(df[(df["Age"] < 21) & (df["Score"] > 80)])
print(df.loc[4, "Score"])
print(df.sort_values("Score", ascending = False))
print(df.describe())