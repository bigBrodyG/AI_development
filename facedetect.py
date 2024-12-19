'''
Autore: Giordano Fornari (3BAU)
Versione: 1.1
'''

import face_recognition
import cv2
import numpy as np


# WARNING: questo esempio usa OpenCV (la libreria `cv2`) quindi verifica di averlo installato.


# Dichiara la tua webcam (n. 0 pk quella predefinita)
video_capture = cv2.VideoCapture(0)
# Carica una immagine e crea l'encoding di essa
my_image = face_recognition.load_image_file("am-i.jpg")
pala_encoding = face_recognition.face_encodings(my_image)[0]

# Carica una immagine e crea l'encoding di essa
pala_image = face_recognition.load_image_file("paladini.jpg")
pala_encoding = face_recognition.face_encodings(pala_image)[0]

# Crea un array per gli encoding delle immagini
known_encodings = [
    my_encoding,
    pala_encoding
]


# Crea un array per gli encoding delle immagini
known_names = [
    "Giordano Fornari",
    "Massimiliano Paladini"
]

while True:
    # Prendi un frame del video --> ret è una variabile booleana di ritorno; in frame invece sono salvati gli array delle immagini;
    ret, frame = video_capture.read()

    # Convertiamo l'immagine dal colore BGR (utilizzato da OpenCV) al colore RGB (utilizzato da face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Ottieni le coordinate delle facce 
    coord = face_recognition.face_locations(rgb_frame)
    #poi crea gli encoding delle facce alle cordinate
    encodings = face_recognition.face_encodings(rgb_frame, coord)

    # Controlla ogni faccia presente nella videocamera
    for (alto, destra, basso, sinistra), encoding in zip(coord, encodings):
        # Controlla se c'è un riconoscimento di una faccia
        matches = face_recognition.compare_faces(known_encodings, encoding)

        nome = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            #prendi il primo volto conosciuto e scrivi l'indice corrispondente nella variabile
            first_match_index = matches.index(True)
            #assegna il nome corrispondente
            nome = known_face_names[first_match_index]

        # Disegna un rettangolo attorno all immagine
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Disegna il nome
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        # Scelgo il font
        font = cv2.FONT_HERSHEY_DUPLEX
        # Con +-6 aggiungo un minimo di spaziatura che sara: 6-2 = 4px
        cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Comando per chiudere premendo 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Chiudi accesso a webcam
video_capture.release()
# Cancella tutte le finestre
cv2.destroyAllWindows()
