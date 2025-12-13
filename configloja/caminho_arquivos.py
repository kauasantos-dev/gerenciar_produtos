import os

base_dir = os.path.join(os.path.dirname(__file__), '..', 'produtos')
os.makedirs(base_dir, exist_ok=True)
save_to = os.path.join(base_dir, 'lista_produtos.json')