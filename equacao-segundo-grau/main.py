# Calcular as Raízes de uma Equação do 2º Grau completa
def raizes(a, b, c):
    delta = (b**2 - 4*a*c)
    x_uma_linha = (-b + delta**(1/2)) / (2*a)
    x_duas_linha = (-b - delta**(1/2)) / (2*a)
    return x_uma_linha, x_duas_linha

if __name__ == '__main__':
    while True:
        print('Calculando as raízes de uma equação de 2º grau (ax² + bx + c = 0)\n')
        a = int(input('Informe o valor de a: '))
        b = int(input('Informe o valor de b: '))
        c = int(input('Informe o valor de c: '))
      
        resultado = (raizes(a, b, c))

        print(f'\nO valor de x1 e x2 é:  {resultado}.\n')

        continuar = input('Digite SAIR para finalizar ou aperte ENTER para fazer um novo cálculo.\n')

        if continuar.upper() == 'SAIR':
            break