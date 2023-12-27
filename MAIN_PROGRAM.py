#Main Program 

from FUNCTIONS import *
from CAPTURE_IMAGE import *
from AUTHENTICATION import *
from PIL import Image
import cv2

while True:

    option = 0
    name = None
    Reg_Result = False
    A_Result = False
    Registered_check = False
    Array_Name, Array_Img = retrieve()
    #print(Array_Name, Array_Img)

    line = "WELCOME TO THE EXAM PAGE...\n"
    Design(line)
    line = "Choose your option:\n1. New candidate registration\n2. Take exam\n3. close page\n"
    Design(line)
    while option != 1 and option != 2 and option != 3:
        option = int(input("Enter option(1 or 2 or 3):"))

    if option == 1:
        line = "User Registration.....\n"
        Design(line)
        TimeDelay(1)

        while name == None or Reg_Result == False:
            line = "Please Enter Your Full Name:"
            FluidText(line)
            name = input()
            Reg_Result = TypeCheck(name)

        line = "\n-->Press C to capture photo.\n-->If photo is fine close the image and press Q to quit video screen.\n"
        Design(line)
        line = "enter any key after reading to proceed"
        FluidText(line)
        input()
        junkname, regname, frame = Image_Capture('R')

        if junkname == None:
            line = "no image taken. Thank You.\n"
            FluidText(line)
        else:
            line = "please hit enter to check if u want to continue with this photo.\nClose the photo to come back to this page\n"
            FluidText(line)
            input()
            LatestImage = Image.open(junkname)
            LatestImage.show()

            line = "Type '1' if u want this image to be registered\n"
            FluidText(line)
            line = "Type '2' if u dont want it to be registered.\n"
            FluidText(line)
            option = input("option 1 or 2:")

            if option == "1":
                cv2.imwrite(regname, frame)
                Array_Name.append(name)
                Array_Img.append(regname)
                #print(Array_Name, Array_Img)
                save(Array_Name, Array_Img)
            else:
                line = "Did not register. Thank you."
                FluidText(line)

    elif option == 2:
        line = "User authentication.....\n"
        Design(line)
        TimeDelay(1)

        while name == None or A_Result == False:
            line = "Please Enter Your Full Name (as per your hall ticket):"
            FluidText(line)
            name = input()
            A_Result = TypeCheck(name)
            #print("A_result=", A_Result)
            Registered_check,index = PresenceCheck(Array_Name, name)
            #print(Registered_check, index)
            if Registered_check == False:
                line = "Sorry. U have not registered under the name {}\n".format(name)
                FluidText(line)
                break

        if Registered_check == True:
            line = "\n-->Press C to capture photo.\n-->If photo is fine close the image and press Q to quit video screen.\n"
            Design(line)
            line = "enter any key after reading to proceed"
            FluidText(line)
            input()
            junkname, imgname, frame = Image_Capture('A')

            if junkname == None:
                line = "no image taken. Thank You.\n"
                FluidText(line)
            else:
                line = "please hit enter to check if u want to continue with this photo.\nClose the photo to come back to this page\n"
                FluidText(line)
                input()
                LatestImage = Image.open(junkname)
                LatestImage.show()

                line = "Type '1' if u want this to be authenticated\n"
                FluidText(line)
                line = "Type '2' if u dont want it to be authenticated.\n"
                FluidText(line)
                option = input("option 1 or 2:")

                if option == "1":
                    cv2.imwrite(imgname, frame)
                    #pic=Image.open(Array_Img[index])
                    #pic.show()
                    #pic=Image.open(imgname)
                    #pic.show()
                    #print(Array_Img[index],imgname)
                    result = Authenticate(Array_Img[index], imgname)
                    #print(result)

                    if result == [True]:
                        line = "Identity checked. You can take the exam\n"
                        FluidText(line)
                    elif result == [False]:
                        line = "Image did not match\n"
                        delete_image(imgname)
                        FluidText(line)
                else:
                    line = "Image was not authenticated. You cannot take the test. Thank You\n"
                    FluidText(line)

    else:
        print("Thank you")

    line = "-->press Q to quit\n-->press anyother key to go to main menu.\n"
    Design(line)
    key = input(":")
    if key == "q":
        break

print("THANK YOU")

 
