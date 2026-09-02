# Out-of-distribution - Introduction

> This folder centralizes the OOD-related papers, ideas, and contributors for robust monitoring and deployment.

## At a glance
[📚 Bibliography](BIBLIOGRAPHY.md)<br>
[💡 Ideas](IDEAS.md)<br>
[👥 Researchers](RESEARCHERS.md)

## Context

Out-of-distribution (OOD) refers to the situation where the data seen at inference time
comes from a different distribution than the one used during training. This can happen when
new environments, unseen classes, corrupted features, or shifted user behaviors appear after
deployment. In such cases, the model may still be asked to make predictions on inputs that
it has not learned to handle reliably.

The impact on model performance can be severe. A model trained on one data distribution may
produce overconfident but wrong predictions when faced with OOD samples, especially if it has
not learned to recognize uncertainty or novelty. This often leads to silent failures, reduced
reliability, and poor trust in the system, even when the model performs well on ordinary
in-distribution examples.

This is why OOD detection is crucial in practical AI pipelines. By identifying whether an
input is unusual or inconsistent with the training distribution, systems can decide to abstain,
route the sample to human review, trigger retraining, or simply flag the case for monitoring.

## Resources

The resources in this folder are intended to support both research and practical work,
from understanding the state of the art to turning ideas into experiments and product
improvements. In this folder you can find:

[📚 Bibliography](BIBLIOGRAPHY.md): core papers and references on OOD detection<br>
[💡 Ideas](IDEAS.md): open questions and research directions<br>
[👥 Researchers](RESEARCHERS.md): authors and contributors in the field
