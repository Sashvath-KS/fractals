import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

atol=pow(10,-10)

def d(f,z):
    h=pow(10,-10)*(1+1j)
    return (f(z+h)-f(z))/h

def newton_raphson(z0,f,n=1000):
    
    z=z0
    
    for i in range(n):
        try:
            dz= f(z)/d(f,z)

        except ZeroDivisionError:
            return None
        
        else:
            if abs(dz)<atol:
                return z
            z-=dz


def indicing(r,roots):
    try:
        return np.where(np.isclose(roots,r,atol))[0][0]
    
    except:
        roots.append(r)
        return len(roots)-1

def plot(f, n=1000 , domain={'x':(-1,1),'y':(-1,1)}):
    pixel_grid=np.zeros((n,n),dtype=int)
    x_min , x_max = domain['x']
    y_min , y_max = domain['y']
    roots=[]

    for x_index , x in enumerate(np.linspace(x_min,x_max,n)):
        for y_index , y in enumerate(np.linspace(y_min,y_max,n)):
            z0= x + y*1j
            r=newton_raphson(z0,f)
            if r!=None:
                r_index=indicing(r,roots)
                print(r_index,end='')
                pixel_grid[x_index,y_index]=r_index

    plt.imshow(pixel_grid,cmap='hsv',origin='lower')
    plt.show()

f = lambda z: z**5 -1

plot(f)