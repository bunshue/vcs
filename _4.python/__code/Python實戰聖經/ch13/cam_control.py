import numpy as np
import cv2
from time import sleep
import tensorflow.keras

labels = ['normal','left','right']
current_x = 300
move = 10
model = tensorflow.keras.models.load_model('left_right.h5')

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while True:
    success, image = cap.read()
    if success == True:
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = cv2.flip(image,1) #左右反轉
        img = cv2.resize(image,(224,224))
        img = np.array(img,dtype=np.float32)
        img = np.expand_dims(img,axis=0)
        img = (img/127.0) - 1 #正規化
        data[0] = img

        prediction = model.predict(data) #預測
        predicted_class = np.argmax(prediction[0], axis=-1)
        predicted_class_name = labels[predicted_class]
        print(current_x, predicted_class_name)
		
        if predicted_class_name == 'left':
            current_x -= move
            if current_x < 0:
                current_x = 0
        elif predicted_class_name == 'right':
            current_x += move
            if current_x > width:
                current_x = width
        cv2.putText(image, 'O', (current_x,100), cv2.FONT_HERSHEY_PLAIN, 0.4, (255, 0, 0), cv2.LINE_AA)
        cv2.imshow("Frame",image)
        sleep(0.2)
		           	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()	    	
