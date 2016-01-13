#!/usr/bin/env python
# -*- coding: utf-8 -*-

from svmutil import *
from util import *
import sys

def main():

    #Loading training data and labels
    train_corpus , train_labels , valid_corpus ,valid_labels= io.loadDat(mode='train',data='train')

    #bow transform to numeric matrix
    train_matrix = transform.BOWtransform(train_corpus,'train',sys.argv[1])

    print('Data preprocessing end...\nStart training SVM...')
    svm_classify_model = svm_train(train_labels,train_matrix,'-t 0 -b 1 -q')
    svm_save_model('{}/{}.model'.format(marcos.SVM_MODEL_DIR,sys.argv[1]),svm_classify_model)

    print('Training finished!\nStart validating...')

    #bow transform to numeric matrix
    valid_matrix = transform.BOWtransform(valid_corpus,'test',sys.argv[1])

    svm_classify_model= svm_load_model('{}/{}.model'.format(marcos.SVM_MODEL_DIR,sys.argv[1]))
    p_labels,p_acc,p_val=svm_predict(valid_labels,valid_matrix,svm_classify_model,'-b 1')


    #write ans
    with open('output/{}.out'.format(sys.argv[1]),'w') as ans:
        for p_dis in p_val:
            for p in p_dis:
                ans.write('{} '.format(p))
            ans.write('\n')

if __name__ == "__main__":
    main()
