import os

class Nota:
    def __init__(self, titulo: str, anotacao: str):
        # Remove caracteres inválidos para nomes de arquivos no sistema operacional
        self.titulo = titulo.strip()
        self.anotacao = anotacao

    @staticmethod
    def limpa_titulo(titulo: str) -> str:
        """Deixa o titulo limpo sem nada de caracteres"""
        titulo_limpo = titulo.strip().replace("/", "-").replace("\\", "-")

        if titulo_limpo.lower().endswith(".txt"):
            titulo_limpo = titulo_limpo[:-4]

        return titulo_limpo

    def obter_nome_arquivo(self) -> str:
        """Gera o nome do arquivo substituindo espaços por sublinhados se necessário."""
        nome_limpo = self.titulo.replace("/", "-").replace("\\", "-").replace(".txt", "")
        return f"{nome_limpo}.txt"

    @staticmethod
    def arquivo_existe(titulo: str) -> str:
        """Verifica se já existe um arquivo com este título."""

        titulo_limpo = Nota.limpa_titulo(titulo)
        nome_arquivo = f"{titulo_limpo}.txt"
        return os.path.exists(nome_arquivo)

    def salvar_txt(self):
        """Salva a nota em um arquivo de texto individual (.txt)."""
        nome_arquivo = self.obter_nome_arquivo()

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"=== {self.titulo.upper()} ===\n\n")
            arquivo.write(f"{self.anotacao}\n")
    @classmethod
    def amostrar_notas(cls):
        notas = [arq for arq in  os.listdir() if arq.endswith(".txt")]

        if not notas:
            print("Nenhuma nota encontrada.")
        else:
            print("\n --SUAS NOTAS-- \n")
            for indice, nome_arquivo in enumerate(notas, start=1):
                titulo_limpo = nome_arquivo.replace(".txt", "")
                print(f"{indice} - {titulo_limpo}")

        return notas

    @classmethod
    def ler_notas(cls, nome_arquivo: str) -> str:
        """ler e retorna o arquivo selecionado."""
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()