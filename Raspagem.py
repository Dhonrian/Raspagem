import requests, time
from bs4 import BeautifulSoup

start_time = time.clock()
count = 0
txt = []
val = []
soma = 0

print('\n')
ult_pag = input("Digite o número de páginas (1 a 32299)[Apenas ENTER para 500 itens] : ")
print('\n')
if ult_pag == '':
    ult_pag = 34
for i in range(1, int(ult_pag)+1):
    pag = requests.get('http://www.portaldatransparencia.gov.br/convenios/convenioslistageral.asp?bogus=1&Pagina='+str(i))
    soup = BeautifulSoup(pag.content, 'lxml')
    valores = soup.findAll('td','colunaValor')
    obj = soup.findAll('td', style="width: 30em;")

    for v,o in zip(valores[2:], obj):
        obj = o.getText().replace('\n','').replace('\r','')
        obj = ''.join(obj.strip())
        val.append(v.getText().replace('.','').replace(',','.').replace('\n','').replace('\r',''))    
        txt.append(obj)
        count += 1
        
        for s in val:
            soma += float(s)

    for p in range(len(txt)):
        print(txt[p],' -> R$: ',val[p])
        print('\n')

print("Valor total R$:", round(soma, 3))
print("Itens encontrados :", count)
print("--- %s segundos ---" % (time.clock() - start_time))

