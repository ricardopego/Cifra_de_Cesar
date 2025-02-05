"""
Implementação da Cifra de César em Python.

Este código realiza a cifragem de um texto, deslocando cada letra em um
certo número de passos no alfabeto, definido por uma chave.
Letras maiúsculas e minúsculas são tratadas separadamente,
enquanto caracteres especiais, espaços e pontuação permanecem inalterados.

Exemplos:
"abc" com chave 1 -> "bcd"
"ABCDE" com chave 2 -> "CDEFG"
"Cachorro" com chave -1 -> "Bzbgnqqn"
"Olá Mundo!" com chave 3 -> "Roá Pxqgr!"
"""

def cifrar_caracteres(caractere, seq, chave):
    """
    Função que cifra um único caractere com base em uma sequência de caracteres e uma chave de deslocamento.
    :param caractere: O caractere a ser cifrado.
    :param seq: A sequência de referência (letras minúsculas ou maiúsculas).
    :param chave: O número de posições a deslocar.
    :return: O caractere cifrado.
    """
    indice_atual = seq.index(caractere)  # Obtém o índice do caractere na sequência
    novo_indice = indice_atual + chave  # Aplica o deslocamento da chave
    
    # Ajusta o índice caso ultrapasse o tamanho da sequência (circular)
    while novo_indice >= len(seq):
        novo_indice -= len(seq)
    
    while novo_indice < 0:
        novo_indice += len(seq)
    
    return seq[novo_indice]  # Retorna o caractere cifrado

# Definição dos alfabetos em minúsculas e maiúsculas
minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = minusculas.upper()

# Entrada do usuário
texto = str(input('Digite uma palavra: '))  # Solicita um texto para cifrar
chave = 3  # Define o número de deslocamentos (chave da cifra)
cifra = ''  # String que armazenará o texto cifrado

# Percorre cada caractere do texto
for caractere in texto:
    if caractere in minusculas:
        caractere_cifra = cifrar_caracteres(caractere, minusculas, chave)  # Cifra minúsculas

    elif caractere in maiusculas:
        caractere_cifra = cifrar_caracteres(caractere, maiusculas, chave)  # Cifra maiúsculas
        
    else:
        caractere_cifra = caractere  # Mantém caracteres especiais e espaços inalterados
    
    cifra += caractere_cifra  # Adiciona o caractere cifrado ao resultado final

# Exibe o resultado
print(f'A palavra "{texto}" cifrada é -- "{cifra}"')