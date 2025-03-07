from datetime import datetime,timedelta
import zoneinfo
#data
hoje=datetime.now()
print(hoje)

#contas com datas
amanha=hoje +timedelta(days=1)
print(amanha)


data_contrato=datetime(year=2022,month=9,day=1)
tempo_atrasado=hoje-data_contrato
print(tempo_atrasado)


#extrair datas em outro formatos
data="01/09/2022"
data=datetime.strptime(data,'%d/%m/%Y')#pega de um texto e transforma em data
print(data)


#formato brasileiro
print(hoje.strftime("%d/%m/%Y"))#Transforma data em texto


#fuso horário
novo_hoje=hoje-timedelta(hours=1)
print(novo_hoje)

zona=zoneinfo.ZoneInfo('Singapore')
hoje_cuiaba=hoje.astimezone(zona)
print(hoje_cuiaba)