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



        # Validação: impede a criação se o título já existir
        if Nota.arquivo_existe(tit):
            console.print(f'[bold red]Erro: Já existe uma nota com o título "{tit}"![/bold red]')
        else:
            anot = str(input(f'Anotação do {tit}: '))
            nota = Nota(titulo=tit, anotacao=anot)
            nota.salvar_txt()
            console.print(f'[bold green]Arquivo "{nota.obter_nome_arquivo()}" criado com sucesso![/bold green]')

    if esc == 2:
        bloco.escolher_nota()


    if esc == 3:
        print('Saindo do bloco de notas!')

if __name__ == '__main__':
    main()