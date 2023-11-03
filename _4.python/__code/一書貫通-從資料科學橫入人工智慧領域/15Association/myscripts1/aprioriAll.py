# -*- coding: utf-8 -*-

'''
Created on Sep. 30, 2017
Apriori modified script
@author: ZRQ
'''

import sys
sys.path.append('E:/myscripts')

import itertools
import pandas as pd
from apriori import apriori


def createLs1(dataSet, min_support):# 'Ls' for Large Sequence
    n = len(dataSet)
    flattenSet = list(itertools.chain(*dataSet))
    flatten_n = len(flattenSet)
    
    # Transform the min_support to litemset_support
    min_support_new = min_support * n /flatten_n
    litemsets = apriori(flattenSet, min_support=min_support_new)
        
    mapping = {v: k for k, v in enumerate(litemsets)}
    # Transform the litemset_support to sequence_support
    supportLs1 = {(mapping[k],):v * flatten_n / n for k, v in litemsets.items()}
    
    return mapping, supportLs1
	
def seqMapping(seq, mapping):
    newSeq = []
    for iSet in seq:
        newSet = [v for k, v in mapping.items() if k <= set(iSet)]
        if newSet != []:
            newSeq.append(newSet)
    return newSeq

def transform(dataSet, mapping):
    
    transformDS = []
    for seq in dataSet:
        newSeq = seqMapping(seq, mapping)
        if newSeq != []:
            transformDS.append(newSeq)
    return transformDS                    
	
def seqGen(seqA, seqB):
    
    newA, newB = seqA.copy(), seqB.copy()
    if seqA[:-1] == seqB[:-1]:
        newA.append(seqB[-1])
        newB.append(seqA[-1])
        return [newA, newB]

def CsGen(Ls):
    Cs = []
    for seqA, seqB in itertools.combinations(Ls, 2):
        newSeqs = seqGen(seqA, seqB)
        if newSeqs != None:
            Cs.extend(newSeqs)
    return [seq for seq in Cs if seq[1:] in Ls] #  Pruning  
	

def isSubSeq(seq, cusSeq):
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

			
def calcSupport(transformDS, Cs, min_support):
    '''
    Return: a list of large-sequences
            a dictionary of `large-sequence: support` pairs
    '''
    supportLsk = {}; n = len(transformDS)
    if len(Cs) >= 1:
        for seq in Cs:
            support = sum([isSubSeq(seq, cusSeq) for cusSeq in transformDS]) / n
            if support >= min_support:
                supportLsk.update({tuple(seq): support})
    return [list(k) for k in supportLsk], supportLsk       
	
	
	
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

    if seq == cusSeq:
        return True
    else:
        return not isSubSeq2(seq, cusSeq)
		

				
def maxLs(Ls, supportLs):
    LsCopy = Ls.copy()
    lenL, lenC = len(Ls), len(LsCopy)

    while lenC > 1 and lenL > 1:
        if LsCopy[lenC - 1] in Ls:
            mask = [notProperSubSeq(seq, LsCopy[lenC - 1]) for seq in Ls]
            Ls = list(itertools.compress(Ls, mask))
            lenL = len(Ls)
            
        lenC -= 1
    supportLs = {tuple(seq): supportLs[tuple(seq)] for seq in Ls} # Dict comprehension
    return Ls, supportLs
	
	
	
def aprioriAll(dataSet, min_support=0.25):
    '''
    Proceeding aprioriall algorithm to mining sequential patterns
    
    Refer to:    
    Agrawal,R.,Srikant,R.,Institute of Electric and Electronic 
    Engineer et al. Mining sequential patterns[C]. Proceedings 
    of the Eleventh International Conference on Data Engineering,
    Washington DC, USA: IEEE Computer Society,1995:3-14.
    '''
    mapping, supportLs1 = createLs1(dataSet, min_support)
    
    Ls1 = [list(k) for k in supportLs1]
    transformDS  = transform(dataSet, mapping)
    
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
    supportLs = {tuple([tr_mapping[i] for i in k]):v for k, v in supportLs.items()}
    
    Ls, supportLs = maxLs(Ls, supportLs)
       
    return pd.DataFrame(list(supportLs.items()), columns=['sequence', 'support'])
	
	
	
if __name__ == '__main__':
    print ('This script should be imported instead of running directly!')
else:
    print ('aprioriAll imported!')