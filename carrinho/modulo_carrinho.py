def AdicionarProduto(carrinho):
    nome = input('Digite o nome do produto: ')
    for item in carrinho:
        if item[0] == nome:
            print('---- PRODUTO JÁ EXISTENTE, ATUALIZE O PRODUTO ----')
            return
    categoria = input('Digite a categoria do produto: ')
    quantidade = int(input('Digite a quantidade de produtos: '))
    valor = float(input('Digite o valor do produto: '))
    novo_produto = [nome, categoria, quantidade, valor]
    carrinho.append(novo_produto)
    print('----PRODUTO ADICIONADO!----')

    
def RemoverProduto(carrinho):
    produto = input('Digite o nome do produto que deseja remover: ')
    encontrado = False
    for i, item in enumerate(carrinho):
        if item[0] == produto:
            del carrinho[i]
            print('---- ITEM REMOVIDO COM SUCESSO :) ----')
            encontrado = True
            break
    if not encontrado:
        print('---- ITEM INEXISTENTE :( ----')

        
def AtualizarProduto(carrinho):
    produto = input('Digite o nome do produto que deseja atualizar: ')
    encontrado = False

    for i in range(len(carrinho)):
        if carrinho[i][0] == produto:
            nova_categoria = input('Digite a nova categoria do produto: ')
            nova_quantidade = int(input('Digite a nova quantidade de produtos: '))
            novo_valor = float(input('Digite o novo valor do produto: '))
            carrinho[i] = [produto, nova_categoria, nova_quantidade, novo_valor]
            print('---- PRODUTO ATUALIZADO :) ----')
            encontrado = True
            break

    if not encontrado:
        print('---- PRODUTO INEXISTENTE :( ----')

def VerCarrinho(carrinho):
    tamanho_carrinho = len(carrinho)
    total_compras = 0
    if tamanho_carrinho == 0:
        print('---- CARRINHO VAZIO :( ----')
    else:
        for i in range(tamanho_carrinho):
            print(f'--- {carrinho[i][0]} ---')
            print(f'Categoria: {carrinho[i][1]}')
            print(f'Quantidade: {carrinho[i][2]}')
            print(f'Valor da Unidade:{carrinho[i][3]:.2f}\n')
            total = carrinho[i][2] * carrinho[i][3]
            total_compras += total
    print(f' R$: {total_compras:.2f}')

def VerCategoria(carrinho):
    total_compras = 0
    achados = False
    categoria = input('Que categoria você procura?: ')

    for i in range(len(carrinho)):
        if carrinho[i][1] == categoria:
            achados = True
            print(f'--- {carrinho[i][0]} ---')
            print(f'Categoria: {carrinho[i][1]}')
            print(f'Quantidade: {carrinho[i][2]}')
            print(f'Valor da Unidade: R$ {carrinho[i][3]:.2f}\n')
            total_compras += carrinho[i][2] * carrinho[i][3]

    if not achados:
        print('Nenhum produto dessa categoria foi encontrado.')
    else:
        print(f'O valor total dos produtos da categoria -- "{categoria}" -- é R${total_compras:.2f}')        

def FimDasCompras(carrinho):
    total_compras = 0
    if len(carrinho) == 0:
        print('---NENHUM ITEM ENCONTRADO---')
    else:
        for item in carrinho:
            total_compras += item[2] * item[3]
        carrinho.clear()
    print(f' Total a pagar = R$: {total_compras:.2f}')
