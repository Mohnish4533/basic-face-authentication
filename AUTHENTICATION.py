# checking face matches

def Authenticate(Registered_image,new_image):

    from PIL import Image
    import face_recognition 

    Registered_face = face_recognition.load_image_file(Registered_image)
    Registered_face_location = face_recognition.face_locations(Registered_face)
    Registered_face_encodings = face_recognition.face_encodings(Registered_face, Registered_face_location)[0]

    face = face_recognition.load_image_file(new_image)
    face_locations = face_recognition.face_locations(face)
    face_encodings = face_recognition.face_encodings(face, face_locations)[0]

    result = face_recognition.compare_faces([Registered_face_encodings], face_encodings)
    return result
