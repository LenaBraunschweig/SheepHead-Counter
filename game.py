import csv
import pandas as pd
import datetime

question_type = None
partner = None
winner = None
rank = {"regular": 5, "no schnitz": 10, "no tricker": 20}
players = []
dealer_index = 0
input_file = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
game_continue = True
next_round = True

# attributes for player: score, name, picker, partner
class Player:
    def __init__(self, name, number):
        self.score = 0
        self.number = number
        self.name = name
        self.picker = False
        self.partner = False

def startup(file_name):
    # create the people
    player_names = []
    for player_number in range(1, 6):
        player_name = input(f"Name of player {player_number}: ")
        player_names.append(player_name)
        current_player = Player(player_name, player_number)
        players.append(current_player)
    
    # create the spreadsheet
    file = file_name + ".csv"
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(player_names)
    
def find_person(person):
    for player in players:
        if ((player.name == person) or (person.isdigit() and (player.number == int(person)))):
            return player
    return None
        
def reset_round():
    for player in players:
        player.picker = False
        player.partner = False

def write_score(file_name):
    current_scores = []
    print("\n")
    for player in players:
        current_scores.append(player.score)
    file = file_name + ".csv"
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(current_scores)

def display_scores(file_name):
    file = file_name + ".csv"
    df = pd.read_csv(file)
    row_count = len(df)
    if row_count > 0:
        print(df.to_string(index=False))

def run_round():
    global next_round
    next_round = True
    global dealer_index
    print(f"\n{players[dealer_index].name} is the dealer for this round")
    question_type = input("\nWas kind of round was this (regular or leaster): ")
    if "regular" in question_type:
        regular_round()
    elif "leaster" in question_type:
        leaster_round()
    else:
        print("Not a valid answer")
        next_round = False
    if next_round:
        dealer_index += 1
        if dealer_index == 5:
            dealer_index = 0

def regular_round():
    global next_round
    picker = input("\nWho was the picker: ")
    picker_person = find_person(picker)
    if picker_person is None:
        print("Not a valid answer")
        next_round = False
        return
    picker_person.picker = True
    def picker_wins(partner_yesno, ranking):
        global next_round
        if ranking not in rank:
            print("Not a valid game")
            next_round = False
            return
        if partner_yesno == None:
            # picker gets 4x whatever losers lose based on rank
            picker_person.score += (4 * rank[ranking])
            for player in players:
                if player.picker == False:
                    player.score -= rank[ranking]
        else:
            # picker gets double whatever losers lose and partner gets the same
            picker_person.score += (2 * rank[ranking])
            partner_person.score += rank[ranking]
            for player in players:
                if ((player.picker == False) and (player.partner == False)):
                    player.score -= rank[ranking]

    def picker_loses(partner_yesno, ranking):
        if partner_yesno == None:
            # picker get negative 4x whatever the others won
            picker_person.score -= (4 * rank[ranking])
            for player in players:
                if player.picker == False:
                    player.score += rank[ranking]
        else:
            # make it so picker loses double and partner loses regular
            picker_person.score -= (2 * rank[ranking])
            partner_person.score -= rank[ranking]
            for player in players:
                if ((player.picker == False) and (player.partner == False)):
                    player.score += rank[ranking]
    
    partner_choice = input("Was there a partner (yes or no): ")
    if partner_choice == "yes":
        partner = input("Which player was the partner: ")
        partner_person = find_person(partner)
        if partner_person is None:
            print("Not a valid answer")
            next_round = False
            return
        partner_person.partner = True
    elif partner_choice == "no":
        partner_person = None
    else:
        print("Not a valid answer")
        next_round = False
        return
    
    win_lose = input("Did the picker win (yes or no): ")
    ranking = input("What kind of round was it (regular, no schnitz, or no tricker): ")
    if win_lose == "yes":
        picker_wins(partner_person, ranking)
    else:
        picker_loses(partner_person, ranking)

def leaster_round():
    global next_round
    winner = input("Who was the winner? (type 'tie' for a tie): ")
    if "tie" not in winner:
        winner_choice = find_person(winner)
        if winner is None:
            print("Not a valid answer")
            next_round = False
            return
        winner_choice.score += 20
        for player in players:
            if player != winner_choice:
                player.score -= 5

def game():
    global game_continue
    global next_round
    startup(input_file)
    while game_continue:
        run_round()
        if next_round:
            write_score(input_file)
        display_scores(input_file)
        reset_round()
        for player in players:
            if player.score >= 100 or player.score <= -100:
                game_continue = False
                print("\n")

game()