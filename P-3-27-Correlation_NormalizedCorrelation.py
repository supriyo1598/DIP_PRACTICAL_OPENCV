import numpy as np

f = [0,3,2,4,1,3,8,4,0,3,8,0,7,7,7,1,2,0]
w = [3,7,5]
w_len = len(w)
f_len = len(f)
corelation = []
normalized_corelation = []
distance = []
first_part = 0
for i in range(w_len):
    first_part = first_part + (w[i])**2

m = int(np.floor(w_len/2))
for i in range(m, f_len-m):
    second_part = 0
    third_part = 0
    for x in range(-m, m+1):
        second_part = second_part + (f[i+x])**2
        third_part = third_part + (f[i+x] * w[m + x])
    corelation.append(third_part)
    dist = first_part + second_part - (2 * third_part)
    dist = int(np.round(np.sqrt(dist)))
    distance.append(dist)
    norm_cor = (third_part/np.sqrt(first_part*second_part))
    norm_cor = np.round(norm_cor,2)
    normalized_corelation.append(norm_cor)

print("Corelation array: ", corelation)
print("Normalized Corelation array: ", normalized_corelation)
print("Distance array: ", distance)