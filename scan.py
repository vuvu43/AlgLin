import numpy as np
import random


class CTscan:
    def __init__(self, slice): #recebe uma matriz mxn que é a informação real do corpo escaneado
        self.slice = []
        for i in slice:
            self.slice.extend(i) # "planificando" a matriz slice para facilitar a implementação

        self.slice = np.array(self.slice)  #matriz que é um slice 2d do corpo real
        self.qnt_var = len(slice[0])*len(slice)  #colunas x linhas


    def acha_subs(self, qnt_eq=1000): #simula equações dos raios que passam pelo corpo
        '''
        Parâmetros:
        - qnt_eq:int   define a quantidade de equações, quanto mais equações, mais preciso

        Retorna:
        - solução de onde estão as substâncias por mínimos quadrados
        '''
        M = np.zeros((qnt_eq, self.qnt_var))
        resultado = np.zeros(qnt_eq)

        for lin in range(qnt_eq):
            M[lin] = np.array([random.randint(0, 1) for i in range(self.qnt_var)]) #cria as equações de forma aleatória

        for i in range(qnt_eq):
            for j in range(self.qnt_var):
                if M[i, j] == 1:
                    resultado[i] += self.slice[j] 


        return self._trata_resposta(np.linalg.solve(M.T@M, M.T@resultado))  #resolver com mínimos quadrados


    @staticmethod 
    def _trata_resposta(resp):
        for i in range(len(resp)):
            if resp[i] < 0.00001: resp[i] = 0
        
        return resp



corpo_slice = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1]
])

maq = CTscan(corpo_slice)
print(np.linalg.norm(maq.slice - maq.acha_subs()) < 0.0000001)