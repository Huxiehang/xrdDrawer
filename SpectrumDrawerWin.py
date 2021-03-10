# -*- coding: utf-8 -*-

"""
Created on 2021/03/02
@author: Cao Shuqi
@file: AutoSpectrumDrawer
@description: 创建窗口

Global
+--- MainWin(QVBoxLayout)
     +--- PathInput(QHBoxLayout)
     |    +--- QLabel
     |    +--- QLineEdit
     |    +--- QPushButton
     |
     +--- HBox(QHBoxLayout)
          +--- Params(QFormLayout)
          |    +--- QLabel
          |
          |
          +--- ImageView
"""

import sys
import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QFormLayout
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton

from ImageView import ImageView
from SpectrumDrawer import SpectrumDrawer

"""
主窗口
"""
class MainWin(QWidget):
    def __init__(self,parent=None):
        super(MainWin,self).__init__(parent)

        #初始化绘图器
        self.drawer=SpectrumDrawer()

        self.setWindowTitle("读取文件测试") 
        self.resize(1000, 600)  
        layout = QVBoxLayout(self)
        layout.addWidget(PathInput())
        layout.addWidget(HBox())
        #这里再加一个色条就好了

class PathInput(QWidget):
    def __init__(self,parent=None):
        super(PathInput,self).__init__(parent)
        layout=QHBoxLayout(self)

        self.path=""

        lab1=QLabel("Path:")

        self.btn1 = QPushButton("读取")
        #读取并将数据储存在主窗体中
        self.btn1.clicked.connect(lambda :self.btn1.setText("读取成功" if self.parent().drawer.read(self.path) else "读取失败"))
        self.btn1.setEnabled(False)

        self.path_input1=QLineEdit() #r"C:\Users\WLK001\3D Objects\QT\SNS")
        self.path_input1.setPlaceholderText('请输入完整文件夹路径')
        self.path_input1.setEchoMode(QLineEdit.Normal)
        self.path_input1.textChanged.connect(lambda :self.path_input1_changed_event())

        #路径存在，则读取按钮生效
        layout.addWidget(lab1)
        layout.addWidget(self.path_input1)
        layout.addWidget(self.btn1)
    
    def path_input1_changed_event(self):
        self.path=self.path_input1.text().strip()
        self.btn1.setText("读取")
        self.btn1.setEnabled(os.path.exists(self.path) and os.path.isdir(self.path))
        

class HBox(QWidget):
    def __init__(self,parent=None):
        super(HBox,self).__init__(parent)

        vlayout = QHBoxLayout(self)
        
        self.params=Params(self)
        self.params.setMaximumWidth(200)
        self.viewer=ImageView()

        self.params.mySignal.connect(self.signal_received_event)

        vlayout.addWidget(self.params)
        vlayout.addWidget(self.viewer)
        
    def signal_received_event(self,connect):
        image=self.parent().drawer.drawSpectrum(connect)
        #print(type(image))
        self.viewer.setPixmap(image)

class Params(QWidget):
    mySignal = pyqtSignal(list)
    def __init__(self,parent=None):
        super(Params,self).__init__(parent)
        layout=QFormLayout(self)
        
        self.k=QLineEdit("2")
        self.a=QLineEdit("4")
        self.i=QLineEdit("1")
        self.j=QLineEdit("all")
        btn1 = QPushButton("生成图像")

        btn1.clicked.connect(lambda : self.btn1_clicked_event())
         # 发射信号

        layout.addRow("k:",self.k)
        layout.addRow("a:",self.a)
        layout.addRow("i:",self.i)
        layout.addRow("j:",self.j)
        layout.addRow("",btn1)

    def btn1_clicked_event(self):
        int_k=int(self.k.text())-1        # 1
        int_a=int(self.a.text())          # 4
        int_i=max(int(self.i.text())-1,0) # 0
        int_j=-1                          #-1
        try:
            int_j=int(self.j.text())-1
        except:
            int_j=-1
        self.mySignal.emit([int_k,int_i,int_j,int_a])

def main():
    app = QApplication(sys.argv) 
    
    mainWin = MainWin()

    mainWin.show()
    sys.exit(app.exec_())

if __name__ == "__main__":  
    main()