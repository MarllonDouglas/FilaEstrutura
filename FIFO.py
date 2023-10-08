ultimo = 10
fila=list(range(1,ultimo + 1))
while True:
    print(f'\nExistem {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print('''\n-------- Atendimento eletrônico --------\n
[F] - Para adicionar um cliente ao fim da fila;
[A] - Para realizar o atendimento;
[S] - Para sair.\n''')
    operacao = input('Operação (F , A ou S):')
    operacao = operacao.upper()
    if operacao == 'A':
        if len(fila)>0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido.')
        else:
            print('Fila Vazia! Ninguém para atender.')
    elif operacao == 'F':
        ultimo +=1
        fila.append(ultimo)
        print('Cliente adicionado a fila de atendimento.')
    elif operacao == 'S':
        break
    else:
        print('Operação inválida! Digite apenas F, A ou S!')