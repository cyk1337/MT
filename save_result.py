#!/usr/bin/env python

# encoding: utf-8

'''
  
             \ \ / /__| | ___   _ _ __    / ___| | | |  / \  |_ _|
              \ V / _ \ |/ / | | | '_ \  | |   | |_| | / _ \  | | 
               | |  __/   <| |_| | | | | | |___|  _  |/ ___ \ | | 
               |_|\___|_|\_\\__,_|_| |_|  \____|_| |_/_/   \_\___
 ==========================================================================
@author: CYK

@license: School of Informatics, Edinburgh

@contact: s1718204@sms.ed.ac.uk

@file: save_result.py

@time: 14/03/2018 22:35

@desc:         
               
'''              
import matplotlib.pyplot as plt
import os
import pandas as pd


result={'fr':[], 'en':[], 'prec':[],'rec':[]}


save_dir='q9'
def save_result(data, csv_name, subdir=False, save_dir=save_dir):
    assert csv_name[-4:] == '.csv', "Error: didnot give a valid csv_name!"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    if subdir is not False:
        subdir = os.path.join(save_dir, subdir)
        if not os.path.isdir(subdir):
            os.mkdir(subdir)
        csv_file = os.path.join(subdir, csv_name)
        # =========================
        # 1. save to txt
        # with open(filename, 'w') as f:
        #     f.write(str(history))
        # ==========================
        hist = pd.DataFrame.from_dict(data, orient='columns')
        hist.to_csv(csv_file, encoding='utf-8')
        print('History is written into {}'.format(csv_file))
        print('-'*80)



def compute_diff(subdir='ATT'):
    subdir = os.path.join(save_dir, subdir)
    assert os.path.isdir(subdir) == True, "Error: {} does not exists!".format(subdir)

    # sum_plot = os.path.join(save_dir, 'plot_all')
    sum_plot = subdir
    if not os.path.isdir(sum_plot):
        os.mkdir(sum_plot)

    data={}
    for i, filename in enumerate(os.listdir(subdir)):
        if filename[-4:] != '.csv': continue
        name=filename[:-4]
        csv_file = os.path.join(subdir, filename)
        data[name] = pd.read_csv(csv_file, encoding = 'utf8')
    return data

data = compute_diff()
file_att='1-1_NO_ATTN'
file_noatt='1-1_ATTN'
prec_cond = data[file_att]['prec'] - data[file_noatt]['prec']> 0
#     pass
att_result = data[file_att][prec_cond]
no_att_result = data[file_noatt][prec_cond]

att_result[['No_att_prec','No_att_rec']] = no_att_result[['prec','rec']]
print(att_result)