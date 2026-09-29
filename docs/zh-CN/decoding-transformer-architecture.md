# 解析 Transformer 架构

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Decoding Transformer Architecture](https://outcomeschool.com/blog/decoding-transformer-architecture)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文拆解 Transformer 的嵌入、位置信息、注意力、前馈网络、残差和归一化，并介绍原始编码器—解码器的工作路径。

## 面试解析

讲解仅解码器 LLM 时，从 token ID 到隐藏状态、因果自注意力、FFN、词表投影和采样逐步说明；同时标明训练并行与自回归生成的差别。

## 常见误区与边界

原始 Transformer 的交叉注意力不一定出现在仅解码器模型里；位置编码和归一化实现也可能变化，不能把所有模型都画成同一张架构图。

## 面试追问

训练时能够并行处理整段文本，为什么生成时通常仍逐 token 进行？

## 相关阅读

- [注意力的数学原理：Q、K 和 V](math-behind-attention-qkv.md)
- [LLM 中的前馈网络](feed-forward-networks-in-llms.md)
- [注意力中的因果掩码](causal-masking-in-attention.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
