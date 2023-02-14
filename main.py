import cv2
import os

files_names = os.listdir("./images")

for file_name in files_names:
    show_image = True
    index = -1
    while show_image:
        image = cv2.imread("images/" + file_name)
        height, width, channels = image.shape
        for count in range(height):
            y = count * int(height/10)
            cv2.line(image, (0, y), (width, y), (255, 0, 0), 1, 1)
            cv2.putText(image, str(count), (10, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
        if not index == -1:
            start_point = (0, index * int(height/10))
            end_point = (width, ((index + 5) * int(height/10)) + int((height/10) * 0.6))
            cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
            end_point = (width, (index + 2) * int(height/10))
            cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)
        cv2.imshow('frame', image)
        key = cv2.waitKey(0)
        if key == 49:
            index -= 1
        elif key == 50:
            index += 1
        elif key == 13:
            show_image = False


    
