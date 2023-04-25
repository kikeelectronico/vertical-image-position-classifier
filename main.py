import cv2
import os
import shutil

DIVISIONS = 10

if not os.path.exists("images"): os.mkdir("images")

files_names = os.listdir("./images")

if len(files_names) == 0:
    print("No images to be classified")
    exit()

for file_name in files_names:
    show_image = True
    index = 0
    while show_image:
        # Read the image
        image = cv2.imread("images/" + file_name)
        # Get image data
        image_height, image_width, channels = image.shape
        # Draw view port rectangles
        screen_height = int((image_width * 9) / 16)
        top_left_corner = (0, index * int((image_height - screen_height)/DIVISIONS))
        bottom_right_corner = (image_width, (screen_height + (index * int((image_height - screen_height)/DIVISIONS))))
        cv2.rectangle(image, top_left_corner, bottom_right_corner, (255, 0, 0), 2)
        # Show the image
        cv2.imshow('frame', image)
        # Wait for user input
        key = cv2.waitKey(0)
        if key == 49:
            if index > 0:
                index -= 1
        elif key == 50:
            if index < 10:
                index += 1
        elif key == 13:
            if not os.path.exists("classified"): os.mkdir("classified")
            if not os.path.exists("classified/" + str(index)): os.mkdir("classified/" + str(index))
            shutil.move("images/" + file_name, "classified/" + str(index) + "/" + file_name)
            show_image = False
