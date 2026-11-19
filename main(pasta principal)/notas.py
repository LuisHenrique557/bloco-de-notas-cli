import sqlite3

DB_NAME = "bloco_de_notas.db"


class Nota:
    def __init__(self, titulo: str, anotacao: str):
        self.titulo = self.limpa_titulo(titulo)
        self.anotacao = anotacao

    @staticmethod
    def iniciar_banco():
        """Cria a tabela no banco de dados SQLite caso ela ainda não exista."""
        with sqlite3.connect(DB_NAME) as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT UNIQUE NOT NULL,
                    anotacao TEXT NOT NULL
                )
            """)
            conexao.commit()

    @staticmethod
    def limpa_titulo(titulo: str) -> str:
        """Limpa espaços extras nas extremidades do título."""
        return titulo.strip()

    @staticmethod
    def arquivo_existe(titulo: str) -> bool:
        """Verifica no banco de dados se já existe uma nota registrada com este título."""
        titulo_limpo = Nota.limpa_titulo(titulo)
        with sqlite3.connect(DB_NAME) as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT 1 FROM notas WHERE LOWER(titulo) = LOWER(?)", (titulo_limpo,))
            return cursor.fetchone() is not None

    def salvar_db(self):
        """Insere a nota atual como um novo registro na tabela 'notas'."""
        with sqlite3.connect(DB_NAME) as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO notas (titulo, anotacao) VALUES (?, ?)",
                (self.titulo, self.anotacao)
            )
            conexao.commit()

    @classmethod
    def amostrar_notas(cls) -> list:
        """Busca todos os títulos cadastrados no banco de dados."""
        with sqlite3.connect(DB_NAME) as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT titulo FROM notas ORDER BY id ASC")
            registros = cursor.fetchall()

        if not registros:
            print("Nenhuma nota encontrada.")
            return []

        print("\n --SUAS NOTAS-- \n")
        titulos = []
        for indice, (titulo,) in enumerate(registros, start=1):
            print(f"{indice} - {titulo}")
            titulos.append(titulo)

        return titulos

    @classmethod
    def ler_notas(cls, titulo: str) -> str:
        """Retorna o conteúdo textual da anotação referente ao título fornecido."""
        with sqlite3.connect(DB_NAME) as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT anotacao FROM notas WHERE titulo = ?", (titulo,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            return "Nota não encontrada."