import cv2
import os
import shutil

files_names = os.listdir("./images")

for file_name in files_names:
    show_image = True
    index = 0
    while show_image:
        # Read the image
        image = cv2.imread("images/" + file_name)
        # Get image data
        height, width, channels = image.shape
        # Draw horizontal guide lines and put text
        for count in range(height):
            y = count * int(height/10)
            cv2.line(image, (0, y), (width, y), (255, 0, 0), 1, 1)
            cv2.putText(image, str(count), (10, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
        # Draw view port rectangles
        start_point = (0, index * int(height/10))
        end_point = (width, ((index + 5) * int(height/10)) + int((height/10) * 0.6))
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
        end_point = (width, (index + 2) * int(height/10))
        cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)
        # Show the image
        cv2.imshow('frame', image)
        # Wait for user input
        key = cv2.waitKey(0)
        if key == 49:
            index -= 1
        elif key == 50:
            index += 1
        elif key == 13:
            if not os.path.exists("classified"): os.mkdir("classified")
            if not os.path.exists("classified/" + str(index)): os.mkdir("classified/" + str(index))
            shutil.move("images/" + file_name, "classified/" + str(index) + "/" + file_name)
            show_image = False
