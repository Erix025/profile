---
title: "PSA: Pyramid Sparse Attention for Efficient Video Understanding and Generation"
date: 2025-12-03
pubtype: "Preprint"
featured: true
description: "PSA introduce an efficient attention mechanism to accelerate video understanding and generation. It leverages a multi-level sparse attention strategy, enabling the model to effectively mitigates information loss while preserving computational efficiency under a low compute budget."
authors: ["Xiaolong Li*", "Youping Gu*", "Xi Lin*", "Weijie Wang", "Bohan Zhuang"]
tags: ["Computer Vision", "Deep Learning", "Attention Mechanisms"]
image: "/img/publications/PSA_workflow.png"
link: "https://arxiv.org/abs/2512.04025"
venue: "Preprint"
weight: 300
sitemap:
  priority: 0.8
---

Abstract:
Attention mechanisms are the core of foundation models, but their quadratic complexity remains a critical bottleneck for scaling. This challenge has driven the development of efficient attention mechanisms, with sparsity emerging as the dominant paradigm. Current methods typically retain or discard entire key-value blocks with binary masks, resulting in substantial information loss under high sparsity. To mitigate this gap, we present Pyramid Sparse Attention (PSA), a versatile module applicable to both video understanding and generation tasks. Instead of binary masking, PSA introduces multi-level pooled KV representations, enabling finer mask granularity. Specifically, each query block dynamically allocates lower pooling levels to critical KV blocks and higher levels to less important ones, creating an informative interpolation between full retention and complete pruning. This design, analogous to fixed-point quantization and classical feature pyramid networks in computer vision, effectively mitigates information loss while preserving computational efficiency under a low compute budget. It works with a native, hardware-friendly kernel that leverages decoupled block-tile design to ensure efficient execution. Across video understanding and generation benchmarks, PSA preserves contextual information and visual fidelity, consistently outperforming or achieving comparable performance over existing sparse attention baselines with superior efficiency-quality trade-offs. Our code and model weights are publicly available at: [PSA](https://ziplab.co/PSA).
