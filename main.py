import PySimpleGUI as sg
import os.path
import cv2
import numpy as np
from matplotlib import pyplot as plt
import threading
# First the window layout in 2 columns
specgraphout=[[]]
def spectrum(filename):
    global specgraphout
    print("reached")
    print(filename)
    img = cv2.imread(filename)
    specgraph = np.zeros(img.shape, np.uint8)
    print(img.shape[1])
    print()
    for i in range (img.shape[1]):
        print(i)
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
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

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
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            th = threading.Thread(target=spectrum, args=(filename, ))
            th.start()
            th.join()
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(data=cv2.imencode('.png', specgraphout)[1].tobytes())

        except:
            pass

window.close()
