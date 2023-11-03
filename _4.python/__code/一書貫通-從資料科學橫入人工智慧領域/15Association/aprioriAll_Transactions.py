
# coding: utf-8
# ### 应用

# In[ ]:
###########################################################################################################

import os, sys
import itertools
import pandas as pd
os.chdir(r"D:\Python_book\15Association")

sys.path.append('./myscripts2')
#需要把Apriori所在的目录"D:\Python_book\15Association\myscripts2"设置到python工作目录，
#设置方式为Tools->PYTHONPATH manager 
from aprioriAll import aprioriAll

transactions = pd.read_csv(r'Transactions.csv')


# In[ ]:


'''
Sort phase: The database is sorted, with customer-id as the major key 
and transaction-time as the minor key. This step implicitly 
converts the original transaction database into a database of 
customer sequences.
'''


# In[ ]:


def aggFunc(*args):
    agg = itertools.chain(*args)
    return list(agg)

baskets = transactions['Model'].groupby([transactions['OrderNumber'], transactions['LineNumber']]).apply(aggFunc)
baskets.head()


# In[ ]:


dataSet = list(baskets.groupby(level=0).apply(list))
dataSet[:3]


# In[ ]:


seq=aprioriAll(dataSet, min_support=0.04)
#%%

###########################################################################################################
#以下是学习aprioriAll算法的内容

# ### 测试数据集

# In[ ]:


seq1 = [           [30], [90]          ]
seq2 = [ [10, 20], [30], [40, 60, 70]  ]
seq3 = [         [30, 50, 70],         ]
seq4 = [      [30], [40, 70], [90]     ]
seq5 = [              [90],            ]
dataSet = [seq1, seq2, seq3, seq4, seq5]
min_support=0.25


# In[ ]:
import os
os.chdir(r"D:\Python_book\15Association")

import sys
sys.path.append('./myscripts2')

import itertools
import pandas as pd
from apriori import apriori


# ### 1、Sort Phase
# 过程略，直接使用整理过的示例数据

# ### 2、Litemset Phase
# 搜索litemset，直接使用apriori算法，主要的区别在于计算支持度时，一个客户customer购买了同样的项集（itemset）时，支持频度仅计算一次。这是因为在apriori算法中，支持度是对交易(transaction)而言的，但在序列模式的计算中，大项集的支持度是对客户(customer)而言的

# In[ ]:


def createLs1(dataSet, min_support):
    '''
    Using  algorithm apriorito mining large 1-sequences 
    `Ls` for Large Sequence
    '''
    n = len(dataSet)
    flattenSet = list(itertools.chain(*dataSet))
    flatten_n = len(flattenSet)
    
    # Transform the min_support to litemset_support
    min_support_new = min_support * n /flatten_n
    litemsets = apriori(flattenSet, min_support=min_support_new)
    mapping = {v: k for k, v in enumerate(litemsets)}
    
    # Transform the litemset_support to sequence_support
    supportLs1 = {(mapping[k],): v *flatten_n / n 
                  for k, v in litemsets.items()}
    
    return mapping, supportLs1


# - 测试

# In[ ]:


mapping, supportLs1 = createLs1(dataSet, min_support=min_support)
mapping


# In[ ]:


supportLs1


# In[ ]:


Ls1 = [list(k) for k in supportLs1]
Ls1


# ### 3、Transformation Phase

# In[ ]:


def seqMapping(seq, mapping):
    '''
    Mapping litemsets to integer objects, for treating litemsets as
    single entities, and reducing the time required 
    '''
    newSeq = []
    for iSet in seq:
        newSet = [v for k, v in mapping.items() if k <= set(iSet)]
        if newSet != []:
            newSeq.append(newSet)
    return newSeq

def transform(dataSet, mapping):
    '''
    Transform each customer sequence into an alternative representation.
    '''
    transformDS = []
    for seq in dataSet:
        newSeq = seqMapping(seq, mapping)
        if newSeq != []:
            transformDS.append(newSeq)
    return transformDS                    


# - 测试

# In[ ]:


transformDS  = transform(dataSet, mapping)
for seq in transformDS :
    print(seq)


# ### 4、Sequence Phase

# 产生候选序列

# In[ ]:


def seqGen(seqA, seqB):
    '''
    Generate candidate k+1 sequences with two large k-sequences
    '''
    newA, newB = seqA.copy(), seqB.copy()
    if seqA[:-1] == seqB[:-1]:
        newA.append(seqB[-1])
        newB.append(seqA[-1])
        return [newA, newB]

def CsGen(Ls):
    '''
    Generate all candidate k+1 sequences from large k-sequences
    '''
    Cs = []
    for seqA, seqB in itertools.combinations(Ls, 2):
        newSeqs = seqGen(seqA, seqB)
        if newSeqs != None:
            Cs.extend(newSeqs)
    return [seq for seq in Cs if seq[1:] in Ls] #  Pruning  


# - 测试

# In[ ]:


testLs = [
    [1, 2, 3], 
    [1, 2, 4],
    [1, 3, 4],
    [1, 3, 5],
    [2, 3, 4]]
CsGen(testLs)


# 子序列判断

# In[ ]:


def isSubSeq(seq, cusSeq):
    '''
    Check if a sequence is contained in a customer sequence.
    '''
    nSeq, nCusSeq = len(seq), len(cusSeq)
    if nSeq > nCusSeq:
        return False 
    if nSeq == 1:        
        return any([seq[0] in i for i in cusSeq])
    if nSeq > 1 :
        head = [seq[0] in i for i in cusSeq]
        if any(head):
            split = head.index(True)
            return isSubSeq(seq[1:], cusSeq[split + 1:]) # Recursion
        else:
            return False


# - 测试

# In[ ]:


seq = [3, 4, 8]
cusSeq = [[7], [3, 8], [9], [4, 5, 6], [8]]
isSubSeq(seq, cusSeq)


# 产生频繁k序列，此步骤需要迭代执行

# In[ ]:


def calcSupport(transformDS, Cs, min_support):
    '''
    Return: 1. a list of large-sequences
            2. a dictionary of `large-sequence: support` pairs
    '''
    supportLsk = {}; n = len(transformDS)
    if len(Cs) >= 1:
        for seq in Cs:
            support = sum([isSubSeq(seq, cusSeq) for cusSeq in transformDS]) / n
            if support >= min_support:
                supportLsk.update({tuple(seq): support})
    return [list(k) for k in supportLsk], supportLsk       


# - 测试

# In[ ]:


Cs2 = CsGen(Ls1)
Ls2, supportLs2 = calcSupport(transformDS, Cs2, min_support)
print(Ls2)
print(supportLs2)


# ### 5、Maximal Phase

# - 一个更快速搜寻子序列的算法可参考：
# R. Agrawal and R. Srikant. Mining sequential patterns. Research Report RJ 9910, IBM Almaden Research Center, San Jose, California, Oc
# tober 1994.

# 需要将大序列中的项集转换回原始的购物篮再进行序列最大化

# In[ ]:


tr_mapping = {v: k for k, v in mapping.items()}

Ls = Ls1 + Ls2
Ls = [[tr_mapping[k] for k in seq] for  seq in Ls ]

supportLs = {}
supportLs.update(supportLs1); supportLs.update(supportLs2)
supportLs = {tuple([tr_mapping[i] for i in k]):v for k, v in supportLs.items()}

print(supportLs)


# 序列最大化需要保留的是某个序列的非空真子序列（类似于非空真子集，此处要保留该序列本身），该步骤与Transformation阶段中判断子序列的方法类似，区别在于已经将其中的项集映射回来了，因此稍作修改

# In[ ]:


def isSubSeq2(seq, cusSeq):
    nSeq, nCusSeq = len(seq), len(cusSeq)
    
    if nSeq > nCusSeq:
        return False 
    if nSeq == 1:        
        return any([seq[0].issubset(i) for i in cusSeq])
    if nSeq > 1 :
        head = [seq[0].issubset(i) for i in cusSeq]
        if any(head):
            split = head.index(True)
            return isSubSeq2(seq[1:], cusSeq[split:]) # Recursion
        else:
            return False           

def notProperSubSeq(seq, cusSeq):
    '''
    Return True if `seq` is not proper sub sequence of `cusSeq`
    '''
    if seq == cusSeq:
        return True
    else:
        return not isSubSeq2(seq, cusSeq)


# 将备选序列中的最大化的序列保留下来

# In[ ]:


def maxLs(Ls, supportLs):
    LsCopy = Ls.copy()
    lenL, lenC = len(Ls), len(LsCopy)
    while lenC > 1 and lenL > 1:
        if LsCopy[lenC - 1] in Ls:
            mask = [notProperSubSeq(seq, LsCopy[lenC - 1]) for seq in Ls]
            Ls = list(itertools.compress(Ls, mask))
            lenL = len(Ls)
            
        lenC -= 1
        
    supportLs = {tuple(seq): supportLs[tuple(seq)] for seq in Ls} 
    return Ls, supportLs


# In[ ]:


Ls, supportLs = maxLs(Ls, supportLs)
supportLs


# ### aprioriAll

# In[ ]:


def aprioriAll(dataSet, min_support=0.4):
    '''
    Proceeding aprioriall algorithm to mining sequential patterns
    
    Refer to:    
    Agrawal,R.,Srikant,R.,Institute of Electric and Electronic 
    Engineer et al. Mining sequential patterns[C]. Proceedings 
    of the Eleventh International Conference on Data Engineering,
    Washington DC, USA: IEEE Computer Society,1995:3-14.
    '''
    # Litemset Phase
    mapping, supportLs1 = createLs1(dataSet, min_support)
    Ls1 = [list(k) for k in supportLs1]
    
    # Transformation Phase
    transformDS  = transform(dataSet, mapping)
    
    # Sequence Phase
    LsList = [Ls1]; supportLs = supportLs1.copy()
    k = 1
    while k >= 1 and len(LsList[-1]) > 1:
        Csk = CsGen(LsList[-1])
        Lsk, supportLsk = calcSupport(transformDS, Csk, min_support)
        if len(Lsk) > 0:
            LsList.append(Lsk); supportLs.update(supportLsk)
            k += 1
        else:
            break
            
    Ls = list(itertools.chain(*LsList))
    tr_mapping = {v: k for k, v in mapping.items()}
    Ls = [[tr_mapping[k] for k in seq] for  seq in Ls ]
    supportLs = {tuple([tr_mapping[i] for i in k]):v 
                 for k, v in supportLs.items()}
    
    # Maximal Phase
    Ls, supportLs = maxLs(Ls, supportLs)
       
    return pd.DataFrame(list(supportLs.items()), 
                        columns=['sequence', 'support'])


# In[ ]:


aprioriAll(dataSet, min_support=0.25)


# In[ ]:


testSet = [
    [[1, 5], [2], [3], [4] ],
    [[1], [3], [4], [3, 5] ],
    [[1], [2], [3], [4]    ],
    [[1], [3], [5]         ],
    [[4], [5]              ]
    ]


# In[ ]:


import sys
sys.path.append(r'D:\Python_book\15Association\myscripts2')
from aprioriAll import aprioriAll


# In[ ]:


aprioriAll(testSet, min_support=0.4)


#%%