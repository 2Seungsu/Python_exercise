from GameDealer import GameDealer


class Player:
    def __init__(self, user):
        self.user=user
        self.holdingCards=[]
        self.openCards=[]

    def open(self):
        cards=self.holdingCards
        holds2=[]
        while True:
            src_card = cards[0]
            flag=False
            for i in range(1,len(self.holdingCards)):
                dst_card = self.holdingCards[i]
                if(src_card.number == dst_card.number):
                    self.holdingCards.remove(dst_card)
                    self.holdingCards.remove(src_card)
                    self.openCards.append(dst_card)
                    self.openCards.append(src_card)
                    flag=True
                    break
            if (flag==False):
                self.holdingCards.remove(src_card)
                holds2.append(src_card)

            if(len(self.holdingCards)==0):
                break
        
        self.holdingCards = holds2


    def bunbae(self, dealer,num=10):
        self.holdingCards += dealer.distribute(num)
        return self.holdingCards


    def result(self):

        print('='*30)
        print(f'[{self.user}] open card list : {len(self.openCards)}')
        print(self.openCards)
        print()
        print(f'[{self.user}] holding card list : {len(self.holdingCards)}')
        print(self.holdingCards)
        return None
