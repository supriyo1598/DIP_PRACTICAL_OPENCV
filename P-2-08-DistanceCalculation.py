import numpy as np
row1=100
col1=100
row2=150
col2=150
def Eucladian_Distance(p_x,p_y,q_x,q_y):
    Eu_dist=np.sqrt(np.square(p_x-q_x)+np.square(p_y-q_y))
    return Eu_dist

def CityBlock_Distance(p_x,p_y,q_x,q_y):
    City_dist=np.abs(p_x-q_x)+np.abs(p_y-q_y)
    return City_dist

def Chessboard_Distance(p_x,p_y,q_x,q_y):
    a=np.abs(p_x-q_x)
    b=np.abs(p_y-q_y)
    if a==b: return a
    else:
        Chess_dist=np.max(a,b)
    return Chess_dist

print("Eucladian Distance:",Eucladian_Distance(row1,col1,row2,col2))
print("City Block Distance:",CityBlock_Distance(row1,col1,row2,col2))
print("Chessboard Distance:",Chessboard_Distance(row1,col1,row2,col2))
