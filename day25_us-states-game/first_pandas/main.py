
import logging as l

l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', level=l.INFO, datefmt='%I:%M:%S')

#Using just file methods
with open("weather_data.csv") as f:
    data = f.readlines()
    l.debug(data)

#Using csv library
import csv

with open("weather_data.csv") as f:
    data = csv.reader(f)
    temperatures : list[int] = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    l.debug(temperatures)


# Using the pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
l.debug(type(data))
l.debug(type(data["temp"]))


data_dict = data.to_dict()
l.debug(data_dict)

temp_list = data["temp"].to_list()
l.debug(temp_list)
l.debug(len(temp_list))


l.debug(data["temp"].mean())
l.debug(data["temp"].max())

#Get Data in Columns
l.debug(data["condition"])
l.debug(data.condition)

l.debug(type(data["condition"]))



# Get Data in Row
l.debug(data[data.day == "Monday"])
l.debug(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
l.debug(monday_temp_F)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



#Central Park Squirrel Data Analysis
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

l.info(grey_squirrels_count)
l.info(red_squirrels_count)
l.info(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")






