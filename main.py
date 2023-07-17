#pandas - integraçao do py com excel
# openpyxl - idem ao panda
#twilio integração do python com SMS
import pandas as pd #o pd é a forma como irei invocar algo relacionado a biblio

#passo a passo
#1 abri os 6 arquivos em exce
listaMeses= ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']#'' ou " " tanto faz

for mes in listaMeses: #para cada mes na listaMeses:
   # print(mes)   #\/pd metodo da biblio pandas
    tabela_vendas=pd.read_excel(f'{mes}.xlsx') #f de formatação p/ mudar os valores de uma forma dinamica
   # print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():# se alguma (any) coluna da table > 55.000
        vendedor=tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]#o values serve p retornar somente o valor, sem ele o loc vai retornar a tabela onde tem o valor
        vendas=tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'no mês {mes} Tem alguém! Vendedor: {vendedor} Vendas: {vendas}')

#tabela_vendas=pd.read_excel ('janeiro.xlsx')
#print(tabela_vendas)

#AINDA NÃO COLOQUEI A PARTE DO TWILIO PQ DEU PREGUIÇA DE CRIAR CONTA



# para cada arquico
# verificar se algum valor é maior que 55.000
#se maior que 55.000, enviar SMS com nome, o mes e as vendas do vendedor
#caso não não faz nada