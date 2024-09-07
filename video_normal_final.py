import cv2
import numpy as np

# CONTANTS
AREA_LIMIT_CONTOUR = 10000
GRAY_THRESHOLD = 5

def draw_text(image: np.array, x: int, y: int, text: str):
    # takes image, (x, y) coordinates and adds text at x, y
    image = cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

def preprocess_image(image: np.array) -> np.array:
    # takes raw rgb img, returns grayscale image
    img = cv2.GaussianBlur(image,(5,5),0) 

    #subtract average color
    height, width, _ = np.shape(img)
    avg_color_row = np.average(img, axis=0)
    avg_colors = np.average(avg_color_row, axis=0)
    int_average = np.array(avg_colors, dtype=np.uint8)
    average_image = np.zeros((height, width, 3), np.uint8)
    average_image[:] = int_average + 50
    img = cv2.subtract(img, average_image)

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, GRAY_THRESHOLD, 255, cv2.THRESH_BINARY)
    return threshold

def find_shapes(image: np.array):
    # takes rgb img, adds contour labels and text
    new_img = preprocess_image(image)  # do grayscale and processing
    contours, _ = cv2.findContours(new_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # get contours
    for i, contour in enumerate(contours):  # loop over each contour
        if i == 0: continue  # skip whole image contour
        area = cv2.contourArea(contour)  # get enclosed area of contour
        if area < AREA_LIMIT_CONTOUR: continue  # if too small to be shape, skip
        approx = cv2.approxPolyDP( 
            contour, 0.01 * cv2.arcLength(contour, True), True)
        if(len(approx)) < 3: continue  # if not enough sides to be actual shape, continue

        cv2.drawContours(image, [contour], 0, (0, 0, 255), 5) 

        M = cv2.moments(contour) 
        if M['m00'] != 0.0: 
            x = int(M['m10']/M['m00']) 
            y = int(M['m01']/M['m00']) 
            cv2.circle(image, (x, y), radius = 3, color=(0,0,255),thickness=-1)
            draw_text(image, x+10, y+10, f"({x}, {y})")
    return image

# Creating a VideoCapture object to read the video
vid = cv2.VideoCapture('PennAir_2024_App_Dynamic.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('processed_video.mp4',fourcc, 20, (1920,1080))

i = 0  # frame counter
# Read each frame
while (vid.isOpened()):
    print(f"Frame: {i}")
    ret, frame = vid.read()
    if frame is None: # if frame is None
        break
    fl = find_shapes(frame) # draw contours and text
    fl = cv2.resize(fl, (1920, 1080))  # resize to output
    out.write(fl)  # write to output video
    i+=1

# destroy all windows and release objects to end
vid.release()
out.release()
cv2.destroyAllWindows()





