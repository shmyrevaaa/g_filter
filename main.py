import numpy as np
import cv2 as cv
from interface03 import Ui_Dialog
#h=float(input('введите размер маски = '))
object  = Ui_Dialog()
I= object.graphicsView.viewport().size()
#I= cv.imread('C:/imgs/photo2023.jpg')
#cv.imshow('image',I)
#cv.waitKey()
X = I[:, :, 1]
Z = I[:, :, 0]
C = I[:, :, 2]
X =X.astype(float)
Z= Z.astype(float)
C = C.astype(float)

#X = cv.cvtColor(X, cv.COLOR_BGR2GRAY)
#X=np.ones((10, 11))  # исходное изображение
#X = np.array([[1, 1, 1, 1, 1],
              # [1, 1, 1, 1, 1],
              # [1, 1, 1, 1, 1],
              # [1, 1, 1, 1, 1]])
#A1 = input('введите коэффициент для подъема = ')  # коэффициент для подъема центральной апертуры
#A2 = input('введите увеличения центрального элемента = ')  # коэффициент для увеличения центрального элемента матрицы на заданное значение
h =7
#h = object.spinBox.value()
A1 =1
#A1= object.spinBox_2.value()
#print(A1)
A2=0
#A2= object.spinBox_3.value()
# ---------------------------------------------------------------------------—
# —— РЕЦИРКУЛЯТОРЫ ——
v=h+1
v=v/2
if v % 2 == 0: #выявление четности
    d1=v-1 #значение рециркулятора  d1, при четном значении
else:
    d1=v #значение рециркулятора  d1, при нечетном значении
d2=(h-d1)/2+1 # Значение рециркуляторов d2
# —-------— ОСНОВНАЯ МАТРИЦА —--------—
d11=int(d1)
Y1 = np.ones((1, d11))
#i1 = X.size[1]
i1=np.size(X, 1) #кол-во столбцов в X матрице
j1 = np.size(X, 0) # кол-во строк в X матрице
i2 = np.size(Y1, 1)
j2 = np.size(Y1, 0)
nuliki1=np.zeros((j1,i2-1))
X1=np.hstack(( X, nuliki1))
k = j1
m = i1 + (i2 - 1)
y1 = np.zeros((k, m))
for k in range(0, j1):
    for m in range(0, i1 + (i2 - 1)):
        if m == 0:
            y1[k,m] = X1[k,m]
        if m > 0 and m < i2 + 1:
            y1[k,m] = X1[k,m] + y1[k,m-1]
        if m - i2 >= 0:
            y1[k,m] = X1[k,m] - X1[k,m-i2] + y1[k,m-1]
d22=int(d2)
Y2 = np.ones((1, d22))
i1 = np.size(y1, 1)
j1 = np.size(y1, 0)
i2 = np.size(Y1, 1)
j2 = np.size(Y2, 0)
nuliki2 = np.zeros((j1, i2 - 1))
X2 = np.hstack((y1, nuliki2))
k = j1
m = i1 + (i2 - 1)
y2 = np.zeros((k, m))
for k in range(0, j1):
    for m in range(0, i1 + (i2 - 1)):
        if m == 0:
            y2[k,m] = X2[k,m]
        if m > 0 and m < i2 + 1:
            y2[k,m] = X2[k,m] + y2[k,m-1]
        if m - i2 >= 0:
            y2[k,m] = X2[k,m] - X2[k,m-i2] + y2[k,m-1]
Y3 = np.ones((1, d22))
i1 = np.size(y2, 1)
j1 = np.size(y2, 0)
i2 = np.size(Y3, 1)
j2 = np.size(Y3, 0)
nuliki3 = np.zeros((j1, i2 - 1))
X3 = np.hstack((y2, nuliki3))
k = j1
m = i1 + (i2 - 1)
y3 = np.zeros((k, m))
for k in range(0, j1):
    for m in range(0, i1 + (i2 - 1)):
        if m == 0:
            y3[k,m] = X3[k,m]
        if m > 0 and m < i2 + 1:
            y3[k,m] = X3[k,m] + y3[k,m-1]
        if m - i2 >= 0:
            y3[k,m] = X3[k,m] - X3[k,m-i2] + y3[k,m-1]
Y4 = np.ones((d11, 1))
i1 = np.size(y3, 1)
j1 = np.size(y3, 0)
i2 = np.size(Y4, 1)
j2 = np.size(Y4, 0)
X4 = np.zeros((j1 + (j2 - 1), i1))
X4[0:j1,:] = y3
k = j1 + (j2 - 1)
m = i1
y4 = np.zeros((k, m))
for k in range(0, j1 + (j2 - 1)):
    for m in range(0, i1):
        if k == 0:
            y4[k,m] = X4[k,m]
        if k > 0 and k < j2 + 1:
            y4[k,m] = X4[k,m] + y4[k-1,m]
        if k - j2 >= 0:
            y4[k,m] = X4[k,m] - X4[k-j2,m] + y4[k-1,m]
Y5 = np.ones((d22, 1))
i1 = np.size(y4, 1)
j1 = np.size(y4, 0)
i2 = np.size(Y5, 1)
j2 = np.size(Y5, 0)
X5 = np.zeros((j1 + (j2 - 1), i1))
X5[0:j1,:] = y4;
k = j1 + (j2 - 1)
m = i1
y5 = np.zeros((k, m))
for k in range(0, j1 + (j2 - 1)):
    for m in range(0, i1):
        if k == 0:
            y5[k,m] = X5[k,m]
        if k > 0 and k < j2 + 1:
            y5[k,m] = X5[k,m] + y5[k-1,m]
        if k - j2 >= 0:
            y5[k,m] = X5[k,m] - X5[k-j2,m] + y5[k-1,m]
Y6 = np.ones((d22, 1))
i1 = np.size(y5, 1)
j1 = np.size(y5, 0)
i2 = np.size(Y6, 1)
j2 = np.size(Y6, 0)
X6 = np.zeros((j1 + (j2 - 1), i1))
X6[0:j1,:] = y5
k = j1 + (j2 - 1)
m = i1
y6 = np.zeros((k, m))
for k in range(0, j1 + (j2 - 1)):
    for m in range(0, i1):
        if k == 0:
            y6[k,m] = X6[k,m]
        if k > 0 and k < j2 + 1:
            y6[k,m] = X6[k,m] + y6[k-1,m]
        if k - j2 >= 0:
            y6[k,m] = X6[k,m] - X6[k-j2,m] + y6[k-1,m]
#--------------Расчет размеров рециркуляторов для дполнительной матрицы---------------
m1=((h-1)-d1+1)/2
m11=int (m1)
#--------------Расчет суммы коэффициентов матриц---------------
S0=(d11*d22*d22)*(d11*d22*d22) #сумма каждого элемента первой матрицы при свертке единицы
P=(m11*m11)*(m11*m11) #сумма элементов при свертке доп матрицей единицы
D=S0/P  #коэффициент для свертки
D=D-(D-np.fix(D))  #итоговый коэффициент свертки
W=S0-(16*D)
# ----------------------— КОЭФФ ?Ц ?ЕНТ СДВ ?ГА —--------------------—
k = h + 1  # приведение к четности
if k % 4 == 0:  # если делится без остатка на 4
    q = k / 4  # то поделить на 4, это будет отве
else:
    q = (k + 2) / 4  # если не делится на 4, то привести к возможности деления и поделить
q1 = q + 1
Y7 = np.ones((1, m11))  # Строчный рециркулятор при М=2
D1=int(D)
X7 = X * (D1+A1)  # изображение, умноженное на коэффициент
i1 = np.size(X, 1)#X.size[1]  # количесвто стобцов в Х0 матрице
j1 = np.size(X, 0)#X.size[0]  # количество строк в X0 матрице
i2 = np.size(Y7, 1)#Y7.size[1]  # колчиество
# столбцов во Y0 матрице
j2 = np.size(Y7, 0)#Y7.size[0]  # количество строк во Y0 матрице
nuliki4 = np.zeros((j1, i2 - 1))
X7 = np.hstack((X7, nuliki4))  # Матрица Х0 дополненая нулями с
# правой стороны
k = j1
m = i1 + (i2 - 1)
y7 = np.zeros((k, m))
for k in range(0, j1):  # выбор строки обработки
    for m in range(0, i1 + (i2 - 1)):  # выбор стлобца обработки
        # условие когда выходное изображение еще не сформированно
        if m == 0:
            y7[k,m] = X7[k,m]
    # задержка равна 0 имеется только входное и выходное значение
        if m > 0 and m < i2 + 1:
            y7[k,m] = X7[k,m] + y7[k,m-1]
    # Общее уравнение рециркулятора по строке
        if m - i2 >= 0:
            y7[k,m] = X7[k,m] - X7[k,m-i2] + y7[k,m-1]
Y8 = np.ones((1, m11))  # Строчный рециркулятор при М=2
i1 = np.size(y7, 1)   # количесвто стобцов в Х0 матрице
j1 = np.size(y7, 0)   # количество строк в X0 матрице
i2 = np.size(Y8, 1)   # колчиество столбцов во Y0 матрице
j2 = np.size(Y8, 0)   # количество строк во Y0 матрице
nuliki5 = np.zeros((j1, i2 - 1))
X8 = np.hstack((y7, nuliki5))  # Матрица Х0 дополненая нулями с правой стороны
k = j1
m = i1 + (i2 - 1)
y8 = np.zeros((k, m))
for k in range(0, j1):  # выбор строки обработки
    for m in range(0, i1 + (i2 - 1)):  # выбор стлобца обработки
        # условие когда выходное изображение еще не сформированно
        if m == 0:
            y8[k,m] = X8[k,m]
        # задержка равна 0 имеется только входное и выходное значение
        if m > 0 and m < i2 + 1:
            y8[k,m] = X8[k,m] + y8[k,m-1]
        # Общее уравнение рециркулятора по строке
        if m - i2 >= 0:
            y8[k,m] = X8[k,m] - X8[k,m-i2] + y8[k,m-1]
Y9 = np.ones((m11, 1))  # Кадровый рециркулятор при М=2
i1 = np.size(y8, 1)  # количесвто стобцов в у0 матрице
j1 = np.size(y8, 0)  # количество строк в у0 матрице
i2 = np.size(Y9, 1)  # колчиество столбцов во Y1 матрице
j2 = np.size(Y9, 0)  # количество строк во Y1 матрице
X9 = np.zeros((j1 + (j2 - 1), i1))  # матрица нулевая
X9[0:j1,:] = y8  # матрица у0 окруженная нулями
k = j1 + (j2 - 1)
m = i1
y9 = np.zeros((k, m))
for k in range(0, j1 + (j2 - 1)):  # выбор строки обработки
    for m in range(0, i1):  # выбор стлобца обработки
        # условие когда выходное изображение еще не сформированно
        if k == 0:
            y9[k,m] = X9[k,m]
        # задержка равна 0 имеется только входное и выходное значение
        if k > 0 and k < j2 + 1:
            y9[k,m] = X9[k,m] + y9[k-1,m]
        # Общее уравнение кадрового рециркулятора
        if k - j2 >= 0:
            y9[k,m] = X9[k,m] - X9[k-j2,m] + y9[k-1,m]
Y10 = np.ones((m11, 1))  # Кадровый рециркулятор при М=2
i1 = np.size(y9, 1)  # количесвто стобцов в у0 матрице
j1 = np.size(y9, 0)  # количество строк в у0 матрице
i2 = np.size(Y10, 1)  # колчиество столбцов во Y1 матрице
j2 = np.size(Y10, 0)  # количество строк во Y1 матрице
X10 = np.zeros((j1 + (j2 - 1), i1))  # матрица нулевая
X10[0:j1,:] = y9  # матрица у0 окруженная нулями
k = j1 + (j2 - 1)
m = i1
y10 = np.zeros((k, m))
for k in range(0, j1 + (j2 - 1)):  # выбор строки обработки
    for m in range(0, i1):  # выбор стлобца обработки
        # условие когда выходное изображение еще не сформированно
        if k == 0:
            y10[k,m] = X10[k,m]
        # задержка равна 0 имеется только входное и выходное значение
        if k > 0 and k < j2 + 1:
            y10[k,m] = X10[k,m] + y10[k-1,m]
        # Общее уравнение кадрового рециркулятора
        if k - j2 >= 0:
            y10[k,m] = X10[k,m] - X10[k-j2,m] + y10[k-1,m]
i2=np.size(y6,1) #кол-во столбцов в основной матрице
j2=np.size(y6,0) #кол-во строк основной матрице
i1 = np.size(y10, 1) #y10.size[1]  # кол-во столбцов в у8
j1 = np.size(y10, 0) #y10.size[0]
Z1=np.zeros((j2,i2))  #нулевая матрица размером с внешнюю, основа
q11= int(q1-1)
n1=int(q1+j1-1)
n2=int(q1+i1-1)
Z1[q11:n1,q11:n2] = y10 #итоговая вторая матрица
S2=P*D  #запоминаем сумму без значения А1 для подсчета коэф третьей маски
A3=int(S0-S2) #недостающее значение в маске (основная минус доп)
W=X*(A2+A3) #исходное изображение, домноженное на коэффициент А2 и недостающее знач-е
i1=np.size(W, 1) #количество столбцов во второй матрице
j1=np.size(W, 0) #количество строк во второй матрице
q2=d1+1
W0=np.zeros((j2,i2)) #нулевая матрица размера с основную
q22=int(q2-1)
g2=int(q2+j1-1)
g3=int(q2+i1-1)
W0[q22:g2,q22:g3] = W #матрица W, окруженная нулями
S=A1*P #сумма коэффициентов при подъеме внутренней маски
rez=(W0+(Z1-y6))/(A2+S) #результат с нормированием яркости изображения при использовании коэффициента А1 и А2
print(rez)
isWritten = cv.imwrite('C:/imgs/photo2023_2.jpg', rez)
cv.imshow('image', rez)
cv.waitKey()

