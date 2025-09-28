question_type = None
partner = None
winner = None
rank = {"regular": 5, "no schnitz": 10, "no tricker": 20}
players = []
dealer_index = 0

# attributes for player: score, name, picker, partner
class Player:
    def __init__(self, name, number):
        self.score = 0
        self.number = number
        self.name = name
        self.picker = False
        self.partner = False

def startup():
    # create the people
    for player_number in range(1, 6):
        player_name = input(f"What is the name of player {player_number}")
        current_player = Player(player_name, player_number)
        players.append(current_player)

def find_person(person):
    for player in players:
        if ((player.number == int(person)) or (player.name == person)):
            return player
    return None
        
def reset_round():
    for player in players:
        player.picker = False
        player.partner = False

def write_score():
    pass

def display_scores():
    pass

def run_round():
    print(f"{players[dealer_index].name} is the dealer for this round")
    question_type = input("Was this a regular round or a leaster round: ")
    if question_type == "regular":
        regular_round()
    elif question_type == "leaster":
        leaster_round()
    else:
        print("Not an answer")
    dealer_index += 1
    if dealer_index == 5:
        dealer_index = 0

def regular_round():
    picker = input("Who was the winner?")
    picker_person = find_person(picker)
    picker_person.picker = True
    def picker_wins(partner_yesno, ranking):
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
    
    partner_choice = input("Was there a partner, yes or no?")
    if partner_choice == "yes":
        partner = input("Which player was the partner?")
        partner_person = find_person(partner)
        partner_person.partner = True
    else:
        partner_person = None
    
    win_lose = input("Did the picker win?")
    ranking = input("Was it a regular round, no schnitz, or no tricker")
    if win_lose == "yes":
        picker_wins(partner_person, ranking)
    else:
        picker_loses(partner_person, ranking)

def leaster_round():
    winner = input("Who was the winner? (type 'tie' for a tie)")
    if winner != "tie":
        winner_choice = find_person(winner)
        winner_choice.score += 20
        for player in players:
            if player != winner_choice:
                player.score -= 5