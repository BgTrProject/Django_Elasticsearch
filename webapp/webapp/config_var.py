import threading
import os
import sys
class varib:
    def __init__(self):
        self.abc="abcdfg"
        self.bcd="bcdfgh"
        self.cde = "bcdfghi"
        self.klm = "klm"
        self.lmn="lmn"
        self.mnn="mnn"
    def save_abc(self,a):
        self.abc = a
        return self.abc
    def save_bcd(self,b):
        self.bcd=b
        return self.bcd
    def save_cde(self,c):
        self.cde=c
        return self.cde

    def save_klm(self,k):
        self.klm = k
        return self.klm
    def save_lmn(self,l):
        self.lmn = l
        return self.lmn
    def save_mnn(self,m):
        self.mnn = m
        return self.mnn

    def print_abc(self):
        return self.abc
    def print_bcd(self):
        return self.bcd
    def print_cde(self):
        return self.cde

    def print_klm(self):
        return self.klm
    def print_lmn(self):
        return self.lmn
    def print_mnn(self):
        return self.mnn
