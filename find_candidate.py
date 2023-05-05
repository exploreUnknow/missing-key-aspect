# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:53:55 2023

@author: hanly2
"""
import numpy as np
import spacy
import os
import openai
from guohan_extarct import guohao_extract
openai.api_key = ""

def euclideanDist(A, B):
    return np.sqrt(sum((A - B) ** 2))
def RandomCenters(dataSet, k):
    n = dataSet.shape[0]
    centerIndex = np.random.choice(range(n), size=k, replace=False)
    centers = dataSet[centerIndex]
    return centers
def KMeans(dataSet, k):
    Centers = RandomCenters(dataSet, k)
    n, m = dataSet.shape
    DistMatrix = np.zeros((n, 2))  #n*2的矩阵用于存储 类簇索引
    centerChanged = True
    while centerChanged == True:
        centerChanged = False
        for i in range(n):
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                dist = euclideanDist(dataSet[i, :], Centers[j, :])
                if dist < minDist:    #获取每个样本聚类最近的聚类中心点及其聚类
                    minDist = dist
                    minIndex = j
            if DistMatrix[i, 0] != minIndex:
                centerChanged = True
            DistMatrix[i, 0] = minIndex   #存储的是索引
            DistMatrix[i, 1] = minDist    #存储的是距离
        if centerChanged == True:  # 如何聚类中心有变化，那么接下来就要更新聚类中心
            for i in range(k):
                dataMean = dataSet[DistMatrix[:, 0] == i]  # dataMean中是相同类簇的样本
                Centers[i] = np.mean(dataMean, axis=0)
    return Centers, DistMatrix
 
def PointSelection(DistMatrix,k,n):
    points = []
    for i in range(k):
        minDist = np.inf
        closeIndex = -1
        for j in range(n):
            if DistMatrix[j,0] == i:
                if DistMatrix[j,1] < minDist:
                    minDist = DistMatrix[j,1]
                    closeIndex = j
        points.append(closeIndex)
    return points
def condidate(sentence, data_des, all_aspect, target_key_aspect):
        scout = 0
        cve_example = sentence
        number = {}
        des_aspect = {}
        for i in range(len(all_aspect)):
            n = 0
            temp = [j[0] for j in all_aspect[i]]
            for j in temp:
                if j in cve_example:
                    n += 1
            number[data_des[i]] = n
            des_aspect[data_des[i]] = all_aspect[i]
        
        cve_example_similary = []
        max_number = max(number.values())
        for i in number:
            if number[i] >= max_number-1:
                # if 'vulnerability_type' in [d[1] for d in des_aspect[i]]:
                if target_key_aspect in [d[1] for d in des_aspect[i]]:    
                    cve_example_similary.append([i,des_aspect[i]])
                   
        c = 0
        temp_c = []
        # print('===========')
        # print(len(cve_example_similary))
        while len(cve_example_similary) < 10 or len(cve_example_similary) >3000:
            
            # print(len(cve_example_similary))
            temp_c.append(len(cve_example_similary))
            if c > max_number:
                scout = 1
                # print('这个cve找不到相似的')
                # print(cve_example)
                break
            else:
                cve_example_similary = []
                max_number = max(number.values())
                for i in number:
                    if number[i] >= max_number-c:
                        # if 'vulnerability_type' in [d[1] for d in des_aspect[i]]:
                        if target_key_aspect in [d[1] for d in des_aspect[i]]:    
                            cve_example_similary.append([i,des_aspect[i]])
    
                c += 1
        if scout == 1:

       
            return {"resCode": "1", "message": "success","data":'找不到跟它相似的，跳过'}
        #先把cve转化为字典，方便查看
        cve_example_similary_dic = []
        for i in cve_example_similary:
            temp = {}
            for j in i[1]:
                temp[j[1]] = j[0]
            cve_example_similary_dic.append([i[0],temp])

        data = [i[0] for i in cve_example_similary_dic]
        nlp = spacy.load("en_core_web_lg")
        emb_data = [nlp(i).vector for i in data]

        
        X = emb_data
        n = len(X)
        k = 10
        Center, DistMat = KMeans(np.array(emb_data), k)
        Points = PointSelection(DistMat,k,n)
        sentences = [cve_example_similary_dic[i] for i in Points]
        return sentences
    
    
def condidate_v1(sentence, all_aspect_dic):

        cve_example = sentence

        cve_example_similary = []
        for i in range(len(all_aspect_dic)):
            if 'affected_product' in all_aspect_dic[i] and 'vulnerability_type' in all_aspect_dic[i]:
                product = all_aspect_dic[i]['affected_product']
                vulnerability_type = all_aspect_dic[i]['vulnerability_type']
                if product in cve_example and vulnerability_type in cve_example:
                    cve_example_similary.append(all_aspect_dic[i])
        return cve_example_similary
product_names = []
with open('CPE_DICT_PRODUCT.txt', 'r') as f:
    for i in f.readlines():
        product_names.append(i.replace('\n',''))    
def condidate_v2(sentence, data_des, all_aspect, target_key_aspect, target_key_aspect1):
    if target_key_aspect == 'affected_product':
        cve_example = sentence.lower()
        match_name = ''
        for name in product_names:
            if name in cve_example and len(name) > len(match_name):
                match_name = name

        des_aspect = {}
        cve_example_similary = []
        for i in range(len(all_aspect)):
            for j in all_aspect[i]:
                if j[1] == 'affected_product':

                    if j[0].lower() in match_name and target_key_aspect1 in [a[1] for a in all_aspect[i]]:
                        cve_example_similary.append([data_des[i], all_aspect[i]])
           
        if len(cve_example_similary) == 0:
            return {"resCode": "1", "message": "success","data":'找不到跟它相似的，跳过'}
        else:

            #先把cve转化为字典，方便查看
            cve_example_similary_dic = []
            for i in cve_example_similary:
                temp = {}
                for j in i[1]:
                    temp[j[1]] = j[0]
                cve_example_similary_dic.append([i[0],temp])
            if len(cve_example_similary) <= 10:
                return  cve_example_similary_dic
            else:
                data = [i[0] for i in cve_example_similary_dic]
                nlp = spacy.load("en_core_web_lg")
                emb_data = [nlp(i).vector for i in data]

                
                X = emb_data
                n = len(X)
                k = 10
                Center, DistMat = KMeans(np.array(emb_data), k)
                Points = PointSelection(DistMat,k,n)
                sentences = [cve_example_similary_dic[i] for i in Points]
                return sentences
    else:
        scout = 0
        cve_example = sentence
        number = {}
        des_aspect = {}
        for i in range(len(all_aspect)):
            n = 0
            temp = [j[0] for j in all_aspect[i]]
            for j in temp:
                if j in cve_example:
                    n += 1
            number[data_des[i]] = n
            des_aspect[data_des[i]] = all_aspect[i]
        
        cve_example_similary = []
        max_number = max(number.values())
        for i in number:
            if number[i] >= max_number-1:
                # if 'vulnerability_type' in [d[1] for d in des_aspect[i]]:
                if target_key_aspect in [d[1] for d in des_aspect[i]]:    
                    cve_example_similary.append([i,des_aspect[i]])
                   
        c = 0
        temp_c = []
        # print('===========')
        # print(len(cve_example_similary))
        while len(cve_example_similary) < 10 or len(cve_example_similary) >3000:
            
            # print(len(cve_example_similary))
            temp_c.append(len(cve_example_similary))
            if c > max_number:
                scout = 1
                # print('这个cve找不到相似的')
                # print(cve_example)
                break
            else:
                cve_example_similary = []
                max_number = max(number.values())
                for i in number:
                    if number[i] >= max_number-c:
                        # if 'vulnerability_type' in [d[1] for d in des_aspect[i]]:
                        if target_key_aspect in [d[1] for d in des_aspect[i]]:    
                            cve_example_similary.append([i,des_aspect[i]])
    
                c += 1
        if scout == 1:

       
            return {"resCode": "1", "message": "success","data":'找不到跟它相似的，跳过'}
        #先把cve转化为字典，方便查看
        cve_example_similary_dic = []
        for i in cve_example_similary:
            temp = {}
            for j in i[1]:
                temp[j[1]] = j[0]
            cve_example_similary_dic.append([i[0],temp])

        data = [i[0] for i in cve_example_similary_dic]
        nlp = spacy.load("en_core_web_lg")
        emb_data = [nlp(i).vector for i in data]

        
        X = emb_data
        n = len(X)
        k = 10
        Center, DistMat = KMeans(np.array(emb_data), k)
        Points = PointSelection(DistMat,k,n)
        sentences = [cve_example_similary_dic[i] for i in Points]
        return sentences              
def condidate_v3(sentence, data_des, all_aspect, target_key_aspect='affected_product'):
    if target_key_aspect == 'affected_product':
        cve_example = sentence.lower()
        print(cve_example)
        des_aspect = {}
        cve_example_similary = []
        affected_product = ''
        for i in range(len(all_aspect)):
            for j in all_aspect[i]:
                if j[1] == 'affected_product':

                    if j[0].lower() in cve_example:
                        # print(j[0])
                        cve_example_similary.append([data_des[i], all_aspect[i]])

                       
           
        if len(cve_example_similary) == 0:
            return {"resCode": "1", "message": "success","data":'找不到跟它相似的，跳过'}
        else:

            #先把cve转化为字典，方便查看
            cve_example_similary_dic = []
            for i in cve_example_similary:
                temp = {}
                for j in i[1]:
                    temp[j[1]] = j[0]
                cve_example_similary_dic.append([i[0],temp])
            if len(cve_example_similary) <= 10:
                return  cve_example_similary_dic
            else:
                data = [i[0] for i in cve_example_similary_dic]
                nlp = spacy.load("en_core_web_lg")
                emb_data = [nlp(i).vector for i in data]

                
                X = emb_data
                n = len(X)
                k = 10
                Center, DistMat = KMeans(np.array(emb_data), k)
                Points = PointSelection(DistMat,k,n)
                sentences = [cve_example_similary_dic[i] for i in Points]
                return sentences
    else:
        scout = 0
        cve_example = sentence
        number = {}
        des_aspect = {}
        for i in range(len(all_aspect)):
            n = 0
            temp = [j[0] for j in all_aspect[i]]
            for j in temp:
                if j in cve_example:
                    n += 1
            number[data_des[i]] = n
            des_aspect[data_des[i]] = all_aspect[i]
        
        cve_example_similary = []
        max_number = max(number.values())
        for i in number:
            if number[i] >= max_number-1:
                # if 'vulnerability_type' in [d[1] for d in des_aspect[i]]:
                if target_key_aspect in [d[1] for d in des_aspect[i]]:    
                    cve_example_similary.append([i,des_aspect[i]])
                   
        c = 0
        temp_c = []
        # print('===========')
        # print(len(cve_example_similary))
        while len(cve_example_similary) < 10 or len(cve_example_similary) >3000:
            
            # print(len(cve_example_similary))
            temp_c.append(len(cve_example_similary))
            if c > max_number:
                scout = 1
                # print('这个cve找不到相似的')
                # print(cve_example)
                break
            else:
                cve_example_similary = []
                max_number = max(number.values())
                for i in number:
                    if number[i] >= max_number-c:
                        # if 'vulnerability_type' in [d[1] for d in des_aspect[i]]:
                        if target_key_aspect in [d[1] for d in des_aspect[i]]:    
                            cve_example_similary.append([i,des_aspect[i]])
    
                c += 1
        if scout == 1:

       
            return {"resCode": "1", "message": "success","data":'找不到跟它相似的，跳过'}
        #先把cve转化为字典，方便查看
        cve_example_similary_dic = []
        for i in cve_example_similary:
            temp = {}
            for j in i[1]:
                temp[j[1]] = j[0]
            cve_example_similary_dic.append([i[0],temp])

        data = [i[0] for i in cve_example_similary_dic]
        nlp = spacy.load("en_core_web_lg")
        emb_data = [nlp(i).vector for i in data]

        
        X = emb_data
        n = len(X)
        k = 10
        Center, DistMat = KMeans(np.array(emb_data), k)
        Points = PointSelection(DistMat,k,n)
        sentences = [cve_example_similary_dic[i] for i in Points]
        return sentences    
def ask_chatgpt(prompt):

# =============================================================================
#     a = openai.Completion.create(
#       model="text-davinci-003",
#       prompt=prompt,
#       max_tokens=100,
#       temperature=0
#     )
#     return a['choices'][0].text
# =============================================================================
# =============================================================================
#     a = openai.ChatCompletion.create(
#       model="gpt-3.5-turbo",
#       messages=[
#             {"role": "system", "content": "You are an expert in the field of software vulnerability."},
#             {"role": "user", "content": prompt_set[0][0]},
#             {"role": "assistant", "content": "Remote code execution vulnerability."},
#             {"role": "user", "content": 'please give your reason step by step.'},
#         ]
#     )
# =============================================================================
    a = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are an expert in the field of software vulnerability."},
            {"role": "user", "content": prompt}
        ]
    )
    return a['choices'][0].message['content'].strip()

def ask_chatgpt_history(history_prompt, answer, prompt):
    a = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are an expert in the field of software vulnerability."},
            {"role": "user", "content": history_prompt},
            {"role": "assistant", "content": answer},
            {"role": "user", "content": prompt},
        ]
    )
    return a['choices'][0].message['content'].strip()


def add_knowledge(sentences):
    temp = sentences
    # prompt = 'Give a description of about 50 words: In the field of software vulnerablility, what arethe characteristics of the product '
    for i in temp:
        prompt = 'Give a description of about 30 words: In the field of software vulnerablility, what arethe characteristics of the product '
        if 'affected_product' in i[1]:
            prompt = prompt + i[1]['affected_product'] + '?'
            i[1]['affected_product_knowledge'] = ask_chatgpt(prompt)
    return temp

                    
def extract_key_aspect(sentence):
    lack = {"vulnerability description":sentence}
    aspct = guohao_extract(['1',sentence])
    s = 0
    while s < len(aspct):
        if aspct[s] != '' and s == 1:
            lack['vulnerability_type'] = aspct[s]
        if aspct[s] != '' and s == 2:
            lack['attacker_type'] = aspct[s]
        if aspct[s] != '' and s == 3:
            lack['root_cause'] = aspct[s]
        if aspct[s] != '' and s == 4:
            lack['impact'] = aspct[s]                
        if aspct[s] != '' and s == 5:
            lack['attacker_vector'] = aspct[s] 
        s += 1    
    return lack        
    
    
    
    
    
    
    
    