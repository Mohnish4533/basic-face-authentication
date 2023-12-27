#captured image

def Image_Capture(use):                                 # use --> R: register, A: Authentication

    import cv2                                          #work with images
    import uuid                                         #gives unique identification to images
    from PIL import Image                               #display images module
    from FUNCTIONS import FluidText, delete_image       #importing my own program for designing 
    
    cap = cv2.VideoCapture(0)                            #accesses computers camera
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))       #width of frame
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))     #height of frame

    junkname = None
    regname = None 
    imgname = None
    frame = None
    filename = None

    while True:
        ret, frame = cap.read()
        cv2.imshow('video', frame)
        PressedKey = cv2.waitKey(1) & 0xFF

        if PressedKey == ord('c'):
            filename = str(uuid.uuid1())
            junkname = './JUNK/{}.jpg'.format(filename)
            #print(junkname)
            cv2.imwrite(junkname, frame)

            if use == 'R':
                regname = './Registration/{}.jpg'.format(filename)
                TheFrame = frame
            if use == 'A':
                imgname = './Authentication/{}.jpg'.format(filename)
                TheFrame = frame

            picture = Image.open(junkname)
            picture.show()

        if PressedKey == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if use == 'R':
        return junkname, regname, TheFrame
    if use == 'A':
        return junkname, imgname, TheFrame



