from menu import Opcao
from rich.console import Console

# Instanciamos o Console forçando a saída de cores ANSI no PyCharm
console = Console(force_terminal=True)


def main():
    bloco = Opcao()
    bloco.exibir()

    opcao_valida = [1,2,3]

    while True:
        try:
            esc = int(input('ESCOLHA SUA OPÇÃO: '))

            if esc not in opcao_valida:
                raise ValueError('[bold red]Opção inexistente![/bold red]')
        except ValueError as e:
            if '[bold red]' in str(e):
                console.print(str(e))

            else:
                console.print('[bold red]Opção inválida![/bold red]')
        else:
            console.print('[bold green]OPÇÃO ACEITA![/bold green]')
            break


if __name__ == '__main__':
    main()