# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:00:17 2023

@author: hanly2
"""
import numpy as np
import pandas as pd
from predict_fun import predict_vulnerability_type, predict_attack_vector, predict_root_cause,\
    predict_impact
import random
from find_candidate import extract_key_aspect,ask_chatgpt
from translate_api import translate
from generate_prompt import get_reason, gengerate_answer_byReason
import spacy
nlp = spacy.load("en_core_web_lg")
knowledgeBase = np.load('知识库.npy', allow_pickle=True).item()
all_aspect = knowledgeBase['aspect']
data_des = knowledgeBase['des']
c = list(zip(all_aspect,data_des))              # 将a,b整体作为一个zip,每个元素一一对应后打乱
random.shuffle(c)               # 打乱c
all_aspect[:],data_des[:] = zip(*c)             # 将打乱的c解开
all_aspect_dic = []
s = 0

for i in all_aspect:
    temp = {'vulnerability description':data_des[s]}
    for j in i:
        temp[j[1]] = j[0]
    all_aspect_dic.append(temp)
    s += 1
d=ksk
#对缺陷类型进行补全
s = 0
vulnerability_ans = []
for i in range(len(all_aspect_dic)):
    try:
        temp = all_aspect_dic[i]
        if 'vulnerability_type' not in temp:
            res = predict_vulnerability_type(temp['vulnerability description'], temp)
            vulnerability_ans.append([temp, res])
            print("缺陷类型：",s)
            s += 1
    except Exception as e:
        print('=====')
        print('出错了hanlinyi')
        print(e)
        print('====')
        pass
with open('res_vulnerability.txt','w') as f:
    for i in vulnerability_ans:
        f.write(str(i))
        f.write('\n')
# =============================================================================
# with open('res_vulnerability.txt','r') as f:
#     ff = f.readlines()   
# ff = [eval(i) for i in ff]    
# =============================================================================

#对攻击方式进行补全
s = 0
attack_vector_ans = []
for i in range(len(all_aspect_dic)):
    try:
        temp = all_aspect_dic[i]
        if 'attack_vector' not in temp:
            res = predict_attack_vector(temp['vulnerability description'], temp)
            attack_vector_ans.append([temp, res])
            print("攻击方式：",s)
            s += 1 
    except Exception as e:
        print('=====')
        print('出错了hanlinyi')
        print(e)
        print('====')
        pass
    if s>1000:
        sa=sjsjshga
with open('res_attack_vector.txt','w') as f:
    for i in attack_vector_ans:
        f.write(str(i))
        f.write('\n')            
#对根本原因进行补全
s = 0
root_cause_ans = []
for i in range(len(all_aspect_dic)):
    try:
        temp = all_aspect_dic[i]
        if 'root_cause' not in temp:
            res = predict_root_cause(temp['vulnerability description'], temp)
            root_cause_ans.append([temp, res])
            print("根本原因：",s)
            s += 1 
    except Exception as e:
        print('=====')
        print('出错了hanlinyi')
        print(e)
        print('====')
        pass
    if s>600:
        sa=sjsjshga
with open('res_rootcause.txt','w') as f:
    for i in root_cause_ans:
        f.write(str(i))
        f.write('\n')        
#对影响进行补全
s = 0
impact_ans = []
for i in range(len(all_aspect_dic)):
    try:
        temp = all_aspect_dic[i]
        if 'impact' not in temp:
            res = predict_impact(temp['vulnerability description'], temp)
            impact_ans.append([temp, res])
            print("影响：",s)
            s += 1 
    except Exception as e:
        print('=====')
        print('出错了hanlinyi')
        print(e)
        print('====')
        pass
    if s>600:
        sa=sjsjshga       
with open('res_impact.txt','w') as f:
    for i in impact_ans:
        f.write(str(i))
        f.write('\n')  





# 使用陈鹏的数据进行实验

# 攻击方式
data = pd.read_excel(r'数据集2.0\删除攻击向量.xlsx')
target_sentences = data['new_sentence'].tolist()
target_labels = data['attacker_vector'].tolist()

answer_zhuguanti = []
answer_tiankongti = []
answer_jianchadaan = []
prompt_set = []
j = 0
s = 0
attack_vector_ans = []
while j < len(target_sentences):
# for j in range(len(target_sentences)):
    temp = extract_key_aspect(target_sentences[j])
    try:
        res = predict_attack_vector(target_sentences[j], temp)
        # attack_vector_ans.append([temp, res])
        record = []
        if res != {}:
            w = 0
            while w<5:
                
                answer = res['prompt_answer']
                answer_prompt = res['promopt']
                reason = get_reason(answer_prompt, answer)
                new_prompt = gengerate_answer_byReason('attack vector', reason, target_sentences[j])
                new_answer = ask_chatgpt(new_prompt)
                record.append([new_answer, answer])
                if nlp(new_answer).similarity(nlp(answer)) > 0.9:
                    break
                else:
                    res = predict_attack_vector(target_sentences[j], temp)
                w += 1
        print("检查次数：",w)
        if w == 5:
            attack_vector_ans.append([temp, {}, res, reason, new_answer, record])
        else:
            attack_vector_ans.append([temp, res])
        print("攻击方式：",s)
        s += 1 
    except Exception as e:
        print('=====')
        print('出错了hanlinyi')
        print(e)
        print('====')
        attack_vector_ans.append([{}, {}, {}, {}, {}, {}])
    j += 1

with open('res_attack_vector_new.txt','w') as f:
    for i in attack_vector_ans:
        f.write(str(i))
        f.write('\n')    


a = pd.DataFrame()
a['原始句子'] = data['description'].tolist()[:len(attack_vector_ans)]
a['原始句子_chn'] = [translate(i) for i in a['原始句子']]
a['修改句子'] = target_sentences[:len(attack_vector_ans)]
a['修改句子_chn'] = [translate(i) for i in a['修改句子']]
a['正确答案'] = [i[1]['final_answer'] if i[1] != {} else {} for i in attack_vector_ans]
a['错误答案'] = [i[1]['another_answer'] if i[1] != {} else {} for i in attack_vector_ans]
a['正确答案_chn'] = [translate(i) if i != {} else {} for i in a['正确答案']]
a['错误答案_chn'] = [translate(i) if i != {} else {} for i in a['错误答案']]
a['标准答案'] = target_labels
a['标准答案_chn'] = [translate(i) for i in target_labels]
a.to_excel(r'test_result_attack_vector11.xlsx',index=None)

# 根本原因
data = pd.read_excel(r'数据集2.0\删除root_cause.xlsx')
target_sentences = data['new_sentence'].tolist()
target_labels = data['root_cause'].tolist()

answer_zhuguanti = []
answer_tiankongti = []
answer_jianchadaan = []
prompt_set = []
j = 0
s = 0
root_cause_ans = []
while j < len(target_sentences):
# for j in range(len(target_sentences)):
    temp = extract_key_aspect(target_sentences[j])
    try:
        res = predict_root_cause(target_sentences[j], temp)
        root_cause_ans.append([temp, res])
        print("根本原因：",s)
        s += 1 
    except Exception as e:
        print('=====')
        print('出错了hanlinyi')
        print(e)
        print('====')
        pass
    j += 1

with open('res_root_cause_new.txt','w') as f:
    for i in root_cause_ans:
        f.write(str(i))
        f.write('\n')   
a = pd.DataFrame()
a['原始句子'] = data['description'].tolist()[:len(root_cause_ans)]
a['原始句子_chn'] = [translate(i) for i in a['原始句子']]
a['修改句子'] = target_sentences[:len(root_cause_ans)]
a['修改句子_chn'] = [translate(i) for i in a['修改句子']]
a['正确答案'] = [i[1]['final_answer'] if i[1] != {} else {} for i in root_cause_ans]
a['错误答案'] = [i[1]['another_answer'] if i[1] != {} else {} for i in root_cause_ans]
a['正确答案_chn'] = [translate(i) if i != {} else {} for i in a['正确答案']]
a['错误答案_chn'] = [translate(i) if i != {} else {} for i in a['错误答案']]
a['标准答案'] = target_labels
a['标准答案_chn'] = [translate(i) for i in target_labels]
a.to_excel(r'test_result_root_cause.xlsx',index=None)
# 影响
data = pd.read_excel(r'数据集2.0\删除impact.xlsx')
target_sentences = data['new_sentence'].tolist()
target_labels = data['impact'].tolist()

answer_zhuguanti = []
answer_tiankongti = []
answer_jianchadaan = []
prompt_set = []
j = 0
s = 0
impact_ans = []
while j < len(target_sentences):
# for j in range(len(target_sentences)):
    temp = extract_key_aspect(target_sentences[j])
    try:
        res = predict_impact(target_sentences[j], temp)
        impact_ans.append([temp, res])
        print("影响：",s)
        s += 1 
    except Exception as e:
        print('=====')
        print('出错了hanlinyi')
        print(e)
        print('====')
        pass
    j += 1

with open('res_impact_new.txt','w') as f:
    for i in impact_ans:
        f.write(str(i))
        f.write('\n')
a = pd.DataFrame()
a['原始句子'] = data['description'].tolist()[:len(impact_ans)]
a['原始句子_chn'] = [translate(i) for i in a['原始句子']]
a['修改句子'] = target_sentences[:len(impact_ans)]
a['修改句子_chn'] = [translate(i) for i in a['修改句子']]
a['正确答案'] = [i[1]['final_answer'] if i[1] != {} else {} for i in impact_ans]
a['错误答案'] = [i[1]['another_answer'] if i[1] != {} else {} for i in impact_ans]
a['正确答案_chn'] = [translate(i) if i != {} else {} for i in a['正确答案']]
a['错误答案_chn'] = [translate(i) if i != {} else {} for i in a['错误答案']]
a['标准答案'] = target_labels
a['标准答案_chn'] = [translate(i) for i in target_labels]
a.to_excel(r'test_result_impact.xlsx',index=None)



