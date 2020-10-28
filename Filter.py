import cv2
faces=cv2.CascadeClassifier("a.xml")
eye_mask=cv2.imread("masking.png",-1)
glasses=cv2.imread("black_glass.png",-1)
thug_chain=cv2.imread("chain.png",-1)
batman=cv2.imread("krish.png",-1)
cap=cv2.imread("cap.png",-1)
print("1) Mask")
print("2) Thug Chain")
print("3) Thug Glasses")
print("4) Krish")
print("5) cap")
choice=int(input("Enter the Choice"))
eye_mask=cv2.resize(eye_mask,(500,500))
def functy(src,overlay,pos=(0,0),scale=1):
    overlay=cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    h,w,_=overlay.shape
    rows,cols,_=src.shape
    y,x,=pos[0],pos[1]
    for i in range(h):
        for j in range(w):
            if x+i>=rows and y+j>=cols:
                continue
            alpha=float(overlay[i][j][3]/255.0)
            src[x+i][y+j]=alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]
    return src
capture=cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=faces.detectMultiScale(gray,1.3,5,0,(120,120),(350,350))
    for (x,y,w,h) in face:
        mask_min=int(y+1*h/5)
        mask_max=int(y+6.3*h/5)
        mask=mask_max-mask_min
        glass_min=int(y+1.5*h/5)
        glass_max=int(y+2.9*h/5)
        specy=glass_max-glass_min
        chain_min=int(y+5*h/5)
        chain_max=int(y+8*h/5)
        joker_min=int(y+2)
        joker_max=int(y+4.5*h/5)
        joker=joker_max-joker_min
        chain=chain_max-chain_min
        hat_min=int(y-50)
        hat_max=int(y+1.5*h/5)
        hat=hat_max-hat_min
        hat_face=frame[hat_min:hat_max,x:x+w]
        chain_face=frame[chain_min:chain_max,x:x+w]
        face_mask=frame[mask_min:mask_max,x:x+w]
        glass_mask=frame[glass_min:glass_max,x:x+w]
        joker_face=frame[joker_min:joker_max,x:x+w]
        masky=cv2.resize(eye_mask,(w,mask),interpolation=cv2.INTER_CUBIC)
        glassy=cv2.resize(glasses,(w,specy),interpolation=cv2.INTER_CUBIC)
        chain_pro=cv2.resize(thug_chain,(w,chain),interpolation=cv2.INTER_CUBIC)
        joker_pro=cv2.resize(batman,(w,joker),interpolation=cv2.INTER_CUBIC)
        hat_pro=cv2.resize(cap,(w,hat),interpolation=cv2.INTER_CUBIC)
        if choice==1:
            functy(face_mask,masky)
        elif choice==2:
            functy(chain_face,chain_pro)
        elif choice==3:
            functy(glass_mask,glassy)
        elif choice==5:
            functy(hat_face,hat_pro)
            functy(glass_mask, glassy)
        else:
            functy(joker_face,joker_pro)
        cv2.imshow("Frame",frame)
    if cv2.waitKey(1)==13:
        break

capture.release()
cv2.destroyAllWindows()