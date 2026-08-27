import pandas

read = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260826.csv")
#print(read["Primary Fur Color"])

gray_squirrels_count = len(read[read["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(read[read["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(read[read["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

squirrels_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrels_data)
df.to_csv("squirrel_color_count.csv")
