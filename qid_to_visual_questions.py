#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


import os
import json
from tqdm import tqdm
from textwrap import fill


with open('v2_mscoco_val2014_annotations.json') as file:
    val_annotations = json.load(file)

val_qid2label = pd.read_csv('val_qid_label.csv', index_col='qid')

def qid2imgfile(qid, path_to_val2014='./val2014'):
    return os.path.join(path_to_val2014, 'COCO_val2014_{0:012d}.jpg'.format(qid))

with open('v2_OpenEnded_mscoco_val2014_questions.json') as file:
    questions = json.load(file)

qdf = json_normalize(questions, 'questions')

qdf.set_index('question_id', inplace=True)

val_all = pd.read_csv('val_all.csv', index_col='qid')




ans_cols = [
    'i_answer',
    'q_answer',
    'iq_answer',
    'butd_answer',
    'mfb_answer',
    'mfh_answer',
    'ban_4_answer',
    'ban_8_answer',
    'mcan_small_answer',
    'mcan_large_answer',
    'pythia_v3_answer',
]


ent_cols = [
    'i_entropy',
    'q_entropy',
    'iq_entropy',
    'butd_entropy',
    'mfb_entropy',
    'mfh_entropy',
    'ban_4_entropy',
    'ban_8_entropy',
    'mcan_small_entropy',
    'mcan_large_entropy',
    'pythia_v3_entropy'
]


reason_cols = [
    'DFF', 'AMB', 'SYN', 'GRN'
]

method_names = ['I', 
                'Q', 
                'Q+I', 
                'BUTD', 
                'MFB', 
                'MFH', 
                'BAN4', 
                'BAN8', 
                'MCAN-small', 
                'MCAN-large', 
                'Pythia v0.3']



def reason2str(r):
    s = ''
    for i,v in zip(r.index, r.values):
        s += '{0}: {1:.4f}'.format(i, v) + '\n'
    return s.strip()


def a2str(a):
    s = ''
    for i,v in zip(a.index, a.values):
        s += '%s x %d' % (i, v) + '\n'
    return s

def ae2str(ae):
    s = ''
    for row in ae.itertuples():
        s += '{0}: {1} ({2:.4f})'.format(row.Index, row.answer, row.entropy) + '\n'
    return s.strip()

ans_type_dic = {'yes/no': 'yn', 'number': 'n', 'other': 'o'}



for a in tqdm(val_annotations['annotations'][:100]):
# for a in tqdm(val_annotations['annotations'][:]):

    qid = a['question_id']

    cluster_no = val_qid2label.loc[qid].label

    if cluster_no >= 0:
        
        # predicted answers and entropy
        aedf = pd.DataFrame( {'answer':val_all.loc[qid][ans_cols].values, 
                              'entropy':val_all.loc[qid][ent_cols].values },
                             index=method_names)
        a_text_methods = ae2str(aedf)

        # reasons
        r_text = reason2str(val_all.loc[qid][reason_cols])

        # question
        q_text = fill(qdf.loc[qid].question, width=30)

        # GT answers
        adf = json_normalize(a, 'answers')
        a_text = a2str(adf.answer.value_counts())

        # image
        img_file = qid2imgfile(a['image_id'])
        img = plt.imread(img_file)

        fig = plt.figure(figsize=(3,3))
        plt.imshow(img)
        plt.axis('off')

        plt.title('Q: ' + q_text + '\n' + a_text + '\n' + a_text_methods + '\n' + r_text,
                  loc='left', fontsize=9)

        pdf_file = os.path.join('val_clusters', 
                                str(cluster_no), 
                                ans_type_dic[a['answer_type']],
                                '{}.pdf'.format(qid))

        # print(os.path.dirname(pdf_file))
        os.makedirs(os.path.dirname(pdf_file), exist_ok=True)
        
        plt.savefig(pdf_file, bbox_inches='tight', dpi=150)
        plt.clf();
        plt.close();
        # plt.show()
