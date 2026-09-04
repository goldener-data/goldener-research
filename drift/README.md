# Drift - Introduction

> This folder tracks the methods and questions related to detecting distribution shifts and model drift.

## At a glance
[📚 Bibliography](BIBLIOGRAPHY.md)<br>
[💡 Ideas](IDEAS.md)<br>
[👥 Researchers](RESEARCHERS.md)<br>
[🧰 Tools](TOOLS.md)

## Context

Data drift is one of the main reasons AI systems lose performance after deployment. It happens
when the distribution of incoming data changes over time, for example because new user
behaviors, environmental conditions, acquisition pipelines, or market shifts alter the
statistical properties of the features. In this situation, the model is still operating on
real data, but the data no longer resembles the distribution it was trained on.

The bad impact of data drift is often silent but costly: prediction quality drops, false
positives or false negatives increase, and the system may appear stable in aggregate metrics
while failing on the scenarios that matter most. In monitoring pipelines, drift can also hide
important changes in subpopulations or long-tail segments, leading to unfair, brittle, or
misleading decisions.

This is why drift monitoring is essential in real AI pipelines. By tracking the evolution of
input distributions and comparing them to reference data, it becomes possible to detect early
signals of degradation before they become severe.

## Resources

The resources in this folder are intended to support both research and practical work,
from understanding the state of the art to turning ideas into experiments and product
improvements. In this folder you can find:

[📚 Bibliography](BIBLIOGRAPHY.md): core papers and surveys on drift<br>
[💡 Ideas](IDEAS.md): open research questions and directions<br>
[👥 Researchers](RESEARCHERS.md): contributors and authors in the drift literature<br>
[🧰 Tools](TOOLS.md): libraries and frameworks
