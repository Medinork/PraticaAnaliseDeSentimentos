from collections import Counter

def classificar_perfil(texto):
    categorias = {
        "tecnológico": ["computador", "programa", "software", "código"],
        "esportivo": ["futebol", "basquete", "corrida", "atleta"],
        "político": ["eleição", "governo", "deputado", "presidente"],
        "divertido": ["filme", "série", "piada", "meme"]
    }
    palavras = texto.lower().split()
    contagem = Counter(palavras)
    perfil = {cat: sum(contagem[p] for p in palavras_chave if p in contagem)
              for cat, palavras_chave in categorias.items()}
    return max(perfil, key=perfil.get)

texto_exemplo = "Eu gosto de assistir filmes e memes na internet!"
print("Perfil detectado:", classificar_perfil(texto_exemplo))