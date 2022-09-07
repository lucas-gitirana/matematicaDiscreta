usuario = ''
senha = ''

print('BEM-VINDO(A)!')
while usuario != 'aluno' and senha != 'alunoIFC123#':
    usuario = input('Usuário: ')
    senha = input('Senha: ')

    if usuario != 'aluno' or senha != 'alunoIFC123#':
        print("Usuário ou senha incorretos!")

continuar = 's'

print('CADASTRO DE ALUNO')
while continuar == 's' or continuar == 'S':

    nomeAluno = input("Nome do aluno: ")

    aulas = -1
    faltas = -1

    while ((aulas <= 0) or (aulas > 365)) or ((faltas <= 0) or (faltas > aulas)):
        aulas = int(input("Informe o número total de aulas no ano: "))
        faltas = int(input("Informe o número total de faltas do aluno no ano: "))

        if ((aulas <= 0) or (aulas > 365)) or ((faltas <= 0) or (faltas > aulas)):
            print("Insira valores válidos!")


    percentualFaltas = (faltas / aulas) * 100

    tri1 = -1
    tri2 = -1
    tri3 = -1

    while (tri1 < 0 or tri1 > 10) or (tri2 < 0 or tri2 > 10) or (tri3 < 0 or tri3 > 10):

        tri1 = float(input("Informe a nota do primeiro trimestre: "))
        tri2 = float(input("Informe a nota do segundo trimestre: "))
        tri3 = float(input("Informe a nota do terceiro trimestre: "))

        if (tri1 < 0 or tri1 > 10) or (tri2 < 0 or tri2 > 10) or (tri3 < 0 or tri3 > 10):
            print("Insira valores entre 0 e 10!")

    mediaFinal = (tri1 + tri2 + tri3) / 3
    situacao = ''

    if (mediaFinal >= 7) and (percentualFaltas < 25):
        situacao = 'Aprovado(a)'
    else:
        situacao = 'Reprovado(a)'

    print(f'O aluno {nomeAluno} está {situacao}.')
    print(f'Faltas do aluno: {faltas} aulas - {percentualFaltas}%')
    print(f'Média final do aluno: {mediaFinal}')

    continuar = input('Deseja cadastrar um novo aluno? (Digite S ou N): ')






