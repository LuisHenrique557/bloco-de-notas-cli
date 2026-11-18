from menu import Opcao
from notas import Nota
from rich.console import Console

console = Console(force_terminal=True)


def main():
    bloco = Opcao()
    bloco.exibir()

    opcao_valida = [1, 2, 3]

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

    if esc == 1:
        tit = str(input('Digite o titulo do bloco de notas: ')).strip()

        # Instanciamos temporariamente para testar a existência
        nota_teste = Nota(titulo=tit, anotacao="")

        # Validação: impede a criação se o título já existir
        if nota_teste.arquivo_existe():
            console.print(f'[bold red]Erro: Já existe uma nota com o título "{tit}.txt"![/bold red]')
        else:
            anot = str(input(f'Anotação do {tit}: '))
            nota = Nota(titulo=tit, anotacao=anot)
            nota.salvar_txt()
            console.print(f'[bold green]Arquivo "{nota.obter_nome_arquivo()}" criado com sucesso![/bold green]')

    if esc == 2:
        Nota.amostrar_notas()

if __name__ == '__main__':
    main()