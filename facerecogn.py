import face_recognition

# Load the jpg files into numpy arrays
image1 = face_recognition.load_image_file("1.jpg")
image2 = face_recognition.load_image_file("2.jpg")
u_image = face_recognition.load_image_file("u.jpg")

try:
    i1_encoding = face_recognition.face_encodings(image1)[0] #restituisce un insieme di array di tipo nunpy. Noi sappiamo di avere un solo volto nell'immagine e perciò scegliamo solo l'elemento di indice 0
    i2_encoding = face_recognition.face_encodings(image2)[0]
    unknown_encoding = face_recognition.face_encodings(u_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    i1_encoding,
    i2_encoding
]

results = face_recognition.compare_faces([known_faces], u_encoding)
# results è un array Booleano che indica se il volto sconosciuto corrisponde a qualcuno nell'array known_faces 

print(f"Is the unknown face a picture of image1 face? {results[0]}")
print(f"Is the unknown face a picture of image2 face? {results[0]}")
print(f"Is the unknown face a new person that we've never seen before? {not True in results}")
