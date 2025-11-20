import caminho_arquivos
import json

class AbrirArquivos:
    @staticmethod
    def arquivo_r():
        try:
            with open(caminho_arquivos.save_to, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return False
        
    @staticmethod
    def arquivo_w(produtos):
        with open(caminho_arquivos.save_to, "w", encoding="utf-8") as file:
            json.dump(produtos, file, indent=2, ensure_ascii=False)