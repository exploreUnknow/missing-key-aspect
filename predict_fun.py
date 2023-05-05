# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:11:51 2023

@author: hanly2
"""
from find_candidate import condidate_v2, add_knowledge, ask_chatgpt
import numpy as np
import time
from generate_prompt import vulnerability_gengerate_zhuguanti,vulnerability_gengerate_tiankongti,\
    vulnerability_gengerate_jianchadaan, attack_vector_gengerate_zhuguanti,\
    attack_vector_gengerate_tiankongti, attack_vector_gengerate_jianchadaan,\
        root_cause_gengerate_zhuguanti, root_cause_gengerate_tiankongti,\
            root_cause_gengerate_jianchadaan, impact_gengerate_zhuguanti,\
                impact_gengerate_tiankongti, impact_gengerate_jianchadaan
                
import spacy
nlp = spacy.load("en_core_web_lg")
knowledgeBase = np.load('知识库.npy', allow_pickle=True).item()
all_aspect = knowledgeBase['aspect']
data_des = knowledgeBase['des']
all_aspect_dic = []
s = 0

for i in all_aspect:
    temp = {'vulnerability description':data_des[s]}
    for j in i:
        temp[j[1]] = j[0]
    all_aspect_dic.append(temp)
    s += 1
def predict_vulnerability_type(sentence, key_aspect):
    condidate_sentences = condidate_v2(sentence, data_des, all_aspect, 'affected_product','vulnerability_type')
    cve_example_similary = []
    cve_example = sentence
    for i in range(len(all_aspect_dic)):
        if 'affected_product' in all_aspect_dic[i]:
            product = all_aspect_dic[i]['affected_product']
            
            if product in cve_example:
                cve_example_similary.append(all_aspect_dic[i])



    if type(condidate_sentences)==dict:
        return {}

    try:
        time.sleep(1)
        condidate_sentences_knowledge = add_knowledge(condidate_sentences)
        
        lack = key_aspect
        
        prompt_zhuguanti = vulnerability_gengerate_zhuguanti(condidate_sentences, lack)
        prompt_tiankongti = vulnerability_gengerate_tiankongti(condidate_sentences, lack)
        answerA = ask_chatgpt(prompt_zhuguanti)
        answerB = ask_chatgpt(prompt_tiankongti)
        prompt_jianchadaan = vulnerability_gengerate_jianchadaan(condidate_sentences, lack,
                                                                 [answerA, answerB])
        answerC = ask_chatgpt(prompt_jianchadaan)
        nlp_A = nlp(answerA)
        nlp_B = nlp(answerB)
        nlp_C = nlp(answerC)
        if nlp_C.similarity(nlp_A) > nlp_C.similarity(nlp_B):
            return {"final_answer":answerC, "promopt":prompt_zhuguanti, "prompt_answer":answerA, 
                    "another_answer":answerB}
        else:
            return {"final_answer":answerC, "promopt":prompt_tiankongti, "prompt_answer":answerB, 
                    "another_answer":answerA}
    except Exception as e:
        print('============')
        print('请注意：出错了')
        print(e)
        time.sleep(60)
        return {}

def predict_attack_vector(sentence, key_aspect):
    condidate_sentences = condidate_v2(sentence, data_des, all_aspect, 'affected_product','attack_vector')
    cve_example_similary = []
    cve_example = sentence
    for i in range(len(all_aspect_dic)):
        if 'affected_product' in all_aspect_dic[i]:
            product = all_aspect_dic[i]['affected_product']
            
            if product in cve_example:
                cve_example_similary.append(all_aspect_dic[i])



    if type(condidate_sentences)==dict:
        return {}

    try:
        time.sleep(1)
        condidate_sentences_knowledge = add_knowledge(condidate_sentences)
        
        lack = key_aspect
        
        prompt_zhuguanti = attack_vector_gengerate_zhuguanti(condidate_sentences, lack)
        prompt_tiankongti = attack_vector_gengerate_tiankongti(condidate_sentences, lack)
        answerA = ask_chatgpt(prompt_zhuguanti)
        answerB = ask_chatgpt(prompt_tiankongti)
        prompt_jianchadaan = attack_vector_gengerate_jianchadaan(condidate_sentences, lack,
                                                                 [answerA, answerB])
        answerC = ask_chatgpt(prompt_jianchadaan)
        nlp_A = nlp(answerA)
        nlp_B = nlp(answerB)
        nlp_C = nlp(answerC)
        if nlp_C.similarity(nlp_A) > nlp_C.similarity(nlp_B):
            return {"final_answer":answerC, "promopt":prompt_zhuguanti, "prompt_answer":answerA, 
                    "another_answer":answerB}
        else:
            return {"final_answer":answerC, "promopt":prompt_tiankongti, "prompt_answer":answerB, 
                    "another_answer":answerA}
    except Exception as e:
        print('============')
        print('请注意：出错了')
        print(e)
        time.sleep(60)
        return {}

def predict_root_cause(sentence, key_aspect):
    condidate_sentences = condidate_v2(sentence, data_des, all_aspect, 'affected_product','root_cause')
    cve_example_similary = []
    cve_example = sentence
    for i in range(len(all_aspect_dic)):
        if 'affected_product' in all_aspect_dic[i]:
            product = all_aspect_dic[i]['affected_product']
            
            if product in cve_example:
                cve_example_similary.append(all_aspect_dic[i])



    if type(condidate_sentences)==dict:
        return {}

    try:
        time.sleep(1)
        condidate_sentences_knowledge = add_knowledge(condidate_sentences)
        
        lack = key_aspect
        
        prompt_zhuguanti = root_cause_gengerate_zhuguanti(condidate_sentences, lack)
        prompt_tiankongti = root_cause_gengerate_tiankongti(condidate_sentences, lack)
        answerA = ask_chatgpt(prompt_zhuguanti)
        answerB = ask_chatgpt(prompt_tiankongti)
        prompt_jianchadaan = root_cause_gengerate_jianchadaan(condidate_sentences, lack,
                                                                 [answerA, answerB])
        answerC = ask_chatgpt(prompt_jianchadaan)
        nlp_A = nlp(answerA)
        nlp_B = nlp(answerB)
        nlp_C = nlp(answerC)
        if nlp_C.similarity(nlp_A) > nlp_C.similarity(nlp_B):
            return {"final_answer":answerC, "promopt":prompt_zhuguanti, "prompt_answer":answerA, 
                    "another_answer":answerB}
        else:
            return {"final_answer":answerC, "promopt":prompt_tiankongti, "prompt_answer":answerB, 
                    "another_answer":answerA}
    except Exception as e:
        print('============')
        print('请注意：出错了')
        print(e)
        time.sleep(60)
        return {}

def predict_impact(sentence, key_aspect):
    condidate_sentences = condidate_v2(sentence, data_des, all_aspect, 'affected_product','impact')
    cve_example_similary = []
    cve_example = sentence
    for i in range(len(all_aspect_dic)):
        if 'affected_product' in all_aspect_dic[i]:
            product = all_aspect_dic[i]['affected_product']
            
            if product in cve_example:
                cve_example_similary.append(all_aspect_dic[i])



    if type(condidate_sentences)==dict:
        return {}

    try:
        time.sleep(1)
        condidate_sentences_knowledge = add_knowledge(condidate_sentences)
        
        lack = key_aspect
        
        prompt_zhuguanti = impact_gengerate_zhuguanti(condidate_sentences, lack)
        prompt_tiankongti = impact_gengerate_tiankongti(condidate_sentences, lack)
        answerA = ask_chatgpt(prompt_zhuguanti)
        answerB = ask_chatgpt(prompt_tiankongti)
        prompt_jianchadaan = impact_gengerate_jianchadaan(condidate_sentences, lack,
                                                                 [answerA, answerB])
        answerC = ask_chatgpt(prompt_jianchadaan)
        nlp_A = nlp(answerA)
        nlp_B = nlp(answerB)
        nlp_C = nlp(answerC)
        if nlp_C.similarity(nlp_A) > nlp_C.similarity(nlp_B):
            return {"final_answer":answerC, "promopt":prompt_zhuguanti, "prompt_answer":answerA, 
                    "another_answer":answerB}
        else:
            return {"final_answer":answerC, "promopt":prompt_tiankongti, "prompt_answer":answerB, 
                    "another_answer":answerA}
    except Exception as e:
        print('============')
        print('请注意：出错了')
        print(e)
        time.sleep(60)
        return {}





