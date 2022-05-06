import cv2
import pickle

img=cv2.imread() # image name

width,height=107,48

try:
    with open('CarParkPos','rb') as f:   #image name
        posList=pickle.load(f)

except:
    posList=[]

def mouseClick(events,x,y,flags,param):
    if events==cv2.EVENT_LBUTTONDOWN:       #for drawing on frame
        posList.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:       #for deleting on frame
        for i,pos in enumerate (posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

 
        
    
    with open('CarParkPos','wb') as f:   #image name
        pickle.dump(posList,f)   

def checkParkingSpace():
        for pos in posList:
            x,y=pos
            cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)
            imgCrop=img[y:y+height,x:x+width]
            cv2.imshow(str(x+y),imgCrop)

while True:
    img=cv2.imread()
    for pos in posList:
        cv2.rectangle(img,pos(pos[0]+width,img,pos(pos[1]+height),(,),(255,0,255),2)   # width n height acc. to img
    
    cv2.imshow("Image",img)
    cv2.waitkey(1)