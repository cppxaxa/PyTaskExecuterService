import matplotlib.pyplot as plt
import cv2
img = cv2.imread('image.jpg')

def PyPlot(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

def ImShow(window, image, millis = 0):
    val = 0
    count = 0
    while val != ord('q'):
        cv2.imshow(window, image)
        val = cv2.waitKey(30)
        count += 1
        if (millis != 0 && (count * 30) > millis):
            break
    cv2.destroyAllWindows()
        
# PyPlot(img)
ImShow('DEBUG', img)