# -*- coding:utf-8 -*-
# ! usr/bin/env python3
"""
Created on 17/01/2024 13:25
@Author: yao
"""
import os


def main():



    base_path = f'/home/kyzhou/xzyao/RiceAlterome/textual_data/rice_scientific_data_1'
    src_file_list = [f'{base_path}/{file}' for file in os.listdir(base_path)]

    save_prefix = f'rice-alterome-include-rice'
    save_path = f'/home/kyzhou/xzyao/RiceAlterome/textual_data/blah_expr_dir'
    sent_save_file = f'{save_path}/{save_prefix}.1k-sent.txt'
    event_save_file = f'{save_path}/{save_prefix}.1k-event.txt'

    sent_num = 1000
    sent_count = 1

    saved_sent_set = set()

    ## 1. Only save the sent identified events.
    ## 2. Only save the sent that length less than 120.
    ## 3. Save two file. Pure sent file and event file.
    with open(sent_save_file, 'w') as wf_sent, open(event_save_file, 'w') as wf_event:
        for src_file in src_file_list:
            with open(src_file) as f:
                head = f.readline().strip().split('\t')

                pmid_idx = head.index('PMID')
                sent_idx = head.index('Sentence')
                include_idx = head.index('Include Event')
                event_idx = head.index('Events')

                for line in f:
                    l = line.strip().split('\t')

                    pmid = l[pmid_idx]
                    sent = l[sent_idx]

                    include_event = l[include_idx]
                    events = l[event_idx]

                    # one sent once
                    if sent in saved_sent_set:
                        continue
                    saved_sent_set.add(sent)

                    # fixme: include events.
                    if include_event != 'true':
                        continue

                    # fixme: length limitation is 120 tokens for sent.
                    if len(sent) > 200:
                        continue

                    # fixme: include Rice in sent
                    if not 'rice' in sent.lower() and not 'oryza' in sent.lower():
                        continue

                    wf_sent.write(f'sent-{sent_count}: {pmid} {sent}\n')

                    wf_event.write(f'sent-{sent_count}: {pmid} {sent}\n')
                    wf_event.write(f'{events}\n')
                    wf_event.write(f'\n')
                    sent_count += 1

                    if sent_count >= sent_num+1:
                        break
                if sent_count >= sent_num+1:
                    break
    print(f'{sent_count-1} sentences saved.')
    print(f'{sent_save_file} and {event_save_file} saved.')

if __name__ == '__main__':

    main()
