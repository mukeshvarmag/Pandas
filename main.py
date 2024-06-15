import pandas as pd
import matplotlib.pyplot as plt

# s = pd.Series([1, 2, 3, 4, 5])
#
# print(s)
#
# data = {
#     "x": [1, 2, 3],
#     "y": [1, 8, 27]
# }
# df = pd.DataFrame(data)
# print(df)
# df.plot(x="x", y="y", kind="line")
# plt.show()


ReadCSV = pd.read_csv('C:/Users/mukes/CodeWorkSpace/Pandas/tips.csv')
df = pd.DataFrame(ReadCSV)
# print(df)
# print(df["tip"])
# filtered = df[df["tip"] > 4]
filtered = df[df["sex"] == "Male"]
print(filtered)
