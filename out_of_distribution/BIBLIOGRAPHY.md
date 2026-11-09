# Out-of-distribution - Bibliography

## Survey/Benchmark

<div>
  <a href="https://scholar.google.fr/citations?view_op=view_citation&hl=fr&user=TB5OwW8AAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=TB5OwW8AAAAJ:abG-DnoFyZgC">
    <strong>ImageNet-OOD: Deciphering modern out-of-distribution detection algorithms</strong>
  </a><br>
  <small><em>👤 First author: William Yang</em></small><br>
  <small><em>📍 Origin: International Conference on Learning Representations (ICLR) (2024)</em></small><br>
  📝 Note: No note provided.
</div>


---

## Metrics

<div>
  <a href="https://arxiv.org/abs/2602.10062">
    <strong>Vendi Novelty Scores for Out-of-Distribution Detection</strong>
  </a><br>
  <small><em>👤 First author: Amey P. Pasarkar</em></small><br>
  <small><em>📍 Origin: arXiv (2026)</em></small><br>
  📝 Note: No note provided.
</div>

---

## Leverage embeddings

<div>
  <a href="https://arxiv.org/abs/2407.12427">
    <strong>GeneralAD: Anomaly Detection Across Domains by Attending to Distorted Features</strong>
  </a><br>
  <small><em>👤 First author: Luc P.J. Sträter</em></small><br>
  <small><em>📍 Origin: European Conference on Computer Vision (ECCV) (2024)</em></small><br>
  📝 Note: self-supervised anomaly generation on ViT patch features (noise, shuffling) with an attention-based discriminator, reaching state-of-the-art results across both semantic and industrial anomaly detection benchmarks.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2412.11148">
    <strong>Redefining Normal: A Novel Object-Level Approach for Multi-Object Novelty Detection</strong>
  </a><br>
  <small><em>👤 First author: Mohammadreza Salehi</em></small><br>
  <small><em>📍 Origin: Asian Conference on Computer Vision (ACCV) (2024)</em></small><br>
  📝 Note: redefines normality at the object level via dense feature fine-tuning on normal data and masked knowledge distillation, improving multi-object novelty detection.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2608.09427">
    <strong>Foundation Models are Implicit Deepfake Detectors</strong>
  </a><br>
  <small><em>👤 First author: Stefan Smeu</em></small><br>
  <small><em>📍 Origin: arXiv (2026)</em></small><br>
  📝 Note: finds that fake samples systematically produce lower-magnitude pretrained representations than real ones, so treating detection as an anomaly-detection problem on feature magnitude rivals far more sophisticated deepfake detectors.
</div>
<br>
<div>
  <a href="https://eccv.ecva.net/virtual/2026/poster/3729">
    <strong>Unified Multi-Layer Subspace Modeling for Cross-Domain OOD Detection</strong>
  </a><br>
  <small><em>👤 First author: Gerhard Krumpl</em></small><br>
  <small><em>📍 Origin: European Conference on Computer Vision (ECCV) (2026)</em></small><br>
  📝 Note: fuses intermediate and deep features into one embedding, models its in-distribution principal subspace and scores Mahalanobis distance plus residual energy, working across natural, medical and industrial inspection images.
</div>
<br>
<div>
  <a href="https://eccv.ecva.net/virtual/2026/poster/3575">
    <strong>Distribution-Aware Feature Selection for Post-hoc Out-of-Distribution Detection</strong>
  </a><br>
  <small><em>👤 First author: Max Gutbrod</em></small><br>
  <small><em>📍 Origin: European Conference on Computer Vision (ECCV) (2026)</em></small><br>
  📝 Note: ranks feature dimensions by the Wasserstein distance between in-distribution and proxy-OOD features and keeps only the most discriminative ones for post-hoc detectors.
</div>
<br>
<div>
  <a href="https://eccv.ecva.net/virtual/2026/poster/5630">
    <strong>Exploiting Local Flatness for Efficient Out-of-Distribution Detection</strong>
  </a><br>
  <small><em>👤 First author: Seonghwan Park</em></small><br>
  <small><em>📍 Origin: European Conference on Computer Vision (ECCV) (2026)</em></small><br>
  📝 Note: exploits the larger feature-space Hessian curvature of OOD inputs with partial feature normalization, giving a post-hoc detector as cheap as a forward pass.
</div>
<br>
<div>
  <a href="https://eccv.ecva.net/virtual/2026/poster/4401">
    <strong>Why Feature Magnitude Deceives OOD Detectors: An Angular Separation Perspective</strong>
  </a><br>
  <small><em>👤 First author: Hanlin Li</em></small><br>
  <small><em>📍 Origin: European Conference on Computer Vision (ECCV) (2026)</em></small><br>
  📝 Note: shows feature magnitude lets low-norm OOD samples evade distance-based detectors and l2-normalizes features before the classifier to learn angular separation.
</div>
<br>
<div>
  <a href="https://eccv.ecva.net/virtual/2026/poster/5320">
    <strong>A Comprehensive Analysis about Unsupervised Outlier Detection for Images</strong>
  </a><br>
  <small><em>👤 First author: Zhonghang Liu</em></small><br>
  <small><em>📍 Origin: European Conference on Computer Vision (ECCV) (2026)</em></small><br>
  📝 Note: revisits unsupervised image outlier detection beyond frozen natural-image features by exploiting distribution priors, covering industrial, medical and natural domains.
</div>
<br>
<div>
  <a href="https://papers.miccai.org/miccai-2026/0614-Paper0289.html">
    <strong>MaRS: Robust Out-of-Distribution Detection via Mahalanobis Residual Scoring</strong>
  </a><br>
  <small><em>👤 First author: Francesco Di Salvo</em></small><br>
  <small><em>📍 Origin: Medical Image Computing and Computer Assisted Intervention (MICCAI) (2026)</em></small><br>
  📝 Note: scores reconstruction residuals of frozen foundation model embeddings with a Mahalanobis distance instead of an L2 norm, making latent reconstruction a robust label-free OOD detector.
</div>
<br>
<div>
  <a href="https://papers.miccai.org/miccai-2026/0827-Paper4773.html">
    <strong>PROTON: Prototype-Based Test-Time Online OOD Detection for Medical VLMs</strong>
  </a><br>
  <small><em>👤 First author: Abhijit Das</em></small><br>
  <small><em>📍 Origin: Medical Image Computing and Computer Assisted Intervention (MICCAI) (2026)</em></small><br>
  📝 Note: keeps an online bank of embedding prototypes from confident test predictions and fuses prototype distance with concept matching to catch covariate shifts invisible in softmax space.
</div>
<br>
<div>
  <a href="https://papers.miccai.org/miccai-2026/0163-Paper1242.html">
    <strong>CHILD: Human-in-the-Loop OOD Detection for Safe Clinical Deployment</strong>
  </a><br>
  <small><em>👤 First author: Jinlun Ye</em></small><br>
  <small><em>📍 Origin: Medical Image Computing and Computer Assisted Intervention (MICCAI) (2026)</em></small><br>
  📝 Note: sends only the most decision-uncertain streaming samples to physicians and calibrates OOD scores by retrieval over a compact feature cache of the reviewed samples.
</div>
<br>
<div>
  <a href="https://papers.miccai.org/miccai-2026/1147-Paper0474.html">
    <strong>Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging</strong>
  </a><br>
  <small><em>👤 First author: Bernhard Kainz</em></small><br>
  <small><em>📍 Origin: Medical Image Computing and Computer Assisted Intervention (MICCAI) (2026)</em></small><br>
  📝 Note: selects healthy reference images by sliced Wasserstein distance between DINOv3 patch distributions to improve zero-shot VLM anomaly localisation.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2606.21386">
    <strong>VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models</strong>
  </a><br>
  <small><em>👤 First author: Florian Seligmann</em></small><br>
  <small><em>📍 Origin: Conference on Robot Learning (CoRL) (2026)</em></small><br>
  📝 Note: detects runtime failures of vision-language-action policies without failure data, notably with a token-wise last-layer Mahalanobis distance to training features.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2508.03108">
    <strong>Pseudo-label Induced Subspace Representation Learning for Robust Out-of-Distribution Detection</strong>
  </a><br>
  <small><em>👤 First author: Tarhib Al Azad</em></small><br>
  <small><em>📍 Origin: IEEE International Conference on Image Processing (ICIP) (2026)</em></small><br>
  📝 Note: learns a pseudo-label-induced subspace of the feature space with a subspace-distance regularizer to separate in-distribution and OOD samples.
</div>
<br>
<div>
  <a href="https://people.cs.nycu.edu.tw/~yushuen/data/CBAM_OOD_26.pdf">
    <strong>Out-of-Distribution Detection with Angular-Magnitude Likelihood and Targeted Feature Refinement</strong>
  </a><br>
  <small><em>👤 First author: Atik Garg</em></small><br>
  <small><em>📍 Origin: IEEE International Conference on Image Processing (ICIP) (2026)</em></small><br>
  📝 Note: fuses the angular (confidence) and magnitude (feature norm) components of the feature vector into one likelihood score, with attention-refined layers making feature norms more reliable.
</div>
<br>
<div>
  <a href="https://doi.org/10.1109/ISBI53787.2023.10230433">
    <strong>Fine-Grained Out-of-Distribution Detection of Medical Images using Combination of Feature Uncertainty and Mahalanobis Distance</strong>
  </a><br>
  <small><em>👤 First author: Jie Wei</em></small><br>
  <small><em>📍 Origin: IEEE International Symposium on Biomedical Imaging (ISBI) (2023)</em></small><br>
  📝 Note: combines multi-scale feature uncertainty with the Mahalanobis distance to training class distributions in feature space to flag unseen fine-grained disease classes.
</div>
