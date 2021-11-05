import time
import json

import yaml


if __name__ == "__main__":
    with open("params.yaml", "r") as fd:
        params = yaml.safe_load(fd)

    print("Train...")
    
    with open("resources/test.txt", "r") as f:
        data = f.read()

    with open("resources/model.txt", "r") as f:
        model = f.read()

    print("Smth difficult...")
    time.sleep(2)
    print("Save metrics...")

    with open("metrics.json", "w") as f:
        json.dump(
            {
                "accuracy": 0.82,
                "f1": 0.83,
            }, 
            f, 
            indent=4,
        )
    