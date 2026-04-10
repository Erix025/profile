---
title: "TriAttention: Efficient Long Reasoning with Trigonometric KV Compression"
date: 2026-04-07
pubtype: "Preprint"
featured: true
description: "TriAttention proposes a novel KV cache compression approach for long reasoning in LLMs. It leverages trigonometric series based on fixed centers in pre-RoPE space to score key importance, achieving 2.5x higher throughput or 10.7x KV memory reduction while matching Full Attention reasoning accuracy."
authors: ["Weian Mao", "Xi Lin", "Wei Huang", "Yuxin Xie", "Tianfu Fu", "Bohan Zhuang", "Song Han", "Yukang Chen"]
tags: ["Large Language Models", "KV Cache Compression", "Efficient Inference"]
image: "/img/publications/TriAttention.png"
link: "https://arxiv.org/abs/2604.04921"
arxiv: "https://arxiv.org/abs/2604.04921"
github: "https://github.com/WeianMao/triattention"
project_page: "https://weianmao.github.io/tri-attention-project-page/"
venue: "Preprint"
weight: 200
sitemap:
  priority: 0.8
---

Abstract:
Extended reasoning in large language models (LLMs) creates severe KV cache memory bottlenecks. Leading KV cache compression methods estimate KV importance using attention scores from recent post-RoPE queries. However, queries rotate with position during RoPE, making representative queries very few, leading to poor top-key selection and unstable reasoning. To avoid this issue, we turn to the pre-RoPE space, where we observe that Q and K vectors are highly concentrated around fixed non-zero centers and remain stable across positions -- Q/K concentration. We show that this concentration causes queries to preferentially attend to keys at specific distances (e.g., nearest keys), with the centers determining which distances are preferred via a trigonometric series. Based on this, we propose TriAttention to estimate key importance by leveraging these centers. Via the trigonometric series, we use the distance preference characterized by these centers to score keys according to their positions, and also leverage Q/K norms as an additional signal for importance estimation. On AIME25 with 32K-token generation, TriAttention matches Full Attention reasoning accuracy while achieving 2.5x higher throughput or 10.7x KV memory reduction, whereas leading baselines achieve only about half the accuracy at the same efficiency. TriAttention enables OpenClaw deployment on a single consumer GPU, where long context would otherwise cause out-of-memory with Full Attention.
