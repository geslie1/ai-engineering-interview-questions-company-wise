# 解析视觉 Transformer（ViT）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Decoding Vision Transformer (ViT)](https://outcomeschool.com/blog/decoding-vision-transformer-vit)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 ViT 将图像切成 patch，投影为 token，加入位置信息后交给 Transformer 编码器；分类可利用聚合表示。

## 面试解析

对 H×W 图像、边长 P 的 patch，整除时 token 数为 (H/P)(W/P)。减小 patch 或提高分辨率会增加 token 数，标准全注意力的交互开销增长更快。

## 常见误区与边界

CLS token 是常见设计而非所有视觉 Transformer 的必需组件。高分辨率细节、数据量和预训练方式都会影响与 CNN 的比较。

## 面试追问

图像边长翻倍且 patch 不变时，token 数和全注意力矩阵大小各增长多少？

## 相关阅读

- [解析 LLM 中的 FlashAttention](decoding-flash-attention.md)
- [多模态 AI](multimodal-ai.md)
- [图像嵌入如何工作？](how-do-image-embeddings-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
