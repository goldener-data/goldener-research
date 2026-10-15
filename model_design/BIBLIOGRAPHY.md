# Model design - Bibliography

## No embeddings

<div>
  <a href="https://arxiv.org/abs/2602.08351">
    <strong>The Chicken and Egg Dilemma: Co-optimizing Data and Model Configurations for LLMs</strong>
  </a><br>
  <small><em>👤 First author: Zhiliang Chen</em></small><br>
  <small><em>📍 Origin: arXiv (2026)</em></small><br>
  📝 Note: use scaling laws applied after a few training steps to select the best configuration.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2410.13609">
    <strong>All models are wrong, some are useful: Model Selection with Limited Labels</strong>
  </a><br>
  <small><em>👤 First author: Patrik Okanovic</em></small><br>
  <small><em>📍 Origin: Proceedings of The 28th International Conference on Artificial Intelligence and Statistics (AISTATS) (2025)</em></small><br>
  📝 Note: use less data to find the best model and training config before training on the full data.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2605.24981">
    <strong>Large Language Model Selection with Limited Annotations</strong>
  </a><br>
  <small><em>👤 First author: Yavuz Durmazkeser</em></small><br>
  <small><em>📍 Origin: International Conference on Learning Representations (ICLR) (2026)</em></small><br>
  📝 Note: select the best LLM from restricted data selected from a reference model output.
</div>
<br>
<div>
  <a href="https://scholar.google.fr/citations?view_op=view_citation&hl=fr&user=xf1T870AAAAJ&sortby=pubdate&citation_for_view=xf1T870AAAAJ:QUX0mv85b1cC">
    <strong>LT-Soups: Bridging Head and Tail Classes via Subsampled Model Soups</strong>
  </a><br>
  <small><em>👤 First author: Masih Aminbeidokhti</em></small><br>
  <small><em>📍 Origin: Advances in Neural Information Processing Systems (NeurIPS) (2025)</em></small><br>
  📝 Note: No note provided.
</div>
<br>
<div>
  <a href="https://eccv.ecva.net/virtual/2026/poster/4464">
    <strong>Unsupervised Source-Free Ranking of Biomedical Segmentation Models Under Distribution Shift</strong>
  </a><br>
  <small><em>👤 First author: Joshua Talks</em></small><br>
  <small><em>📍 Origin: European Conference on Computer Vision (ECCV) (2026)</em></small><br>
  📝 Note: ranks pretrained segmentation models on a new unlabeled dataset by prediction consistency under perturbations, enabling black-box model selection under distribution shift.
</div>

### AutoML
<div>
  <a href="https://arxiv.org/abs/1603.06560">
    <strong>Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization</strong>
  </a><br>
  <small><em>👤 First author: Lisha Li</em></small><br>
  <small><em>📍 Origin: Journal of Machine Learning Research (JMLR) (2018)</em></small><br>
  📝 Note: speeds up random search by allocating a resource such as iterations, data samples or features to sampled configurations and early-stopping the weak ones.
</div>
<br>
<div>
  <a href="https://proceedings.neurips.cc/paper_files/paper/2015/hash/11d0e6287202fced83f79975ec59a3a6-Abstract.html">
    <strong>Efficient and Robust Automated Machine Learning</strong>
  </a><br>
  <small><em>👤 First author: Matthias Feurer</em></small><br>
  <small><em>📍 Origin: Advances in Neural Information Processing Systems (NeurIPS) (2015)</em></small><br>
  📝 Note: auto-sklearn: warm-starts the pipeline search from past performance on similar datasets and ensembles the models evaluated during the search.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/1908.00709">
    <strong>AutoML: A Survey of the State-of-the-Art</strong>
  </a><br>
  <small><em>👤 First author: Xin He</em></small><br>
  <small><em>📍 Origin: Knowledge-Based Systems (2021)</em></small><br>
  📝 Note: survey of the AutoML pipeline, from data preparation and feature engineering to hyperparameter optimization and neural architecture search.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2107.05847">
    <strong>Hyperparameter Optimization: Foundations, Algorithms, Best Practices and Open Challenges</strong>
  </a><br>
  <small><em>👤 First author: Bernd Bischl</em></small><br>
  <small><em>📍 Origin: WIREs Data Mining and Knowledge Discovery (2023)</em></small><br>
  📝 Note: reviews HPO methods and gives practical recommendations, including resampling-based performance evaluation and combining HPO with ML pipelines.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/1605.07079">
    <strong>Fast Bayesian Optimization of Machine Learning Hyperparameters on Large Datasets</strong>
  </a><br>
  <small><em>👤 First author: Aaron Klein</em></small><br>
  <small><em>📍 Origin: International Conference on Artificial Intelligence and Statistics (AISTATS) (2017)</em></small><br>
  📝 Note: Fabolas: models validation error and cost as a function of training set size to explore configurations on small data subsets and extrapolate to the full dataset.
</div>
<br>
<div>
  <a href="https://ojs.aaai.org/index.php/AAAI/article/view/9354">
    <strong>Initializing Bayesian Hyperparameter Optimization via Meta-Learning</strong>
  </a><br>
  <small><em>👤 First author: Matthias Feurer</em></small><br>
  <small><em>📍 Origin: AAAI Conference on Artificial Intelligence (AAAI) (2015)</em></small><br>
  📝 Note: starts Bayesian hyperparameter optimization from configurations that performed well on similar datasets.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2007.04074">
    <strong>Auto-Sklearn 2.0: Hands-free AutoML via Meta-Learning</strong>
  </a><br>
  <small><em>👤 First author: Matthias Feurer</em></small><br>
  <small><em>📍 Origin: Journal of Machine Learning Research (JMLR) (2022)</em></small><br>
  📝 Note: meta-feature-free meta-learning and bandit budget allocation make AutoML work on large datasets under tight time limits, with the AutoML policy itself chosen automatically.
</div>
<br>
<div>
  <a href="https://doi.org/10.1162/EVCO_a_00069">
    <strong>Resampling Methods for Meta-Model Validation with Recommendations for Evolutionary Computation</strong>
  </a><br>
  <small><em>👤 First author: Bernd Bischl</em></small><br>
  <small><em>📍 Origin: Evolutionary Computation (2012)</em></small><br>
  📝 Note: discusses cross-validation, subsampling, bootstrapping and nested resampling for validating models, with their pitfalls for model selection and performance assessment.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/1802.02219">
    <strong>Practical Transfer Learning for Bayesian Optimization</strong>
  </a><br>
  <small><em>👤 First author: Matthias Feurer</em></small><br>
  <small><em>📍 Origin: arXiv (2018)</em></small><br>
  📝 Note: transfers knowledge from hyperparameter optimization runs on previous datasets to speed up the search on a new dataset.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2212.06751">
    <strong>Speeding Up Multi-Objective Hyperparameter Optimization by Task Similarity-Based Meta-Learning for the Tree-Structured Parzen Estimator</strong>
  </a><br>
  <small><em>👤 First author: Shuhei Watanabe</em></small><br>
  <small><em>📍 Origin: International Joint Conference on Artificial Intelligence (IJCAI) (2023)</em></small><br>
  📝 Note: meta-learns multi-objective TPE across tasks weighted by a task similarity defined by the overlap of their top domains.
</div>
<br>
<div>
  <a href="https://openreview.net/forum?id=5aYGXxByI6">
    <strong>MASIF: Meta-learned Algorithm Selection using Implicit Fidelity Information</strong>
  </a><br>
  <small><em>👤 First author: Tim Ruhkopf</em></small><br>
  <small><em>📍 Origin: Transactions on Machine Learning Research (TMLR) (2023)</em></small><br>
  📝 Note: selects an algorithm for a new dataset by meta-learning on the algorithms' learning behaviour across fidelities instead of cheap dataset properties or landmarks.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2405.15393">
    <strong>Reshuffling Resampling Splits Can Improve Generalization of Hyperparameter Optimization</strong>
  </a><br>
  <small><em>👤 First author: Thomas Nagler</em></small><br>
  <small><em>📍 Origin: Advances in Neural Information Processing Systems (NeurIPS) (2024)</em></small><br>
  📝 Note: shows that reshuffling the train-validation or cross-validation splits for every configuration often improves the generalization of the selected configuration.
</div>

---

## Leverage embeddings

### Dataset assessment

<div>
  <a href="https://arxiv.org/abs/2605.29448">
    <strong>How Much Is a Dataset Worth? Scaling Laws, the Vendi Score, and Matrix Spectral Functions</strong>
  </a><br>
  <small><em>👤 First author: Jeff A. Bilmes</em></small><br>
  <small><em>📍 Origin: arXiv (2026)</em></small><br>
  📝 Note: No note provided.
</div>
<br>
<div>
  <a href="https://arxiv.org/abs/2210.02410">
    <strong>The vendi score: A diversity evaluation metric for machine learning</strong>
  </a><br>
  <small><em>👤 First author: Dan Friedman</em></small><br>
  <small><em>📍 Origin: Transactions on Machine Learning Research (TMLR) (2023)</em></small><br>
  📝 Note: No note provided.
</div>
