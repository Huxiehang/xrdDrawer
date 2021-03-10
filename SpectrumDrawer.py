# -*- coding: utf-8 -*-
"""
Created on 2021/03/03
@author: Cao Shuqi
@file: AutoSpectrumDrawer
@description: 将文件转换为图片  
"""

import DocReader
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_agg import FigureCanvasAgg

class SpectrumDrawer:
    dataset=None
    #img=None
    def __init__(self,dir=None):

        if dir:
            self.dataset=DocReader.readDir(dir)

    def read(self,dir):
        self.dataset=DocReader.readDir(dir)
        return self.dataset!=None

    def drawSpectrum(self,params=[1,0,-1,4]):
        k,i,j,a=params
        if self.dataset==None:
            return
        N=len(self.dataset)
        line_len=len(self.dataset[0])-a-1
        j=line_len if j<0 or j>line_len else j
        img_data=np.empty([N,j-i])
        for t,data in enumerate(self.dataset):
            # normalize
            line_data=np.array([x[k] for x in data[a:-1]])
            _range = np.max(line_data) - np.min(line_data)
            line_data =(line_data - np.min(line_data)) / _range
            
            img_data[t,:]=line_data[i:j]

        x = np.arange(j-i+1)
        y = np.arange(N+1)

        fig, ax = plt.subplots(figsize=(14, 9))
        fig.set_tight_layout(True)

        cmap = plt.get_cmap('viridis')
        ax.pcolormesh(x, y, img_data,cmap=cmap)

        # canvas = plt.get_current_fig_manager().canvas

        # agg = canvas.switch_backends(FigureCanvasAgg)
        # agg.draw()
        # s, (width, height) = agg.print_to_buffer()

        # # Convert to a NumPy array.
        # img = np.frombuffer(s, np.uint8).reshape((height, width, 4))

        plt.savefig("cache.jpg")
        return "cache.jpg"


if __name__ == '__main__':
    dir=r"C:\Users\WLK001\3D Objects\QT\SNS"
    drawer=SpectrumDrawer(dir)
    img=drawer.drawSpectrum()
    
    # from cv2 import cv2
    # cv2.imwrite('test.jpg',img)