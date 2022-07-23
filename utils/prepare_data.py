import os
import shutil
import numpy as np
import tqdm

from pycocotools.coco import COCO
data_source = COCO(annotation_file='raw_data/annotations.json')

label_transfer = {5: 0, 12: 1}

img_ids = data_source.getImgIds()
catIds = data_source.getCatIds()
categories = data_source.loadCats(catIds)
categories.sort(key=lambda x: x['id'])

classes = {}
coco_labels = {}
coco_labels_inverse = {}
supercategories = {}
label_transfer = {}

for c in categories:
    if not c['supercategory'] in supercategories:
        supercategories[c['supercategory']] = len(supercategories)

for c in categories:
    coco_labels[len(classes)] = c['id']
    coco_labels_inverse[c['id']] = len(classes)
    classes[c['name']] = len(classes)
    print(c)
    label_transfer[c['id']] = supercategories[c['supercategory']]

print(len(supercategories))
print(supercategories.keys())
print('')
print(label_transfer)
    

'''class_num = {}

for index, img_id in tqdm.tqdm(enumerate(img_ids), desc='change .json file to .txt file'):
    img_info = data_source.loadImgs(img_id)[0]
    save_name = img_info['file_name'].replace('/', '_')
    file_name = save_name.split('.')[0]

    height = img_info['height']
    width = img_info['width']
    save_path =  'data/' + file_name + '.txt'
    is_exist = False

    with open(save_path, mode='w') as fp:
        annotation_id = data_source.getAnnIds(img_id)
        boxes = np.zeros((0, 5))
        
        if len(annotation_id) == 0:
            fp.write('')
            continue
        annotations = data_source.loadAnns(annotation_id)
        lines = ''
        for annotation in annotations:
            label = coco_labels_inverse[annotation['category_id']]
            if label in label_transfer.keys():
                is_exist = True
                box = annotation['bbox']
                if box[2] < 1 or box[3] < 1:
                    continue

                box[0] = round((box[0] + box[2] / 2) / width, 6)
                box[1] = round((box[1] + box[3] / 2) / height, 6)
                box[2] = round(box[2] / width, 6)
                box[3] = round(box[3] / height, 6)
                label = label_transfer[label]
                if label not in class_num.keys():
                    class_num[label] = 0
                class_num[label] += 1
                lines = lines + str(label)
                for i in box:
                    lines += ' ' + str(i)
                lines += '\n'
        fp.writelines(lines)
    if is_exist:
        shutil.copy('raw_data/{}'.format(img_info['file_name']), os.path.join('data/', save_name))
    else:
        os.remove(save_path)
'''