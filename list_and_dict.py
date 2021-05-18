def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Albert", "lastname": "Coronado"}

    super_list = [
        {"firstname": "Albert", "lastname": "Coronado"},
        {"firstname": "Octa", "lastname": "mejia"},
        {"firstname": "Rojo", "lastname": "Ruvalcava"},
        {"firstname": "lola", "lastname": "Pamela chu"},
        {"firstname": "Albert", "lastname": "Wesker"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums":[1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f"{value}, {key}") #turned to check values and keys 

if __name__ == "__main__":
    run()
