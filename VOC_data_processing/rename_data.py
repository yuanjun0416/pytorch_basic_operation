import os

from matplotlib import image


#将经过爬虫获得图片的名字由无序变为有序编号（000000.jpg->999999.jpg)
def rename_img(Img_dir, Annotation_dir):
    '''
    重新命名Img, 这里假设图像名称表示为000000.jpg~002058.jpg
    重新命名与Img相对应的Annotation
    Img_dir:数据集中的图片
    Annotation_dir:数据集中标注的图片（Img_dir）的内容
    '''
    img_listdir = os.listdir(Img_dir)    #获得Img_dir的文件列表目录，也就是图片的名称列表
    Ann_listdir = os.listdir(Annotation_dir)
    #print(img_listdir)
    for step, line in enumerate(img_listdir):  #step:表示的是图片的序列，line:表示的是每一张图片的名称
        if line[-4:] == '.jpg':           #判断图片名称是不是以jpg格式的
            line_first_half = line.split('.')[0]       #获得图片名称前半部分，也就是假设line:000000.jpg->line_first_half:000000
            ann_name = os.path.join(line_first_half + '.xml')   #获得与图片名称标注的相对应的内容的文件（xml），假设line；000000.jpg->ann_name:000000.xml
            newname_img = '{:0>6}'.format(step) + '.jpg'     #获得新的图片名称，即0.jpg->000000.jpg
            newname_ann = '{:0>6}'.format(step) + '.xml'     #获得新的标注名称，即0.xml->000000.xml
            os.rename(os.path.join(Img_dir + line), os.path.join(Img_dir + newname_img))      #将图片名称由旧名称改为新名称
            os.rename(os.path.join(Annotation_dir + ann_name), os.path.join(Annotation_dir + newname_ann))  #将标注（标注与图片相对应）名称由旧名称改为新名称


if __name__ == '__main__':
    image_root = './data/VOC2020/JPEGImages/'
    ann_root = './data/VOC2020/Annotations/'
    rename_img(image_root, ann_root)