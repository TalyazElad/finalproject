from brisque import BRISQUE
from PIL import Image
import numpy as np
import concurrent.futures
import statistics

# Define the directory where the images are stored

# Initialize the BRISQUE object
brisq = BRISQUE()

# Define a function to compute the score for a given image
def compute_score(img_path):
    img = Image.open(img_path)
    img = np.array(img)
    score = brisq.score(img)
    print(f"BRISQUE score for {img_path}: {score:.2f}")
    return score

# Compute the scores in parallel using multithreading
with concurrent.futures.ThreadPoolExecutor() as executor:
    scores = list(executor.map(compute_score, [f"frame{i}.jpg" for i in range(1, 849)]))

# Calculate the average score using the mean function from the statistics module
average_score = statistics.mean(scores)
print(f"Average BRISQUE score: {average_score:.2f}")
