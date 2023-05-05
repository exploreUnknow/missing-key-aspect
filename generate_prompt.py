# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:46:20 2023

@author: hanly2
"""
from find_candidate import ask_chatgpt_history
def vulnerability_gengerate_zhuguanti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成vulnerability的主观题的prompt

    '''
    prompt = "please infer target vulnerability type(No more than 10 words) based on similar vulnerability description, similar vulnerability key aspect, target vulnerability description and target vulnerability key aspect.\nSimilar vulnerabilities:\n["
    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question:what is the vulnerability type?(answer should be not more than 10 words，and should not be include explanation)\nAnswer:' 
    return prompt



def attacker_type_gengerate_zhuguanti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成attacker_type的主观题的prompt

    '''
    prompt = "please infer target attacker type(No more than 10 words and just include attacker type) based on similar vulnerability description, similar vulnerability key aspect, target vulnerability description and target vulnerability key aspect.\nSimilar vulnerabilities:\n["
    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question:what is the attacker type?(answer should be not more than 10 words，and should not be include explanation)\nAnswer:' 
    return prompt





def attack_vector_gengerate_zhuguanti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成attacker_type的主观题的prompt

    '''
    prompt = "please infer target attack vector(No more than 10 words and just include attack vector) based on similar vulnerability description, similar vulnerability key aspect, target vulnerability description and target vulnerability key aspect.\nSimilar vulnerabilities:\n["
    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question:what is the attack vector?(answer should be not more than 10 words，and should not be include explanation)\nAnswer:' 
    return prompt

def root_cause_gengerate_zhuguanti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成attacker_type的主观题的prompt

    '''
    prompt = "please infer target vulnerability root cause(No more than 10 words and just include root cause) based on similar vulnerability description, similar vulnerability key aspect, target vulnerability description and target vulnerability key aspect.\nSimilar vulnerabilities:\n["
    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question:what is the root cause?(answer should be not more than 10 words，and should not be include explanation)\nAnswer:' 
    return prompt


def impact_gengerate_zhuguanti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成attacker_type的主观题的prompt

    '''
    prompt = "please infer target impact(No more than 10 words and just include impact) based on similar vulnerability description, similar vulnerability key aspect, target vulnerability description and target vulnerability key aspect.\nSimilar vulnerabilities:\n["
    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question:what is the impact?(answer should be not more than 10 words，and should not be include explanation)\nAnswer:' 
    return prompt


def vulnerability_gengerate_tiankongti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成vulnerability的填空题的prompt

    '''
    prompt = "please infer vulnerability type (No more than 10 words) based on similar vulnerabilities, examples of inferring, target vulnerability description and target vulnerability key aspects.\nSimilar vulnerabilities:\n["

    similar_sentences_0_5 = similar_sentences[:int(len(similar_sentences)/2)]
    similar_sentences_5_10 = similar_sentences[int(len(similar_sentences)/2):]
    for i in similar_sentences_0_5:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Examples of inferring:\n['
    for i in similar_sentences_5_10:
        des = i[0]
        aspect = i[1]
        des = des.replace(aspect['vulnerability_type'], '(missing vulnerability_type)')
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            if j != 'vulnerability_type':
                prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + 'vulnerability_type could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nvulnerability_type: '
        prompt = prompt + aspect['vulnerability_type'] + '\n},\n'
 
    
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'vulnerability_type could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nvulnerability_type: ' 
    return prompt

def attacker_type_gengerate_tiankongti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成vulnerability的填空题的prompt

    '''
    prompt = "please infer attacker type (No more than 10 words and just include attacker type) based on similar vulnerabilities, examples of inferring, target vulnerability description and target vulnerability key aspects.\nSimilar vulnerabilities:\n["

    similar_sentences_0_5 = similar_sentences[:int(len(similar_sentences)/2)]
    similar_sentences_5_10 = similar_sentences[int(len(similar_sentences)/2):]
    for i in similar_sentences_0_5:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Examples of inferring:\n['
    for i in similar_sentences_5_10:
        des = i[0]
        aspect = i[1]
        des = des.replace(aspect['attacker_type'], '(missing attacker type)')
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            if j != 'attacker_type':
                prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + 'attacker type could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nattacker type: '
        prompt = prompt + aspect['attacker_type'] + '\n},\n'
 
    
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'attacker type could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nattacker type: ' 
    return prompt

def attack_vector_gengerate_tiankongti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成vulnerability的填空题的prompt

    '''
    prompt = "please infer attack vector (No more than 10 words and just include attack vector) based on similar vulnerabilities, examples of inferring, target vulnerability description and target vulnerability key aspects.\nSimilar vulnerabilities:\n["

    similar_sentences_0_5 = similar_sentences[:int(len(similar_sentences)/2)]
    similar_sentences_5_10 = similar_sentences[int(len(similar_sentences)/2):]
    for i in similar_sentences_0_5:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Examples of inferring:\n['
    for i in similar_sentences_5_10:
        des = i[0]
        aspect = i[1]
        des = des.replace(aspect['attack_vector'], '(missing attack vector)')
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            if j != 'attack_vector':
                prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + 'attack vector could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nattack vector: '
        prompt = prompt + aspect['attack_vector'] + '\n},\n'
 
    
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'attack vector could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nattack vector: ' 
    return prompt

def root_cause_gengerate_tiankongti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成vulnerability的填空题的prompt

    '''
    prompt = "please infer root cause (No more than 10 words and just include root_cause) based on similar vulnerabilities, examples of inferring, target vulnerability description and target vulnerability key aspects.\nSimilar vulnerabilities:\n["

    similar_sentences_0_5 = similar_sentences[:int(len(similar_sentences)/2)]
    similar_sentences_5_10 = similar_sentences[int(len(similar_sentences)/2):]
    for i in similar_sentences_0_5:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Examples of inferring:\n['
    for i in similar_sentences_5_10:
        des = i[0]
        aspect = i[1]
        des = des.replace(aspect['root_cause'], '(missing root cause)')
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            if j != 'root_cause':
                prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + 'root cause could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nroot cause: '
        prompt = prompt + aspect['root_cause'] + '\n},\n'
 
    
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'root cause could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nroot cause: ' 
    return prompt


def impact_gengerate_tiankongti(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成vulnerability的填空题的prompt

    '''
    prompt = "please infer impact (No more than 10 words and just include impact) based on similar vulnerabilities, examples of inferring, target vulnerability description and target vulnerability key aspects.\nSimilar vulnerabilities:\n["

    similar_sentences_0_5 = similar_sentences[:int(len(similar_sentences)/2)]
    similar_sentences_5_10 = similar_sentences[int(len(similar_sentences)/2):]
    for i in similar_sentences_0_5:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Examples of inferring:\n['
    for i in similar_sentences_5_10:
        des = i[0]
        aspect = i[1]
        des = des.replace(aspect['impact'], '(missing impact)')
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            if j != 'impact':
                prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + 'impact could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nimpact: '
        prompt = prompt + aspect['impact'] + '\n},\n'
 
    
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'impact could be inferred based on vulnerability description, key aspects, Similar vulnerabilities;\nimpact: ' 
    return prompt


def vulnerability_gengerate_jianchadaan(similar_sentences, target_sentences, answers):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
        
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素
    answers : [txt,txt,...txt]
        答案1，答案2，答案3...
       
    Returns
    -------
    prompt : txt
        生成vulnerability的检查答案的prompt

    '''
    prompt = "Please select the correct answer from the vulnerability type options based on similar vulnerabilities, target vulnerability description, and target vulnerability key aspect.\nNoting: just return option text\nvulnerability type options: "
    bianhao = ['A','B']
    s = 0
    for i in answers:
        s += 1
        prompt = prompt + bianhao[s-1] + '. ' + answers[s-1] + '; '
    prompt = prompt + "\nSimilar vulnerabilities:\n["

    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
   
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question: Please select the correct vulnerability type from the vulnerability type options.\nAnswer:' 
    return prompt


def attacker_type_gengerate_jianchadaan(similar_sentences, target_sentences, answers):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
        
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素
    answers : [txt,txt,...txt]
        答案1，答案2，答案3...
       
    Returns
    -------
    prompt : txt
        生成vulnerability的检查答案的prompt

    '''
    prompt = "Please select the correct answer from the attacker type options based on similar vulnerabilities, target vulnerability description, and target vulnerability key aspect.\nNoting: just return option text\nattacker type options: "
    bianhao = ['A','B']
    s = 0
    for i in answers:
        s += 1
        prompt = prompt + bianhao[s-1] + '. ' + answers[s-1] + '; '
    prompt = prompt + "\nSimilar vulnerabilities:\n["

    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
   
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question: Please select the correct attacker type from the attacker type options.\nAnswer:' 
    return prompt



def attack_vector_gengerate_jianchadaan(similar_sentences, target_sentences, answers):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
        
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素
    answers : [txt,txt,...txt]
        答案1，答案2，答案3...
       
    Returns
    -------
    prompt : txt
        生成vulnerability的检查答案的prompt

    '''
    prompt = "Please select the correct answer from the attack vector options based on similar vulnerabilities, target vulnerability description, and target vulnerability key aspect.\nNoting: just return option text\nattack vector options: "
    bianhao = ['A','B']
    s = 0
    for i in answers:
        s += 1
        prompt = prompt + bianhao[s-1] + '. ' + answers[s-1] + '; '
    prompt = prompt + "\nSimilar vulnerabilities:\n["

    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
   
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question: Please select the correct attack vector from the attack vector options.\nAnswer:' 
    return prompt

def root_cause_gengerate_jianchadaan(similar_sentences, target_sentences, answers):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
        
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素
    answers : [txt,txt,...txt]
        答案1，答案2，答案3...
       
    Returns
    -------
    prompt : txt
        生成vulnerability的检查答案的prompt

    '''
    prompt = "Please select the correct answer from the root cause options based on similar vulnerabilities, target vulnerability description, and target vulnerability key aspect.\nNoting: just return option text\nroot cause options: "
    bianhao = ['A','B']
    s = 0
    for i in answers:
        s += 1
        prompt = prompt + bianhao[s-1] + '. ' + answers[s-1] + '; '
    prompt = prompt + "\nSimilar vulnerabilities:\n["

    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
   
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question: Please select the correct root cause from the root cause options.\nAnswer:' 
    return prompt

def impact_gengerate_jianchadaan(similar_sentences, target_sentences, answers):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
        
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素
    answers : [txt,txt,...txt]
        答案1，答案2，答案3...
       
    Returns
    -------
    prompt : txt
        生成vulnerability的检查答案的prompt

    '''
    prompt = "Please select the correct answer from the impact options based on similar vulnerabilities, target vulnerability description, and target vulnerability key aspect.\nNoting: just return option text\nimpact options: "
    bianhao = ['A','B']
    s = 0
    for i in answers:
        s += 1
        prompt = prompt + bianhao[s-1] + '. ' + answers[s-1] + '; '
    prompt = prompt + "\nSimilar vulnerabilities:\n["

    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
   
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question: Please select the correct impact from the impact options.\nAnswer:' 
    return prompt
# a = vulnerability_gengerate_tiankongti(sentences, lack[kk], )






def vulnerability_gengerate_zhuguanti1(similar_sentences, target_sentences):
    '''
    

    Parameters
    ----------
    similar_sentences : [[[文本1],{关键因素}],[[文本2],{关键因素}],]
        相似文本和关键因素选集.
    target_sentences : {‘目标文本’:
                        ‘关键因素’：
                        }
        目标文本和关键因素

    Returns
    -------
    prompt : txt
        生成vulnerability的主观题的prompt

    '''
    prompt = "please infer target vulnerability type(Let’s think step by step) based on similar vulnerability description, similar vulnerability key aspect, target vulnerability description and target vulnerability key aspect.\nSimilar vulnerabilities:\n["
    for i in similar_sentences:
        des = i[0]
        aspect = i[1]
        prompt = prompt + '{\nvulnerability description: ' + des + ';\n'
        for j in aspect:
            prompt = prompt + j + ': ' + aspect[j] + '\n'
        prompt = prompt + '},\n'
    prompt = prompt + ']\n' + 'Target vulnerability:\n'
    for i in target_sentences:
        prompt = prompt + i + ': ' + target_sentences[i] + '\n'
    
    prompt = prompt + 'Question:what is the vulnerability type?\nLet’s think step by step\nAnswer:' 
    return prompt

def get_reason(prompt, answer):
    return ask_chatgpt_history(prompt, answer, 'please give your reason step by step.')

def gengerate_answer_byReason(key_aspect_name, reason, sentence):
    prompt = "please infer the " + key_aspect_name + " of the vulnerability description according to reasoning basis.\n" 
    prompt = prompt + "vulnerability description: " + sentence + '\n'
    prompt = prompt + "reasoning basis: " + reason + '\n'
    prompt = prompt + key_aspect_name + ": "
    return prompt

