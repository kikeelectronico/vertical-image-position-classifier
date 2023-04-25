import cv2
import os
import shutil

DIVISIONS = 10
ALPHA = 0.6

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
        overlay = image.copy()
        # Get image data
        image_height, image_width, channels = image.shape
        # Draw view port rectangle
        screen_height = int((image_width * 9) / 16)
        view_port_top_left_corner = (0, index * int((image_height - screen_height)/DIVISIONS))
        view_port_bottom_right_corner = (image_width, (screen_height + (index * int((image_height - screen_height)/DIVISIONS))))
        cv2.rectangle(overlay, view_port_top_left_corner, view_port_bottom_right_corner, (255, 0, 0), 2)
        # Draw view port shadows
        top_left_corner = (0, 0)
        bottom_right_corner = (image_width, index * int((image_height - screen_height)/DIVISIONS))
        cv2.rectangle(overlay, top_left_corner, bottom_right_corner, (255, 0, 0), -1)
        top_left_corner = (0, (screen_height + (index * int((image_height - screen_height)/DIVISIONS))))
        bottom_right_corner = (image_width, image_height)
        cv2.rectangle(overlay, top_left_corner, bottom_right_corner, (255, 0, 0), -1)
        # Add overlay
        image_with_overlay = cv2.addWeighted(overlay, ALPHA, image, 1 - ALPHA, 0)
        # Show the image
        cv2.imshow('Visor', image_with_overlay)
        cropped_image = image[view_port_top_left_corner[1]:view_port_bottom_right_corner[1], 0:view_port_bottom_right_corner[0]]
        cv2.imshow('Visor 2', cropped_image)
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
