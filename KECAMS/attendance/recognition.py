from mtcnn import MTCNN
from deepface import DeepFace
import cv2

def run_recognition(images, session):
    names = []
    face_cordinates = []
    for pic in images:
        img = cv2.imread(f"./media/attend_pic/{pic}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        detector = MTCNN()
        results = detector.detect_faces(img)
        for face in results:
            confidence = face['confidence']
            if confidence > 0.90:
                x, y, w, h = face['box']
                x, y = abs(x), abs(y)
                detected_face = img[y:y+h, x:x+w]
                face_cordinates.append(detected_face)
    for each_cordinate in face_cordinates:
        name = DeepFace.find(each_cordinate, db_path=f"./media/Dataset/{session}", enforce_detection=False)
        if not name[0]['identity'].empty:
                name = name[0]["identity"].iloc[0].split('\\')[1].split('/')[1].split('.')[0]
                if name not in names:
                    names.append(name)

    names.sort()
    print(names)
    return names