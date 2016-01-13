#!/usr/bin/env python
# -*- coding: utf-8 -*-

train_data_file="misc_data/train.dat"
srcs=['apple','newtalk','chinatimes','fong','ming','freedom']
with open(train_data_file,'w') as train_data:
    for src in srcs:
        with open ('data/{}_final.txt'.format(src)) as file :
            for line in file:
                train_data.write('{},{}'.format(src,line))
