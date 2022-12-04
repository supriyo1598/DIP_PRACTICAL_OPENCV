#gamma transformation behavior
import numpy as np
import matplotlib.pyplot as plt
x=[a for a in range(0,256)]
y=[a for a in range(0,256)]
x=np.asarray(x).astype(np.float)
y=np.asarray(y).astype(np.float)
y006=np.power(y,0.06)*184
y012=np.power(y,0.12)*132
y025=np.power(y,0.25)*64
y050=np.power(y,0.50)*16
y=x
y2=np.power(y,2)*0.0039
y4=np.power(y,4)*0.00000006
y8=np.power(y,8)*0.0000000000000000143
y16=np.power(y,16)*0.0000000000000000000000000000000000008
#
plt.text(10,237,"γ=0.06",color="darkblue"),plt.plot(x,y006)
plt.text(10,205,"γ=0.12",color="orange"),plt.plot(x,y012)
plt.text(10,160,"γ=0.25",color="green"),plt.plot(x,y025)
plt.text(10,100,"γ=0.50",color="red"),plt.plot(x,y050)
plt.text(10,40,"γ=1.00",color="darkslateblue"),plt.plot(x,y)
plt.text(200,10,"γ=2.00",color="darkgoldenrod"),plt.plot(x,y2)
plt.text(200,50,"γ=4.00",color="darkslategray"),plt.plot(x,y4)
plt.text(200,100,"γ=8.00",color="magenta"),plt.plot(x,y8)
plt.text(200,170,"γ=16.00",color="saddlebrown"),plt.plot(x,y16)
plt.show()
