# -*- coding: utf-8 -*-
"""
Created on 2021/03/03
@author: Cao Shuqi
@file: AutoSpectrumDrawer
@description: 数据文件读取
读取结构：
--dataset
----doc
------line
--------cell    
"""

import os

def readDir(dir):
    try:
        dataset=[]
        doclist=os.listdir(dir)
        doclist.sort( key=lambda x:int(x[:-4]), reverse=False)
        for doc in doclist:
            dataset.append(readDoc(os.path.join(dir,doc)))
        return dataset
    except:
        return

def readDoc(doc):
    lineset=[]
    with open(doc,'r') as f:
        line=' '
        while line:
            line=f.readline()
            lineset.append(readLine(line))
    return lineset

def readLine(line):
    line=line.strip()
    try:
        return [float(s) for s in line.split('  ')]
    except:
        return []

if __name__ == '__main__':
    # dir=input("Complete Dir Path:")
    dir=r"C:\Users\WLK001\3D Objects\QT\SNS"
    readDir(dir)
