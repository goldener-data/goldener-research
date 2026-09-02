# Model design - Introduction

> This folder focuses on choosing architectures, training configurations, and model-selection strategies.

## At a glance
[📚 Bibliography](BIBLIOGRAPHY.md)<br>
[💡 Ideas](IDEAS.md)<br>
[👥 Researchers](RESEARCHERS.md)

## Context

Model design is the process of searching for the best architecture and training
configuration before a model is deployed in production. This includes choosing the model
family, depth, width, regularization, learning rate, batch size, schedule, and many other
hyperparameters that influence learning speed, stability, and final performance. In practice,
this search is not just a technical formality: it determines whether a model is accurate,
robust, efficient, and cost-effective in the real world.

The challenge is that the space of possible architectures and hyperparameters is very large,
and evaluating them naively can be expensive and unreliable. A model that looks excellent on a
single benchmark may still perform poorly under different data conditions, labeling noise, or
deployment constraints. Without a careful search procedure, teams may overfit to a small
validation set, choose settings that are brittle, or burn large amounts of compute on
configurations that bring little value.

## Resources

The resources in this folder are intended to support both research and practical work,
from understanding the state of the art to turning ideas into experiments and product
improvements. In this folder you can find:

[📚 Bibliography](BIBLIOGRAPHY.md): model-design and selection references<br>
[💡 Ideas](IDEAS.md): research questions and candidate directions<br>
[👥 Researchers](RESEARCHERS.md): active contributors in this topic
