import csv
import json
import os


def get_data_json(test_category=None, test_sub_category=None):
    import sys
    print(sys._getframe().f_code.co_name)
    file_path = "../test/test_data/test_data.json"
    # file_path = "test/test_data/test_data.json"
    fh = open(file_path)
    _data = json.load(fh)
    fh.close()
    posts = _data.get('posts')
    test = _data.get('test_cases')
    return_data = {}
    test_data = []
    for t in test:
        if t.get('enabled'):
            if test_category is not None and t.get('test_category') == test_category:
                if test_sub_category is not None and t.get('test_sub_category') == test_sub_category:
                    test_data.append(t)
                elif test_sub_category is None:
                    test_data.append(t)
            elif test_category is None:
                test_data.append(t)

    return_data['posts'] = posts
    return_data['test_data'] = test_data
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

#
# data = get_data_json("positive")
# print(data)
#
print(os.path.relpath("/Users/sumitjain/Work/python/api-automation-framwork/test/test_data/test_data.json"))
