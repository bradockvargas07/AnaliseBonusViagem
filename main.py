import pandas as pd
from twilio.rest import Client
# Your Auth Token from twilio.com/console
account_sid = "ACe75f2b88f8abe33eda972ff1913e7c03"
auth_token = "c96cd7c5dadca99fd63ef4b7328b40d4"
client = Client(account_sid, auth_token)

#abrir arquivos excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
   # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+5547991663065",
            from_="+16187268670",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

