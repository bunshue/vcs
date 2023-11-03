# -*- coding:utf-8 -*-
# file: pytree.py
#
G = [ 'G', [] ]
H = [ 'H', [] ]
I = [ 'I', [] ]
K = [ 'K', [] ]
E = [ 'E', [ G, H, I, K] ]
D = [ 'D', [] ]
F = [ 'F', [] ]
A = [ 'A', [ D, E] ]
B = [ 'B', [] ]
C = [ 'C', [ F ] ]
Root = [ 'Root', [ A, B, C ] ]
print(Root)
