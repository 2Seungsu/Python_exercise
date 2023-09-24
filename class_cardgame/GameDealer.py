from Card import Card
import random

class GameDealer:
    def __init__(self):
        self.deck = []

    def print(self):
        print('-'*30)
        print(f'[GameDealer] 딜러가 가진 카드 수 :{len(self.deck)}')
        print('='*30)

        count = 0
        for x in self.deck:
            print(x, end =" ")
            count += 1
            if count % 13 == 0:
                print()


    def make_deck(self):
        card_suits = ["♠","♥","♣","◆"]
        card_numbers = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        
        for suit in card_suits:
            for num in card_numbers:
                self.deck.append(Card(suit,num))  #덱생성
        
        print('[GameDealer] 초기 카드 생성')
        self.print()
        print('-'*30)

    def shuffle(self):
        print(f'[GameDealer] 카드랜덤하게 섞기')

        random.shuffle(self.deck)
        self.print()
        print('-'*30)

    
    def distribute(self,num=10):
        card_list = []
        for _ in range(num):
            card_list.append(self.deck.pop())

    
        return card_list




if __name__ == '__main__':    
    a = GameDealer()
    a.make_deck()
    a.shuffle()

