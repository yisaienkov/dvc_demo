import yaml

if __name__ == "__main__":
    with open("params.yaml", "r") as fd:
        params = yaml.safe_load(fd)

    print("Split...")
    
    with open("resources/data.txt", "r") as f:
        data = f.read()

    with open("resources/train.txt", "w") as f:
        f.write(data[1::2])

    # params["split"]["seed"]
    
    with open("resources/test.txt", "w") as f:
        f.write(data[0::2])