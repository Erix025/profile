---
title: "FlashQLA: Flash Qwen Linear Attention"
date: 2026-04-29
link: "https://github.com/QwenLM/FlashQLA"
image: "https://qianwen-res.oss-cn-beijing.aliyuncs.com/flashqla/flashqla.png"
description: "A high-performance linear attention kernel library for Qwen, built on TileLang. FlashQLA optimizes GDN Chunked Prefill with fused kernels, gate-driven context parallelism, and hardware-friendly reformulation."
tags:
  - LLM Inference
  - Linear Attention
  - GPU Kernels
  - TileLang
  - Qwen
featured: true
weight: 10
sitemap:
  priority: 0.8
---

FlashQLA is an open-source Qwen Infra project I worked on during my research internship at Alibaba Cloud. It provides high-performance linear attention kernels for Qwen, with a focus on GDN Chunked Prefill.

The public release describes FlashQLA as a TileLang-based kernel library that applies operator fusion and performance optimization to both forward and backward passes. Compared with the FLA Triton kernel, the README reports 2-3x forward speedup and 2x backward speedup across multiple scenarios on NVIDIA Hopper and Blackwell GPUs.

Key ideas include gate-driven intra-card context parallelism, hardware-friendly algebraic reformulation, and TileLang fused warp-specialized kernels. My work focused on efficient inference infrastructure for Qwen, including GPU-kernel-oriented optimization and benchmarking for linear attention workloads.

See the [GitHub repository](https://github.com/QwenLM/FlashQLA) and [Qwen blog post](https://qwen.ai/blog?id=flashqla) for more details.

![FlashQLA overview](https://qianwen-res.oss-cn-beijing.aliyuncs.com/flashqla/flashqla.png)
