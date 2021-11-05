import os
import time
import json
import random

import yaml
import numpy as np
import cv2


if __name__ == "__main__":
    with open("params.yaml", "r") as fd:
        params = yaml.safe_load(fd)

    random.seed(params["eval"]["seed"])
    np.random.seed(params["eval"]["seed"])

    print("Train...")
    
    with open("resources/test.txt", "r") as f:
        data = f.read()

    with open("resources/model.txt", "r") as f:
        model = f.read()

    print("Smth difficult...")
    time.sleep(1)
    print("Save metrics...")

    os.makedirs("resources/images/", exist_ok=True)
    for i in range(3):
        pixels = np.random.randint(0, 256, size=(256, 256, 3))
        # It's the best code in my life
        cv2.rectangle(
            pixels, 
            (50 * (i + 1), 50 * (i + 1)), 
            (75 * (i + 1), 75 * (i + 1)), 
            (255 * ((i + 1) % 3 == 1), 255 * ((i + 2) % 3 == 1), 255 * ((i + 3) % 3 == 1)), 
            thickness=5,
        )
        cv2.imwrite(f"resources/images/{i}.png", pixels)

    with open("metrics.json", "w") as f:
        json.dump(
            {
                "accuracy": 0.82,
                "f1": 0.83,
            }, 
            f, 
            indent=4,
        )
    