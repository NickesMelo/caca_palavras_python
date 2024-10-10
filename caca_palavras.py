#Caça-Palavras#
conjunto_letras = [
    ["b", "e", "f", "g", "a", "b", "a", "c", "a", "x", "i", "n", "o", "m"],
    ["r", "r", "o", "d", "e", "l", "e", "f", "a", "n", "t", "e", "p", "u"],
    ["a", "ç", "a", "a", "p", "e", "s", "b", "e", "f", "a", "d", "d", "y"],
    ["s", "y", "m", "m", "r", "j", "o", "c", "o", "l", "a", "t", "e", "s"],
    ["i", "q", "h", "d", "m", "o", "n", "t", "a", "n", "h", "a", "s", "a"],
    ["l", "v", "z", "g", "t", "s", "e", "t", "r", "e", "l", "a", "e", "r"],
    ["u", "t", "b", "k", "c", "a", "f", "e", "e", "l", "a", "p", "i", "n"],
    ["l", "m", "h", "x", "b", "o", "r", "b", "o", "l", "e", "t", "a", "l"],
    ["o", "a", "f", "c", "e", "m", "r", "o", "g", "i", "t", "u", "j", "d"],
    ["l", "s", "i", "j", "v", "a", "a", "j", "a", "r", "d", "i", "m", "t"],
    ["z", "x", "y", "s", "e", "s", "o", "c", "e", "a", "n", "u", "g", "s"],
    ["p", "g", "b", "h", "o", "b", "g", "a", "l", "a", "x", "i", "a", "o"],
    ["e", "d", "c", "y", "r", "r", "l", "c", "a", "f", "e", "b", "m", "a"],
    ["m", "t", "c", "x", "i", "r", "v", "i", "a", "g", "e", "m", "i", "s"],
    ["l", "v", "b", "w", "u", "t", "e", "o", "j", "e", "m", "y", "f", "r"],
]

conjunto_palavras = [
    "abacaxi", "carro", "elefante", "montanha", "estrela",
    "caderno", "borboleta", "piano", "chocolate", "oceano",
    "galáxia", "relógio", "sorriso", "arco-iris", "café",
    "caneta", "jardim", "viagem", "sol", "livro", "brasil"
]

letras_encontradas = []


while True:
    palpite = input("\nDigite uma palavra: ").lower()
    if palpite.isalpha():
        break
    else:
        print("Valor de entrada inválido. Apenas letras são permitidas!\n")

# Busca as letras do palpite no conjunto de letras
for letra in palpite:
    for linha in conjunto_letras:
        if letra in linha:
            letras_encontradas.append(letra)
            break
        
# Verifica a palavra encontrada
palavra_encontrada = ''.join(letras_encontradas)
# print(palavra_encontrada.title())

if palavra_encontrada in conjunto_palavras:
    print(f"\n** Parabéns! Você encontrou a palavra: {palavra_encontrada.title()} **\n")
else:
    print("\nOps...! Palavra não encontrada.\n")