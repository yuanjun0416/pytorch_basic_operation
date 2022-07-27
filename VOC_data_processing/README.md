#对本文夹中的一些函数的简介

## rename_data.py
* 将经过爬虫获得图片的名字由无序变为有序编号（000000.jpg->999999.jpg)
* 这个函数中是将标注好了的图片和标注信息（即JPEGImages and Annotations)重新命名

## rename_data_xml.py
* 是对rename_data.py的补充
* 由于网上爬虫的图片和标注过的信息经过rename_data.py后，annotation中的filename和path还未改变，需对其进行重写
* rename_data_xml.py就是对<filename>和<path>的内容进行修改的

## split_data.py
* 是对rename_data_xml.py的补充
* 由于在经过rename_data_xml.py处理之后，并没有划分训练集、验证集，本代码是将VOC（JPEGImages、Annotations）数据集划分到train.txt和val.txt，具体的默认比例是0.5，可以自行修改

## view_dataset_categories.py
* 当pascal voc数据集不知道需要检测的目标种类是什么时，直接运行该代码，即可得到目标类别列表
