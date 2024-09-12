import numpy as np
import matplotlib.pyplot as plt

def turn(angle):
    c=np.cos(angle)
    s=np.sin(angle)
    Q=[[c,s],[-s,c]]
    return Q

# задачи 1-4

points_B=[[1,1],[1,3],[2,2],[1,2],[2,1],[1,1]]
points_B=np.array(points_B)

points_C=[[4,1],[3,1],[3,3],[4,3]]
points_C=np.array(points_C)

plt.plot(points_B[:,0], points_B[:,1]) 
plt.plot(points_C[:,0], points_C[:,1]) 

plt.show()

# задача 5

m1=[[1,0],[0,-1]]
m1=np.array(m1)

B_oX=np.matmul(points_B,m1)
C_oX=np.matmul(points_C,m1)
plt.plot(B_oX[:,0], B_oX[:,1]) 
plt.plot(C_oX[:,0], C_oX[:,1]) 
plt.show()

# задача 6

NewB=np.matmul(points_B,turn(2*np.pi/3))    #
NewC=np.matmul(points_C,turn(2*np.pi/3))    # 120 градусов
plt.plot(NewB[:,0],NewB[:,1])
plt.plot(NewC[:,0],NewC[:,1])
NewB=np.matmul(points_B,turn(4*np.pi/3))    #
NewC=np.matmul(points_C,turn(4*np.pi/3))    # 240 градусов
plt.plot(NewB[:,0],NewB[:,1])
plt.plot(NewC[:,0],NewC[:,1])
plt.show()


x5Matrix=[[5,0],[0,5]]                      
x5Matrix=np.array(x5Matrix)
NewB=np.matmul(points_B,x5Matrix)           #
NewC=np.matmul(points_C,x5Matrix)           # увеличиваем в 5 раз по осям x и y
plt.plot(NewB[:,0],NewB[:,1])
plt.plot(NewC[:,0],NewC[:,1])
plt.show()

for k in range(5):
    NewB=np.matmul(NewB,turn(np.pi/3))      #
    NewC=np.matmul(NewC,turn(np.pi/3))      #
    plt.plot(NewB[:,0],NewB[:,1])           #
    plt.plot(NewC[:,0],NewC[:,1])           # уножаем 5 раз матрицу на pi/6 
plt.show()

# задача 7

Matrix=[[-1,1],[4,0]]
Matrix=np.array(Matrix)                     

NewB=np.matmul(points_B,Matrix)
NewC=np.matmul(points_C,Matrix)
plt.plot(NewB[:,0],NewB[:,1])
plt.plot(NewC[:,0],NewC[:,1])
plt.show()

reverseMatrix=np.linalg.inv(Matrix)         # находим обратную

NewB=np.matmul(NewB,reverseMatrix)          #
NewC=np.matmul(NewC,reverseMatrix)          #
plt.plot(NewB[:,0],NewB[:,1])               #
plt.plot(NewC[:,0],NewC[:,1])               # проверка
plt.show()










