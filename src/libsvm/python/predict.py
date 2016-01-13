#!/usr/bin/env python
# -*- coding: utf-8 -*-

from svmutil import *
from util import *
import sys

lab_map=["Old media","New media"]
lab_set=[]

def main():

    # load testing data
    test_corpus = io.loadDat(mode='test',data=sys.argv[2])
    # bow transform
    test_matrix_tmp = transform.BOWtransform(test_corpus,'test',sys.argv[1])
    test_matrix = transform.dimReduction(test_matrix_tmp,'test',sys.argv[1])

    #use SVM to classify
    #dummy label
    con_labels=[0]*len(test_corpus)

    svm_classify_model= svm_load_model('{}/{}.model'.format(marcos.SVM_MODEL_DIR,sys.argv[1]))
    lab_set = svm_classify_model.get_labels()
    p_labels,p_acc,p_val=svm_predict(con_labels,test_matrix,svm_classify_model,'-b 1')


    #write ans
    for lab in p_labels:
        print(lab_map[int(lab)])
    # print("\t{}\t{}".format(lab_map[1],lab_map[0]))
    # for doc_id,p_dis in enumerate(p_val,1):
        # # print("***********************")
        # print("Doc{}:\t{}".format(doc_id,"\t".join(format(p,"10.3f") for p in p_dis)))
        # # for i,p in enumerate(p_dis):
            # # print("{}:{:.3f}".format(lab_map[lab_set[i]],p))



if __name__ == "__main__":
    main()
