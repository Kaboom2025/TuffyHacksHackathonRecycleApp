import cv2
import numpy as np
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--webcam', help="True/False", default=False)
parser.add_argument('--play_video', help="Tue/False", default=False)
parser.add_argument('--image', help="Tue/False", default=False)
parser.add_argument('--video_path', help="Path of video file", default="videos/car_on_road.mp4")
parser.add_argument('--image_path', help="Path of image to detect objects", default="Images/bicycle.jpg")
parser.add_argument('--verbose', help="To print statements", default=True)
args = parser.parse_args()


# Load yolo
def load_yolo():
    net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    output_layers = [layer_name for layer_name in net.getUnconnectedOutLayersNames()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    return net, classes, colors, output_layers


def load_image(img_path):
    # image loading
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape
    return img, height, width, channels


"""def start_webcam():
    cap = cv2.VideoCapture(0)

    return cap"""


def display_blob(blob):
    '''
        Three images each for RED, GREEN, BLUE channel
    '''
    for b in blob:
        for n, imgb in enumerate(b):
            cv2.imshow(str(n), imgb)


def detect_objects(img, net, outputLayers):
    blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(outputLayers)
    return blob, outputs


def get_box_dimensions(outputs, height, width):
    boxes = []
    confs = []
    class_ids = []
    for output in outputs:
        for detect in output:
            scores = detect[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]
            if conf > 0.3:
                center_x = int(detect[0] * width)
                center_y = int(detect[1] * height)
                w = int(detect[2] * width)
                h = int(detect[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confs.append(float(conf))
                class_ids.append(class_id)
    return boxes, confs, class_ids


def draw_labels(boxes, confs, colors, class_ids, classes, img):
    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
    cv2.imshow("Image", img)


def image_detect(img_path):
    model, classes, colors, output_layers = load_yolo()
    image, height, width, channels = load_image(img_path)
    blob, outputs = detect_objects(image, model, output_layers)
    boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
    draw_labels(boxes, confs, colors, class_ids, classes, image)
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break


"""def webcam_detect():
    model, classes, colors, output_layers = load_yolo()
    cap = start_webcam()
    while True:
        _, frame = cap.read()
        height, width, channels = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
        draw_labels(boxes, confs, colors, class_ids, classes, frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()"""


"""def start_video(video_path):
    model, classes, colors, output_layers = load_yolo()
    cap = cv2.VideoCapture(video_path)
    while True:
        _, frame = cap.read()
        height, width, channels = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
        draw_labels(boxes, confs, colors, class_ids, classes, frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()"""


if __name__ == '__main__':
    webcam = args.webcam
    video_play = args.play_video
    image = args.image
    if webcam:
        if args.verbose:
            print('---- Starting Web Cam object detection ----')
        webcam_detect()
    if video_play:
        video_path = args.video_path
        if args.verbose:
            print('Opening ' + video_path + " .... ")
        start_video(video_path)
    if image:
        image_path = args.image_path
        if args.verbose:
            print("Opening " + image_path + " .... ")
        image_detect(image_path)
        

    cv2.destroyAllWindows()







    import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate('tuffyhackssaalik-firebase-adminsdk-hjmm1-c961cf6521.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


labels = ['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
image_path = ""

class User:
    def __init__(self):
        email = input("enter email: ")
        password = input("enter password")
        wallid = input("walletID:    ")
        user = auth.create_user(email=email, password=password)
        self.user = user
        CONVERSONRATE = 1 #tokens * x to get $
        """data = {
            u'WalletID': wallid,
            u'TokensGiven': 0
        }"""
        #ref =  db.collection(u'Users').document(user.uid)
        #db.collection(u'Users').document(u'WalletIDs').set(data)
    def getWallID(self):
        return wallid
    def imagetoLabel(self, image_path):
        return ("bottle")
    def labelToValue(self, label):
        value = labels.index()+1
        return value
    def sendmoney(self, value, walletID):
        sendTokens(labelToValue(imagetoLabel()), getWallID())


u1 = User()
u1.imagetoLabel(image_path)
val = u1.labelToValue(u1.imagetoLabel())
u1.sendmoney()



def sendTokens(value, walletID):
    print("Sending " + value + "TuffyTokens to " + walletID)
    print("Sending..")
    import time

    for i in range(101):
        print("Sending " + i + "%")
        time.sleep(.06)
    print("Transation Complete")