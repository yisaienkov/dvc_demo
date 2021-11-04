# dvc_demo


```bash
$ git init

$ dvc init

$ dvc remote add -d storage gdrive://1i8GJfL6E3n7KFPZESjTD974rHRo9d8uG

$ dvc add resources/data.txt

$ dvc run -n split \
    -p split \
    -d resources/data.txt \
    -d requirements.txt \
    -d src/split.py \
    -o resources/train.txt \
    -o resources/test.txt \
    python src/split.py

$ dvc run -n split -p split -d resources/data.txt -d requirements.txt -d src/split.py -o resources/train.txt -o resources/test.txt python src/split.py

$ dvc run -n train \
    -p train \
    -d resources/train.txt \
    -d requirements.txt \
    -d src/train.py \
    -o resources/model.txt \
    python src/train.py

$ dvc run -n train -p train -d resources/train.txt -d requirements.txt -d src/train.py -o resources/model.txt python src/train.py

$ dvc run -n eval \
    -p eval \
    -d resources/test.txt \
    -d resources/model.txt \
    -d requirements.txt \
    -d src/eval.py \
    -M metrics.yaml \
    python src/eval.py

$ dvc run -n eval -p eval -d resources/test.txt -d resources/model.txt -d requirements.txt -d src/eval.py -M metrics.yaml python src/eval.py

$ git add .

$ git commit -m ""

$ dvc push

$ git push

```