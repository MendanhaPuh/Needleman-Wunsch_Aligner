import time

def needleman_wunsch(seq1, seq2, match, mismatch, gap):
    start_time = time.time()

    m, n = len(seq1), len(seq2)
    score = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Inicialização da matriz de pontuação
    for i in range(m + 1):             #O(m)
        score[i][0] = gap * i
    for j in range(n + 1):             #O(n)
        score[0][j] = gap * j

    # Preenchimento da matriz de pontuação
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_score = score[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            delete_score = score[i - 1][j] + gap
            insert_score = score[i][j - 1] + gap
            score[i][j] = max(match_score, delete_score, insert_score)

    # Exibir a matriz de pontuação preenchida
    print("\nMatriz de Pontuação:")
    for row in score:
        print(row)

    # Rastreamento do caminho ótimo
    i, j = m, n
    alinhamento1, alinhamento2 = "", ""
    while i > 0 or j > 0:
        if i > 0 and j > 0 and score[i][j] == score[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            alinhamento1 = seq1[i - 1] + alinhamento1
            alinhamento2 = seq2[j - 1] + alinhamento2
            i -= 1
            j -= 1
        elif i > 0 and score[i][j] == score[i - 1][j] + gap:
            alinhamento1 = seq1[i - 1] + alinhamento1
            alinhamento2 = "-" + alinhamento2
            i -= 1
        else:
            alinhamento1 = "-" + alinhamento1
            alinhamento2 = seq2[j - 1] + alinhamento2
            j -= 1

    # Calcula a pontuação do alinhamento
    pontuacao = score[m][n]

    end_time = time.time()
    exec_time = end_time - start_time

    return alinhamento1, alinhamento2, pontuacao, exec_time

# Exemplo de uso
seq1 = input("Digite a 1ª sequência: ")
seq2 = input("Digite a 2ª sequência: ")
match = 1
mismatch = -1
gap = -2

alinhamento1, alinhamento2, pontuacao, exec_time = needleman_wunsch(seq1, seq2, match, mismatch, gap)
print("\nAlinhamento 1:", alinhamento1)
print("Alinhamento 2:", alinhamento2)
print("Pontuação:", pontuacao)
print(f"Tempo de execução: {exec_time:.6f} segundos")
