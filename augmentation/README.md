# Augmentation - Introduction

> This folder brings together the literature and discussion around data augmentation strategies for AI pipelines.

## At a glance
[📚 Bibliography](BIBLIOGRAPHY.md)<br>
[💡 Ideas](IDEAS.md)<br>
[👥 Researchers](RESEARCHERS.md)

## Context

Data augmentation is a central component of modern AI training because it increases data
diversity without
requiring additional labels. By creating controlled transformations of existing samples,
augmentation helps models learn invariances, improve robustness to noise, reduce
overfitting, and generalize better on small or imbalanced datasets. In practice, it is
often the difference between a model that memorizes the training set and a model that
captures stable features useful beyond the observed examples.

However, augmentation can also be inefficient. Many transformations are generic,
redundant, or even harmful when they distort the semantics of the data. Random
augmentations may create many low-value examples, increase training time, and waste
compute without improving the downstream task.

This topic therefore focuses on how the initial (real) data can drive synthetic
augmentation: choosing which samples or regions of the data to augment (e.g. from
learning dynamics), filtering or auditing generated samples against the original samples
(e.g. in an embedding space), measuring the fidelity and coverage of synthetic data
relative to the real distribution, or checking the downstream benefit of synthetic data
on real data. Papers that only propose a new way to generate or mix samples, without
using the original data to guide or validate them, are out of scope.

## Resources

The resources in this folder are intended to support both research and practical work,
from understanding
the state of the art to turning ideas into experiments and product improvements. In this
folder you can find:

[📚 Bibliography](BIBLIOGRAPHY.md): key papers and references on augmentation<br>
[💡 Ideas](IDEAS.md): open questions and research directions<br>
[👥 Researchers](RESEARCHERS.md): authors and contributors active in this area
