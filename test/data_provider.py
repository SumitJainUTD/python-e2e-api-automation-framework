import csv
import json
import os


def get_data_json(cname):
    file_path = "../../test/test_data/test_data.json"
    fh = open(file_path)
    data = json.load(fh)
    return_data = []
    for d in data:
        if d.get('enabled') and d.get('test_category') == cname:
            return_data.append(d)
    fh.close()
    return return_data


def get_data_csv(cname, method):
    fileName = "../test/test_data/test_data.csv"
    rows = []
    with open(fileName, 'r') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=",")
        next(csvreader)  # skip header
        for row in csvreader:
            if row[1] == "TRUE" and row[2] == cname and row[3] == method:
                lenth = get_range(row)
                rows.append(row[4:lenth])
        return rows


def get_range(rows):
    for index in range(len(rows)):
        if rows[index] == '':
            return index
    return len(rows)


data = get_data_json("negative")
print(data)

print(os.path.relpath("/Users/sumitjain/Work/python/api-automation-framwork/test/test_data/test_data.json"))
