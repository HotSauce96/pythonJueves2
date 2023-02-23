# Condicionales con Python

nivelDeAgua=int(input("Digita el nivel de agua: "))
if nivelDeAgua >= 0 and nivelDeAgua <= 250:
    print(f'El nivel de agua es muy bajo; {nivelDeAgua} U')
elif nivelDeAgua > 250 and nivelDeAgua <= 450:
    print(f'El nivel de agua es óptimo; {nivelDeAgua} U')
elif nivelDeAgua > 450: 
    print(f'El nivel de agua es crítico, evacúe; {nivelDeAgua} U')    
else: 
    print(f'Revise el sensor')
    
    nivelDeAgua= 800
    
    
