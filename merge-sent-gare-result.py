# -*- coding:utf-8 -*-
# ! usr/bin/env python3
"""
Created on 13/02/2024 14:13
@Author: yao
"""

"""
该代码用于合并chatgpt生成结果和原始的sent文件
因为有些他没给句子表上去
"""

def read_sent_file(sent_file: str):

    sent_id_to_sent = {}
    with open(sent_file) as f:
        for line in f:
            l = line.strip().split(' ')
            sent_id = l[0]
            sent = ' '.join(l[1:])

            sent_id_to_sent[sent_id] = sent
    print(f'{len(sent_id_to_sent):,} sentences.')
    return sent_id_to_sent

def file_merge(sent_id_to_sent: dict,
               gare_file: str,
               save_file: str):

    with open(gare_file) as f, open(save_file, 'w') as wf:
        for line in f:
            if not line.startswith('sent-'):
                wf.write(line)
                continue

            sent_id = line.strip().split(' ')[0]

            wf.write(f'{sent_id} {sent_id_to_sent[sent_id]}\n')

    print(f'{save_file} saved.')


def main():
    base_path = '/Users/yao/Nutstore Files/Mac2PC/BLAH8/会议相关工作/RiceAlterome-LLM'
    sent_file = f'{base_path}/blah_expr_dir/rice-alterome.1k-sent.txt'

    save_path = f'/Users/yao/Nutstore Files/Mac2PC/BLAH8/会议相关工作/RiceAlterome-LLM/chat-gpt-result'
    gare_file = f'{save_path}/rice-alterome-1000.gpt-3.5.2024-01-19 12:45:56.txt'

    save_file = f'{save_path}/rice-alterome-gpt.1k.tsv'

    sent_id_to_sent = read_sent_file(sent_file)

    file_merge(sent_id_to_sent, gare_file, save_file)



if __name__ == '__main__':
    main()


