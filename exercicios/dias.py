




dia = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

dia_segundo = dia * 86400
hora_segundo = horas * 3600
minuto_segundo = minutos * 60

total = dia_segundo + hora_segundo + minuto_segundo


print(f'Seus dias {dia} em segundos {dia_segundo}')
print(f'Suas horas {horas} em segundos {hora_segundo}')
print(f'Seus minutos {minutos} em segundos {minuto_segundo}')
print(f'Total: {total}')
