#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
import re

try:
    import psyco
    psyco.full()
except:
    pass

from zh_wiki import zh2Hant, zh2Hans, zh2TW, zh2HK, zh2CN, zh2SG
#from zhtools.zh_wiki import zh2Hant, zh2Hans, zh2TW, zh2HK, zh2CN, zh2SG

import sys
py3k = sys.version_info >= (3, 0, 0)
print(sys.version_info)
print('py3k = ', py3k)

if py3k:
    print('1111')
    UEMPTY = ''
else:
    print('2222')
    _zh2Hant, _zh2Hans = {}, {}
    for old, new in ((zh2Hant, _zh2Hant), (zh2Hans, _zh2Hans)):
        for k, v in old.items():
            new[k.decode('utf8')] = v.decode('utf8')
    zh2Hant = _zh2Hant
    zh2Hans = _zh2Hans
    UEMPTY = ''.decode('utf8')

# states
(START, END, FAIL, WAIT_TAIL) = list(range(4))
# conditions
(TAIL, ERROR, MATCHED_SWITCH, UNMATCHED_SWITCH, CONNECTOR) = list(range(5))

MAPS = {}

class Node(object):
    def __init__(self, from_word, to_word=None, is_tail=True,
            have_child=False):
        self.from_word = from_word
        if to_word is None:
            self.to_word = from_word
            self.data = (is_tail, have_child, from_word)
            self.is_original = True
        else:
            self.to_word = to_word or from_word
            self.data = (is_tail, have_child, to_word)
            self.is_original = False
        self.is_tail = is_tail
        self.have_child = have_child

    def is_original_long_word(self):
        return self.is_original and len(self.from_word)>1

    def is_follow(self, chars):
        return chars != self.from_word[:-1]

    def __str__(self):
        return '<Node, %s, %s, %s, %s>' % (repr(self.from_word),
                repr(self.to_word), self.is_tail, self.have_child)

    __repr__ = __str__

class ConvertMap(object):
    def __init__(self, name, mapping=None):
        self.name = name
        self._map = {}
        if mapping:
            self.set_convert_map(mapping)

    def set_convert_map(self, mapping):
        convert_map = {}
        have_child = {}
        max_key_length = 0
        for key in sorted(mapping.keys()):
            if len(key)>1:
                for i in range(1, len(key)):
                    parent_key = key[:i]
                    have_child[parent_key] = True
            have_child[key] = False
            max_key_length = max(max_key_length, len(key))
        for key in sorted(have_child.keys()):
            convert_map[key] = (key in mapping, have_child[key],
                    mapping.get(key, UEMPTY))
        self._map = convert_map
        self.max_key_length = max_key_length

    def __getitem__(self, k):
        try:
            is_tail, have_child, to_word  = self._map[k]
            return Node(k, to_word, is_tail, have_child)
        except:
            return Node(k)

    def __contains__(self, k):
        return k in self._map

    def __len__(self):
        return len(self._map)

class StatesMachineException(Exception): pass

class StatesMachine(object):
    def __init__(self):
        self.state = START
        self.final = UEMPTY
        self.len = 0
        self.pool = UEMPTY

    def clone(self, pool):
        new = deepcopy(self)
        new.state = WAIT_TAIL
        new.pool = pool
        return new

    def feed(self, char, map):
        node = map[self.pool+char]

        if node.have_child:
            if node.is_tail:
                if node.is_original:
                    cond = UNMATCHED_SWITCH
                else:
                    cond = MATCHED_SWITCH
            else:
                cond = CONNECTOR
        else:
            if node.is_tail:
                cond = TAIL
            else:
                cond = ERROR

        new = None
        if cond == ERROR:
            self.state = FAIL
        elif cond == TAIL:
            if self.state == WAIT_TAIL and node.is_original_long_word():
                self.state = FAIL
            else:
                self.final += node.to_word
                self.len += 1
                self.pool = UEMPTY
                self.state = END
        elif self.state == START or self.state == WAIT_TAIL:
            if cond == MATCHED_SWITCH:
                new = self.clone(node.from_word)
                self.final += node.to_word
                self.len += 1
                self.state = END
                self.pool = UEMPTY
            elif cond == UNMATCHED_SWITCH or cond == CONNECTOR:
                if self.state == START:
                    new = self.clone(node.from_word)
                    self.final += node.to_word
                    self.len += 1
                    self.state = END
                else:
                    if node.is_follow(self.pool):
                        self.state = FAIL
                    else:
                        self.pool = node.from_word
        elif self.state == END:
            # END is a new START
            self.state = START
            new = self.feed(char, map)
        elif self.state == FAIL:
            raise StatesMachineException('Translate States Machine '
                    'have error with input data %s' % node)
        return new

    def __len__(self):
        return self.len + 1

    def __str__(self):
        return '<StatesMachine %s, pool: "%s", state: %s, final: %s>' % (
                id(self), self.pool, self.state, self.final)
    __repr__ = __str__

class Converter(object):
    def __init__(self, to_encoding):
        self.to_encoding = to_encoding
        self.map = MAPS[to_encoding]
        self.start()

    def feed(self, char):
        branches = []
        for fsm in self.machines:
            new = fsm.feed(char, self.map)
            if new:
                branches.append(new)
        if branches:
            self.machines.extend(branches)
        self.machines = [fsm for fsm in self.machines if fsm.state != FAIL]
        all_ok = True
        for fsm in self.machines:
            if fsm.state != END:
                all_ok = False
        if all_ok:
            self._clean()
        return self.get_result()

    def _clean(self):
        if len(self.machines):
            self.machines.sort(key=lambda x: len(x))
            # self.machines.sort(cmp=lambda x,y: cmp(len(x), len(y)))
            self.final += self.machines[0].final
        self.machines = [StatesMachine()]

    def start(self):
        self.machines = [StatesMachine()]
        self.final = UEMPTY

    def end(self):
        self.machines = [fsm for fsm in self.machines
                if fsm.state == FAIL or fsm.state == END]
        self._clean()

    def convert(self, string):
        self.start()
        for char in string:
            self.feed(char)
        self.end()
        return self.get_result()

    def get_result(self):
        return self.final


def registery(name, mapping):
    global MAPS
    MAPS[name] = ConvertMap(name, mapping)

registery('zh-hant', zh2Hant)
registery('zh-hans', zh2Hans)
registery('zh-tw', zh2TW)
registery('zh-hk', zh2HK)
registery('zh-cn', zh2CN)
registery('zh-sg', zh2SG)

del zh2Hant, zh2Hans, zh2TW, zh2HK, zh2CN, zh2SG

'''
中國大陸（zh-cn）、新加坡（zh-sg）及馬來西亞（zh-my）的地區詞為簡體中文
台灣（zh-tw）、香港（zh-hk）及澳門（zh-mo）的地區詞為正體／繁體中文
'''

print('簡中用語 => 正中用語')
word_1 = '帮助文件'
word_2 = Converter('zh-hant').convert(word_1)
print(word_1, word_2)

print('正中用語 => 簡中用語')
word_1 = '顯著'
word_2 = Converter('zh-hans').convert(word_1)
print(word_1, word_2)

print('轉 台灣用語')
word_1 = '缺省'
word_2 = Converter('zh-tw').convert(word_1)
print(word_1, word_2)

print('轉 香港用語')
word_1 = '字节'
word_2 = Converter('zh-hk').convert(word_1)
print(word_1, word_2)

print('轉 中國用語')
word_1 = '記憶體'
word_2 = Converter('zh-cn').convert(word_1)
print(word_1, word_2)

print('轉 新加坡用語')
word_1 = '蹦极跳'
word_2 = Converter('zh-sg').convert(word_1)
print(word_1, word_2)
