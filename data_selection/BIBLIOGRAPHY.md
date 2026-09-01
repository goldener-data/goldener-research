# Data selection - Bibliography

## Survey
<div>
  <a href="https://aclanthology.org/2025.acl-long.708/">
    <strong>From selection to generation: A survey of LLM-based active learning</strong>
  </a><br>
  <small><em>First author: Yu Xia</em></small><br>
  <small><em>Origin: ACL Anthology (2025)</em></small><br>
  Note: No note provided.
</div>

---

## No embedding

### Random sampling:

<div>
  <a href="https://link.springer.com/chapter/10.1007/978-3-642-23808-6_10">
    <strong>On the stratification of multi-label data</strong>
  </a><br>
  <small><em>First author: Konstantinos Sechidis</em></small><br>
  <small><em>Origin: Lecture Notes in Computer Science (2011)</em></small><br>
  Note: make sampling by stratifying the differences in class association
</div>

<div>
  <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/68b8d2bc77268facfc75a78782da9559-Abstract-Conference.html">
    <strong>Repeated random sampling for minimizing the time-to-accuracy of learning</strong>
  </a><br>
  <small><em>First author: Patrik Okanovic</em></small><br>
  <small><em>Origin: International Conference on Learning Representations (2024)</em></small><br>
  Note: show that changing the training set each epoch brings higher performance faster
</div>

### Active learning:
<div>
  <a href="https://dl.acm.org/doi/abs/10.1145/2513092.2513094">
    <strong>Batch mode active sampling based on marginal probability distribution matching</strong>
  </a><br>
  <small><em>First author: Rita Chattopadhyay</em></small><br>
  <small><em>Origin: ACM Digital Library</em></small><br>
  Note: select the next samples so that they match the distribution of already available labeled data (no embedding model)
</div>

### Smarter selection
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/7b75da9b61eda40fa35453ee5d077df6-Abstract-Conference.html">
    <strong>Beyond neural scaling laws: beating power law scaling via data pruning</strong>
  </a><br>
  <small><em>First author: Ben Sorscher</em></small><br>
  <small><em>Origin: Advances in Neural Information Processing Systems (2022)</em></small><br>
  Note: data selection based on an SSL-computed metric
</div>

<div>
  <a href="https://aclanthology.org/2026.findings-eacl.229/">
    <strong>Language model-driven data pruning enables efficient active learning</strong>
  </a><br>
  <small><em>First author: Abdul Hameed Azeemi</em></small><br>
  <small><em>Origin: ACL Anthology (2026)</em></small><br>
  Note: data selection from LLM perplexity and LLM-based data quality assessment
</div>

<div>
  <a href="https://arxiv.org/abs/2503.00808">
    <strong>Predictive data selection: The data that predicts is the data that teaches</strong>
  </a><br>
  <small><em>First author: Kashun Shum</em></small><br>
  <small><em>Origin: International Conference on Machine Learning (ICML) (2025)</em></small><br>
  Note: Train a selector by linking loss and performance of pretrained models (if loss is aligned with performance, the sample is good to use)
</div>

<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/c4bec0d2fd217e6c2c3eafeced432582-Abstract-Conference.html">
    <strong>Mates: Model-aware data selection for efficient pretraining with data influence models</strong>
  </a><br>
  <small><em>First author: Zichun Yu</em></small><br>
  <small><em>Origin: Advances in Neural Information Processing Systems (2024)</em></small><br>
  Note: Train a model that allows specifying, for each epoch, which data will have the biggest influence. The training data evolve for each epoch.
</div>

<div>
  <a href="https://openreview.net/pdf?id=PObXviy706">
    <strong>DAFT: Data-Aware Fine-Tuning of Foundation Models for Efficient and Effective Medical Image Segmentation</strong>
  </a><br>
  <small><em>First author: Alexander Pfefferle</em></small><br>
  <small><em>Origin: Medical Image Segmentation Foundation Models (MedSAM on Laptop @ CVPR 2024), LNCS (2025)</em></small><br>
  Note: Train different models depending on the data source.
</div>

---

## Leverage embeddings

### Smarter selection
<div>
  <a href="https://arxiv.org/abs/2606.07086">
    <strong>An Adaptive Data cleaning Framework for Noisy Label Detection</strong>
  </a><br>
  <small><em>First author: Chen-Hsuan Fang</em></small><br>
  <small><em>Origin: arXiv.org (2026)</em></small><br>
  Note: Method for selecting among noisy datasets
</div>

<div>
  <a href="https://arxiv.org/abs/2506.01701">
    <strong>InfoMax: Data pruning by information maximization</strong>
  </a><br>
  <small><em>First author: Haoru Tan</em></small><br>
  <small><em>Origin: International Conference on Learning Representations (ICLR) (2025)</em></small><br>
  Note: coreset selection for data pruning
</div>

<div>
  <a href="https://arxiv.org/abs/2605.19407">
    <strong>A bitter lesson for data filtering</strong>
  </a><br>
  <small><em>First author: Christopher Mohri</em></small><br>
  <small><em>Origin: arXiv.org (2026)</em></small><br>
  Note: demonstrate that data filtering during LLM pretraining is useless if you have unlimited compute.
</div>

<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/c6b508249ffd707720885d7a5bba5cb5-Abstract-Conference.html">
    <strong>Analyzing similarity metrics for data selection for language model pretraining</strong>
  </a><br>
  <small><em>First author: Dylan Sam</em></small><br>
  <small><em>Origin: Advances in Neural Information Processing Systems (2026)</em></small><br>
  Note: Big LLM embeddings are not well suited for similarity measures
</div>

<div>
  <a href="https://openaccess.thecvf.com/content/WACV2026/html/Griffin_Zero-Shot_Coreset_Selection_via_Iterative_Subspace_Sampling_WACV_2026_paper.html">
    <strong>Zero-Shot Coreset Selection via Iterative Subspace Sampling</strong>
  </a><br>
  <small><em>First author: Brent A. Griffin</em></small><br>
  <small><em>Origin: Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (2026)</em></small><br>
  Note: Select most interesting samples for computer vision training
</div>

<div>
  <a href="https://scholar.google.fr/citations?view_op=view_citation&hl=fr&user=5yYPHwYAAAAJ&sortby=pubdate&citation_for_view=5yYPHwYAAAAJ:NhqRSupF_l8C">
    <strong>Advancing Cost Efficiency and Robustness of Machine Learning through the Lens of Data</strong>
  </a><br>
  <small><em>First author: Nezihe Gürel</em></small><br>
  <small><em>Origin: Doctoral dissertation, ETH Zurich (2022)</em></small><br>
  Note: No note provided.
</div>

### Smarter selection based on clustering
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/24a8968affe71ffe4067d022b9d16566-Abstract-Datasets_and_Benchmarks_Track.html">
    <strong>Nemotron-climb: Clustering-based iterative data mixture bootstrapping for language model pre-training</strong>
  </a><br>
  <small><em>First author: Shizhe Diao</em></small><br>
  <small><em>Origin: Advances in Neural Information Processing Systems (2026)</em></small><br>
  Note: Data selection during LLM pretraining
</div>

<div>
  <a href="https://www.sciencedirect.com/science/article/pii/S2643651526000798">
    <strong>MoCoProto: Enhancing few-shot pest image classification with self-supervised representation learning</strong>
  </a><br>
  <small><em>First author: Dong Jin</em></small><br>
  <small><em>Origin: Plant Phenomics (2026)</em></small><br>
  Note: data selection during SSL on images
</div>

<div>
  <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/e4bc9cdebfbcc43b0800cf99ffec5ee1-Abstract-Conference.html">
    <strong>Effective pruning of web-scale datasets based on complexity of concept clusters</strong>
  </a><br>
  <small><em>First author: Amro Kamal</em></small><br>
  <small><em>Origin: International Conference on Learning Representations (2024)</em></small><br>
  Note: Remove data in clusters at different rates depending on population
</div>
    
### Active learning:
<div>
  <a href="https://arxiv.org/abs/2606.07630">
    <strong>Active Learning with Foundation Model Priors: Efficient Learning under Class Imbalance</strong>
  </a><br>
  <small><em>First author: Jiancheng Zhang</em></small><br>
  <small><em>Origin: International Conference on Machine Learning (ICML) (2026)</em></small><br>
  Note: Make data selection using a foundation model and a small classifier model for image and text with imbalance and label noise
</div>
