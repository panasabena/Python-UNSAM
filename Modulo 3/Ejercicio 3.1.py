## Ejercicio 3.1
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i]=='A':
            
            return True
           
        else: ## Se saco el return False, porque nos estaba cortando el programa
            i += 1
            print(i)

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
