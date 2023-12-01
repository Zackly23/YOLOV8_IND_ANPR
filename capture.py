import cv2
from pathlib import Path

sourcePath = 'samples/video1.mp4'
# sourcePath = Path(sourcePath)
# print(so)
cap = cv2.VideoCapture(sourcePath)
while True:
    ret, frame = cap.read()
    print('frame : ', frame)
    
    cv2.imshow('YOLO V8 Detection', frame)   
    
    # video_output.write(frame) # Save detection video

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

video_output.release()
cap.release()
cv2.destroyAllWindows()
