from rich.console import Console
from rich.table import Table
from rich import box

console = Console(force_terminal=True)


class Opcao:
    def __init__(self):
        pass

    def exibir(self):

        tabela = Table(title="Bloco De Notas", box=box.ROUNDED)

        tabela.add_column("OPÇÃO", style="cyan", justify="center")
        tabela.add_column("Ação", style="bold yellow")


        tabela.add_row("1", "Criar Nota")
        tabela.add_row("2", "Listar Notas")
        tabela.add_row("3", "Sair")

        console.print(tabela)

    


def main():
    menu = Opcao()
    menu.exibir()


if __name__ == '__main__':
    main()