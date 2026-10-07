# Training strategy - Introduction

> This folder gathers the strategies that shape efficient and robust model training over time.

## At a glance
[📚 Bibliography](BIBLIOGRAPHY.md)<br>
[💡 Ideas](IDEAS.md)<br>
[👥 Researchers](RESEARCHERS.md)<br>
[🧰 Tools](TOOLS.md)

## Context

A training strategy defines how data and learning signals are presented to a model over time.
Rather than simply feeding all examples in a random order, a strategy can decide which samples
to use first, which ones to revisit later, which ones to label, and how to adapt the training
schedule as the model improves. Examples include active learning, where the model focuses on
uncertain or informative samples; curriculum learning, where the model starts with easier
examples and gradually moves to harder ones; and continual learning, where the model updates
without losing past knowledge.

These strategies are important because optimization is not only about the model architecture or
loss function. The order and selection of data can strongly influence convergence speed,
robustness, and the quality of the final representation. Simple random shuffling is common in
practice because it is easy and stable, but it can be inefficient. When training data contains
redundant examples, class imbalance, noisy labels, or difficult edge cases, random shuffling
often wastes time on low-value examples and delays useful learning signals.

This is why smarter training strategies matter: they can improve sample efficiency, reduce
annotation cost, speed up convergence, and help the model focus on the regions of the data
space that matter most.

This topic therefore focuses on training strategies driven by the data itself: deciding which
samples to present, when, and how often (curriculum learning, online batch selection,
over/under-sampling of imbalanced data), active and continual learning with data-aware
selection or replay, using learning dynamics or embeddings to identify easy, hard,
redundant, or mislabeled samples, and data-driven checkpointing or train/validation
updates. Papers that only change the optimizer, schedule, or architecture, without using
information about the data, are out of scope.

## Resources

The resources in this folder are intended to support both research and practical work,
from understanding the state of the art to turning ideas into experiments and product
improvements. In this folder you can find:

[📚 Bibliography](BIBLIOGRAPHY.md): training-strategy references and surveys<br>
[💡 Ideas](IDEAS.md): research questions and open directions<br>
[👥 Researchers](RESEARCHERS.md): authors and contributors in this area<br>
[🧰 Tools](TOOLS.md): practical tools and libraries
