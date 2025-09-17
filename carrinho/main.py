import modulo_carrinho
carrinho = []
while True:
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar produto")
    print("4 - Ver carrinho")
    print("5 - Ver por categoria")
    print("6 - Finalizar compras")
    print("7 - Finalizar Programa")
    escolha = int(input())
    if escolha == 1:
        modulo_carrinho.AdicionarProduto(carrinho)
    elif escolha == 2:
        modulo_carrinho.RemoverProduto(carrinho)
    elif escolha == 3:
        modulo_carrinho.AtualizarProduto(carrinho)
    elif escolha == 4:
        modulo_carrinho.VerCarrinho(carrinho)
    elif escolha == 5:
        modulo_carrinho.VerCategoria(carrinho)
    elif escolha == 6:
        modulo_carrinho.FimDasCompras(carrinho)
    elif escolha == 7:
        print('----FIM DO PROGRAMA ---')
        break
    else:
        print('---DIGITE UMA OPÇÃO VALIDA---')
