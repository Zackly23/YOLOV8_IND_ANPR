import numpy as np
import cv2

class BBOXAnnotator:
    def draw_bbox(self, ImgPath, bboxPlate, plateNumber):
        img = ImgPath

        for idc, bb in enumerate(bboxPlate):
            # print('bboxp : ', bboxp)
            # print('bb : ', bb)
            x1, y1, x2, y2 = map(int, bb)  # Ubah koordinat ke dalam integer
            color = (0, 255, 0)  # Warna bounding box (hijau)
            thickness = 2  # Ketebalan garis bounding box

            # Gambar bounding box pada gambar
            cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

            # Tambahkan label nama di atas bounding box
            if len(plateNumber) == len(bboxPlate):
                print('plateNumber : ', plateNumber)
                # print('idc : ', idc)
                cv2.putText(img, plateNumber[idc], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)
            
        return img, plateNumber[0]