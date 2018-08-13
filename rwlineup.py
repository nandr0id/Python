import csv

# a file in the current directory
FILENAME = "player_list.csv"

def write_lineup(player_list):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(player_list) 

def read_lineup():
    player_list = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            player_list.append(row)
    return player_list
