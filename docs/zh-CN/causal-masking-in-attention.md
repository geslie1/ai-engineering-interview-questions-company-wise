# 注意力中的因果掩码

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Causal Masking in Attention](https://outcomeschool.com/blog/causal-masking-in-attention)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文说明因果掩码阻止当前位置读取未来 token，使并行训练时的可见信息与自回归生成约束一致。

## 面试解析

对位置 i 的隐藏状态，通常允许关注位置 j≤i；训练标签向后移一位，用该状态预测下一个 token。掩码在 softmax 前屏蔽非法位置。

## 常见误区与边界

把分数乘以零不等于消除 softmax 概率。实现时还要结合 padding、缓存位置和分块计算，检查边界与全屏蔽行。

## 面试追问

加入 KV 缓存后，只有一个查询 token 时为什么仍需处理正确的位置偏移？

## 相关阅读

- [注意力的数学原理：Q、K 和 V](math-behind-attention-qkv.md)
- [什么是 LLM 中的 KV 缓存？](kv-cache-in-llms.md)
- [Transformer 中的自注意力](self-attention-in-transformers.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
