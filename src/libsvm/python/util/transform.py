"""
File: transformer.py
Author: sunprinceS (TonyHsu)
Email: sunprince12014@gmail.com
Github: https://github.com/sunprinceS
Description: turn text into numric matrix
"""

import sys
import joblib as jl
import numpy as np
import scipy as sp

from . import io,marcos


def BOWTransformer():

    preprocess_pipe = marcos.PREPROCESS_PIPE

    #set bag of word's param
    preprocess_pipe.set_params(bow__min_df=1)
    # preprocess_pipe.set_params(bow__stop_words='english')

    #set tf-idf param
    # feat_pipe.set_params(tfidf__?=)

    #set PCA transformer
    # preprocess_pipe.set_params(pca__n_components=1000)

    #set LDA transformer
    # dim_reduc_pipe.set__params(lda__n_topics=1000)

    return preprocess_pipe

def BOWtransform(corpus,mode,idx):

    data_matrix=[]
    print('Transform data...')

    if mode == 'train':
        bow_transformer = BOWTransformer()
        data_matrix = bow_transformer.fit_transform(corpus)

        #save transform model
        jl.dump(bow_transformer,'{}/{}.model'.format(marcos.TRANSFORM_MODEL_DIR,idx))

    elif mode == 'test':
        bow_transformer = jl.load('{}/{}.model'.format(marcos.TRANSFORM_MODEL_DIR,idx))
        data_matrix = bow_transformer.transform(corpus)

    else:
        print("Unexpected mode in BOWtransform",file=sys.stderr)
        sys.exit()

    # turn dt matrix to list
    print ("The shape of dt matrix is {}\n".format(data_matrix.shape))

    if sp.sparse.isspmatrix_csr(data_matrix):
        data_matrix = data_matrix.toarray().tolist()
    else: #pass through dimension reduction pipe
        data_matrix = data_matrix.tolist()

    return data_matrix

def dimReduction(corpus,mode,idx):
    
    print("Dimension reduction...")
    if sp.sparse.isspmatrix_csr(corpus):
        data_matrix = corpus.toarray()
    data_matrix=[]
    if mode == 'train':
        dim_reduc_pipe = marcos.DIMREDUC_PIPE
        dim_reduc_pipe.set_params(pca__n_components=1000)

        # bow_transformer = BOWTransformer()
        data_matrix = dim_reduc_pipe.fit_transform(corpus)

        #save transform model
        jl.dump(dim_reduc_pipe,'{}/{}.model_reduc'.format(marcos.TRANSFORM_MODEL_DIR,idx))

    elif mode == 'test':
        dim_reduc_pipe = jl.load('{}/{}.model_reduc'.format(marcos.TRANSFORM_MODEL_DIR,idx))
        data_matrix = dim_reduc_pipe.transform(corpus)

    else:
        print("Unexpected mode in BOWtransform",file=sys.stderr)
        sys.exit()

    # turn dt matrix to list
    print ("The shape of dt matrix is {} (after dimension reduction)\n".format(data_matrix.shape))

    return data_matrix.tolist()
