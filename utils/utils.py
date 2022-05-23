def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_total(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional') or item.get('preco_quantitativo')
            for item
            in carrinho.values()
        ]
    )

