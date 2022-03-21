from card import Card
import csv
import random

class Deck:
    def __init__(self):
        self.card_list = []
        self.point_dict = {}
        with open("data/quiddler_cards.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #print(row)
                self.point_dict[row["Card"]] = row["Points"]
                for i in range(int(row["How Many"])):
                    self.card_list.append(Card(row["Card"]))
        self.shuffle()
        self.print()

    def print(self):
        print(*self.card_list, sep=",")

    def shuffle(self):
        random.shuffle(self.card_list)
        for i in range(len(self.card_list)):
            self.card_list[i].z = i
    
    def draw(self, n=1):
        l = []
        for i in range(n):
            l.append(self.card_list.pop())
            l[i].flip_over()
            #l[i].face_up = True
        return l

