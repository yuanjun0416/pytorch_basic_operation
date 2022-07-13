#对本文夹中的一些函数的简介

## rename_data.py
* 将经过爬虫获得图片的名字由无序变为有序编号（000000.jpg->999999.jpg)
* 这个函数中是将标注好了的图片和标注信息（即JPEGImages and Annotations)重新命名

## rename_data_xml.py
* 是对rename_data.py的补充
* 由于网上爬虫的图片和标注过的信息经过rename_data.py后，annotation中的filename和path还未改变，需对其进行重写
* rename_data_xml.py就是对<filename>和<path>的内容进行修改的
