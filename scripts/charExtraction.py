from scripts.extractor import CharExtractor
from ultralytics import YOLO
import numpy as np
import cv2


class CharExtraction:
    def __init__(self, wPlatePath, wCharacterPath, classList, sizePlate, conf):
        self.wPlatePath = wPlatePath
        self.wCharacterPath = wCharacterPath
        self.classList = classList
        self.width, self.height = sizePlate
        self.conf = conf
        
        self.model_plat = YOLO(self.wPlatePath)
        self.model_char = YOLO(self.wCharacterPath)
        
        self.extractor = CharExtractor()
        
    def predict(self, image):
        if self.conf == None:
            self.conf = 0.5

        charpredict = []
        platePrediction = self.model_plat(image, conf=self.conf)
        platBoxes, croppedPlateImg = self._get_cropped_plate(platePrediction)
        # print('lcrop : ', len(croppedPlateImg))
        
        for croppImg in croppedPlateImg:
            characterPrediction = self.model_char(croppImg, conf=self.conf)
            charpredict.append(characterPrediction)
            
        # print('lchar : ', len(charpredict))
        characterBBOX, characterClass = self._get_bboxClass_char(charpredict, self.classList)
        # print('charBox : ', len(characterBBOX))
        plateNumber = self.extractor._extract_bbox(characterBBOX, characterClass)
        # print('Plate Number : ', plateNumber)   
        
        # print('plateboxes : ', platBoxes)
        # print('platenum : ', plateNumber)
        return platBoxes, plateNumber             
    
    def _get_cropped_plate(self, imgPlate):
        croppedImage = []
        boxes = imgPlate[0].boxes
        originalImage = imgPlate[0].orig_img
        h,w,c = originalImage.shape
        if len(boxes) != 0:
            for box in boxes.xyxy:
                x1,y1,x2,y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
                croppedPlateImage = originalImage[y1:y2, x1:x2, :]
                croppedPlateImage = cv2.resize(croppedPlateImage, (self.width, self.height))
                croppedImage.append(croppedPlateImage)
        else:
            croppedImage.append(originalImage)
        
        return boxes.xyxy, croppedImage
    
    def _get_bboxClass_char(self, imgCroppedPlate, classList):
        boxChar, classC = [], []
        for imgCropped in imgCroppedPlate:
            boxes = imgCropped[0].boxes
            if len(boxes.cls) != 0:
                # print(boxes.cls)
                classId = [int(x) for x in boxes.cls.numpy()]
                # print('classId : ', classId)
                classCharacter = np.array(classList[classId])
                characterBBOX = boxes.xywh
                boxChar.append(characterBBOX)
                classC.append(classCharacter)
            # else:
            #     classCharacter = []
            #     characterBBOX = []
            
        return boxChar, classC
        