"""
File: io.py
Author: sunprinceS (TonyHsu)
Email: sunprince12014@gmail.com
Github: https://github.com/sunprinces
Description: basic i/o
"""

from __future__ import print_function
import random
import joblib as jl
import numpy as np
import scipy as sp

from sklearn.feature_extraction.text import CountVectorizer , TfidfTransformer

from . import marcos

old_media=['apple','chinatimes','freedom']
new_media=['newtalk','fong','ming']

def loadDat(mode,data,idx=None):
    print('Loading data...')
    if mode == 'train':
        labs=[]
        corpus=[]
        with open('{}/{}.dat'.format(marcos.MISC_DIR,data)) as file:
            src=file.read().splitlines()
            random.shuffle(src)
            for new in src:
                tmp = new.split(',')

                if tmp[0] in old_media:
                    labs.append(0)
                elif tmp[0] in new_media:
                    labs.append(1)
                else:
                    printf('Unexpected label!',file=sys.stderr)

                corpus.append(tmp[1])

        s = int(len(labs) * 0.8)
        return corpus[:s],labs[:s],corpus[s:],labs[s:]
    elif mode =='test':
        corpus=[]
        with open('{}/{}.dat'.format(marcos.MISC_DIR,data)) as file:
            src=file.read().splitlines()
            for new in src:
                corpus.append(new)
        return corpus
    else:
        print('Unexpected mode!',file=sys.stderr)
