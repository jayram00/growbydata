import os
import pandas as pd
import json


def all_json(files_dir):
    file_list =[]
    for file in os.listdir(files_dir):
        if file.endswith('.json'):
            file_list.append(file)
    return file_list
files_dir = r"C:\Users\jayram raut\Desktop\task 1\jayram"

file_list = all_json(files_dir)


index_list = []

#print(file_list)

#empty data frame
final_dataframe = pd.DataFrame()

for file in file_list:

    data_in_series = pd.DataFrame()
    data = json.load(open(file))
    #normalizing the json data
    df = pd.json_normalize(data["data"])
    # df = pd.DataFrame(df)
    # print(df)


# selection of table header
    tdf = df[df['element'] == "TH"]
    tdf = tdf[["text"]]

    #squeezing to store serially
    tseries = tdf['text'].squeeze()

    #converting into list
    titles = tseries.tolist()
    titles.append("")

    data_frame = df[df['element'].str.contains('TD') & df['attributes.class'].str.contains('SH30Lb')]
    unique_y = data_frame['y'].unique()
    l = len(unique_y)

    frame_split = [None] * l

    series = [None] * l

    for key in range(l):

        frame_split[key] = data_frame[data_frame['y'] == unique_y[key]][["text"]]
        # frame_split[key] = frame_split[key][["text"]]
        frame_split[key] = frame_split[key].reset_index(drop=True)
        frame_split[key] = frame_split[key].replace('Opens in a new window', '', regex=True)

        series[key] = frame_split[key]['text'].squeeze()

    data_frame1 = pd.concat(series, axis=1).T

    data_frame1 = data_frame1.reset_index(drop=True)

    data_frame1.columns = titles
#
    data_frame1["Total price"] = data_frame1["Total price"].str.split('Item').str[0]
    file_name = file.split(".")
    file_name=file_name[0]


#converting all to csv files

    pd.set_option('display.max_rows', 500)

# locating the file from last
    data_frame1 = data_frame1.iloc[:, :-1]

    colums = len(data_frame1.columns)

    new_series = [None] * colums

    # print(data_frame1)
    for i in range(colums):
        new_series[i] = data_frame1.iloc[:, i]
        new_series[i].to_frame()
        title_list = [new_series[i].name] * len(data_frame1)

        series_title = pd.Series(title_list)

        # print(series_title)
        new_series[i].name = None

        new_series[i] = pd.concat([series_title, new_series[i]], axis=1)

        # print(data_frame)

        for j in range(len(data_frame1)):

            # index_list.append(str(sp) + '.' + str(i) + '.' + str(j))
            index_list.append(str(file_name) + '.' + str(i) + '.' + str(j))
    # ind = ind +1
        # print("\n")
        # print(new_series[i])

    for i in range(colums):
        data_in_series = data_in_series.append(new_series[i], ignore_index=True)
# print(data_in_series)
#
    # print(data_in_series)
    final_dataframe = final_dataframe.append(data_in_series, ignore_index=True)


#adding index and converting to csv file

final_dataframe['index'] = index_list
final_dataframe = final_dataframe.set_index("index")

# print(final_dataframe)
final_dataframe.to_csv("allcsv23.csv")