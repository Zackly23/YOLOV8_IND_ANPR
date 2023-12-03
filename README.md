# YOLOV8_IND_ANPR
Welcome to our Automatic Number Plate Recognition (ANPR) repository, powered by YOLOv8! This open-source project focuses on leveraging the state-of-the-art YOLOv8 (You Only Look Once) object detection framework to achieve efficient and accurate license plate recognition in images and videos.

## Automatic Number Plate Recognition (ANPR) using YOLOv8

This project implements an Automatic Number Plate Recognition (ANPR) system using YOLOv8, a powerful and efficient object detection model. ANPR technology enables automatic recognition of vehicle license plates from images or videos, with applications ranging from public security to traffic monitoring and parking management.

Main Features:

Automatic License Plate Detection: Utilizes YOLOv8 to automatically detect and extract license plates from images or videos.
Character Segmentation: Separates individual characters on the license plate to facilitate character recognition.
Character Recognition: Employs Optical Character Recognition (OCR) techniques to recognize the characters on the license plate.
Interactive and User-Friendly: Provides a user-friendly interface for testing the model with new images or videos.

Example Simulations:
Below are visual representations of the ANPR model in action, showcasing its ability to accurately detect and recognize license plates in various scenarios.

Simulation on Video:

![ezgif com-video-to-gif](https://github.com/Zackly23/YOLOV8_IND_ANPR/assets/65446701/10caae53-3356-48b8-9329-b03d456fa57e)

Here the ANPR system successfully identifies license plates from moving vehicles. The real-time detection capabilities of YOLOv8 ensure efficient processing even in dynamic environments

Simulation on Image

![output_sample](https://github.com/Zackly23/YOLOV8_IND_ANPR/assets/65446701/b2ee34be-570b-4624-9787-d462b3524695)

This image illustrates the model's performance in capturing and extracting license plate information from a still frame. The bounding boxes highlight the detected license plates, and subsequent character recognition provides accurate results.

How to Use:

Clone this repository to your local system.
Install the required dependencies by running pip install -r requirements.txt.
Run the main.py script to test the model with new images or videos.
Note:
Ensure you have a suitable GPU to enhance the detection speed using YOLOv8.

Contributions and Issues:
Contributions and issue reports are highly appreciated. Feel free to open new issues or submit pull requests to enhance this project.

Thank you for exploring the ANPR project using YOLOv8! We hope this project proves valuable to the community and anyone interested in automatic license plate identification.
