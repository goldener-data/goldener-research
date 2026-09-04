# Data selection - Bibliography

## Survey
<div>
  <a href="https://aclanthology.org/2025.acl-long.708/">
    <strong>From selection to generation: A survey of LLM-based active learning</strong>
  </a><br>
  <small><em>👤 First author: Yu Xia</em></small><br>
  <small><em>📍 Origin: ACL Anthology (2025)</em></small><br>
  📝 Note: No note provided.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2505.17799">
    <strong>A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances</strong>
  </a><br>
  <small><em>👤 First author: Brian B. Moser</em></small><br>
  <small><em>📍 Origin: arXiv (2025)</em></small><br>
  📝 Note: survey of the coreset-selection landscape, including recent methodological advances.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2402.16827">
    <strong>A survey on data selection for language models</strong>
  </a><br>
  <small><em>👤 First author: Alon Albalak</em></small><br>
  <small><em>📍 Origin: arXiv (2024)</em></small><br>
  📝 Note: survey of data selection methods for language models and their trade-offs.
</div>

---

## No embedding

### Random sampling:

<div>
  <a href="https://link.springer.com/chapter/10.1007/978-3-642-23808-6_10">
    <strong>On the stratification of multi-label data</strong>
  </a><br>
  <small><em>👤 First author: Konstantinos Sechidis</em></small><br>
  <small><em>📍 Origin: Lecture Notes in Computer Science (2011)</em></small><br>
  📝 Note: make sampling by stratifying the differences in class association
</div>
<br>
<div>
  <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/68b8d2bc77268facfc75a78782da9559-Abstract-Conference.html">
    <strong>Repeated random sampling for minimizing the time-to-accuracy of learning</strong>
  </a><br>
  <small><em>👤 First author: Patrik Okanovic</em></small><br>
  <small><em>📍 Origin: International Conference on Learning Representations (2024)</em></small><br>
  📝 Note: show that changing the training set each epoch brings higher performance faster
</div>

### Active learning:
<div>
  <a href="https://dl.acm.org/doi/abs/10.1145/2513092.2513094">
    <strong>Batch mode active sampling based on marginal probability distribution matching</strong>
  </a><br>
  <small><em>👤 First author: Rita Chattopadhyay</em></small><br>
  <small><em>📍 Origin: ACM Digital Library (2013)</em></small><br>
  📝 Note: select the next samples so that they match the distribution of already available labeled data (no embedding model)
</div>

### Smarter selection
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/7b75da9b61eda40fa35453ee5d077df6-Abstract-Conference.html">
    <strong>Beyond neural scaling laws: beating power law scaling via data pruning</strong>
  </a><br>
  <small><em>👤 First author: Ben Sorscher</em></small><br>
  <small><em>📍 Origin: Advances in Neural Information Processing Systems (2022)</em></small><br>
  📝 Note: data selection based on an SSL-computed metric
</div>
<br>
<div>
  <a href="https://aclanthology.org/2026.findings-eacl.229/">
    <strong>Language model-driven data pruning enables efficient active learning</strong>
  </a><br>
  <small><em>👤 First author: Abdul Hameed Azeemi</em></small><br>
  <small><em>📍 Origin: ACL Anthology (2026)</em></small><br>
  📝 Note: data selection from LLM perplexity and LLM-based data quality assessment
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2503.00808">
    <strong>Predictive data selection: The data that predicts is the data that teaches</strong>
  </a><br>
  <small><em>👤 First author: Kashun Shum</em></small><br>
  <small><em>📍 Origin: International Conference on Machine Learning (ICML) (2025)</em></small><br>
  📝 Note: Train a selector by linking loss and performance of pretrained models (if loss is aligned with performance, the sample is good to use)
</div>
<br>
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2024/hash/c4bec0d2fd217e6c2c3eafeced432582-Abstract-Conference.html">
    <strong>Mates: Model-aware data selection for efficient pretraining with data influence models</strong>
  </a><br>
  <small><em>👤 First author: Zichun Yu</em></small><br>
  <small><em>📍 Origin: Advances in Neural Information Processing Systems (2024)</em></small><br>
  📝 Note: Train a model that allows specifying, for each epoch, which data will have the biggest influence. The training data evolve for each epoch.
</div>
<br>
<div>
  <a href="https://openreview.net/pdf?id=PObXviy706">
    <strong>DAFT: Data-Aware Fine-Tuning of Foundation Models for Efficient and Effective Medical Image Segmentation</strong>
  </a><br>
  <small><em>👤 First author: Alexander Pfefferle</em></small><br>
  <small><em>📍 Origin: Medical Image Segmentation Foundation Models (MedSAM on Laptop @ CVPR 2024), LNCS (2025)</em></small><br>
  📝 Note: Train different models depending on the data source.
</div>

---

## Leverage embeddings

### Smarter selection
<div>
  <a href="https://arxiv.org/abs/2606.07086">
    <strong>An Adaptive Data cleaning Framework for Noisy Label Detection</strong>
  </a><br>
  <small><em>👤 First author: Chen-Hsuan Fang</em></small><br>
  <small><em>📍 Origin: arXiv.org (2026)</em></small><br>
  📝 Note: Method for selecting among noisy datasets
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2506.01701">
    <strong>InfoMax: Data pruning by information maximization</strong>
  </a><br>
  <small><em>👤 First author: Haoru Tan</em></small><br>
  <small><em>📍 Origin: International Conference on Learning Representations (ICLR) (2025)</em></small><br>
  📝 Note: coreset selection for data pruning
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2605.19407">
    <strong>A bitter lesson for data filtering</strong>
  </a><br>
  <small><em>👤 First author: Christopher Mohri</em></small><br>
  <small><em>📍 Origin: arXiv.org (2026)</em></small><br>
  📝 Note: demonstrate that data filtering during LLM pretraining is useless if you have unlimited compute.
</div>
<br>
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/c6b508249ffd707720885d7a5bba5cb5-Abstract-Conference.html">
    <strong>Analyzing similarity metrics for data selection for language model pretraining</strong>
  </a><br>
  <small><em>👤 First author: Dylan Sam</em></small><br>
  <small><em>📍 Origin: Advances in Neural Information Processing Systems (2026)</em></small><br>
  📝 Note: Big LLM embeddings are not well suited for similarity measures
</div>
<br>
<div>
  <a href="https://openaccess.thecvf.com/content/WACV2026/html/Griffin_Zero-Shot_Coreset_Selection_via_Iterative_Subspace_Sampling_WACV_2026_paper.html">
    <strong>Zero-Shot Coreset Selection via Iterative Subspace Sampling</strong>
  </a><br>
  <small><em>👤 First author: Brent A. Griffin</em></small><br>
  <small><em>📍 Origin: Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (2026)</em></small><br>
  📝 Note: Select most interesting samples for computer vision training
</div>
<br>
<div>
  <a href="https://scholar.google.fr/citations?view_op=view_citation&hl=fr&user=5yYPHwYAAAAJ&sortby=pubdate&citation_for_view=5yYPHwYAAAAJ:NhqRSupF_l8C">
    <strong>Advancing Cost Efficiency and Robustness of Machine Learning through the Lens of Data</strong>
  </a><br>
  <small><em>👤 First author: Nezihe Gürel</em></small><br>
  <small><em>📍 Origin: Doctoral dissertation, ETH Zurich (2022)</em></small><br>
  📝 Note: No note provided.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/1906.11829">
    <strong>Selection via proxy: Efficient data selection for deep learning</strong>
  </a><br>
  <small><em>👤 First author: Christopher Coleman</em></small><br>
  <small><em>📍 Origin: arXiv (2019)</em></small><br>
  📝 Note: select samples via a lightweight proxy model to reduce the cost of expensive data acquisition.
</div>
<br>
<div>
  <a href="https://openreview.net/pdf?id=7D5EECbOaf9">
    <strong>Moderate coreset: A universal method of data selection for real-world data-efficient deep learning</strong>
  </a><br>
  <small><em>👤 First author: Xiaobo Xia</em></small><br>
  <small><em>📍 Origin: ICLR (2022)</em></small><br>
  📝 Note: coreset selection method designed to be robust across real-world data-efficient settings.
</div>
<br>
<div>
  <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Joneidi_Select_to_Better_Learn_Fast_and_Accurate_Deep_Learning_Using_CVPR_2020_paper.pdf">
    <strong>Select to better learn: Fast and accurate deep learning using data selection from nonlinear manifolds</strong>
  </a><br>
  <small><em>👤 First author: Mehran Joneidi</em></small><br>
  <small><em>📍 Origin: CVPR (2020)</em></small><br>
  📝 Note: active data selection by exploiting nonlinear manifold structure in the data.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2412.10032">
    <strong>Single-Pass Object-Focused Data Selection</strong>
  </a><br>
  <small><em>👤 First author: Niclas Popp</em></small><br>
  <small><em>📍 Origin: arXiv (2024)</em></small><br>
  📝 Note: single-pass object-focused selection strategy for efficient dataset reduction.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2311.08675">
    <strong>Refined coreset selection: Towards minimal coreset size under model performance constraints</strong>
  </a><br>
  <small><em>👤 First author: Xuelei Xia</em></small><br>
  <small><em>📍 Origin: arXiv (2023)</em></small><br>
  📝 Note: refined coreset selection for minimal subset sizes while meeting performance targets.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2209.05785">
    <strong>Adversarial coreset selection for efficient robust training</strong>
  </a><br>
  <small><em>👤 First author: Hadi M. Dolatabadi</em></small><br>
  <small><em>📍 Origin: International Journal of Computer Vision (2023)</em></small><br>
  📝 Note: select coresets that improve robustness while keeping training efficient.
</div>
<br>
<div>
  <a href="https://openreview.net/pdf?id=fpzA8uRA95">
    <strong>Efficient adversarial contrastive learning via robustness-aware coreset selection</strong>
  </a><br>
  <small><em>👤 First author: Xinyi Xu</em></small><br>
  <small><em>📍 Origin: NeurIPS (2023)</em></small><br>
  📝 Note: robustness-aware coreset selection for adversarial contrastive learning.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/1906.01827">
    <strong>Coresets for data-efficient training of machine learning models</strong>
  </a><br>
  <small><em>👤 First author: Baharan Mirzasoleiman</em></small><br>
  <small><em>📍 Origin: ICML (2020)</em></small><br>
  📝 Note: foundational coreset method for efficient, data-efficient model training.
</div>
<br>
<div>
  <a href="https://proceedings.mlr.press/v139/van-gorp21a/van-gorp21a.pdf">
    <strong>Active deep probabilistic subsampling</strong>
  </a><br>
  <small><em>👤 First author: H. Van Gorp</em></small><br>
  <small><em>📍 Origin: ICML (2021)</em></small><br>
  📝 Note: active subsampling using deep probabilistic methods to select informative samples.
</div>
<br>
<div>
  <a href="https://openreview.net/pdf?id=SJeq9JBFvH">
    <strong>Deep probabilistic subsampling for task-adaptive compressed sensing</strong>
  </a><br>
  <small><em>👤 First author: I. Huijben</em></small><br>
  <small><em>📍 Origin: ICLR (2020)</em></small><br>
  📝 Note: probabilistic subsampling tuned to the downstream task through compressed sensing.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2501.01118">
    <strong>Pruning-based Data Selection and Network Fusion for Efficient Deep Learning</strong>
  </a><br>
  <small><em>👤 First author: H. Kousar</em></small><br>
  <small><em>📍 Origin: arXiv (2025)</em></small><br>
  📝 Note: combine data pruning with network fusion to improve deep learning efficiency.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2103.00123">
    <strong>Grad-match: Gradient matching based data subset selection for efficient deep model training</strong>
  </a><br>
  <small><em>👤 First author: Krishnateja Killamsetty</em></small><br>
  <small><em>📍 Origin: ICML (2021)</em></small><br>
  📝 Note: select subsets whose gradients match the full dataset for efficient training.
</div>
<br>
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/b8ab7288e7d5aefc695175f22bbddead-Paper-Conference.pdf">
    <strong>Automata: Gradient based data subset selection for compute-efficient hyper-parameter tuning</strong>
  </a><br>
  <small><em>👤 First author: Krishnateja Killamsetty</em></small><br>
  <small><em>📍 Origin: NeurIPS (2022)</em></small><br>
  📝 Note: gradient-based subset selection for compute-efficient hyperparameter tuning.
</div>
<br>
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/c1449acc2e64050d79c2830964f8515f-Paper-Conference.pdf">
    <strong>Optimizing data collection for machine learning</strong>
  </a><br>
  <small><em>👤 First author: R. Mahmood</em></small><br>
  <small><em>📍 Origin: NeurIPS (2022)</em></small><br>
  📝 Note: optimize data collection strategy to improve downstream machine learning performance.
</div>
<br>
<div>
  <a href="https://proceedings.mlr.press/v238/bickford-smith24a/bickford-smith24a.pdf">
    <strong>Making better use of unlabelled data in bayesian active learning</strong>
  </a><br>
  <small><em>👤 First author: F. B. Bickford Smith</em></small><br>
  <small><em>📍 Origin: AISTATS (2024)</em></small><br>
  📝 Note: Bayesian active learning that better exploits unlabeled data.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2303.02535">
    <strong>Streaming active learning with deep neural networks</strong>
  </a><br>
  <small><em>👤 First author: A. Saran</em></small><br>
  <small><em>📍 Origin: ICML (2023)</em></small><br>
  📝 Note: active learning in streaming settings with deep neural networks.
</div>
<br>
<div>
  <a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Kim_Coreset_Sampling_From_Open-Set_for_Fine-Grained_Self-Supervised_Learning_CVPR_2023_paper.pdf">
    <strong>Coreset sampling from open-set for fine-grained self-supervised learning</strong>
  </a><br>
  <small><em>👤 First author: S. Kim</em></small><br>
  <small><em>📍 Origin: CVPR (2023)</em></small><br>
  📝 Note: coreset sampling under open-set conditions for self-supervised fine-grained learning.
</div>
<br>
<div>
  <a href="https://proceedings.mlr.press/v202/yang23g/yang23g.pdf">
    <strong>Towards sustainable learning: Coresets for data-efficient deep learning</strong>
  </a><br>
  <small><em>👤 First author: Y. Yang</em></small><br>
  <small><em>📍 Origin: ICML (2023)</em></small><br>
  📝 Note: sustainable learning via coreset-based data-efficient deep learning.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2310.07931">
    <strong>D2 pruning: Message passing for balancing diversity and difficulty in data pruning</strong>
  </a><br>
  <small><em>👤 First author: A. Maharana</em></small><br>
  <small><em>📍 Origin: arXiv (2023)</em></small><br>
  📝 Note: balance diversity and difficulty to prune datasets while preserving learning signal.
</div>
<br>
<div>
  <a href="https://openreview.net/pdf?id=yklJpvB7Dq">
    <strong>ELFS: Label-free coreset selection with proxy training dynamics</strong>
  </a><br>
  <small><em>👤 First author: H. Zheng</em></small><br>
  <small><em>📍 Origin: arXiv (2024)</em></small><br>
  📝 Note: label-free coreset construction driven by proxy training dynamics.
</div>
<br>
<div>
  <a href="https://openreview.net/pdf?id=QwKvL6wC8Yi">
    <strong>Coverage-centric coreset selection for high pruning rates</strong>
  </a><br>
  <small><em>👤 First author: H. Zheng</em></small><br>
  <small><em>📍 Origin: arXiv (2022)</em></small><br>
  📝 Note: coreset selection optimized to maintain coverage under aggressive pruning.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2406.05677?">
    <strong>Evolution-aware variance (EVA) coreset selection for medical image classification</strong>
  </a><br>
  <small><em>👤 First author: Y. Hong</em></small><br>
  <small><em>📍 Origin: ACM Multimedia (2024)</em></small><br>
  📝 Note: coreset selection tailored for medical-image classification via temporal variance awareness.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2508.13653?">
    <strong>GRAFT: Gradient-Aware Fast MaxVol Technique for Dynamic Data Sampling</strong>
  </a><br>
  <small><em>👤 First author: A. Jha</em></small><br>
  <small><em>📍 Origin: arXiv (2025)</em></small><br>
  📝 Note: dynamic sampling based on a gradient-aware fast MaxVol approximation.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2503.18709?">
    <strong>Revisiting Automatic Data Curation for Vision Foundation Models in Digital Pathology</strong>
  </a><br>
  <small><em>👤 First author: B. Chen</em></small><br>
  <small><em>📍 Origin: arXiv (2025)</em></small><br>
  📝 Note: automatic data curation for pathology foundation models.
</div>
<br>
<div>
  <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9519166">
    <strong>Data selection in neural networks</strong>
  </a><br>
  <small><em>👤 First author: J. O. Ferreira</em></small><br>
  <small><em>📍 Origin: IEEE Open Journal of Signal Processing (2021)</em></small><br>
  📝 Note: sample-selection perspectives for neural networks and training efficiency.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/1803.00942">
    <strong>Not all samples are created equal: Deep learning with importance sampling</strong>
  </a><br>
  <small><em>👤 First author: A. Katharopoulos</em></small><br>
  <small><em>📍 Origin: ICML (2018)</em></small><br>
  📝 Note: importance sampling to focus optimization on more informative training examples.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/1707.05246">
    <strong>Learning to select data for transfer learning with bayesian optimization</strong>
  </a><br>
  <small><em>👤 First author: S. Ruder</em></small><br>
  <small><em>📍 Origin: arXiv (2017)</em></small><br>
  📝 Note: learn a sampling policy for transfer-learning data selection with Bayesian optimization.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2406.14876">
    <strong>Training greedy policy for proposal batch selection in expensive multi-objective combinatorial optimization</strong>
  </a><br>
  <small><em>👤 First author: D. Lee</em></small><br>
  <small><em>📍 Origin: arXiv (2024)</em></small><br>
  📝 Note: greedy policy for batch selection in high-cost combinatorial optimization problems.
</div>
<br>
<div>
  <a href="https://proceedings.pnas.org/doi/10.1073/pnas.2409913121">
    <strong>Message-Passing Monte Carlo: Generating low-discrepancy point sets via graph neural networks</strong>
  </a><br>
  <small><em>👤 First author: T. K. Rusch</em></small><br>
  <small><em>📍 Origin: PNAS (2024)</em></small><br>
  📝 Note: graph-based point selection for low-discrepancy sampling.
</div>
<br>
<div>
  <a href="https://elib.dlr.de/75758/1/Loyola_2015.pdf">
    <strong>Smart sampling and incremental function learning for very large high dimensional data</strong>
  </a><br>
  <small><em>👤 First author: D. Loyola</em></small><br>
  <small><em>📍 Origin: Neural Networks (2016)</em></small><br>
  📝 Note: smart sampling and incremental learning for very large high-dimensional data.
</div>
<br>
<div>
  <a href="https://proceedings.mlr.press/v28/mineiro13.pdf">
    <strong>Loss-proportional subsampling for subsequent erm</strong>
  </a><br>
  <small><em>👤 First author: P. Mineiro</em></small><br>
  <small><em>📍 Origin: ICML (2013)</em></small><br>
  📝 Note: subsampling according to loss proportion to improve empirical risk minimization.
</div>
<br>
<div>
  <a href="https://jimahn.com/FiCloud2023-smartquerysampling.pdf">
    <strong>Smart Query Sampling with Feature Coverage and Unsupervised Machine Learning</strong>
  </a><br>
  <small><em>👤 First author: J. Tang</em></small><br>
  <small><em>📍 Origin: FiCloud (2023)</em></small><br>
  📝 Note: feature-coverage-based smart query sampling with unsupervised learning.
</div>
<br>
<div>
  <a href="https://openreview.net/pdf?id=jSz59N8NvUP">
    <strong>Retrieve: Coreset selection for efficient and robust semi-supervised learning</strong>
  </a><br>
  <small><em>👤 First author: K. Killamsetty</em></small><br>
  <small><em>📍 Origin: NeurIPS (2021)</em></small><br>
  📝 Note: retrieve a coreset for efficient and robust semi-supervised learning.
</div>
<br>
<div>
  <a href="https://dl.acm.org/doi/pdf/10.1145/3580305.3599326">
    <strong>Efficient coreset selection with cluster-based methods</strong>
  </a><br>
  <small><em>👤 First author: C. Chai</em></small><br>
  <small><em>📍 Origin: KDD (2023)</em></small><br>
  📝 Note: cluster-based coreset selection for efficient learning.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2302.03169">
    <strong>Data selection for language models via importance resampling</strong>
  </a><br>
  <small><em>👤 First author: Sang Michael Xie</em></small><br>
  <small><em>📍 Origin: NeurIPS (2023)</em></small><br>
  📝 Note: importance-resampling based data selection for language model training.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2505.07437">
    <strong>Lead: Iterative data selection for efficient llm instruction tuning</strong>
  </a><br>
  <small><em>👤 First author: X. Lin</em></small><br>
  <small><em>📍 Origin: arXiv (2025)</em></small><br>
  📝 Note: iterative data selection for efficient LLM instruction tuning.
</div>
<br>
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/ed165f2ff227cf36c7e3ef88957dadd9-Paper-Conference.pdf">
    <strong>Greats: Online selection of high-quality data for llm training in every iteration</strong>
  </a><br>
  <small><em>👤 First author: J. T. Wang</em></small><br>
  <small><em>📍 Origin: NeurIPS (2024)</em></small><br>
  📝 Note: online selection of high-quality training examples in every iteration.
</div>
<br>
<div>
  <a href="https://aclanthology.org/2025.acl-long.466.pdf">
    <strong>Efficient Pretraining Data Selection for Language Models via Multi-Actor Collaboration</strong>
  </a><br>
  <small><em>👤 First author: T. Bai</em></small><br>
  <small><em>📍 Origin: ACL (2025)</em></small><br>
  📝 Note: collaborative multi-actor pretraining-data selection for language models.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2402.05123v2">
    <strong>A survey on data selection for llm instruction tuning</strong>
  </a><br>
  <small><em>👤 First author: B. Zhang</em></small><br>
  <small><em>📍 Origin: Journal of Artificial Intelligence Research (2025)</em></small><br>
  📝 Note: survey of data selection strategies for instruction tuning of LLMs.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2408.02085?">
    <strong>Unleashing the power of data tsunami: A comprehensive survey on data assessment and selection for instruction tuning of language models</strong>
  </a><br>
  <small><em>👤 First author: Y. Qin</em></small><br>
  <small><em>📍 Origin: arXiv (2024)</em></small><br>
  📝 Note: comprehensive survey of data assessment and selection for instruction tuning.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2505.12212">
    <strong>Data whisperer: Efficient data selection for task-specific llm fine-tuning via few-shot in-context learning</strong>
  </a><br>
  <small><em>👤 First author: S. Wang</em></small><br>
  <small><em>📍 Origin: arXiv (2025)</em></small><br>
  📝 Note: select efficient task-specific data via few-shot in-context learning.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2408.03560?">
    <strong>In2core: Leveraging influence functions for coreset selection in instruction finetuning of large language models</strong>
  </a><br>
  <small><em>👤 First author: A. Joaquin</em></small><br>
  <small><em>📍 Origin: arXiv (2024)</em></small><br>
  📝 Note: use influence functions to improve coreset selection for instruction tuning.
</div>
<br>
<div>
  <a href="https://openreview.net/pdf?id=FAfxvdv1Dy">
    <strong>Staff: Speculative coreset selection for task-specific fine-tuning</strong>
  </a><br>
  <small><em>👤 First author: X. Zhang</em></small><br>
  <small><em>📍 Origin: ICLR (2025)</em></small><br>
  📝 Note: speculative coreset selection for task-specific fine-tuning.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2311.08182">
    <strong>Self-evolved diverse data sampling for efficient instruction tuning</strong>
  </a><br>
  <small><em>👤 First author: S. Wu</em></small><br>
  <small><em>📍 Origin: arXiv (2023)</em></small><br>
  📝 Note: self-evolving sampling strategy to improve instruction-tuning efficiency.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2410.07041">
    <strong>Emergent properties with repeated examples</strong>
  </a><br>
  <small><em>👤 First author: François Charton</em></small><br>
  <small><em>📍 Origin: arXiv (2024)</em></small><br>
  📝 Note: study the effects of repeated examples and their role in data selection.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2508.10104">
    <strong>DINOv3</strong>
  </a><br>
  <small><em>👤 First author: O. Siméoni</em></small><br>
  <small><em>📍 Origin: arXiv (2025)</em></small><br>
  📝 Note: representation-based foundation model that can serve as a sampling signal in self-supervised pipelines.
</div>
<br>
<div>
  <a href="https://arxiv.org/pdf/2507.11845">
    <strong>ProtoConNet: Prototypical Augmentation and Alignment for Open-Set Few-Shot Image Classification</strong>
  </a><br>
  <small><em>👤 First author: K. Shi</em></small><br>
  <small><em>📍 Origin: arXiv (2025)</em></small><br>
  📝 Note: prototype-based selection and alignment for few-shot and open-set image classification.
</div>

### Smarter selection based on clustering
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/24a8968affe71ffe4067d022b9d16566-Abstract-Datasets_and_Benchmarks_Track.html">
    <strong>Nemotron-climb: Clustering-based iterative data mixture bootstrapping for language model pre-training</strong>
  </a><br>
  <small><em>👤 First author: Shizhe Diao</em></small><br>
  <small><em>📍 Origin: Advances in Neural Information Processing Systems (2026)</em></small><br>
  📝 Note: Data selection during LLM pretraining
</div>
<br>
<div>
  <a href="https://www.sciencedirect.com/science/article/pii/S2643651526000798">
    <strong>MoCoProto: Enhancing few-shot pest image classification with self-supervised representation learning</strong>
  </a><br>
  <small><em>👤 First author: Dong Jin</em></small><br>
  <small><em>📍 Origin: Plant Phenomics (2026)</em></small><br>
  📝 Note: data selection during SSL on images
</div>
<br>
<div>
  <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/e4bc9cdebfbcc43b0800cf99ffec5ee1-Abstract-Conference.html">
    <strong>Effective pruning of web-scale datasets based on complexity of concept clusters</strong>
  </a><br>
  <small><em>👤 First author: Amro Kamal</em></small><br>
  <small><em>📍 Origin: International Conference on Learning Representations (2024)</em></small><br>
  📝 Note: Remove data in clusters at different rates depending on population
</div>

### Active learning:
<div>
  <a href="https://arxiv.org/abs/2606.07630">
    <strong>Active Learning with Foundation Model Priors: Efficient Learning under Class Imbalance</strong>
  </a><br>
  <small><em>👤 First author: Jiancheng Zhang</em></small><br>
  <small><em>📍 Origin: International Conference on Machine Learning (ICML) (2026)</em></small><br>
  📝 Note: Make data selection using a foundation model and a small classifier model for image and text with imbalance and label noise
</div>
