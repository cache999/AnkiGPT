import cv2

# Read the image
img = cv2.imread('./nir_data/jason/lra.jpg')

# Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute the absolute difference between adjacent pixels
diff = cv2.absdiff(img[:-1,:], img[1:,:])

cv2.imshow('Difference', diff)
cv2.waitKey(0)