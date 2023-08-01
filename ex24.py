# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

total_value = 1000000
loan_date = datetime(2020, 12, 20) #primeira data do emprestimo
loan_time = relativedelta(years=5)
final_date = loan_date + loan_time #data inicial mais os anos de pagamento


installment_date = loan_date
total_installment_dates = [] #lista contem datas/vencimentos

while installment_date < final_date:
    total_installment_dates.append(installment_date)
    installment_date += relativedelta(months=1) 

#Não consegui terminar e segui pelo curso
number_of_installments = len(total_installment_dates)
value_of_installments = f'{total_value / number_of_installments:.2f}'

for datas in total_installment_dates:
    print(datas)

print(f'Total de meses {number_of_installments}, valor das parcelas R${value_of_installments}')
