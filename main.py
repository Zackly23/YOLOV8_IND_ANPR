import os
import cv2
import argparse

from configs.config import Configuration
from scripts.charExtraction import CharExtraction
from scripts.bboxAnnotator import BBOXAnnotator
from scripts.extractor import CharExtractor

def outputFolder():
    outputFolder = os.path.join(os.getcwd(), "runs\detect")    
    listDir = os.listdir(outputFolder)
    filteredFolder = list(filter(lambda file_name: not os.path.splitext(file_name)[1], listDir))
    
    numFolder = len(filteredFolder)
    nameFolder = "predict"+str(numFolder + 1)
    outputDir = os.path.join(outputFolder, nameFolder)
    os.mkdir(outputDir)
    # print("Elemen tanpa ekstensi:", filtered_list)
    
    return outputDir

def main(extractor, annotator, sourcePath, stream=False, video=False, save=False):
    if save:
        outputDirectory = outputFolder()
        
    if stream == True:
        if video == True:     
            cap = cv2.VideoCapture(sourcePath)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Format codec video, bisa disesuaikan dengan format yang diinginkan
            fps = int(cap.get(cv2.CAP_PROP_FPS))  # FPS dari video asli

            # Ukuran frame video (sesuaikan dengan frame hasil pemrosesan Anda)
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            if save:
                output_path = outputDirectory +'\output_video.mp4'  # Ganti 'output_video.mp4' dengan nama berkas keluaran Anda
                # Buat objek VideoWriter
                video_output = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
        else:
            cap = cv2.VideoCapture(0)
        
        tempPlateNum = []
        while True:
            ret, frame = cap.read()
            
            bbox, plateNum = extractor.predict(image=frame)

            annotateImg, plateNum = annotator.draw_bbox(frame, bbox, plateNum)
    
            cv2.imshow('YOLO V8 Detection', annotateImg)
            
            if save:
                tempPlateNum.append(plateNum)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        
            # print('tempPlateNum : ',tempPlateNum)
        
        
        video_output.release()
        cap.release()
        cv2.destroyAllWindows()
        
    else:
        frame = cv2.imread(sourcePath)
        bbox, plateNum = extractor.predict(image=frame)
        annotateImg, plateNum = annotator.draw_bbox(frame, bbox, plateNum)
        print('annotate : ', annotateImg)
        cv2.imshow('Licence Plat Number Recognition', annotateImg)
        if save:
            text_file = open(outputDirectory+'\platenumber.txt', 'w')
            # print('direct txt: ', outputDirectory+'\platenumber.txt')
            text_file.write(plateNum)
            text_file.close()
            cv2.imwrite(outputDirectory+"\prediction.jpg", annotateImg)
            
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Contoh program dengan argparse')

    # Argumen path video
    parser.add_argument('--source', type=str, help='Path ke berkas video/gambar')
    # Argumen bool stream
    parser.add_argument('--conf', type=float, help='Confidence score')
    # Argumen bool stream
    parser.add_argument('--stream', action='store_true', help='Gunakan ini jika Anda ingin streaming dari kamera')
    # Argumen bool video
    parser.add_argument('--video', action='store_true', help='Gunakan ini jika Anda ingin memproses berkas video')
    #Argumen bool menyimpan hasil prediksi
    parser.add_argument('--save', action='store_true', help='Gunakan ini jika Anda ingin menyimpan hasil prediksi')

    # Parsing argumen dari baris perintah
    args = parser.parse_args()
    
    wPathPlat = Configuration['weightPlatDir']
    wPathChar = Configuration['weightCharDir']
    classList = Configuration['classListCharacter']
    sizePlat = Configuration['sizePlat']
    imageSample = Configuration['imageSample']
    
    extractor = CharExtraction(wPlatePath=wPathPlat, wCharacterPath=wPathChar, classList=classList,
                               sizePlate=sizePlat, conf=args.conf)
    annotator = BBOXAnnotator()
    
    main(extractor, annotator, args.source, args.stream, args.video, args.save)