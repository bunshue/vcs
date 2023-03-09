from pylab import *
from numpy import NaN

xmin, xmax, ymin, ymax = -2, 0.8, -1.5, 1.5
max_it = 100    # maximum number of iterations
px     = 3000	# vertical lines
res    = (ymax - ymin) / px   # grid resolution

figure(figsize = (10, 10))

def m(c):
	z = 0
	for n in range(1, max_it + 1):
		z = z**2 + c
		if abs(z) > 2:
			return n
	return NaN

X = arange(xmin, xmax + res, res)
Y = arange(ymin, ymax + res, res)
Z = zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
	#print (iy + 1, "of", len(Y))
	for ix, x in enumerate(X):
		Z[-iy - 1, ix] = m(x + 1j * y)

save("mandel", Z)	# save array to file

imshow(Z, cmap = plt.cm.prism, interpolation = 'none',
  extent = (X.min(), X.max(), Y.min(), Y.max()))
xlabel("Re(c)")
ylabel("Im(c)")

#¦s¹Ï©R¥O
savefig("mandelbrot_python.svg")

show()
