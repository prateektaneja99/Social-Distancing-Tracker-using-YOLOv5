from pycocotools.coco import COCO

coco_train = COCO('instances_train2017.json')
coco_img_ids = coco_train.getImgIds(catIds=1)