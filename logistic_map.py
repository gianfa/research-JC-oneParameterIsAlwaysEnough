"""
Test code, which I used to better understand the paper I used for a Journal Club presentation.

The Paper:
PIANTADOSI, Steven T. One parameter is always enough. AIP Advances, 2018, 8.9: 095118.
https://pdfs.semanticscholar.org/9f4a/4d01294fd1fcc3f80a3a7c876055971b7663.pdf
"""


# %%
""" Code for Logistic Map

Bifurcation Diagram

ref: https://www.kaggle.com/code/miguelrodriguezolmos/plot-the-logistic-map-with-python-matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


x_ini = 0.01 # initial condition in the range (0,1)
r_min, r_max = [0, 4] # maximum range [0, 4]
x_min, x_max = [0, 1]
iters = 1000 #number of iterations, higher is more accurate and more computationally expensive


last = round(0.8 * iters)
n_pixels = 3000
r = np.linspace(r_min, r_max, n_pixels)
x = np.repeat(x_ini, n_pixels)
for i in range(iters):

    x = r * x * (1-x) # logistic map

    if i >= (iters - last): 
        if i == (iters - last): 
            D = np.array([r, x]).T
        else:
            D = np.concatenate([D,np.array([r, x]).T], axis = 0)            
X = D[:,0]
Y = D[:,1]

fig, ax = plt.subplots(figsize=(10, 10), 
                       dpi=300, 
                       facecolor='none', 
                       edgecolor='none'
                      )
ax.set_xlim(r_min, r_max)
ax.set_ylim(x_min, x_max)
ax.set_ylabel("x")
ax.set_xlabel("r")
ax.set_title("Bifurcation Diagram")
# plt.axis('off')
# plt.gca().set_axis_off()
# plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
# plt.margins(0,0)
# plt.gca().xaxis.set_major_locator(plt.NullLocator())
# plt.gca().yaxis.set_major_locator(plt.NullLocator())

plt.scatter(
    X, Y,
    s = (3*72/n_pixels)**2,
    alpha = 0.8,
    c = 'darkred',
    marker = '.'
)

# %%
"""
Logistic Map

Phase Diagram (x_{n} vs x_{n+1})
"""
N = 100 # iterations
r = 0.2 # LogMap parameter
x_0 = 0.5  # i.c.
X = [] # [x_n, x_n+1] container

X.append([x_0, r * x_0 * (1 - x_0)]) # apply the first step of logistic map
for _ in np.arange(N):
    x_n = X[-1][1]
    x_n1 = r * x_n * (1 - x_n)
    X.append([ x_n, x_n1] )

fig, ax = plt.subplots(1,1)
ax.set_xlabel('$x_n$')
ax.set_ylabel('$x_{n+1}$')
ax.plot(x)
ax.set_title("Phase Diagram")
print(x[:7])


# %%
# ref: https://www.youtube.com/watch?v=1ApX-OHGOdw
r = 3

N = 100
x = .5 + np.zeros(N)

for n in range(N-1):
    x[n + 1] = r * x[n] * (1 - x[n])

fig, ax = plt.subplots(1,1)
ax.plot(x, 's-')
ax.set_xlabel('iteration')
ax.set_ylabel('$x$')


# %% Multiplot Logistic Map

N = 100
x_0 = 0.5
rs = np.linspace(0, 5, 8)

hist = {}
for r in rs:
    x = x_0 + np.zeros(N)
    for n in range(N-1):
        x[n + 1] = r * x[n] * (1 - x[n])
    hist[r] = x


ncols = 4
nrows = int(np.ceil(len(rs)/ncols))

fig, axs = plt.subplots(nrows, ncols, figsize=(15, 10))
if axs.ndim == 1:
    axs = axs[None, :]
for i in range(1, ncols*nrows):
    ri = int(np.floor(i/ncols))
    ci = i % ncols
    if i >= len(rs):
        axs[ri, ci].axis('off')
        continue
    ax = axs[ri, ci]
    ax.plot(hist[rs[i]])
    ax.set_title(f"r = {rs[i]:.4}", fontsize=16)
    ax.set_xlabel('iteration')
    ax.set_ylabel('$x$')

    fig.tight_layout()
    fig.suptitle("Logistic Map", y=1.05, fontsize=20)



# %% Dyadic Map
"""

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

iterations = 8 # bits
x0 = 0.2

xs = {}
for x0 in np.linspace(0, 1, 10): # iterate over several x0
    x = np.zeros(iterations) + x0
    for n in range(iterations - 1): # apply the dyadic map
        x[n+1] =  2 * x[n] % 1
        #x[n+1] =  2 * x[n] if 0 <= x[n] < 0.5 else 2 * x[n] -1 

    xs[x0] = x

    # visualize
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))
    fig.suptitle(f"x0 = {x0}", fontsize=18)
    axs[0].plot(x)
    #ax.set_title(f"r = {rs[i]:.4}", fontsize=16)
    axs[0].set_xlabel('iteration')
    axs[0].set_ylabel('$x$')

    axs[1].plot(x[:-1], x[1:], marker='.', linestyle='-')
    #print(x)
    # for x0, x in xs.items():
    #     plt.plot(np.cumsum(x))
# %%
