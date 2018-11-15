import face_recognition
# Load the jpg files into numpy arrays

image1 = face_recognition.load_image_file(r"D:\PYTHON\Scripts\face recognition\test 3\tony stark.jpg")
image2 = face_recognition.load_image_file(r"D:\PYTHON\Scripts\face recognition\test 3\benedict cumberbatch.jpg")
unknown_image = face_recognition.load_image_file(r"D:\PYTHON\Scripts\face recognition\test 3\unknown image of tony stark.jpg")
# images=[image1,image2]

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    image1_face_encoding = face_recognition.face_encodings(image1)[0]
    image2_face_encoding = face_recognition.face_encodings(image2)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    image1_face_encoding,
    image2_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
for id_,res in enumerate(results):
	if res==True:
		print("Looks like the person number {} ".format(str(id_+1)))








# print(results)
# print("Is the unknown face a picture of Margot? {}".format(results[0]))
# print("Is the unknown face a picture of Jaime? {}".format(results[1]))
# print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))