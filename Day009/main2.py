capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {
        "num_times_visited": 5,
        "cities_visited": ["Paris", "Lille", "Bijon"],
    },
    "Germany": {
        "num_times_visited": 3,
        "cities_visited": ["Stuttgart", "Berlin"],
    }
}

print(travel_log["France"])

print(travel_log["France"]["cities_visited"][2])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])
