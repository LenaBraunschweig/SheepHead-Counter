question_type = None

def startup():
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
    pass

def leaster_round():
    pass