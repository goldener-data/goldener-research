# Data selection - Bibliography

## Survey
[From selection to generation: A survey of llm-based active learning](https://aclanthology.org/2025.acl-long.708/)

---

## No Embedding

### Random sampling:

[On the stratification of multi-label data](https://link.springer.com/chapter/10.1007/978-3-642-23808-6_10): make sampling by stratifying the difference association of classes
[Repeated random sampling for minimizing the time-to-accuracy of learning](https://proceedings.iclr.cc/paper_files/paper/2024/hash/68b8d2bc77268facfc75a78782da9559-Abstract-Conference.html): shown that changing the training set each epoch bring higher performances faster

### Active learning:
[Batch mode active sampling based on marginal probability distribution matching](https://dl.acm.org/doi/abs/10.1145/2513092.2513094): select next samples so that they match the distribution of already available labeled data (no embedding model)

### Smarter selection
[Beyond neural scaling laws: beating power law scaling via data pruning](https://proceedings.neurips.cc/paper_files/paper/2022/hash/7b75da9b61eda40fa35453ee5d077df6-Abstract-Conference.html): data selection based on SSL computed metric
[Language model-driven data pruning enables efficient active learning](https://aclanthology.org/2026.findings-eacl.229/): data selection from LLM perpexity and LLM based data quality assessment
[Predictive data selection: The data that predicts is the data that teaches](https://arxiv.org/abs/2503.00808): Train a selector by linking loss and performance of pretrained models (loss is aligned with performance means the sample is good to use)
[Mates: Model-aware data selection for efficient pretraining with data influence models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c4bec0d2fd217e6c2c3eafeced432582-Abstract-Conference.html): Train a model allowing to specify for each epoch which will be the data that will have the biggest influence. The training data evolve for each epoch.

---

## Leverage embeddings

### Smarter selection
[An Adaptive Data cleaning Framework for Noisy Label Detection](https://arxiv.org/abs/2606.07086): Method to make selection among noisy datasets
[InfoMax: Data pruning by information maximization](https://arxiv.org/abs/2506.01701): coreset selection for data pruning
[A bitter lesson for data filtering](https://arxiv.org/abs/2605.19407): demonstrate that data filtering during LLM pretraining is useless if you have unlimited compute.
[Analyzing similarity metrics for data selection for language model pretraining](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c6b508249ffd707720885d7a5bba5cb5-Abstract-Conference.html): Big LLM embeddings are not well suited for similarity measures 
[Zero-Shot Coreset Selection via Iterative Subspace Sampling](https://openaccess.thecvf.com/content/WACV2026/html/Griffin_Zero-Shot_Coreset_Selection_via_Iterative_Subspace_Sampling_WACV_2026_paper.html): Select most interesting samples for computer vision training

### Smarter selection based on clustering
[Nemotron-climb: Clustering-based iterative data mixture bootstrapping for language model pre-training](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24a8968affe71ffe4067d022b9d16566-Abstract-Datasets_and_Benchmarks_Track.html): Data selection during LLM pretraining
[MoCoProto: Enhancing few-shot pest image classification with self-supervised representation learning](https://www.sciencedirect.com/science/article/pii/S2643651526000798): data selection during SSL on images
[Effective pruning of web-scale datasets based on complexity of concept clusters](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e4bc9cdebfbcc43b0800cf99ffec5ee1-Abstract-Conference.html): Remove data in clusters with different rate depending on population
    
### Active learning:
[Active Learning with Foundation Model Priors: Efficient Learning under Class Imbalance](https://arxiv.org/abs/2606.07630): Make data selection from foundation model and small classifier model for image and text with imbalance and label noise






