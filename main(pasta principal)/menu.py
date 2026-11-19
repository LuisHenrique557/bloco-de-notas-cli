from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from notas import Nota

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

    def escolher_nota(self):
        notas = Nota.amostrar_notas()

        if not notas:
            return

        quantidade_de_notas = len(notas)

        while True:
            try:
                escolha = int(input(f'\nQual nota você quer escolher? entre [1 a {quantidade_de_notas}]: '))

                if not (1 <= escolha <= quantidade_de_notas):
                    raise ValueError

            except ValueError:
                console.print(f'[bold red]Opção inválida! Digite um número entre 1 e {quantidade_de_notas}[/bold red]')

            else:
                posicao = escolha - 1
                titulo_selecionado = notas[posicao]
                conteudo = Nota.ler_notas(titulo_selecionado)

                console.print(Panel(conteudo, title=f"--{titulo_selecionado}--", expand=False))
                break