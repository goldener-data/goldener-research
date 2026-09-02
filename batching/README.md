# Batching - Introduction

> This folder brings together the literature and discussion around efficient batch construction and sample grouping.

## At a glance
[📚 Bibliography](BIBLIOGRAPHY.md)<br>
[💡 Ideas](IDEAS.md)<br>
[👥 Researchers](RESEARCHERS.md)

## Context

Batching during neural network training is the strategy of dividing a training dataset
into smaller, uniformly sized subsets—called mini-batches—to compute loss and update model
parameters iteratively, balancing computational speed with gradient accuracy.

Batching serves three primary roles in training neural networks: maximizing computational
throughput via hardware parallelization, injecting stochastic noise to improve
optimization and generalization, and managing physical VRAM constraints.

The standard practice for batching is to divide the training dataset into mini-batches of
size `batch_size` and iterate over the mini-batches. Between the different iterations over
the full dataset, the mini-batches are created from random draws among the samples.

The random selection of mini-batches acts as an implicit regularizer. The resulting noisy
updates help optimizer trajectories escape shallow local minima and flat saddle points,
pushing parameter weights toward flatter, higher-generalizing regions of the loss
landscape. However, this randomness might also be pushing the model toward unwanted areas,
especially when the concept distribution in batches is skewed.

## Resources

The resources in this folder are intended to support both research and practical work,
from understanding the state of the art to turning ideas into experiments and product
improvements. In this folder you can find:

[📚 Bibliography](BIBLIOGRAPHY.md): key papers and references on batching<br>
[💡 Ideas](IDEAS.md): open questions and research directions<br>
[👥 Researchers](RESEARCHERS.md): authors and contributors active in this area
