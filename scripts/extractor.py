import cv2
import numpy as np
import matplotlib.pyplot as plt

class CharExtractor:
    def __init__(self):
        self.classes = None
        self.class_char = []
        self.y_class = None
        self.x_class = None
        self.bbox = None
        self.x_bbox = None
        self.y_bbox = None
    
    def _extract_bbox(self, bboxes, classes):
        plate_number = []
        self.bbox = bboxes
        self.classes = classes
        
        for ix,bbox in enumerate(bboxes):
            if len(bbox) != 0:
                lowest_x, highest_y = self._get_xy(bbox, ix)
                print('x_class : ', self.x_class)
                # print('y_bbox : ', self.y_bbox)
                for idx, point in enumerate(self.y_bbox):
                    x, y = point[0], point[1]
                    if y <= highest_y and x >= lowest_x and self.x_class.size > 1:
                        self.class_char.append(self.x_class[idx])

                plate_num = ''.join(str(v) for v in self.class_char)
                self.class_char.clear()
        
            else:
                plate_num = ''
            
            plate_number.append(plate_num)
        
        return plate_number
    
    def _get_xy(self, bbox, ix):
        y_id = bbox[:, 1].argsort()
        # print('y_id : ', y_)
        if len(bbox[y_id]) >= 4:
            sorted_y = bbox[y_id][:-4]
            self.y_bbox = sorted_y
            # print('y_class : ', self.classes[ix])
            # print('yid : ', y_id)
            self.y_class = np.array(self.classes[ix][y_id])[:-4]
            highest_y = max([x[1] for x in sorted_y])
            
            x_id = sorted_y[:,0].argsort()
            sorted_x = sorted_y[x_id]
            self.x_bbox = sorted_x
            # print('char : ', self.y_class)
            self.x_class = self.y_class[x_id]
            lowest_x = min([x[0] for x in sorted_x])
            
        else:
            sorted_y = bbox[y_id]
            self.y_bbox = sorted_y
            # print('y_class : ', self.classes)
            # print('yid : ', y_id)
            self.y_class = np.array(self.classes[ix][y_id])
            highest_y = max([x[1] for x in sorted_y])
            
            x_id = sorted_y[:,0].argsort()
            sorted_x = sorted_y[x_id]
            self.x_bbox = sorted_x
            # print('char : ', self.y_class)
            self.x_class = self.y_class
            lowest_x = min([x[0] for x in sorted_x])
        
        return lowest_x, highest_y
 
            
        