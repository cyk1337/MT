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

@file: plot_graph.py

@time: 08/03/2018 19:41

@desc:         
               
'''              
import matplotlib.pyplot as plt
import os
import pandas as pd

# pp = []
# bleu = []
# val_loss=[]
# mean_loss=[]
data = {'pp':[],
        'bleu':[],
        'mean_loss':[] ,
        'val_loss':[]
        }
save_dir='plot_data'

def save_data(data, csv_name, subdir=False, save_dir=save_dir):
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
        hist.to_csv(csv_file)
        print('History is written into {}'.format(csv_file))
        print('-'*80)


def save_fig(plt, plot_filename, plot_dir='plot_data'):
    print("plot_dir:", plot_dir)
    if not os.path.exists(plot_dir):
        os.mkdir(plot_dir)
    filename = os.path.join(plot_dir, plot_filename)
    plt.savefig('{}'.format(filename))
    print('{} saved!'.format(filename))



def plot_all_history(subdir, plot_filename='default.pdf', figsize=(16, 9)):
    subdir = os.path.join(save_dir, subdir)
    assert os.path.isdir(subdir) == True, "Error: {} does not exists!".format(subdir)

    # sum_plot = os.path.join(save_dir, 'plot_all')
    sum_plot = subdir
    if not os.path.isdir(sum_plot):
        os.mkdir(sum_plot)

    # set color list
    # colors = [c for c in list(matplotlib.colors.cnames.keys()) if not c.startswith('light')]
    colors = ['green','red','blue','goldenrod','black','lime','cyan','chartreuse','yellow','m','purple','olive','salmon','darkred','pink']
    markers = ['d', '^', 's', '*']
    fontsize = 10
    plt.figure(figsize=figsize)

    plt.subplot(121)
    for i, filename in enumerate(os.listdir(subdir)):
        if filename[-4:] != '.csv': continue
        csv_file = os.path.join(subdir, filename)
        data = pd.read_csv(csv_file)
        line_label = filename[:-4]
        pp = data['pp']
        epochs = range(1, len(pp) + 1)
        # plot pp
        # plt.plot(epochs, acc, color=colors[i%len(colors)], linestyle='-', label='{} training acc'.format(line_label))
        plt.plot(epochs, pp, color=colors[i % len(colors)], marker=markers[i % len(markers)], linestyle='-',
                 label='{}'.format(line_label))
        plt.title('Perplexity', fontsize=fontsize)
    plt.xlabel('Epochs')
    plt.ylabel('Perplexity')
    plt.legend()
    plt.grid()

    plt.subplot(122)
    for i, filename in enumerate(os.listdir(subdir)):
        if filename[-4:] != '.csv': continue
        csv_file = os.path.join(subdir, filename)
        data = pd.read_csv(csv_file)
        line_label = filename[:-4]
        bleu = data['bleu']
        epochs = range(1, len(bleu) + 1)
        # plot bleu
        # plt.plot(epochs, acc, color=colors[i%len(colors)], linestyle='-', label='{} training acc'.format(line_label))
        plt.plot(epochs, bleu, color=colors[i % len(colors)], marker=markers[i % len(markers)], linestyle='-.',
                 label='{}'.format(line_label))
        plt.title('BLEU', fontsize=fontsize)
    plt.xlabel('Epochs')
    plt.ylabel('BLEU')
    plt.legend()
    plt.grid()

    # # plot
    # plt.subplot(223)
    # for i, filename in enumerate(os.listdir(subdir)):
    #     if filename[-4:] != '.csv': continue
    #     csv_file = os.path.join(subdir, filename)
    #     data = pd.read_csv(csv_file)
    #     line_label = filename[:-4]
    #     mean_loss = data['mean_loss']
    #     epochs = range(1, len(mean_loss) + 1)
    #     # plot acc
    #     # plt.plot(epochs, acc, color=colors[i%len(colors)], linestyle='-', label='{} training acc'.format(line_label))
    #     plt.plot(epochs, mean_loss, color=colors[i % len(colors)], marker=markers[i % len(markers)], linestyle='dashed', label='{}'.format(line_label))
    #     plt.title('Mean Loss', fontsize=fontsize)
    # plt.xlabel('Epochs')
    # plt.ylabel('Mean loss')
    # plt.legend()
    # plt.grid()
    #
    # # ==================================
    # plt.subplot(224)
    # for i, filename in enumerate(os.listdir(subdir)):
    #     if filename[-4:] != '.csv': continue
    #     line_label = filename[:-4]
    #     csv_file = os.path.join(subdir, filename)
    #     data = pd.read_csv(csv_file)
    #     # plot val and acc loss
    #     val_loss = data['val_loss']
    #     epochs = range(1, len(val_loss) + 1)
    #
    #     plt.plot(epochs, val_loss, color=colors[i%len(colors)], marker=markers[i % len(markers)], linestyle='dashed', label='{}'.format(line_label))
    # plt.title('Validation loss', fontsize=fontsize)
    # plt.xlabel('Epochs')
    # plt.ylabel('Val Loss')
    #     # plt.grid()
    # plt.legend()
    # plt.grid()
    # =============================






    save_fig(plt, plot_filename=plot_filename, plot_dir=sum_plot)
    print("{} saved!".format(plot_filename))
    print('-'*80)

    plt.show()

if __name__=='__main__':
    subdir = '1-1'
    # subdir = '2-3'
    plot_filename = '{}.pdf'.format(subdir)
    plot_all_history(subdir=subdir, plot_filename=plot_filename, figsize=(14, 5))