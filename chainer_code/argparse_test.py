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

@file: argparse_test.py

@time: 17/02/2018 11:03

@desc:         
               
'''              
import argparse

parser = argparse.ArgumentParser(description='Process some int..')
parser.add_argument('integers', metavar='N', type=int, nargs='+', default=1, help='an int for accmulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum test..')

args = parser.parse_args()
print(dir(args))
print('integers', args.integers)
print('accumulate', args.accumulate)
print(args.accumulate(args.integers))