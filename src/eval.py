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

    with open("metrics.yaml", "w") as f:
        json.dump(
            {
                "accuracy": params["eval"]["accuracy"],
                "f1": params["eval"]["f1"],
            }, 
            f, 
            indent=4,
        )
    