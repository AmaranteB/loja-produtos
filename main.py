from produto import Produto
from log import registrar_log

def main():
    produto1 = Produto("Teclado", 350, estoque=10)
    produto2 = Produto("Mouse", 150, estoque=20)

    print("Lista dos produtos")
    print(produto1)
    print(produto2)

    print("\n Vendendo 5 teclados...")
    if produto1.vender(2):
        print("Venda realizada com sucesso!")
        registrar_log("Venda de 5 teclados realizada com sucesso.")
    else:
        print("Estoque insuficiente.")

if __name__ == "__main__":
    main()