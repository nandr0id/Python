import rwlineup as rw

player_list = [] #created empty global player_list to fill with player as they are created
positions = ("1B", "2B", "3B", "C", "LF", "SS", "CF", "RF", "P"); #positions stored in a tuple

#displays player lineup
def display_player_list():
     print("\t" "Player\t\t" + "POS\t" + "AB\t" + "H\t" + "AVG")
     print("-" * 55)
     for player in player_list:
                  print(str(player_list.index(player)) + "\t" + player[0]
                        + "\t\t" + player[1] + "\t" + str(player[2]) +
                        "\t" + str(player[3]) + "\t" + str(player[4]))

#display menu of options
def display_menu():
    print("=" * 55)
    print("\t\tBaseball Team Manager")
    print("Menu Options")
    print("1-Display the lineup")
    print("2-Add Player")
    print("3-Remove Player")
    print("4-Move Player")
    print("5-Edit Player Position")
    print("6-Edit Player Stats")
    print("7-Exit Program")
    print("Positions")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("=" * 55)
    print()

#captures input from user, and then appends player to player_list             
def add_player():
    name = str(input("Name: ")).title()            
    position = str(input("Postion: ")).upper()
    while position not in positions: #while loop to make sure valid positions are chosen
         position = input("Enter a valid position: ")
    at_bats = int(input("At Bats: "))             
    hits = int(input("Hits: "))
    bat_avg = round((hits/at_bats), 3)
    player = []
    player.append(name)
    player.append(position)
    player.append(at_bats)
    player.append(hits)
    player.append(bat_avg)
    player_list.append(player)
    rw.write_lineup(player_list)
    print(name + " was added.")
    
#deletes player and relevant stats             
def delete_player():
    player_number = int(input("Lineup number:  "))
    print(str(player_list[player_number][0]) + " was removed.")
    player_list.remove(player_list[player_number])
    rw.write_lineup(player_list)

#moves player using lineup value     
def edit_player_lineup():
    player_number = int(input("Current lineup number:  "))
    print(str(player_list[player_number][0]) + " was selected.")
    player_number_new = int(input("New lineup number:  "))
    lineup_new = player_list.pop(player_number)
    player_list.insert(player_number_new, lineup_new)
    rw.write_lineup(player_list)
    print(str(player_list[player_number_new][0]) + " was moved.")

#edits type of player position and ensures valid positions are entered, used global tuple
def edit_player_position():
     player_number = int(input("Lineup number:  "))
     print(player_list[player_number][0] + " was selected.")
     position_new = input("New position :  ").upper()
     while position_new not in positions: #while loop to make sure valid positions are chosen
              position_new = input("Enter a valid position:  ")
     player_list[player_number][1] =  position_new
     rw.write_lineup(player_list)
     print(player_list[player_number][0] + "'s position was updated.")

#edits player at_bats and hits and stores new bat_avg
def edit_player_stat():
     player_number = int(input("Lineup number:  "))
     print("You selected " + player_list[player_number][0] + " AB=" + str(player_list[player_number][2]) + " H=" + str(player_list[player_number][3]))
     at_bats_new = int(input("At bats:  "))
     hits_new = int(input("Hits:  "))
     bat_avg_new = round((hits_new/at_bats_new), 3)
     player_list[player_number][2] =  at_bats_new
     player_list[player_number][3] =  hits_new
     player_list[player_number][4] =  bat_avg_new
     rw.write_lineup(player_list)
     print(player_list[player_number][0] + " was updated.")
                         
def main():
    display_menu() #call banner function only once in beginning
    print()
    player_list = rw.read_lineup()
    #while loop to start
    while True:
        choice = input("Menu option:  ")
        if choice == "1":
            display_player_list()
        elif choice == "2":
            add_player()
        elif choice == "3":
            delete_player()
        elif choice == "4":
            edit_player_lineup()
        elif choice == "5":
            edit_player_position()
        elif choice == "6":
            edit_player_stat()
        elif choice == "7":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
            




