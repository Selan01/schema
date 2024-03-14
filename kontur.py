import numpy as np
# Состовляем матрицу ЭДС
def eds():
    print('Зададим столбец источников напряжения')
    U=[]
    for i in range(1,int(brs)+1):
        equa=input(f'Значение источника напряжения на ветви {i}: ')
        U.append(int(equa))
    U=np.array(U)
    print(U)
    return U

# Зададим матрицу источников тока
def tok():
    print('Зададим столбец источников тока')
    ists={}
    for i in range(1,int(brs)+1):
        equa=input(f'Значение источника тока на ветви {i}:')
        ists[i]=int(equa)
    Iис=list(ists.values())
    Iис=np.array(Iис)
    print(Iис)
    return Iис

#Состовляем матрицу контуров
def kontur():
    print('Составим матрицу контуров')
    K=[]
    for t in range(0,konts):
        first=input('Введите направление токов:')
        test=first.split()
        for f in range(len(test)):
            test[f]=int(test[f])
        K.append(test)
    K=np.array(K)
    print(K)
    return K

# Состовляем квадратную матрицу сопративлений
def resists():
    print('Зададим матрицу сопративлений')
    R=[]
    for i in range(0,int(brs)):
        resist=[]
        for j in range(0,int(brs)-1):
            resist.append(0)
        equa=input(f'Задайте значение сопративления для ветви {i+1}: ')
        resist.insert(i,float(equa))
        R.append(resist)
    R=np.array(R)
    print(R)
    return R
# Находим токи
# Найдем ток Ik
def equa(K,R,U,Iис):
    I=K.dot(R)
    Ktr=np.transpose(K)
    I=I.dot(Ktr)
    I=np.linalg.matrix_power(I,-1)
    I2=K.dot(U)
    I21=K.dot(R)
    I21=I21.dot(Iис)
    I2=I2+I21
    Ik=I.dot(I2)
    print('\nIk',Ik)
    # Найдем токи
    I=Ktr.dot(Ik)
    print('I',I)

if __name__=='__main__':
    # Задаем кол-во контуров
    konts=int(input('Задайте кол-во контуров: '))
    # Задаем кол-во ветвей
    brs=input('Введите кол-во ветвей: ')
    R=resists()
    Iис=tok()
    U=eds()
    K=kontur()
    equa(K,R,U,Iис)
    input()
