# Losses - Introduction

> This folder collects the definitions, references, and discussions around loss design and optimization.

## At a glance
[📚 Bibliography](BIBLIOGRAPHY.md)<br>
[💡 Ideas](IDEAS.md)<br>
[👥 Researchers](RESEARCHERS.md)

## Context

The loss is the quantity a machine learning model tries to minimize during training. It
measures how far the model's predictions are from the desired targets, and it provides the
training signal used by the optimizer to update the model parameters. In other words, the
loss defines what the model considers to be a good or bad prediction, and therefore shapes
what it learns.

Different loss functions are designed for different goals. For classification, they may focus
on separating classes; for regression, they may penalize prediction error; for contrastive
learning, they may emphasize representation similarity and dissimilarity. A good loss should
align with the task objective, encourage stable optimization, and help the model learn
features that generalize beyond the training data.

The main issue is that a poorly chosen or poorly balanced loss can hurt learning even when the
model and data are otherwise reasonable. It may ignore important rare cases, overemphasize
easy examples, become unstable during optimization, or produce representations that are not
useful for the downstream task. In imbalanced or noisy settings, a naive loss can lead to
weak minority-class performance, poor calibration, or a representation space that collapses
or becomes dominated by a few patterns.

This topic therefore focuses on losses that leverage the data itself to shape the training
signal: reweighting samples by density, difficulty, or rarity (e.g. measured in an
embedding space), using the structure of the data to mine positives and negatives for
contrastive learning, pseudo-labels or soft targets derived from data neighborhoods,
robustness to label noise and imbalance, and embedding-based objectives (e.g. matching a
pretrained representation). Papers that propose a new loss purely from an optimization or
architectural point of view, without using properties of the data, are out of scope.

## Resources

The resources in this folder are intended to support both research and practical work,
from understanding the state of the art to turning ideas into experiments and product
improvements. In this folder you can find:

[📚 Bibliography](BIBLIOGRAPHY.md): key papers on loss design and optimization<br>
[💡 Ideas](IDEAS.md): open problems and promising directions<br>
[👥 Researchers](RESEARCHERS.md): authors and contributors in this area
