import numpy as np

class Schema:
    def __init__(self,nds,nds_null,vetvs):
        self.nds=nds
        self.nds_null=nds_null
        self.vetvs=vetvs

    #Формула
    def formula(self,A,Yb,Juc,Uuc):
        AYb=A.dot(Yb)
        print('\nA*Yb\n',AYb,'\n')
        Atr=np.transpose(A)
        AYbAtr=AYb.dot(Atr)
        print('A*Yb*Atr\n',AYbAtr,'\n')
        AYbAtr=np.linalg.matrix_power(AYbAtr,-1)
        print('(A*Yb*Atr)^-1\n',AYbAtr,'\n')
        Uz1=AYbAtr
        AJuc=A.dot(Juc)
        print('A*iис\n',AJuc,'\n')
        aYb=-A.dot(Yb)
        print('A*Yb\n',aYb,'\n')
        AYbUuc=aYb.dot(Uuc)
        print('A*Yb*uис\n',AYbUuc,'\n')
        Uz2=AJuc-AYbUuc
        print('(A*Yb)-(A*Yb*uис)\n',Uz2,'\n')
        Uz=Uz1.dot(Uz2)
        Uz=Uz*(-1)
        print('Напряжения на узлах\n',Uz,'\n')

    # Матрица инцеденций
    def incedent(self):
        print('Составим матрицу инцеденций')
        A=[]
        for i in range(0,int(self.nds)-1):
            print(f'Начальный и конечный узел для узла {i+1}')
            inc_matrix_A_piece=input('Введите начальный и конечный узел, остальным поставьте 0:')
            inc_matrix_A_piece_test=inc_matrix_A_piece.split()
            for j in range(len(inc_matrix_A_piece_test)):
                inc_matrix_A_piece_test[j]=int(inc_matrix_A_piece_test[j])
            A.append(inc_matrix_A_piece_test)
        A=np.array(A)
        print(A)
        return A

    # Матрица независимых источников тока
    def tok_matr(self):
        print('Составим матрицу столбец источников тока')
        istok_dict={}
        for i in range(1,int(self.vetvs)+1):
            istok_equa=input('Введите значение источников тока:')
            istok_dict[i]=int(istok_equa)
        J=list(istok_dict.values())
        J=np.array(J)
        print(J)
        return J

    # Матрица проводимостей
    def resists(self):
        Rdiag=[]
        for i in range(0,int(self.vetvs)):
            resist_list_test=[]
            for j in range(0,int(self.vetvs)-1):
                resist_list_test.append(0)
            resist_equa=input('Введите значение сопративления: ')
            resist_list_test.insert(i,float(resist_equa))
            Rdiag.append(resist_list_test)
        Rdiag=np.array(Rdiag)
        return Rdiag

    def resist_prov(self,Rdiag):
        Yb=[]
        count=0
        for i in Rdiag:
            Yb_test=[]
            for j in i:
                if j != 0:
                    sum=1/j
                    Yb_test.append(sum)
                else:
                    Yb_test.append(0)
            Yb.append(Yb_test)
            count=count+1
        Yb=np.array(Yb)
        print(Yb)
        return Yb
    # Матрица столбцов независимых напряжений
    def eds(self):
        print('Составим столбец источников напряжения')
        E=[]
        for i in range(1,int(self.vetvs)+1):
            eds_equa=input('Введите значение источника напряжения:')
            E.append(int(eds_equa))
        E=np.array(E)
        print(E)
        return E

if __name__=='__main__':
    # Вводим кол-во узлов
    node=input('Введите кол-во узлов: ')
    node_null=input('Выберите опорный: ')
    nd_dict={}
    for uz in range(1,int(node)+1):
        if uz == int(node_null):
            nd_dict[uz]=0
        else:
            nd_dict[uz]=1

    # Вводим кол-во ветвей
    branch=input('Введите кол-во ветвей: ')
    schema = Schema(node,node_null,branch)
    res=schema.resists()
    tok=schema.tok_matr()
    eds=schema.eds()
    incedential=schema.incedent()
    prov=schema.resist_prov(res)
    schema.formula(incedential,prov,tok,eds)
