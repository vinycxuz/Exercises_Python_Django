clientes = []

def menu()->'':
    opcao = input('Escolha sua opcao')
    return int(opcao)    

def criar_cliente ()-> dict:
    nome = input('Digite o nome do cliente: ')
    fone = input('Digite o celular {nome}: ')
    cliente = {
        'nome':  nome,
        'fone': fone
    }
    return cliente

def buscar_indice_nome (nome)-> int:
    resultado = -1
    indice = 0
    while (indice < len(clientes)) and (resultado == -1):
        if (clientes[indice]['nome']==nome):
            resultado = indice
        else:
            indice = indice + 1
    return resultado

def incluir()->None:
    cliente = criar_cliente()
    clientes.append(cliente)
    input('Registro concluido, press Enter...')

def editar()->None:
    cliente = criar_cliente()
    posicao = buscar_cliente_nome('cliente')
    if(posicao != -1):
        clientes = cliente[posicao]
        input('Registro alterado, press Enter...')
    else:
        input('Cliente nao cadastrado, press Enter...')

def remover()->None:
    nome = input(f'Digite o nome do cliente: ')
    posicao = buscar_cliente_nome(nome)
    if(posicao != -1):
        clientes.pop()
        print('Cliente da posicao ->{posicao} removido com sucesso, press Enter...')
    else:
        print('Cliente nao encontrado')

def buscar_cliente_nome()->None:
    nome = input(f'Digite o nome do cliente')
    posicao = buscar_indice_nome(nome)
    if(posicao != -1):
        print('Cliente encontrado:')
        print(f'Nome: {clientes[posicao]["nome"]} ')
        print(f'Telefone: {clientes[posicao]["fone"]} ')
    else:
        print('Cliente nao encontrado')

def localizar_nome(nome)->dict:
    posicao = buscar_indice_nome()
    if(posicao != -1):
        print(f'Nome: {clientes[posicao]["nome"]}')
        print(f'Telefone: {clientes[posicao]["fone"]}')
    else:
        print('Cliente nao encontrado')

def listar_clientes()->None:
    if(len(clientes) == 0):
        print('Nao ha clientes cadastrados')
        input('Press Enter...')
    else:
        for cliente in clientes:
            print(f'Cliente: {clientes["nome"]} ')
            print(f'Telefone: {clientes["fone"]}')
        input('Press enter for menu...')

opcao = 0

while(opcao != 6):
    opcao = menu()
    if (opcao > 6):
        input(f'Opcao invalida, press Enter...')
    elif opcao == 1:
        incluir()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        localizar_nome()
    elif opcao == 5:
        listar_clientes()
    else:
        break
print('sessao encerrada')



