# 光谱自动绘制程序

有N个文件，每个文件里有数据，数据以SNS为例。
有a行的题头，第1列和第k列是需要读取的数据。
这N个文件做二维颜色图，区间是第i行到第j行。

即：x长轴是N张图的序号,y短轴是i-j行，颜色是数值大小。
注意，数值可能有0，有必要的话需要先同样加一个极小的数字。

要求：a,k,i,j全都是可以输入的值，N为当前文件夹所有txt文件个数，这些txt文件全都按数字顺序排列（1,2,3,......,N）。
颜色从深蓝到青到绿到黄

## 结构
- 主程序
  - [SpectrumDrawerWin.py](SpectrumDrawerWin.py) 基于PyQt5的窗口界面，程序入口
  - [SpectrumDrawer.py](SpectrumDrawer.py) 绘图模块，将数据转化为图片
  - [DocReader.py](DocReader.py) 读取模块，将文件格式化读取
  - [ImageView.py](ImageView.py) 预览模块，在窗口中实时查看图片，来自[PyQt5/PyQt](https://github.com/PyQt5/PyQt/blob/master/QGraphicsView/ImageView.py)