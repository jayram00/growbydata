import os
import json
import pandas as pd

file_list =[]
def All_json(files_dir):
    for file in os.listdir(files_dir):
        if file.endswith('.json'):
            file_list.append(file)
    return file_list
files_dir = r"C:\Users\jayram raut\Desktop\task 1\jayram"

file_list = All_json(files_dir)

# print(file_list)
# function to read json
ilist =[]
last_frame = pd.DataFrame()

for file in (file_list):

    data_in_series = pd.DataFrame()
    data = json.load(open(file))
    #normalizing the json data
    df = pd.json_normalize(data["data"])
    df = pd.DataFrame(df)
    # print(df)


# selection of table header
    tdf = df[df['element'] == "TH"]
    tdf = tdf[["text"]]

    #squeezing to store serially
    tseries = tdf['text'].squeeze()

    #converting into list
    titles = tseries.tolist()
    titles.append("")

    dframe = df[df['element'].str.contains('TD') & df['attributes.class'].str.contains('SH30Lb')]
    unique_y = dframe['y'].unique()
    l = len(unique_y)

    framesplit = [None] * l

    series = [None] * l

    for key in range(l):
        framesplit[key] = dframe[dframe['y'] == unique_y[key]]
        framesplit[key] = framesplit[key][["text"]]
        framesplit[key] = framesplit[key].reset_index(drop=True)
        framesplit[key] = framesplit[key].replace('Opens in a new window', '', regex=True)

        series[key] = framesplit[key]['text'].squeeze()

    dframe1 = pd.concat(series, axis=1).T

    dframe1 = dframe1.reset_index(drop=True)

    dframe1.columns = titles

    dframe1.head()

    dframe1["Total price"] = dframe1["Total price"].str.split('Item').str[0]
    sp = file.split(".")


#converting all to csv files

    pd.set_option('display.max_rows', 500)

# locating te file from last
    dframe1 = dframe1.iloc[:, :-1]
    colums = len(dframe1.columns)
    new_series = [None] * colums

    for i in range(colums):
        new_series[i] = dframe1.iloc[:, i]
        new_series[i].to_frame()
        title_list = [new_series[i].name] * len(dframe1)
        series_title = pd.Series(title_list)
        # print(series_title)
        new_series[i].name = None

        new_series[i] = pd.concat([series_title, new_series[i]], axis=1)
        # print(dframe)
        for j in range(len(dframe1)):

            # ilist.append(str(sp) + '.' + str(i) + '.' + str(j))

            ilist.append(str(sp) + '.' + str(i) + '.' + str(j))
    # ind = ind +1
        # print("\n")
        # print(new_series[i])

    for i in range(colums):
        data_in_series = data_in_series.append(new_series[i], ignore_index=True)
# print(data_in_series)
#
    last_frame = last_frame.append(data_in_series,ignore_index=True)

#adding index and converting to csv file
last_frame['index'] = ilist
last_frame = last_frame.set_index("index")
# print(last_frame)
last_frame.to_csv("allcsv15.csv")
