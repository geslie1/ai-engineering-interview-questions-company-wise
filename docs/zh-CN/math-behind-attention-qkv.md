# 注意力的数学原理：Q、K 和 V

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Math behind Attention - Q, K, and V](https://outcomeschool.com/blog/math-behind-attention-qkv)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文按线性投影、匹配打分、缩放、softmax 和加权求和的顺序解释 Q、K、V。注意力输出融合上下文，而不是简单复制得分最高的词。

## 面试解析

令 X 的形状为 n×d_model，Q、K 为 n×d_k，V 为 n×d_v；QKᵀ 得到 n×n 权重矩阵，乘 V 后得到 n×d_v。三组投影权重通过训练学习。

## 常见误区与边界

softmax 沿被关注的 token 维度归一化。加入因果或 padding 掩码时，要在 softmax 前屏蔽无效位置，并处理全屏蔽行。

## 面试追问

为什么 Q 与 K 必须有相同的末维，而 V 的末维可以不同？

## 相关阅读

- [注意力中 √dₖ 缩放因子的数学原理](scaling-dot-product-attention.md)
- [注意力中的因果掩码](causal-masking-in-attention.md)
- [Transformer 中的多头注意力](multi-head-attention-in-transformers.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
