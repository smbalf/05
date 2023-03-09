import cv2

# Create a CascadeClassifier object
classifier = cv2.CascadeClassifier()

# Set the parameters for the training
params = dict(maxWidth=220, maxHeight=250, minWidth=50, minHeight=70, minSize=(50, 70), maxSize=(220, 250),
              flags=cv2.CASCADE_SCALE_IMAGE)

# Load the positive and negative images
positive_images = [f"training_images/positive/pos-{i}.png" for i in range(1, 101)]
negative_images = [f"training_images/negative/neg-{i}.png" for i in range(1, 103)]

# Create the samples and labels arrays
samples = positive_images + negative_images
labels = [1 for _ in positive_images] + [0 for _ in negative_images]

# Load the positive and negative images
positive_images = [cv2.imread(f"training_images/positive/pos-{i}.png", cv2.IMREAD_GRAYSCALE) for i in range(1, 101)]
negative_images = [cv2.imread(f"training_images/negative/neg-{i}.png", cv2.IMREAD_GRAYSCALE) for i in range(1, 103)]

# Start the training
classifier.detectMultiScale(positive_images + negative_images, labels, **params)

# Save the trained classifier to a file
classifier.save("tree_classifier.xml")
