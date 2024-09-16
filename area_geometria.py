print('Informe 1 para calcular a area do triangulo')
print('Informe 2 para calcular a area do retangulo')
print('Informe 3 para calcular a area do circulo')
print('Informe 0 para calcular sair!')                      


while True:
    operação = float(input('Seleccione uma operação: '))

    if operação != 0:
            
        if operação >= 0 and operação <=3:

            match operação:
                case 1:
                    base = float(input('Informe a base do triangulo: '))
                    altura = float(input('Informe a altura do triandgulo: '))

                    area = base * altura/2

                    print('A area do triangulo e: ',area)

                case 2:
                    base = float(input('Informe a base do ratangulo: '))
                    altura = float(input('Informe a altura do retangulo: '))

                    area = base * altura

                    print('A area do retangulo e: ',area)
                            
                case 3:
                    raio = float(input('Informe o radio do circulo: '))

                    area = 3.14 * raio**2
                            
                    print('A area do circulo e: ',area)
        else:
            print("")
            print("Informe uma operação valida!!")

    else:
        print("")
        print("Ate logo!!")
        print("")
        break