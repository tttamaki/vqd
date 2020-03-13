# Visual Question Difficulty (VQD)

The code of "Which visual questions are difficult to answer? Analysis with Entropy of Answer Distributions"


## How to generate images of visual questions for each cluster

```
wget https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Val_mscoco.zip
wget https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Val_mscoco.zip
wget http://images.cocodataset.org/zips/val2014.zip

unzip v2_Annotations_Val_mscoco.zip
unzip v2_Questions_Val_mscoco.zip
unzip val2014.zip

python ./qid_to_visual_questions.py
```

Then PDF files of visual questions are generated in `val_clusters` folder.
(Some example files are already stored)

