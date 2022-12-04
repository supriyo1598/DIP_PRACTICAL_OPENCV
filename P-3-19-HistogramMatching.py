import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

r_k=np.array([0,1,2,3,4,5,6,7])
n_k=np.array([790,1023,850,656,329,245,122,81])
pr_k=n_k/4096
s_k=np.zeros(len(n_k))          # for s_k=T(r_k)
n_s_k=np.zeros(len(n_k))        # pixel mapping n_k --> n_s_k
def histEqualization():
    s_k=np.zeros([len(n_k)])
    for i in range(len(n_k)):
        for j in range(0,i+1):
            s_k[i]+=pr_k[j]
    s_k=7*s_k
    s_k=np.round(s_k)
    for i in range(len(n_k)):
         n_s_k[i]+=np.sum(n_k[s_k==i])
    return n_s_k.astype(np.uint8),s_k.astype(np.uint8)

n_s_k,s_k=histEqualization()
pz_k=np.array([0.00,0.00,0.00,0.15,0.20,0.30,0.20,0.15])
Gz_q=np.zeros([len(pz_k)])
for i in range(len(pz_k)):
    for j in range(0,i+1):
        Gz_q[i]+=pz_k[j]
Gz_q=7*Gz_q
Gz_q=np.round(Gz_q).astype(np.uint8)
nz_k=np.zeros(len(n_k))
s_k_missing=[]
Gz_k_missing=[]
for i in range(len(n_k)):
     ind_gz=Gz_q[i]
     ind_sk=s_k[i]
     if s_k.__contains__(ind_gz):
         val_nk=n_k[s_k==ind_gz]
         nz_k[i]=sum(val_nk)
     if not(s_k.__contains__(ind_gz)) and not(Gz_k_missing.__contains__(ind_gz)):
          Gz_k_missing.append(ind_gz)
     if not(Gz_q.__contains__(ind_sk))and not(s_k_missing.__contains__(ind_sk)):
         s_k.__contains__(ind_gz): (ind_sk) # check the algorithm

s_k_missing=np.asarray(s_k_missing).astype(np.uint8)
for i in range(len(s_k_missing)):
    forward=0
    backward=0
    for j in range(np.round(len(Gz_q)/2).astype(np.uint8)):
        forward=s_k_missing[i]+j
        backward=s_k_missing[i]-j
        if(Gz_q[forward]+j==s_k_missing[i]):
            nz_k[forward]+=n_k[np.where(s_k==s_k_missing)]
            break
        elif (Gz_q[backward]-j==s_k_missing[i]):
            nz_k[backward]+=n_k[np.where(s_k==s_k_missing)]
            break
pz_z=nz_k/4096
np.set_printoptions(precision=2)
print("r_k::",r_k)
print("n_k::",n_k)
print("n_k::",pr_k)
print("s_k::",s_k)
print("n_s_k::",n_s_k)
print("pz_k::",pz_k)
print("Gz_q::",Gz_q)
print("nz_k::",nz_k)
print("pz_z::",pz_z)
