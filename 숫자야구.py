import random
import pandas as pd

random.seed(10)
computer = random.sample(range(1,10),1)
computer.extend(random.sample(range(10),2))
computer




def numBaseball():

    while True:
        person = input('세자리 숫자입력:')
        attack = [int(i) if i.isdigit() else i for i in person]
        if attack[0] == 0 or len(attack) != 3:
            print('세자리 숫자를 다시 입력해주세요.')
        else:
            if all([isinstance(i,int) for i in attack]):
                if computer == attack:
                    print('승리했습니다')
                    break
                elif len(set(computer) & set(attack)) == 0:
                    print('아웃') 
                elif set([(idx,val) for idx,val in enumerate(computer)]) & set([(idx,val) for idx,val in enumerate(attack)]):
                    if set(computer) & set(attack):
                        if len(set(computer) & set(attack))-len(set([(idx,val) for idx,val in enumerate(computer)]) & set([(idx,val) for idx,val in enumerate(attack)])) != 0:
                            print(f'{len(set([(idx,val) for idx,val in enumerate(computer)]) & set([(idx,val) for idx,val in enumerate(attack)]))}스트라이크 {len(set(computer) & set(attack))-len(set([(idx,val) for idx,val in enumerate(computer)]) & set([(idx,val) for idx,val in enumerate(attack)]))}볼')
                        else:
                            print(f'{len(set([(idx,val) for idx,val in enumerate(computer)]) & set([(idx,val) for idx,val in enumerate(attack)]))}스트라이크 ') 
                    else:
                        print(f'{len(set([(idx,val) for idx,val in enumerate(computer)]) & set([(idx,val) for idx,val in enumerate(attack)]))}스트라이크')

                elif not set([(idx,val) for idx,val in enumerate(computer)]) & set([(idx,val) for idx,val in enumerate(attack)]) and set(computer) & set(attack):
                    print(f'{len(set(computer) & set(attack))}볼')
            else:
                print('다시 세자리 숫자를 입력해주십시오.')
                    
import time
before = time.time()
numBaseball()
after = time.time()
print(f'{(after - before):.2f}초만에 승리했습니다.')