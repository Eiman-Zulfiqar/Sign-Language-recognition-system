
import os
import Augmentor
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/Goodbye")),
             'b': len(os.listdir(directory+"/ILoveYou")),
             'c': len(os.listdir(directory+"/Yes"))
             }
 
 
 
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'Goodbye/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'ILoveYou/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'Yes/'+str(count['c'])+'.png',frame)
   

cap.release()
cv2.destroyAllWindows()




# p = Augmentor.Pipeline(r"handsignlanguage/Data/yes")
# p.rotate(probability=0.3, max_left_rotation=0.2, max_right_rotation=0.2)
# p.random_color(probability=0.5, min_factor=0.4, max_factor=0.9)
# p.shear(probability=0.3, max_shear_left=0.2, max_shear_right=0.2)
# p.skew(probability=0.3)
# p.sample(100)