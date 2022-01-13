import pandas as pd
import matplotlib.pyplot as plt

class interpolation:
    def __init__(self,data,dx):
        self.data = data 
        self.dx = dx 
    
    def lagrange(self):
        data = self.data
        xu = data.loc[0,'x']
        n = data.shape[0]-1
        m = int((data.loc[n,'x'] - data.loc[0,'x'])/self.dx)

        ix = []
        iy = []
        for j in range(m+1):
            p = 0
            for k in range(n):
                l = 1
                for i in range(n):
                    if (i != k):
                        l = l * ((xu - data.loc[i,'x'])/(data.loc[k,'x'] - data.loc[i, 'x']))
                p = p + (data.loc[k,'y'] * l)
            ix.append(xu)                
            xu = xu + self.dx 
            iy.append(p)

        return ix,iy

df = pd.read_csv('/Users/auliakhalqillah/Documents/PYTHON/NUMERIK/data.csv')
inter = interpolation(df,0.1)
x,y = inter.lagrange()
print(x)
print(y)

plt.figure()
plt.plot(df['x'], df['y'],'.')
plt.plot(x,y)
plt.show()
