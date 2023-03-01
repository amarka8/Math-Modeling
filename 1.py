import pandas as pd
df=pd.read_csv("/Users/amark/Desktop/Py4e/Puzzles/Prison (1).csv",dtype={"Jurisdiction":"string"},parse_dates=["Admission Date"])
df.dropna(inplace=True,axis=0,subset=["Admission Date","Jurisdiction"])
df.dropna(inplace=True,axis=1,how="all")
start_date = "2001-01-01"
end_date ="2022-01-01"
mask = (df["Admission Date"] >= start_date) & (df["Admission Date"] < end_date)
df = df[mask]
df_insurance=pd.read_csv("/Users/amark/Desktop/Py4e/Puzzles/Iowa_Unemployment_Insurance_Benefit_Payments_and_Recipients_by_County__Monthly_.csv",dtype={"Jurisdiction":'string'},parse_dates=["Admission Date"])
df_insurance.dropna(inplace=True,axis=1,how="all")
df_insurance.dropna(inplace=True,axis=0,subset=["Admission Date","Jurisdiction"])
mask = (df_insurance["Admission Date"] >= start_date) & (df_insurance["Admission Date"] < end_date)
df_insurance = df_insurance[mask]
# one to many relationship (52931)
# nan_count3 = df_insurance["Benefits Paid"].isna().sum().sum()
df2=pd.merge(df,df_insurance,how="left",left_on=["Admission Date","Jurisdiction"],right_on=["Admission Date","Jurisdiction"])
df2.insert(len(df2.columns), "Admission Year", df2["Admission Date"], True)
df2["Admission Year"]=df2["Admission Year"].astype("string")
df2["Admission Year"]=df2["Admission Year"].str.split("-").str.get(0)
df2["Admission Year"]=df2["Admission Year"].astype("int64")
# nan_count4 = df2["Benefits Paid"].isna().sum().sum()
# print(nan_count3)
# print(nan_count4)
# dftest = df2[['Benefits Paid']]
# print(dftest.isnull().values.any())
# df2["Admission Date"]=df2["Admission Date"].str.split("-").str.get(0)
#print(df2["Admission Date"])
# insurance,prison, and income
df1=pd.read_csv("/Users/amark/Desktop/Py4e/Puzzles/Annual_Personal_Income_for_State_of_Iowa_by_County.csv",dtype={"Jurisdiction":"string","Admission Date":"int64","MedianFamilyIncome":"int64"})
df1.dropna(inplace=True,axis=1,how="all")
dfAdditionToIncome=pd.read_csv("/Users/amark/Desktop/Py4e/Puzzles/Annual_Personal_Income_for_State_of_Iowa_by_County__Recent_Year.csv")
dfAdditionToIncome.dropna(inplace=True,axis=1,how="all")
dfAdditionToIncome.dropna(inplace=True,axis=0,how="all")
dfAdditionToIncome["Jurisdiction"]=dfAdditionToIncome["Jurisdiction"].str.removesuffix(", IA")
df1=df1.append(dfAdditionToIncome,ignore_index=True)
df1["Admission Date"]=df1["Admission Date"].astype("int64")
df1["MedianFamilyIncome"]=df1["MedianFamilyIncome"].astype("int64")
# nan_count3 = df1["MedianFamilyIncome"].isna().sum().sum()
df3=pd.merge(df2,df1,how="left",left_on=["Admission Year","Jurisdiction"],right_on=["Admission Date","Jurisdiction"],validate="many_to_one")
# nan_count4 = df3["MedianFamilyIncome"].isna().sum().sum()
dfPopulation=pd.read_csv("/Users/amark/Desktop/Py4e/Puzzles/County_Population_in_Iowa_by_Year.csv",dtype={"Admission Date":"int64","Jurisdiction":"string"})
start_date = 2001
end_date =2022
mask = (dfPopulation["Admission Date"] >= start_date) & (dfPopulation["Admission Date"] < end_date)
dfPopulation = dfPopulation[mask]
# nan_count1 = dfPopulation["Population"].isna().sum().sum()
dfFinal=pd.merge(df3,dfPopulation,how="left",left_on=["Admission Year","Jurisdiction"],right_on=["Admission Date","Jurisdiction"])
# nan_count2 = dfFinal["Population"].isna().sum().sum()
dfFinal.dropna(axis=0,subset=["MedianFamilyIncome","Population","Benefits Paid"],inplace=True)
dfFinal.to_csv("/Users/amark/Desktop/Py4e/Puzzles/Combined_Prison_Final.csv")
# dftest = dfFinal[['Benefits Paid']]
# print(dftest.isnull().values.any())







