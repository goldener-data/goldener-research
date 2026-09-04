# Data selection - Introduction

> This folder focuses on choosing the most informative data points for training, evaluation, and monitoring.

## At a glance
[📚 Bibliography](BIBLIOGRAPHY.md)<br>
[💡 Ideas](IDEAS.md)<br>
[👥 Researchers](RESEARCHERS.md)<br>
[🧰 Tools](TOOLS.md)

## Context

Data selection and splitting are critical because they determine what the model actually learns,
how it is evaluated, and how reliably it will behave in production. High-quality training
samples improve learning efficiency, reduce label noise, and support better generalization,
while careful validation and monitoring splits help detect overfitting, drift, and weak
coverage of important concepts. In short, the choice of data often matters as much as the model
architecture itself.

Random sampling is simple, but it can be inefficient. If the data distribution is imbalanced,
redundant, or dominated by easy cases, random selection may waste compute on low-value examples
and underrepresent rare or difficult patterns. The same issue appears in monitoring and splitting:
random partitions can hide important edge cases, create misleading evaluation scores, and delay
or mask subtle performance degradation. When this happens, the system appears stable on average,
but still fails on the scenarios that matter most.

## Resources

The resources in this folder are intended to support both research and practical work,
from understanding the state of the art to turning ideas into experiments and product
improvements. In this folder you can find:

[📚 Bibliography](BIBLIOGRAPHY.md): relevant papers and surveys on data selection<br>
[💡 Ideas](IDEAS.md): research questions and open directions<br>
[👥 Researchers](RESEARCHERS.md): active researchers in this topic<br>
[🧰 Tools](TOOLS.md): tooling and libraries