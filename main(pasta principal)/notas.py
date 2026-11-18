import os


class Nota:
    def __init__(self, titulo: str, anotacao: str):
        # Remove caracteres inválidos para nomes de arquivos no sistema operacional
        self.titulo = titulo.strip()
        self.anotacao = anotacao

    def obter_nome_arquivo(self) -> str:
        """Gera o nome do arquivo substituindo espaços por sublinhados se necessário."""
        nome_limpo = self.titulo.replace("/", "-").replace("\\", "-")
        return f"{nome_limpo}.txt"

    def arquivo_existe(self) -> bool:
        """Verifica se já existe um arquivo com este título."""
        return os.path.exists(self.obter_nome_arquivo())

    def salvar_txt(self):
        """Salva a nota em um arquivo de texto individual (.txt)."""
        nome_arquivo = self.obter_nome_arquivo()

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"=== {self.titulo.upper()} ===\n\n")
            arquivo.write(f"{self.anotacao}\n")
    @classmethod
    def amostrar_notas(self):
        notas = [arq for arq in  os.listdir() if arq.endswith(".txt")]

        if not notas:
            print("Nenhuma nota encontrada.")
        else:
            print("\n --SUAS NOTAS-- \n")
            for indice, nome_arquivo in enumerate(notas, start=1):
                titulo_limpo = nome_arquivo.replace(".txt", "")
                print(f"{indice} - {titulo_limpo}")

            escolha = int(input("\nDigite o número da nota que voce quer ler: "))

            posicao = escolha - 1

            if 0 <= posicao < len(notas):
                arquivo_selecionado = notas[posicao]

                with open(arquivo_selecionado, "r", encoding="utf-8") as f:
                    print(f.read())

            else:
                print("Número inválido!")