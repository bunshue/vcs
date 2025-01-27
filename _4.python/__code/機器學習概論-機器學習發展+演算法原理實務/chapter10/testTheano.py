from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

t1 = time.time()
vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

x = shared(numpy.asarray(np.random.rand(vlen), config.floatX))
f = function([], T.exp(x))
print(f.maker.fgraph.toposort())
t0 = time.time()
for i in range(iters):
    r = f()

print('Looping %d times took' % iters, t1 - t0, 'seconds')
print('Result is', r)
if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
    print('Used the cpu')
else:
    print('Used the gpu')
print(time.time()-t1)

