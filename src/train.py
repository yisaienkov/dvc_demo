import time

import yaml


if __name__ == "__main__":
    with open("params.yaml", "r") as fd:
        params = yaml.safe_load(fd)

    print("Train...")
    
    with open("resources/train.txt", "r") as f:
        data = f.read()

    print("Smth difficult...")
    time.sleep(10)
    print("Save model...")

    with open("resources/model.txt", "w") as f:
        f.write("import random\nrandom.randint(2)")
    