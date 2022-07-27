import xml.dom.minidom as xmldom
import os

#voc数据集获取所有标签的所有类别数"
annotation_path="E:\\faster_rcnn\\VOCtrainval\\VOCdevkit\\VOC2012\\Annotations"   # annotation文件的根目录

annotation_names=[os.path.join(annotation_path,i) for i in os.listdir(annotation_path)]  # list：获得annotation的所有文件目录的路径

labels = list()
for names in annotation_names:
    xmlfilepath = names      # 每一个xml文件的路径
    domobj = xmldom.parse(xmlfilepath)  # <xml.dom.minidom.Document object at 0x00000253230EAD60>
    # 得到元素对象
    elementobj = domobj.documentElement  # <class 'xml.dom.minidom.Element'>
    #获得子标签
    subElementObj = elementobj.getElementsByTagName("object")   # [<DOM Element: object at 0x253230fc670>, <DOM Element: object at 0x253230fcc10>]
    for s in subElementObj:
        label=s.getElementsByTagName("name")[0].firstChild.data   
        #print(label)
        if label not in labels:
            labels.append(label)
print(labels)

