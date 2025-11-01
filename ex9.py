n = int (input ('Digite o número referente à tabuada que você deseja acessar: '))
controle = 0

while controle < 11:
    print (f'{n} X {controle} = {n*controle}')
    controle += 1