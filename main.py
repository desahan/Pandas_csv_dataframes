import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240314.csv")
grey = data[data["Primary Fur Color"] == "Gray"]
red = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]

grey_count = len(grey)
red_count = len(red)
black_count = len(black)

data_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "Count": [grey_count, red_count, black_count]
}

frame = pandas.DataFrame(data_dict)

print(frame)