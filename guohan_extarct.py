# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:37:23 2022

@author: hanly2
"""
import re
def guohao_extract(row):
    if len(re.findall('allow[^ ]* .*? to ', row[1])):
        aat = re.findall('allow[^ ]* (.*?) to ', row[1])[0]
        pd = row[1].split(re.findall('allow[^ ]* .*? to ', row[1])[0])[0]
        a1 = row[1].split(re.findall('allow[^ ]* .*? to ', row[1])[0])[1]
        rootc = ''
        vt=''
        if len(re.findall('(?:(?: via .*)|(?: by [a-z]+ing .*)|(?: uses? .*))', a1)):
            at = re.findall('(?:(?: via .*)|(?: by [a-z]+ing .*)|(?: uses? .*))', a1)[0]
            im = a1.replace(at, '')
        else:
            im = a1
            at = ''
        if len(re.findall('(?:(?:(?:(?:uffer)|(?:teger)) overflow)|(?:vulnerability?(?:ies)?)) in (.*) allow', pd,
                          re.DOTALL)):
            vt=re.findall('(?:((?:(?:uffer)|(?:teger)) overflow)|(?:vulnerability?(?:ies)?)) in (?:.*) allow', pd,
                            re.DOTALL)[0]
            pd = re.findall('(?:(?:(?:(?:uffer)|(?:teger)) overflow)|(?:vulnerability?(?:ies)?)) in (.*) allow', pd,
                            re.DOTALL)[0]
        if len(re.findall(
                '(?:(?: fails? to )|(?: automatically )|(?: when )|(?: have )|(?: has )|(?: does )|(?: do )|(?: uses? )|(?: returns? )|(?: creates? )|(?: provides? )|(?: relies? )|(?: places? )|(?: generates? )|(?: advertises )|(?: mishandles )|(?: store SSH )|(?: lets? )|(?: handles )|(?: using )|(?: lets? )).*',
                pd)):
            rootc = re.findall(
                '(?:(?: fails? to )|(?: automatically )|(?: when )|(?: have )|(?: has )|(?: does )|(?: do )|(?: uses? )|(?: returns? )|(?: creates? )|(?: provides? )|(?: relies? )|(?: places? )|(?: generates? )|(?: advertises )|(?: mishandles )|(?: store SSH )|(?: lets? )|(?: handles )|(?: using )|(?: lets? )).*',
                pd)[0]
            pd = pd.split(rootc)[0]
        if at == '':
                if len(re.findall(
                        '\A(?:(?:use )|(?:send )|(?:supply )|(?:specially )|(?:upload )|(?:create )|(?:construct )|(?:compromise )).*? to',
                        im)):
                    at = re.findall(
                        '\A(?:(?:use )|(?:send )|(?:supply )|(?:specially )|(?:upload )|(?:create )|(?:construct )|(?:compromise )).*? to',
                        im)[0]
                    im = im.split(at)[-1]
    
        dt = []
        dt.append(row[0])
        dt.append(pd)
        dt.append(aat)
        dt.append(rootc)
        dt.append(im)
        dt.append(at)
        # print(11)
        # print(dt)
        # f2 = open(file2, 'a', newline='', encoding='utf-8')
        # writer = csv.writer(f2)
        # writer.writerow(dt)
        return dt
    else:
        return []
        # print(111)
        # print(row)
        # f2 = open(file3, 'a', newline='', encoding='utf-8')
        # writer = csv.writer(f2)
        # writer.writerow(row)
# a= guohao_extract(['1','Improper privilege management vulnerability in McAfee Consumer Product Removal Tool prior to version 10.4.128 could allow a local user to modify a configuration file and perform a LOLBin (Living off the land) attack. This could result in the user gaining elevated permissions and being able to execute arbitrary code, through not correctly checking the integrity of the configuration file.'])