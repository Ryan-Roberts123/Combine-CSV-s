# This script reads the data from 'Dataset.csv' and 'testdata.csv' and combines them to a single data frame, and outputs it at as new csv.
# Made to combine NHS Covid Hospital data into a single file.


import pandas as pd

df = pd.read_csv("Dataset.csv")

# Makes column names into list
column_list1 = df.columns
dataset_D_Count = 0
dataset_MD = len(column_list1)
dataset_DL = []

# Filters the columns and returns the dates as date_list
while dataset_D_Count < dataset_MD:
    date = column_list1[dataset_D_Count]
    if "-" in date:
        dataset_DL.append(date)
    dataset_D_Count = dataset_D_Count + 1


hospital_unfiltered1 = df["Name"]
dataset_H_Count = 0
dataset_ML = len(hospital_unfiltered1)
dataset_HL = []

# Returns the list of NHS trust names as hospital_list
while dataset_H_Count < dataset_ML:
    hospital = hospital_unfiltered1[dataset_H_Count]
    dataset_HL.append(hospital)
    dataset_H_Count = dataset_H_Count + 1


df2 = pd.read_csv("testdata.csv")

# Makes column names into list
column_list2 = df2.columns
testdata_D_Count = 0
testdata_MD = len(column_list2)
testdata_DL = []

# Filters the columns and returns the dates as date_list
while testdata_D_Count < testdata_MD:
    date2 = column_list2[testdata_D_Count]
    if "-" in date2:
        testdata_DL.append(date2)
    testdata_D_Count = testdata_D_Count + 1


hospital_unfiltered2 = df2["Name"]
testdata_H_Count = 0
testdata_ML = len(hospital_unfiltered2)
testdata_HL = []

# Returns the list of NHS trust names as hospital_list
while testdata_H_Count < testdata_ML:
    hospital2 = hospital_unfiltered2[testdata_H_Count]
    testdata_HL.append(hospital2)
    testdata_H_Count = testdata_H_Count + 1


# Finds the cell value for a specific date and hospital and updates df2. Repeats until done.
def adddata():
    date_count = 0
    dataset_deaths = ""
    global hospital_update
    global hu_index
    while date_count < len(testdata_DL):
        date_update = testdata_DL[date_count]
        du_index2 = testdata_DL.index(date_update)
        deaths = df2.iat[hu_index, du_index2 + 5]
	# Ignores the next step if there are 0 deaths, increases the speed of the script alot.
        if deaths != 0:
            print("On the ", date_update, "there were ", deaths, " deaths in the ", hospital_update)
            try:
                date_index = dataset_DL.index(date_update)
                hospital_index = dataset_HL.index(hospital_update)
                dataset_deaths = df.iat[hospital_index, date_index + 2]
                dataset_DU = dataset_deaths + deaths
                df.iat[hospital_index, date_index + 2] = dataset_DU
                dataset_deaths = df.iat[hospital_index, date_index + 2]
            except ValueError:
                x = True
            print("New df deaths = ", dataset_deaths)
        date_count = date_count + 1


# Gets the first hospital name then runs adddata. Repeats.
hospital_count = 0
while hospital_count < len(testdata_HL):
    hospital_update = testdata_HL[hospital_count]
    hu_index = testdata_HL.index(hospital_update)
    adddata()
    hospital_count = hospital_count + 1

df.to_csv("Updated_CSV.csv")