# Visual Question Difficulty (VQD)

The code of "Which visual questions are difficult to answer? Analysis with Entropy of Answer Distributions"
This paper analysis the VQA v2.0 dataset and
proposes a clustering approach for finding difficult visual questions to answer.
There are 10 clusters, and the difficulty increases from cluster 0 (easyest) to clsuter 9 (hardest).


## How to generate images of visual questions for each cluster

```
wget https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Val_mscoco.zip
wget https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Val_mscoco.zip
wget http://images.cocodataset.org/zips/val2014.zip

unzip v2_Annotations_Val_mscoco.zip
unzip v2_Questions_Val_mscoco.zip
unzip val2014.zip

gunzip test_qid_label.csv.gz val_qid_label.csv.gz val_all.csv.gz 

python ./qid_to_visual_questions.py
```

Then PDF files of visual questions are generated in `val_clusters` folder.
(Some example files are already stored)


# Visual question samples

Here are some examples from cluster 9 and 8.

# Cluster 9
![](./val_clusters/9/o/262189002.png)
![](val_clusters/9/o/393254000.png)


# Cluster 8
![](val_clusters/8/o/262175002.png)
![](val_clusters/8/o/240301000.png)




