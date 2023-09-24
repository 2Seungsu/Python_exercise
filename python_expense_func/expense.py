## 프로젝트
## 가계부

# 속성 : 금액(예산, 수입, 지출) 수입항목, 지출항목, 
# 기능 : 예산보다 지출이 많을 시 경보, 잔고 업데이트, 지출 금액 누적시키기, 총 지출 금액, 총 수입 금액

class ExpenseReport:

    #생성자 인스턴스
    def __init__(self, _fixIncome, _fixOutcome,_plan=200):
        self.plan = _plan
        self.__fixIncome = _fixIncome
        self.__fixOutcome = _fixOutcome
    
    #비공개 인스턴스
    #고정수입과 고정지출은 사적인 사항으로 민감할 수 있기때문에 비공개로 설정   
    @property
    def fixIncome(self): return self.__fixIncome
    @property
    def fixOutcome(self): return self.__fixOutcome


    #고정수입과 고정지출이 변할 수 있으므로 수정접근할 수 있게 만들어줌
    @fixIncome.setter
    def fixIncome(self,new_fixIncome): self.__fixIncome = new_fixIncome
    @fixOutcome.setter
    def fixOutcome(self,new_fixOutcome): self.__fixIncome = new_fixOutcome


    def info(self):
        print(f'가계부의 한달 예산은 {self.plan}만원입니다.\n고정수입은 {self.fixIncome}만원이며 고정지출은 {self.fixOutcome}만원입니다.')

    def balnace(self):
        print(f'남은 예산은 {self.plan}만원입니다.')
    
    def balanceIncome(self,income):
        self.plan=self.plan + income
        return f'{self.plan}만원'

    def balanceOutcome(self,outcome):
        self.plan=self.plan - outcome
        return f'{self.plan}만원'

    def Sign(self):
        if self.fixIncome-self.fixOutcome < self.plan - self.plan*0.2:
            return 'GreenSign'
        elif self.fixIncome-self.fixOutcome - self.plan*0.2 < self.plan:
            return 'YellowSign'
        else:
            return 'RedSgin'
        


class Loan(ExpenseReport):

    def __init__(self, _fixIncome, _fixOutcome,_money=1000, _plan=200 ):
        super().__init__(_fixIncome, _fixOutcome, _plan)
        self.__money = _money
    
    @property
    def money(self): return self.__money 
    @money.setter
    def money(self,new_money): self.__money = new_money


    def poor(self):
        try:
            if self.money - self.plan >= 500:    #돈을 갚을 수 있는 능력: 빌릴액수 - 잔고 >= 500이면 갚을 능력이 없다고 판단 
                raise Exception
            else:
                print('대출가능합니다.')
        except Exception:
            print('대출불가능합니다.')

