from src.app.use_cases.criar_pedido import CriarPedido


def main() -> None:
    criar_pedido = CriarPedido()

    pedido = criar_pedido.executar("Cliente A", 100.0, "normal")

    print("Pedido criado:")
    print(pedido.cliente, pedido.valor_original, pedido.valor_final())


if __name__ == "__main__":
    main()