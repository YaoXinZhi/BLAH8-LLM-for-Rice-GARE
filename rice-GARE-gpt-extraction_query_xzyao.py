# -*- coding:utf-8 -*-
# ! usr/bin/env python3
"""
Created on 08/01/2024 20:04
@Author: yao
"""

import json
from openai import OpenAI
import json
import time

from datetime import datetime
import time

# 打印当前时间
# print("当前时间：", formatted_time)


def read_target_sent(sent_file: str, sent_num: int):

    sent_list = []
    with open(sent_file) as f:
        for line in f:
            # if len(line.strip().split()) < 10:
            #     continue

            sent_list.append(line.strip())

            if len(sent_list) >= sent_num:
                break
    print(f'{len(sent_list):,} sentences loaded.')
    return sent_list

def main():
    # 官网说明 https://platform.openai.com/docs/api-reference/streaming
    # openai api 使用参考 https://zhuanlan.zhihu.com/p/656959227

    # 1-8 blah-8 xzyao api
    api_key = '***'
    # model = "gpt-3.5-turbo"
    model = 'gpt-4'

    target_sent_num = 70
    batch_size = 10

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print(f'---------model: {model}---------')
    # prompt_file = f'./prompt设计/Prompt-任务放前面-only-name.txt'
    base_path = '/Users/yao/Nutstore Files/Mac2PC/BLAH8/会议相关工作/RiceAlterome-LLM'
    prompt_file = f'{base_path}/prompt设计/base-prompt.v4.2.template.txt'
    prompt_text = open(prompt_file).read().strip()

    # sent_file = f'{base_path}/real-data/cancer-alterome.50-test-set.txt'
    # sent_file = f'{base_path}/blah_expr_dir/rice-alterome.1k-sent.txt'
    sent_file = f'{base_path}/blah_expr_dir/rice.70-sent.txt'
    sent_list = read_target_sent(sent_file, target_sent_num)
    sent_num = len(sent_list)

    save_prefix = f'rice-alterome-{sent_num}.{model}'
    save_path = f'{base_path}/chat-gpt-result'
    save_file = f'{save_path}/{save_prefix}.{formatted_time}.txt'

    client = OpenAI(
        api_key=api_key
    )

    if sent_num % batch_size != 0:
        raise ValueError(f'{sent_num}%{batch_size} != 0')

    total_prompt_length = 0
    total_generate_length = 0
    start_index = 0
    start_time = time.time()
    wf = open(save_file, 'w')
    while start_index < sent_num:
        print(f'requesting {start_index} -- {start_index+batch_size} sentences.....')

        batch_sent = sent_list[ start_index: start_index + batch_size ]

        sent_str = '\n'.join(batch_sent)

        new_prompt = prompt_text.replace('<<target_sent_replace_here>>', sent_str)
        start_index += batch_size

        stream = client.chat.completions.create(
            model=model,
            messages=[ {
                "role": "user",
                "content": new_prompt,
            } ],
            # from 0 to 1
            temperature=0,
            # max_tokens=1,
            # only one response
            n=1
        )

        result = stream.choices[ 0 ].message.content

        wf.write(f'{str(result)}\n\n')

        total_prompt_length += len(prompt_text)
        total_generate_length += len(str(result))


    wf.close()
    print(f'{save_file} saved.')
    end_time = time.time()
    print(f'total prompt: {total_prompt_length:,} tokens.')
    print(f'total generate: {total_generate_length:,} tokens.')
    print(f'total tokens: {total_prompt_length + total_generate_length:,} tokens.')
    print(f'time cost: {end_time-start_time:.4f}s.')

if __name__ == '__main__':
    main()
