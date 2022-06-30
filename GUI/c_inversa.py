from math import *
import numpy as np 
from numpy import deg2rad, rad2deg

def c_inversa(L_1:int, L_2:int, D:int, d:int, h:int, P)->tuple[int, list]:
    """ CINEMATICA INVERSA DE ROBOT DELTA 

    Args:
        L_1 (int): Brazo superior, motor 
        L_2 (int): Brazo inferior, parelogramo 
        D (int): Lado del triangulo BASE FIJA 
        d (int): ancho del paralelogramo 
        h (int): Lado del triangulo BASE MOVIL 
        P (np.array): Vector de punto deseado 
    
    Returns:
        tuple[int, list]: si el int es 0 no existe el punto dentro del espacio de trabajo, y la lista son los valores de angulos de los tres motores en grados. 
        
    
    """
    
    
    P = P[:, np.newaxis] # vector columna 
    r = D*sqrt(3)/3 
    ap =  D*sqrt(3)/6
    
    phi = [30, 150, 270]
    R = []
    C = []
    c_plus =  [[(h/sqrt(3))-ap],[0],[0]]
    
    th3 = []
    th2 = []
    th1 = []
    for idx, i in enumerate(phi): 
        R.append(np.array([[cos(deg2rad(i)),sin(deg2rad(i)),0],
                           [-sin(deg2rad(i)),cos(deg2rad(i)), 0],
                           [0, 0, 1]]))
    
        C.append(np.dot(R[idx],P)+c_plus)
    
        th3.append(rad2deg(acos((C[idx][1,0]/L_2)))) #Valor en radiantes 
        try: 
            th2.append(rad2deg(acos((sum(C[idx]**2)-L_1**2-L_2**2)/(2*L_1*L_2*sin(deg2rad(th3[idx]))))))
        
            th1.append(rad2deg(atan2(C[idx][2],C[idx][0]))\
                    -rad2deg(acos(((L_1**2)+(C[idx][2]**2)\
                    +(C[idx][0]**2)-((L_2*sin(deg2rad(th3[idx])))**2))\
                        /(2*L_1*sqrt((C[idx][2]**2)+(C[idx][0]**2)))\
                            )))
        except Exception as e: 
            # print("error: "+ str(e))
            return (0,[ 0,0,0] )
    return 1, th1


if __name__ == "__main__": 
    print(c_inversa(L_1= 200,L_2= 400, D= 415, d= 100,h = 100,P =np.array([-152,0,400])))
    print(c_inversa(L_1= 200,L_2= 400, D= 415, d= 100,h = 100,P =np.array([-152,0,375])))
    print(c_inversa(L_1= 200,L_2= 400, D= 415, d= 100,h = 100,P =np.array([152,0,375])))
    print(c_inversa(L_1= 200,L_2= 400, D= 415, d= 100,h = 100,P =np.array([152,0,400])))
    
    
    # print(c_inversa(L_1= 200,L_2= 400, D= 120, d= 15,h = 80,P =np.array([0,0,0])))