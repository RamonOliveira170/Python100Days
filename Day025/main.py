''' with open("./weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)'''

import csv
import pandas

'''with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)'''

data = pandas.read_csv("./weather_data.csv")
print(data)

data_dict = data.to_dict()
print(data_dict)

'''temp_list = data["temp"].to_list()
print(round(sum(temp_list)/len(temp_list), 2))'''
print(round(data["temp"].mean(), 2))

print(data["temp"].max())

print(data[data["day"] == "Monday"] )

print(data[data["temp"] == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

print(monday.temp[0] * 9/5 + 32)

new_data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

new_data_frame = pandas.DataFrame(new_data_dict)
print(new_data_frame)
new_data_frame.to_csv("./new_data_frame.csv")
