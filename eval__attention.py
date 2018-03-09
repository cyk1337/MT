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

@file: eval__attention.py

@time: 09/03/2018 18:14

@desc:         
               
'''
import pandas as pd
from nmt_config import *
from nmt_translate import *
from chainer import serializers

NUM_EPOCHS=0



if __name__ == '__main__':
    print('+'*100, use_attn)

    # ---------------------------------------------------------------------
    print("Existing model {0:s}".format("found" if os.path.exists(model_fil) else "not found!"))
    print("{0:s}".format("-" * 50))
    if os.path.exists(model_fil):
        if load_existing_model:
            print("loading model ...")
            serializers.load_npz(model_fil, model)
            print("finished loading: {0:s}".format(model_fil))
            print("{0:s}".format("-" * 50))
        else:
            print("""model file already exists!!
                Delete before continuing, or enable load_existing flag""".format(model_fil))

    _ = predict(p_filt=.6, r_filt=.6, plot=False)
    print("{0:s}".format("-" * 50))
