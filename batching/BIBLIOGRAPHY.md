# Batching - Bibliography

## No embeddings

[Concept-aware batch sampling improves language-image pretraining](https://openaccess.thecvf.com/content/CVPR2026/html/Ghosh_Concept-Aware_Batch_Sampling_Improves_Language-Image_Pretraining_CVPR_2026_paper.html): Select data inside a batch in order to meet the concept distribution target when training VLMs.
[Hard example mining with auxiliary embeddings](http://openaccess.thecvf.com/content_cvpr_2018_workshops/w1/html/Smirnov_Hard_Example_Mining_CVPR_2018_paper.html): extract some information from other models and use them to create batches.
[Face representation learning using composite mini-batches](http://openaccess.thecvf.com/content_ICCVW_2019/html/DFW/Smirnov_Face_Representation_Learning_using_Composite_Mini-Batches_ICCVW_2019_paper.html): Mix multiple sampling strategies to construct mini batches.

---

## Leverage embeddings

### With clustering

[Balanced data sampling for language model training with clustering](https://aclanthology.org/2024.findings-acl.833/): Create batches depending on the clustering of embeddings while training LLM
[Breaking the batch barrier (b3) of contrastive learning via smart batch mining](https://proceedings.neurips.cc/paper_files/paper/2025/hash/21aa6840fcaa0cc3a1d16bafede47a2f-Abstract-Conference.html): qualify the whole dataset and then optimize batch configurations for contrastive learning