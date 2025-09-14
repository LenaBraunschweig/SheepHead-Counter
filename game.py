question_type = None
partner = None
winner = None
rank = {"regular": 5, "no schnitz": 10, "no_tricker": 20}

# attributes for player: score, name, dealer (boolean value)


def startup():
    pass

def display_scores():
    pass

def start_round():
    pass

def first_question():
    question_type = input("Is this a regular round or a leaster round: ")
    if question_type == "regular":
        regular_round()
    elif question_type == "leaster":
        leaster_round()
    else:
        print("Not an answer")

def regular_round():
    def picker_wins(partner_yesno, rank):
        if partner_yesno == None:
            # make it so picker gets 4x whatever losers lose based on rank
            pass
        else:
            # make it so picker gets double whatever losers lose and partner gets the same
            pass

    def picker_loses(partner_yesno, rank):
        if partner_yesno == None:
            # make it so picker get negative 4x whatever the others won
            pass
        else:
            # make it so picker loses double and partner loses regular
            pass
        pass
    
    partner_choice = input("Was there a partner, yes or no?")
    if partner_choice == "yes":
        partner = input("Which player was the partner?")
    else:
        partner = None
    
    win_lose = input("Did the picker win?")
    ranking = input("Was it a regular round, no schnitz, or no tricker")
    if win_lose == "yes":
        picker_wins(partner, ranking)
    else:
        picker_wins(partner, ranking)

    pass

def leaster_round():
    winner_choice = input("Who was the winner? (select None for a tie)")
    if winner_choice != "tie":
        winner = winner_choice