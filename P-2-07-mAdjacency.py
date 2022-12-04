import numpy as np
img=np.asarray([[0,1,1],
                [0,1,0],
                [0,0,1]])
v=np.asarray([1])
p_c=p_r=1 # rows represent vertical axis
q_c=p_c+1 # columns represent horizontal axis
q_r=p_r-1
def is_in_n4(p_c,p_r,q_c,q_r):
    if q_c==p_c-1 and q_r==p_r:     return 1
    elif q_c==p_c+1 and q_r==p_r:   return 1
    elif q_c==p_c and q_r==p_r-1:   return 1
    elif q_c==p_c and q_r==p_r+1:   return 1
    else:                           return -1
def is_in_nd(p_c,p_r,q_c,q_r):
    if q_c==p_c-1 and q_r==p_r-1:   return 1
    elif q_c==p_c+1 and q_r==p_r+1: return 1
    elif q_c==p_c+1 and q_r==p_r-1: return 1
    elif q_c==p_c-1 and q_r==p_r+1: return 1
    else:                           return -1
def get_n4(p_c,p_r):
    nlist=[]
    nlist.append([p_r,p_c-1])
    nlist.append([p_r,p_c+1])
    nlist.append([p_r-1,p_c])
    nlist.append([p_r+1,p_c])
    return nlist
def get_intersection(n4p,n4q):
    intersection=[]
    for i in range(len(n4p)):
        if n4p[i] in n4q:
            intersection.append(n4p[i])
    return intersection

if (is_in_n4(p_c,p_r,q_c,q_r)==1): print("m-adjacency")
if (is_in_nd(p_c,p_r,q_c,q_r)==1):
    n4p=get_n4(p_c,p_r)
    n4q=get_n4(q_c,q_r)
    intersection=get_intersection(n4p,n4q)
    for i in range(len(intersection)):
        for j in range(len(v)):
            r,c=intersection[i]
            val=v[j]
            pixval=img[r,c]
            if val==pixval:
                print("no m-adjacency")
                break