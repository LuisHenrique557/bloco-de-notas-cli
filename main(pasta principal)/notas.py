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