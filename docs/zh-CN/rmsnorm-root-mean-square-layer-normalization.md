# RMSNorm（均方根层归一化）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[RMSNorm (Root Mean Square Layer Normalization)](https://outcomeschool.com/blog/rmsnorm-root-mean-square-layer-normalization)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 RMSNorm 用均方根缩放向量，省去 LayerNorm 的减均值步骤，并说明其在现代 Transformer 中的应用。

## 面试解析

常见形式为 y=γ⊙x/√(mean(x²)+ε)。与 LayerNorm 比较时，说明统计维度、是否中心化、可学习缩放和数值稳定项，而不只说“更快”。

## 常见误区与边界

RMSNorm 与 Pre-Norm 分别是归一化方式和放置位置，两者不是同一概念。低精度实现要关注平方与累加的精度。

## 面试追问

当向量所有分量都接近零时，ε 会发挥什么作用？

## 相关阅读

- [LLM 中的前馈网络](feed-forward-networks-in-llms.md)
- [解析 Transformer 架构](decoding-transformer-architecture.md)
- [反向传播的数学原理](math-behind-backpropagation.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
