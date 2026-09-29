# Transformer 中的编码器与解码器

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Encoder vs Decoder in Transformers](https://outcomeschool.com/blog/encoder-vs-decoder-in-transformers)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文比较编码器、解码器和编码器—解码器结构，重点涉及双向注意力、因果注意力与跨注意力。

## 面试解析

选择结构先看信息可见范围和输出方式。表示学习通常需要双向上下文；自回归生成限制未来可见性；序列到序列模型还可通过跨注意力读取输入表示。

## 常见误区与边界

“理解用编码器、生成用解码器”只是粗略经验。解码器也能分类，编码器可用于掩码预测；训练目标、掩码与使用方式共同决定能力。

## 面试追问

翻译模型中，自注意力掩码与跨注意力掩码分别应屏蔽哪些位置？

## 相关阅读

- [解析 Transformer 架构](decoding-transformer-architecture.md)
- [注意力中的因果掩码](causal-masking-in-attention.md)
- [Transformer 中的多头注意力](multi-head-attention-in-transformers.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
