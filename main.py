import PySimpleGUI as sg
import os.path
import cv2
import numpy as np
from matplotlib import pyplot as plt
import threading
import math
# First the window layout in 2 columns
specgraphout=[[]]
adlines=[[]]
elementsin=[]
speed=0
type=""
Mass=""
time=0
def spectrum(filename): #Get spectrum drawing
    global specgraphout
    img = cv2.imread(filename)
    specgraph = np.zeros(img.shape, np.uint8)
    for i in range (img.shape[1]):
        redval=img[int(img.shape[0]/2)][i][2]
        redhieght=(redval*181)/255
        greenval=img[int(img.shape[0]/2)][i][1]
        greenhieght=(greenval*181)/255
        blueval=img[int(img.shape[0]/2)][i][0]
        bluehieght=(blueval*181)/255
        specgraph = cv2.circle(specgraph,(i,int(181-redhieght)), 1, (0,0,255), -1)
        specgraph = cv2.circle(specgraph,(i,int(181-greenhieght)), 1, (0,255,0), -1)
        specgraph = cv2.circle(specgraph,(i,int(181-bluehieght)), 1, (255,0,0), -1)
    specgraphout=specgraph

def getadlines(filename,blur): #Adsorptionlines
    img1 = cv2.imread(filename)
    img=cv2.medianBlur(img1,blur)
    global adlines
    specgraph = np.zeros(img.shape, np.uint8)
    adred=[]
    adblue=[]
    adgreen=[]
    for i in range (3,img.shape[1]-3):
        redval=img[0,i,2]
        redhieght=(redval*181)/255
        greenval=img[0,i,1]
        greenhieght=(greenval*181)/255
        blueval=img[0,i,0]
        bluehieght=(blueval*181)/255
        redprevdif=int(img[0,i,2])-int(img[0,i-3,2])
        redaheadvdif=int(img[0,i,2])-int(img[0,i+3,2])
        greenprevdif=int(img[0,i,1])-int(img[0,i-3,1])
        greenaheadvdif=int(img[0,i,1])-int(img[0,i+3,1])
        blprevdif=int(img[0,i,0])-int(img[0,i-3,0])
        blaheadvdif=int(img[0,i,0])-int(img[0,i+3,0])

        y=0
        if redprevdif < y and redaheadvdif < y:
            adred.append(i)
            #adred.append(i+1)
            #adred.append(i+2)
            #adred.append(i-1)
            #adred.append(i-2)

        if greenprevdif < y and greenaheadvdif < y:
            adgreen.append(i)
            #adgreen.append(i+1)
            #adgreen.append(i+2)
            #adgreen.append(i-1)
            #adgreen.append(i-2)


        if blprevdif < y and blaheadvdif < y:
            adblue.append(i)
            #adblue.append(i+1)
            #adblue.append(i+2)
            #adblue.append(i-1)
            #adblue.append(i-2)

        specgraph = cv2.circle(specgraph,(i,int(181-redhieght)), 1, (0,0,255), -1)
        specgraph = cv2.circle(specgraph,(i,int(181-greenhieght)), 1, (0,255,0), -1)
        specgraph = cv2.circle(specgraph,(i,int(181-bluehieght)), 1, (255,0,0), -1)
    for i in range (2,img.shape[1]-2):
        if i in adgreen and i in adred:
            specgraph = cv2.line(specgraph,(i,0),(i,181),(0,255,255),1)
        if i in adgreen and i in adblue:
            specgraph = cv2.line(specgraph,(i,0),(i,181),(0,255,255),1)
        if i in adblue and i in adred:
            specgraph = cv2.line(specgraph,(i,0),(i,181),(0,255,255),1)
        if (img[0,i,2]+img[0,i,1])<10 and i in adblue:
            specgraph = cv2.line(specgraph,(i,0),(i,181),(0,255,255),1)
    adlines=specgraph


def elements(filename,start,end,blur):
    global elementsin
    img1 = cv2.imread(filename)
    img=cv2.medianBlur(img1,blur)
    adlinesfinal=[]
    specgraph = np.zeros(img.shape, np.uint8)
    adred=[]
    adblue=[]
    adgreen=[]
    wavelength=[]
    for i in range (3,img.shape[1]-3):
        redval=img[0,i,2]
        redhieght=(redval*181)/255
        greenval=img[0,i,1]
        greenhieght=(greenval*181)/255
        blueval=img[0,i,0]
        bluehieght=(blueval*181)/255
        redprevdif=int(img[0,i,2])-int(img[0,i-3,2])
        redaheadvdif=int(img[0,i,2])-int(img[0,i+3,2])
        greenprevdif=int(img[0,i,1])-int(img[0,i-3,1])
        greenaheadvdif=int(img[0,i,1])-int(img[0,i+3,1])
        blprevdif=int(img[0,i,0])-int(img[0,i-3,0])
        blaheadvdif=int(img[0,i,0])-int(img[0,i+3,0])

        y=0
        if redprevdif < y and redaheadvdif < y:
            adred.append(i)
            #adred.append(i+1)
            #adred.append(i+2)
            #adred.append(i-1)
            #adred.append(i-2)

        if greenprevdif < y and greenaheadvdif < y:
            adgreen.append(i)
            #adgreen.append(i+1)
            #adgreen.append(i+2)
            #adgreen.append(i-1)
            #adgreen.append(i-2)


        if blprevdif < y and blaheadvdif < y:
            adblue.append(i)
            #adblue.append(i+1)
            #adblue.append(i+2)
            #adblue.append(i-1)
            #adblue.append(i-2)



    for i in range (2,img.shape[1]-2):
        if i in adgreen and i in adred:
            adlinesfinal.append(i)
        if i in adgreen and i in adblue:
            adlinesfinal.append(i)
        if i in adblue and i in adred:
            adlinesfinal.append(i)
        if (img[0,i,2]+img[0,i,1])<10 and i in adblue:
            adlinesfinal.append(i)
        if (img[0,i,0]+img[0,i,1])<10 and i in adred:
            adlinesfinal.append(i)
        if (img[0,i,2]+img[0,i,0])<10 and i in adgreen:
            adlinesfinal.append(i)
    H=0
    Fe=0
    Mn=0
    He=0
    Heion=0
    CN=0
    Na=0
    TiO=0
    CaH=0
    for i in range(len(adlinesfinal)):
        wavelenght=((float(end)-float(start))*adlinesfinal[i])/int(img1.shape[1])
        wavelenght+=float(start)

        wavelength.append(wavelenght)

    for i in range(len(wavelength)):
        if wavelength[i]<=661 and wavelength[i]>=649: #656
            H+=1
        if wavelength[i]<=409 and wavelength[i]>=400: #404.5
            Fe+=1
            Mn+=1
        if wavelength[i]<=425 and wavelength[i]>=415:
            He+=1
        if wavelength[i]<=445 and wavelength[i]>=435:
            Heion+=1
        if wavelength[i]<=430 and wavelength[i]>=420:
            CN+=1
        if wavelength[i]<=594 and wavelength[i]>=584:
            Na+=1
        if wavelength[i]<=634 and wavelength[i]>=624:
            TiO+=1
        if wavelength[i]<=639 and wavelength[i]>=632:
            CaH+=1
    if  H>=2:
        elementsin.append("Hydrogen")
    if  He>=2:
        elementsin.append("Helium")
    if  Fe>=2:
        elementsin.append("Iron")
    if  Mn>=2:
        elementsin.append("Mn")
    if  Heion>=2:
        elementsin.append("Helium")
    if  CN>=2:
        elementsin.append("CNradical")
    if  TiO>=2:
        elementsin.append("TiO")
    if CaH>=2:
        elementsin.append("CaH")
def speed(filename,start,end,blur):
    global speed
    img1 = cv2.imread(filename)
    img=cv2.medianBlur(img1,blur)
    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)



    adlinesfinal=[]
    specgraph = np.zeros(img.shape, np.uint8)
    adred=[]
    adblue=[]
    adgreen=[]
    wavelength=[]
    for i in range (3,img.shape[1]-3):
        redval=img[0,i,2]
        redhieght=(redval*181)/255
        greenval=img[0,i,1]
        greenhieght=(greenval*181)/255
        blueval=img[0,i,0]
        bluehieght=(blueval*181)/255
        redprevdif=int(img[0,i,2])-int(img[0,i-3,2])
        redaheadvdif=int(img[0,i,2])-int(img[0,i+3,2])
        greenprevdif=int(img[0,i,1])-int(img[0,i-3,1])
        greenaheadvdif=int(img[0,i,1])-int(img[0,i+3,1])
        blprevdif=int(img[0,i,0])-int(img[0,i-3,0])
        blaheadvdif=int(img[0,i,0])-int(img[0,i+3,0])

        y=0
        if redprevdif < y and redaheadvdif < y:
            adred.append(i)
            #adred.append(i+1)
            #adred.append(i+2)
            #adred.append(i-1)
            #adred.append(i-2)

        if greenprevdif < y and greenaheadvdif < y:
            adgreen.append(i)
            #adgreen.append(i+1)
            #adgreen.append(i+2)
            #adgreen.append(i-1)
            #adgreen.append(i-2)


        if blprevdif < y and blaheadvdif < y:
            adblue.append(i)
            #adblue.append(i+1)
            #adblue.append(i+2)
            #adblue.append(i-1)
            #adblue.append(i-2)


    for i in range (2,img.shape[1]-2):
        if i in adgreen and i in adred:
            adlinesfinal.append(i)
        if i in adgreen and i in adblue:
            adlinesfinal.append(i)
        if i in adblue and i in adred:
            adlinesfinal.append(i)
        if (img[0,i,2]+img[0,i,1])<10 and i in adblue:
            adlinesfinal.append(i)
        if (img[0,i,0]+img[0,i,1])<10 and i in adred:
            adlinesfinal.append(i)
        if (img[0,i,2]+img[0,i,0])<10 and i in adgreen:
            adlinesfinal.append(i)
    H=[]
    Fe=[]
    Mn=[]
    He=[]
    Heion=[]
    CN=[]
    Na=[]
    TiO=[]
    CaH=[]
    dopplershift=0
    for i in range(len(adlinesfinal)):
        wavelenght=((float(end)-float(start))*adlinesfinal[i])/int(img1.shape[1])
        wavelenght+=float(start)
        wavelength.append(wavelenght)
    for i in range(len(wavelength)):
        if wavelength[i]<=660 and wavelength[i]>=652: #656
            H.append(wavelength[i])
        if wavelength[i]<=408 and wavelength[i]>=400: #404.5
            Fe.append(wavelength[i])
            Mn.append(wavelength[i])
        if wavelength[i]<=425 and wavelength[i]>=417:
            He.append(wavelength[i])
        if wavelength[i]<=444 and wavelength[i]>=434:
            Heion.append(wavelength[i])
        if wavelength[i]<=429 and wavelength[i]>=421:
            CN.append(wavelength[i])
        if wavelength[i]<=593 and wavelength[i]>=585:
            Na.append(wavelength[i])
        if wavelength[i]<=635 and wavelength[i]>=629:
            TiO.append(wavelength[i])
        if wavelength[i]<=639 and wavelength[i]>=633:
            CaH.append(wavelength[i])
    val=max(len(CaH),len(H),len(Fe),len(Heion),len(CN),len(Na),len(TiO))
    if val==len(TiO):
        avg=sum(TiO)/len(TiO)
        dopplershift=(avg-632)/632
    if val==len(H):
        avg=sum(H)/len(H)
        dopplershift=(avg-656.3)/656.3
    if val==len(He):
        avg=sum(He)/len(He)
        dopplershift=(avg-421)/421
    if val==len(Fe):
        avg=sum(Fe)/len(Fe)
        dopplershift=(avg-404.5)/404.5
    if val==len(Heion):
        avg=sum(Heion)/len(Heion)
        dopplershift=(avg-440)/440
    if val==len(Na):
        avg=sum(Na)/len(Na)
        dopplershift=(avg-588.9)/588.9
    if val==len(CaH):
        avg=sum(CaH)/len(CaH)
        dopplershift=(avg-634)/634
    if val==len(CN):
        avg=sum(CN)/len(CN)
        dopplershift=(avg-420)/420

    c=300000000
    vs=c*dopplershift
    speed=vs

def getwieght(filename):
    global type
    global Mass
    star=cv2.imread(filename)
    Gstar=cv2.imread("Gstar.png")
    Astar=cv2.imread("Astar.png")
    Kstar=cv2.imread("Kstar.png")
    Ostar=cv2.imread("Ostar.png")
    Fstar=cv2.imread("Fstar.png")
    Mstar=cv2.imread("M.png")
    Bstar=cv2.imread("Bstar.png")
    tempG1=Gstar[20:140:,20:300,:]
    tempG2=Gstar[20:140:,500:600,:]
    tempA1=Astar[20:140,20:300,:]
    tempA2=Astar[20:140:,500:600,:]
    tempF1=Fstar[20:140:,20:300,:]
    tempF2=Fstar[20:140:,500:600,:]
    tempO1=Ostar[20:140:,20:300,:]
    tempO2=Ostar[20:140:,500:600,:]
    tempM1=Mstar[20:140:,20:300,:]
    tempM2=Mstar[20:140:,500:600,:]
    tempB1=Bstar[20:140,20:300,:]
    tempB2=Bstar[20:140:,500:600,:]
    tempK1=Kstar[20:140:,20:300,:]
    tempK2=Kstar[20:140:,500:600,:]
    method = 'cv2.TM_CCOEFF_NORMED'
    method = eval(method)

    # Apply template Matching
    resG1 = cv2.matchTemplate(star,tempG1,method)
    min_val, max_valG1, min_loc, max_loc = cv2.minMaxLoc(resG1)
    resG2 = cv2.matchTemplate(star,tempG2,method)
    min_val, max_valG2, min_loc, max_loc = cv2.minMaxLoc(resG2)
    resA1 = cv2.matchTemplate(star,tempA1,method)
    min_val, max_valA1, min_loc, max_loc = cv2.minMaxLoc(resA1)
    resA2 = cv2.matchTemplate(star,tempA2,method)
    min_val, max_valA2, min_loc, max_loc = cv2.minMaxLoc(resA2)
    resM1 = cv2.matchTemplate(star,tempM1,method)
    min_val, max_valM1, min_loc, max_loc = cv2.minMaxLoc(resM1)
    resM2 = cv2.matchTemplate(star,tempM2,method)
    min_val, max_valM2, min_loc, max_loc = cv2.minMaxLoc(resM2)
    resF1 = cv2.matchTemplate(star,tempF1,method)
    min_val, max_valF1, min_loc, max_loc = cv2.minMaxLoc(resF1)
    resF2 = cv2.matchTemplate(star,tempF2,method)
    min_val, max_valF2, min_loc, max_loc = cv2.minMaxLoc(resF2)
    resO1 = cv2.matchTemplate(star,tempO1,method)
    min_val, max_valO1, min_loc, max_loc = cv2.minMaxLoc(resO1)
    resO2 = cv2.matchTemplate(star,tempO2,method)
    min_val, max_valO2, min_loc, max_loc = cv2.minMaxLoc(resO2)
    resB1 = cv2.matchTemplate(star,tempB1,method)
    min_val, max_valB1, min_loc, max_loc = cv2.minMaxLoc(resB1)
    resB2 = cv2.matchTemplate(star,tempB2,method)
    min_val, max_valB2, min_loc, max_loc = cv2.minMaxLoc(resB2)
    resK1 = cv2.matchTemplate(star,tempK1,method)
    min_val, max_valK1, min_loc, max_loc = cv2.minMaxLoc(resK1)
    resK2 = cv2.matchTemplate(star,tempK2,method)
    min_val, max_valK2, min_loc, max_loc = cv2.minMaxLoc(resK2)


    top_left = max_loc
    #bottom_right = (top_left[0] + w, top_left[1] + hA1)


    if max_valG1 + max_valG2  >=1.999:
        type="G"
        Mass="1.4 to 2.1 times the mass of the Sun surface\n temperatures between 7600 and 10,000 K"



    if max_valA1 + max_valA2  >=1.999:
        type="A"
        Mass="2.40-1.62 Sun Mass\n9727-711K"

    if max_valM1 + max_valM2  >=1.999:
        type="M"
        Mass="2,400–3,700 K\n0.08–0.45 sun mass"


    if max_valF1 + max_valF2  >=1.999:
        type="F"
        Mass="	6,000–7,500 K\n1.04–1.4 sun mass"


    if max_valO1 + max_valO2  >=1.999:
        type="O"
        type="temperatures in excess of 30,000 kelvin\nO-type stars range from 10,000 times the Sun to around 1,000,000 times,\ngiants from 100,000 times the Sun to over 1,000,000, and supergiants from about 200,000 times the Sun to several million times"


    if max_valB1 + max_valB2  >=1.999:
        type="B"
        Mass= "upto 16 times the mass of the Sun\nsurface temperatures between 10,000 and 30,000 K"

    if max_valK1 + max_valK2  >=1.999:
        type="K"
        Mass="3,700–5,200 K\n0.45–0.8 sun mass"


def gettime(a1,a2,left,right,timedef):
    global time
    distance=math.sqrt((a1-a2)**2)
    distance1=math.sqrt((left-right)**2)
    time=(timedef*distance1*3.14)/distance







file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(22, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Text("For Image",text_color="#FFFF00",)],
    [sg.Button("OK")],
    [sg.Slider(range=(1,8),
         default_value=4,
         size=(20,15),
         orientation='horizontal',
         font=('Helvetica', 12),
         key="-BLUR-"),],
    [sg.Button("Done")],
    [sg.Text("Start frequency")],
    [sg.InputText(key='-Start-',
    size=(20,15))],
    [sg.Text("End frequency")],
    [sg.InputText(key='-End-',
    size=(20,15))],
    [sg.Submit(), sg.Cancel()],
    [sg.Text("For video",text_color="#FFFF00",)],
    [sg.Text("time")],
    [sg.InputText(key='-time-',
    size=(20,15))],
    [sg.Submit(), sg.Cancel()],

]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout, resizable=True)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif",".mp4"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox

        filename = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
        )

        window["-TOUT-"].update(filename)
        if filename[-4:]==".png" or filename[-4:]==".jpg" or filename[-4:]==".jpeg":
            th = threading.Thread(target=spectrum, args=(filename, ))
            th.start()
            th.join()
            window["-IMAGE-"].update(data=cv2.imencode('.png', specgraphout)[1].tobytes())
            event, values = window.read()
            if event=="OK":
                print ("click")
                t = threading.Thread(target=getadlines, args=(filename,7 ))
                t.start()
                t.join()
                window["-IMAGE-"].update(data=cv2.imencode('.png', adlines)[1].tobytes())
            i=0
            test=1
            val=7
            while True:
                event, values = window.read(timeout=20)
                if event == "Exit" or event == sg.WIN_CLOSED:
                    break
                test= val - values["-BLUR-"]
                if test!=0:
                    val = values["-BLUR-"]
                    val=(int(val)*2)-1
                    t1 = threading.Thread(target=getadlines, args=(filename,val ))
                    t1.start()
                    t1.join()
                    window["-IMAGE-"].update(data=cv2.imencode('.png', adlines)[1].tobytes())
                    if event=="Done":
                        break
            event, values = window.read()
            start=values["-Start-"]
            end=values["-End-"]
            t1 = threading.Thread(target=elements, args=(filename,start,end,val ))
            t1.start()
            t1.join()
            todisplay="elements present:"
            for i in range (len(elementsin)):
                todisplay=todisplay+elementsin[i]+" ,"
            t1 = threading.Thread(target=speed, args=(filename,start,end,val ))
            t1.start()
            t1.join()
            todisplay=todisplay+"\n"+"speed:"+str(speed)
            t1 = threading.Thread(target=getwieght, args=(filename, ))
            t1.start()
            t1.join()
            todisplay=todisplay+"\n"+"type:"+type+"\n"+"Info: "+Mass
            sg.popup('Output',todisplay)
        elif filename[-4:]==".mp4":
            cap = cv2.VideoCapture(filename)

            # take first frame of the video
            ret,frame1 = cap.read()
            frame = cv2.flip(frame1, 0)
            img=cv2.imread('latest_512_0304.jpg',0)
            #current = cv2.imread('Cstar.png')
            blur = cv2.GaussianBlur(img,(35,35),0)
            previousimg = cv2.imread('latest_512_0304.jpg')
            img1 = cv2.imread('latest_512_0304.jpg',1)
            ret,thresh = cv2.threshold(blur,20,255,0)
            thresh1 =cv2.bitwise_not(thresh)
            contours,hierarchy = cv2.findContours(thresh1, 1, 2)
            x=3.9
            cnt = contours[0]
            leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
            rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
            topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
            bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
            leftmost=(int(leftmost[0]*(x+0.1)),int(leftmost[1]*x))
            rightmost=(int(rightmost[0]*(x+0.1)),int(rightmost[1]*x))
            bottommost=(int(bottommost[0]*(x+0.1)),int(bottommost[1]*x))
            topmost=(int(topmost[0]*(x+0.1)),int(topmost[1]*x))





            window["-IMAGE-"].update(data=cv2.imencode('.png', img1)[1].tobytes())


            # setup initial location of window
            r,h,c,w = 400,100,300,100  # simply hardcoded the values
            track_window = (c,r,w,h)

            # set up the ROI for tracking
            roi = frame[r:r+h, c:c+w]
            hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
            roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
            cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

            # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
            term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
            i=1
            s=0
            while(1):
                print("i")
                ret ,frame = cap.read()
                frame = cv2.flip(frame, 0)



                if ret == True:
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

                    # apply meanshift to get the new location
                    ret, track_window = cv2.meanShift(dst, track_window, term_crit)

                    # Draw it on image
                    x,y,w,h = track_window
                    if s==0:
                        x1,y1=x,y
                        s+=1

                else:

                    break
            x2=x
            event, values = window.read()
            timedef=int(values["-time-"])
            t3 = threading.Thread(target=gettime, args=(x1,x2,leftmost[0],rightmost[0],timedef ))
            t3.start()
            t3.join()
            days=time/24
            days=str(days)+" days"
            sg.popup('Output',days)





window.close()
