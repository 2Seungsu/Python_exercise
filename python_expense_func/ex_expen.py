import expense

# 객체 생성
a1=expense.ExpenseReport(300,150)

# 객체를 통해서 고정비용 수정
print(f'고정지출 : {a1.fixOutcome}만원')
a1.fixIncome = 350
print(f'고정수입 : {a1.fixIncome}만원')

# 객체에 대한 정보출력
a1.info()

# 객체의 수입,지출 변동
print(f'남은 예산 : {a1.balanceIncome(30)}')
print(f'남은 예산 : {a1.balanceOutcome(20)}')

# 남은 예산과 이에 대한 경고
print(f'남은 예산: {a1.plan}만원, 경고: {a1.Sign()}')


#객체 생성
a2=expense.Loan(300,150,1500)

#대출 가능 유무 판단 함수
a2.poor()


#################################################################################
# 데이터저장
# 딕셔너리
a1Dict = {'고정수입':a1.fixIncome,'고정지출': a1.fixOutcome, '남은예산':a1.plan}
for k,v in a1Dict.items():
    a1Dict[k] = str(v) + '만원'
print(a1Dict)

a2Dict = {'고정수입':a2.fixIncome,'고정지출': a2.fixOutcome, '남은예산':a2.plan}
for k,v in a2Dict.items():
    a2Dict[k] = str(v) + '만원'
print(a2Dict)


#txt파일
user_name = 'Richard'
fp = open('report.txt', mode = 'w',encoding='utf-8')
for k,v in a1Dict.items():
    fp.write('{}의 {:>6} {:>6}\n'.format(user_name,k,v))

user_name = 'Song'
fp = open('report.txt', mode = 'a',encoding='utf-8')
for k,v in a2Dict.items():
    fp.write('{}의 {:>6} {:>6}\n'.format(user_name,k,v))

fp.close()