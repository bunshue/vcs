# -*- coding: utf-8 -*-

'''
Created on Sep. 7, 2017
Apriori modified script
@author: ZRQ
'''

import itertools
import pandas as pd

def createC1(dataSet):  # 'C1' for Candidate-itemset of 1 item.
    # Flatten the dataSet, leave unique item
    C1 = set(itertools.chain(*dataSet))  
    
    # Transform to a list of frozenset
    return [frozenset([i]) for i in C1]
	
def scanD(dataSet, Ck, min_support): # 'Ck' for Candidate-set of k items.
    support = {}
    
    # Calculate the support of all itemsets
    for i in dataSet:
        for j in Ck:
            if j.issubset(i):
                support[j] = support.get(j, 0) + 1

    n = len(dataSet)
    
    # Return litemset with support
    return {k: v/n for k, v in support.items() if v/n >= min_support}
	
def aprioriGen(Lk):  # 'Lk' for Large-itemset of k items.
    # Generate candidate k+1 itemset  from litemset 
    lenLk = len(Lk)
    k = len(Lk[0])
    if lenLk > 1 and k > 0:
        return set([
                Lk[i].union(Lk[j])
                for i in range(lenLk - 1)
                for j in range(i + 1, lenLk)
                if len(Lk[i] | Lk[j]) == k +1
            ])  #  Use set() to drop duplicates
			
def apriori(dataSet, min_support=0.5): 
    '''
	Return all large itemsets
	'''
    C1 = createC1(dataSet)
    L1 = scanD(dataSet, C1, min_support)
    L = [L1, ]       # Large-itemsets
    k = 2
    while len(L[k-2]) > 1:
        Ck = aprioriGen(list(L[k-2].keys()))
        Lk = scanD(dataSet, Ck, min_support)
        if len(Lk) > 0:
            L.append(Lk)
            k += 1
        else:
             break
                
    # Flatten the freqSets          
    d = {}
    for Lk in L:  
        d.update(Lk)
    return d

def rulesGen(iterable):  
    # Generate nonvoid proper subset of litemset.
    subSet = []
    for i in range(1, len(iterable)):
        subSet.extend(itertools.combinations(iterable, i))
        
    return [(frozenset(lhs), frozenset(iterable.difference(lhs)))
            for lhs in subSet] # Left hand rule and right hand rule

def arules(dataSet, min_support=0.5):
    '''
    Return a pandas.DataFrame of 'rules|support|confidence|lift'    
    '''
    # Generate a dict of 'large-itemset: support' pairs
    L = apriori(dataSet, min_support) 
    
    # Generate candidate rules
    rules = []
    for Lk in L.keys():
        if len(Lk) > 1:
            rules.extend(rulesGen(Lk))
    
    # Calculate support、confidence、lift
    scl = []  # 'scl' for 'Support, Confidence and Lift'
    for rule in rules:
        lhs = rule[0]; rhs = rule[1]
        support = L[lhs | rhs]
        confidence = support / L[lhs]
        lift = confidence / L[rhs]
        scl.append({'LHS':lhs, 'RHS':rhs, 'support':support, 'confidence':confidence, 'lift':lift})
        
    return pd.DataFrame(scl)			



if __name__ == '__main__':
    print ('This script should be imported instead of running directly!')
else:
    print ('apriori imported!')