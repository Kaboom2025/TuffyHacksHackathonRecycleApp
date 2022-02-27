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