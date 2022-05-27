import os
import pandas as pd
import json


def All_json(files_dir):
    file_list =[]
    for file in os.listdir(files_dir):
        if file.endswith('.json'):
            file_list.append(file)
    return file_list
files_dir = r"C:\Users\jayram raut\Desktop\task 1\jayram"

file_list = All_json(files_dir)


index_list = []

#print(file_list)

#empty data frame
final_dataframe = pd.DataFrame()
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

    data_frame = df[df['element'].str.contains('TD') & df['attributes.class'].str.contains('SH30Lb')]
    unique_y = data_frame['y'].unique()
    l = len(unique_y)

    frame_split = [None] * l

    series = [None] * l