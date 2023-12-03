#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:31:38 2019

@author: yhilly
"""

class Sequence(object):

    def __init__(self, identifier, comment, seq):
        self.id      = identifier
        self.comment = comment
        self.seq     = self._clean(seq)


    def _clean(self, seq):

        return seq.replace('\n', "")

    def gc_percent(self):
        seq = self.seq.upper()
        return float(seq.count('G') + seq.count('C')) / len(seq)


dna1 = Sequence('gi214', 'the first sequence', 'tcgcgcaacgtcgcctacatctcaagattca')
dna2 = Sequence('gi3421', 'the second sequence', 'gagcatgagcggaattctgcatagcgcaagaatgcggc')

print(dna1.gc_percent())
print(dna2.gc_percent())
