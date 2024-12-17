import face_recognition
import cv2
import numpy as np


# WARNING: questo esempio usa OpenCV (la libreria `cv2`) quindi verifica di averlo installato.


# Dichiara la tua webcam (n. 0 pk quella predefinita)
video_capture = cv2.VideoCapture(0)
# Carica una immagine e crea l'encoding di essa
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Carica una immagine e crea l'encoding di essa
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Crea un array per gli encoding delle immagini
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]


# Crea un array per gli encoding delle immagini
known_face_names = [
    "Barack Obama",
    "Joe Biden"
]

while True:
    # Prendi un frame del video (ret??)
    ret, frame = video_capture.read()

    # Convertiamo l'immagine dal colore BGR (utilizzato da OpenCV) al colore RGB (utilizzato da face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Ottieni le coordinate delle facce 
    face_locations = face_recognition.face_locations(rgb_frame)
    #poi crea gli encoding delle facce alle cordinate
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
      '''
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
      '''
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
