import numpy as np


def troca_linha(M, i, j):
    M[[i, j], :] = M[[j, i], :]

    return M


def divide_linha(M, i, k):
    M[i, :] = M[i, :] / k

    return M


def subtrai_linha(M, i, j, k=1):
    M[i, :] = M[i, :] - k * M[j, :]

    return M


def acha_pivo(M, i):
    for j, linha in enumerate(M):
        for coluna, valor in enumerate(linha):
            if valor != 0:
                if coluna == i:
                    return j
                break
    return


def ajeita_matriz(M):
    """
    Função para colocar a Matriz M na forma correta do Gauus-Jordan
    """
    ja_foi = 0

    for col in range(len(M[0]) - 1):
        linha_pivo = acha_pivo(M, col)

        if linha_pivo is None: continue

        if linha_pivo >= ja_foi:
            M = troca_linha(M, linha_pivo, ja_foi)
            ja_foi = linha_pivo + 1

    return M


def gauss_jordan(A, b):
    A = np.column_stack((A, b))

    for coluna in range(len(A[0])):
        linha_pivo = acha_pivo(A, coluna)

        if linha_pivo is None:
            continue

        k = A[linha_pivo][coluna]
        A = divide_linha(A, linha_pivo, k)

        for indice, linha in enumerate(A):
            if indice == linha_pivo: continue

            A = subtrai_linha(A, indice, linha_pivo, A[indice][coluna])

    A = ajeita_matriz(A)

    # Nesse ponto a matriz já está pronta, você pode modificar o código
    # para imprimi-la se quiser

    B = np.delete(A, -1, 1)

    if len(B) != len(B[0]):
        for lin in B:
            if np.sum(lin) == 0:
                return "Sistema sem solução"

        return "Sistema com infinitas soluções"

    return A


if __name__ == "__main__":
    matriz = np.array([[0., 3., -6., 6., 0.],
                       [3., -7., 8., -5., 0.],
                       [3., -9., 12., -9., 0.]])

    vet_result = np.array([-5., 9., 15.])

    print(gauss_jordan(matriz, vet_result))
