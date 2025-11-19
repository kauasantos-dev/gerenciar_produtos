import caminho_arquivos
import json

class AbrirArquivos:
    @staticmethod
    def arquivo_r():
        with open(caminho_arquivos.save_to, "r", encoding="utf-8") as file:
            return json.load(file)
        
    @staticmethod
    def arquivo_w(lista):
        with open(caminho_arquivos.save_to, "w", encoding="utf-8") as file:
            json.dump(lista, file, indent=2, ensure_ascii=False)