# Augmentation - Bibliography

## No embeddings

<div>
  <a href="https://arxiv.org/abs/2505.21574">
    <strong>Do We Need All the Synthetic Data? Targeted Image Augmentation via Diffusion Models</strong>
  </a><br>
  <small><em>👤 First author: Dang Nguyen</em></small><br>
  <small><em>📍 Origin: International Conference on Learning Representations (ICLR) (2026)</em></small><br>
  📝 Note: uses the learning dynamics on the real training data to augment only the examples not learned early in training (30–40% of the data), outperforming augmentation of the whole dataset at a fraction of the generation cost.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2312.12112">
    <strong>Curated LLM: Synergy of LLMs and Data Curation for tabular augmentation in low-data regimes</strong>
  </a><br>
  <small><em>👤 First author: Nabeel Seedat</em></small><br>
  <small><em>📍 Origin: International Conference on Machine Learning (ICML) (2024)</em></small><br>
  📝 Note: curates LLM-generated tabular samples with the learning dynamics (confidence and aleatoric uncertainty) of a model trained on the small real dataset, keeping only the synthetic samples consistent with the original data.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2305.09235">
    <strong>Synthetic data, real errors: how (not) to publish and use synthetic data</strong>
  </a><br>
  <small><em>👤 First author: Boris van Breugel</em></small><br>
  <small><em>📍 Origin: International Conference on Machine Learning (ICML) (2023)</em></small><br>
  📝 Note: shows that models trained on synthetic data as if it were real degrade on real data (especially minority classes and sparse regions), and proposes Deep Generative Ensembles to account for generative uncertainty when evaluating on real data.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2310.16981">
    <strong>Reimagining Synthetic Tabular Data Generation through Data-Centric AI: A Comprehensive Benchmark</strong>
  </a><br>
  <small><em>👤 First author: Lasse Hansen</em></small><br>
  <small><em>📍 Origin: Conference on Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks (2023)</em></small><br>
  📝 Note: profiles the real data (easy/ambiguous/hard samples) with data-centric tools and checks whether synthetic data preserves that profile, showing that high statistical fidelity does not guarantee downstream utility on real data.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2310.00158">
    <strong>Feedback-guided Data Synthesis for Imbalanced Classification</strong>
  </a><br>
  <small><em>👤 First author: Reyhane Askari Hemmat</em></small><br>
  <small><em>📍 Origin: arXiv (2023)</em></small><br>
  📝 Note: uses one-shot feedback (loss, entropy) from a classifier trained on the real data to steer diffusion sampling towards useful synthetic samples that stay close to the real data support.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/1706.02633">
    <strong>Real-valued (Medical) Time Series Generation with Recurrent Conditional GANs</strong>
  </a><br>
  <small><em>👤 First author: Cristóbal Esteban</em></small><br>
  <small><em>📍 Origin: arXiv (2017)</em></small><br>
  📝 Note: introduces the Train on Synthetic, Test on Real (TSTR) evaluation, validating synthetic data by the performance on a real test set of a model trained on it.
</div>

---

## Leverage embeddings

<div>
  <a href="https://arxiv.org/abs/2503.10687">
    <strong>Context-guided Responsible Data Augmentation with Diffusion Models</strong>
  </a><br>
  <small><em>👤 First author: Khawar Islam</em></small><br>
  <small><em>📍 Origin: International Conference on Learning Representations Workshops (ICLRW) (2025)</em></small><br>
  📝 Note: discards diffusion-generated augmentations whose CLIP embedding falls below a hard cosine-similarity threshold with the embedding of the original image they were generated from.
</div>
<br>
<div>
  <a href="https://eccv.ecva.net/virtual/2026/poster/5056">
    <strong>HSFM: Hard-Set-Guided Feature-Space Meta-Learning for Robust Classification under Spurious Correlations</strong>
  </a><br>
  <small><em>👤 First author: Aryan Yazdan Parast</em></small><br>
  <small><em>📍 Origin: European Conference on Computer Vision (ECCV) (2026)</em></small><br>
  📝 Note: meta-learns feature-space edits on frozen backbone features, scoring them by the loss of the retrained head on a hard set of real validation samples (the highest-loss ones per class).
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2102.08921">
    <strong>How Faithful is your Synthetic Data? Sample-level Metrics for Evaluating and Auditing Generative Models</strong>
  </a><br>
  <small><em>👤 First author: Ahmed M. Alaa</em></small><br>
  <small><em>📍 Origin: International Conference on Machine Learning (ICML) (2022)</em></small><br>
  📝 Note: embeds real and synthetic samples to compute sample-level α-Precision, β-Recall and Authenticity, enabling auditing that discards synthetic samples falling outside the support of the real data.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/1904.06991">
    <strong>Improved Precision and Recall Metric for Assessing Generative Models</strong>
  </a><br>
  <small><em>👤 First author: Tuomas Kynkäänniemi</em></small><br>
  <small><em>📍 Origin: Conference on Neural Information Processing Systems (NeurIPS) (2019)</em></small><br>
  📝 Note: builds k-NN manifolds of real and generated samples in a pretrained feature space to measure quality and coverage, and derives a per-sample realism score against the real data.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2002.09797">
    <strong>Reliable Fidelity and Diversity Metrics for Generative Models</strong>
  </a><br>
  <small><em>👤 First author: Muhammad Ferjad Naeem</em></small><br>
  <small><em>📍 Origin: International Conference on Machine Learning (ICML) (2020)</em></small><br>
  📝 Note: proposes density and coverage, computed from k-NN neighbourhoods of real-sample embeddings, as outlier-robust measures of how well generated samples match the real data.
</div>
