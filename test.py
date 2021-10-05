import pandas

df = pandas.read_excel("sample.xlsx")
print(df["FECHA"][1])