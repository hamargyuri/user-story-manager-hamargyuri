from models import *


def create_tables():
    answer = None
    while answer not in ("Y", "y", "N", "n"):
        answer = input("Do you want to (re)create the tables? (Y/N) ")
        if answer in ("Y", "y"):
            try:
                db.drop_tables([Story], safe=True)
                db.create_tables([Story], safe=True)
            except:
                db.create_tables([Story], safe=True)
        elif answer in ("N", "n"):
            pass
        else:
            print("Please enter only 'Y' or 'N'.")
