from GameDealer import GameDealer
from Player import Player

class CardGame:
    def main(self):
        
        hb = Player('hb')
        nb = Player('nb')

        abc = GameDealer()
        abc.make_deck()
        abc.shuffle()
        hb.bunbae(abc,10)
        nb.bunbae(abc,10)
        nb.result()
        hb.result()

        print("카드 꺼내기----------------")
        nb.open()
        hb.open()
        nb.result()
        hb.result()


        ####################################
        while True:
            abc.print()
            print('4장씩 나눠주기')
            hb.bunbae(abc,4)
            nb.bunbae(abc,4)
            
            nb.result()
            hb.result()
            nb.open()
            hb.open()
            nb.result()
            hb.result()

            if(len(abc.deck)==0):
                print("무승부 : 딜러 카드 0")
                break

            if(len(nb.holdingCards)==0):
                print("놀부 승 ")
                break

            if(len(hb.holdingCards)==0):
                print("흥부 승 ")
                break

CardGame().main()