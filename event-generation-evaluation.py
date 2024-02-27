# -*- coding:utf-8 -*-
# ! usr/bin/env python3
"""
Created on 18/01/2024 15:24
@Author: yao
"""

# import os
# import re
# from icecream import ic

from collections import defaultdict

def read_gold_file(gold_file: str, sent_num: int):

    true_sent_id_set = set()
    sent_to_events = defaultdict(list)

    sent_id = ''
    sent_idx = 0
    with open(gold_file) as f:
        for line in f:
            if line.startswith('sent-'):
                if sent_idx >= sent_num:
                    break
                sent_id = line.strip().split(':')[0]
                true_sent_id_set.add(sent_id)

                sent_idx += 1

            elif line.startswith('chain-') or line.startswith('event-'):
                event = line.strip().split(':')[1].strip()
                sent_to_events[sent_id].append(event)
    print(f'{len(true_sent_id_set):,} in gold-dataset.')
    return true_sent_id_set, sent_to_events

def read_pred_file(pred_file: str, sent_num: int):

    pred_sent_id_set = set()
    pred_sent_to_event = defaultdict(list)

    sent_id = ''
    sent_idx = 0
    with open(pred_file) as f:
        for line in f:
            if line.startswith('sent-'):

                if sent_idx >= sent_num:
                    break

                sent_id = line.strip().split(':')[ 0 ]
                pred_sent_id_set.add(sent_id)
                sent_idx += 1
            elif line.startswith('event-'):
                event = line.strip().split(':')[ 1 ].strip()
                # fixme: the element number of event must be 4.
                if len(event.split(' -- ')) != 4:
                    continue

                pred_sent_to_event[ sent_id ].append(event)

    print(f'{len(pred_sent_id_set):,} sent in pred sent.')
    return pred_sent_id_set, pred_sent_to_event

def loss_metrics(gold_to_events,
                 pred_sent_id_set, pred_to_events):
    """
    tp 黄金数据集有的，预测也有的 （匹配上）
    fp 黄金数据集没有的，预测有的 （没匹配上的）
    tn 黄金数据集没有的，预测也没有的 （可能只能加上那些没有链条的文件）

    fn 黄金数据集有的，预测没有的 （没匹配上）

    在loss情况下 只有有overlap就算正确
    """

    tp = 0
    fn = 0
    fp = 0
    tn = 0
    for pred_sent_id in pred_sent_id_set:
        pred_events = pred_to_events[pred_sent_id]
        gold_events = gold_to_events[pred_sent_id]

        if len(gold_events) == 0 and len(pred_events) == 0:
            tn += 1

        # gold没有，pred有
        if len(gold_events) == 0 and len(pred_events) !=0:
            # fixme: compute for sentence or for event?
            # now we evaluate base on single event.
            # fp += 1
            # print('FP')
            # print(gold_events)
            # print(pred_events)
            # input()

            fp += len(pred_events)

        # gold有，pred没有 fn
        for gold_event in gold_events:
            included_in_pred = False
            for pred_event in pred_events:
                eq_bool = loose_event_eq(pred_event, gold_event)
                if eq_bool:
                    included_in_pred = True
                    break
            if included_in_pred:
                fn += 1

                # print(f'FN')
                # print(gold_events)
                # print(pred_events)
                # input()



        ## pred有，gold有
        for pred_event in pred_events:
            included_in_gold = False
            ## 判断是否 included in gold
            for gold_event in gold_events:
                eq_bool = loose_event_eq(pred_event, gold_event)

                if eq_bool:
                    included_in_gold = True
                    break

            if included_in_gold:
                tp += 1
            else:
                # sent= sent_id_to_sent[pred_sent_id]
                pass
                # ic(included_in_gold)
                # ic(pred_sent_id)
                # ic(sent)
                # ic(gold_events)
                # ic(pred_events)
                # ic(gold_event)
                # ic(pred_event)
                # input()
    print(f'tp: {tp}, tn: {tn}')
    print(f'fp: {fp}, fn: {fn}')

    # exit()
    precision = tp / (tp + fp)

    recall = tp / (tp + fn)

    f1 = 2 * precision * recall / (precision + recall)

    acc = (tp + tn) / (tp + tn + fp + fn)

    print(f'accuracy: {acc:.4f}')
    print(f'precision: {precision:.4f}, recall: {recall:.4f}, f1: {f1:.4f}')


def loose_event_eq(pred_event, gold_event):

    pred_list = pred_event.split(' -- ')
    gold_list = gold_event.split(' -- ')

    if len(pred_list) != 4:
        return False

    if len(gold_list) != 4:
        raise ValueError(f'gold event len: {len(gold_list)}')

    for idx in range(4):

        pred_ele = pred_list[idx]
        gold_ele = gold_list[idx]

        # fixme: 对 trigger word做特殊处理
        if '(' in pred_ele:
            pred_ele = pred_ele.split('(')[0].strip()
        if '(' in gold_ele:
            gold_ele = gold_ele.split('(')[0].strip()

        pred_ele = pred_ele.lower().strip()
        gold_ele = gold_ele.lower().strip()

        # pred_words_set = set(pred_ele.split())
        # gold_words_set = set(gold_ele.split())

        # 检查两个集合是否有交集
        # overlap = pred_words_set.intersection(gold_words_set)

        # fixme:
        if pred_ele in gold_ele or gold_ele in pred_ele:
        # if len(overlap) > 0:
            pass
        else:
            # ic(gold_event)
            # ic(pred_event)
            #
            # ic(pred_ele)
            # ic(gold_ele)
            # input()

            return False
    return True

def read_sent_file(sent_file: str):
    sent_id_to_sent = {}
    with open(sent_file) as f:
        for line in f:
            sent_id = line.strip().split(':')[0].strip()
            sent = ':'.join(line.strip().split(':')[1:]).strip()

            sent_id_to_sent[sent_id] = sent
    print(f'{len(sent_id_to_sent):,} sentences loaded.')
    return  sent_id_to_sent


def main():
    gold_file = f'./real-data/rice.gold-70-sent.txt'

    # sent_file = f'./real-data/cancer-alterome.1k-sent.txt'

    # sent_id_to_sent = read_sent_file(sent_file)

    # GPT-3.5, GPT-4.0, pipeline
    # model = 'GPT-3.5'
    model = 'GPT-4.0'

    print(f'----------eval model: {model}---------')

    if model == 'GPT-3.5':
        # gpt-3.5 result
        pred_file = f'./chat-gpt-result/rice-alterome-70.gpt-3.5.2024-02-13 21:34:20.txt'
    elif model == 'GPT-4.0':
        # gpt-4 result
        pred_file = f'./chat-gpt-result/rice-alterome-70.gpt-4.2024-02-13 21:38:30.txt'
    else:
        raise ValueError(f'wrong model: {model}')

    print(f'---model: {model}----')

    sent_num = 35

    true_sent_id_set, gold_to_events = read_gold_file(gold_file, sent_num)
    pred_sent_id_set, pred_to_events = read_pred_file(pred_file, sent_num)

    loss_metrics(gold_to_events, pred_sent_id_set, pred_to_events)




if __name__ == '__main__':
    main()


