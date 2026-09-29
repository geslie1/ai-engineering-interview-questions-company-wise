# 注意力中 √dₖ 缩放因子的数学原理

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Math behind √dₖ Scaling Factor in Attention](https://outcomeschool.com/blog/scaling-dot-product-attention)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文从点积方差解释注意力缩放：维度增大时，未缩放的分数更容易让 softmax 过度集中，除以维度平方根有助于稳定数值范围。

## 面试解析

在分量独立、均值为 0、方差为 1 的假设下，Var(q·k)=d_k，因此除以 √d_k 后方差为 1。回答时先说明假设，再写 softmax(QKᵀ/√d_k)V。

## 常见误区与边界

缩放不改变分数排序，也不改变注意力的二次复杂度；不要将“理论方差为 1”说成所有训练中张量都满足的事实。

## 面试追问

如果 Q、K 的分量相关或方差不是 1，推导中哪一步需要修改？

## 相关阅读

- [注意力的数学原理：Q、K 和 V](math-behind-attention-qkv.md)
- [解析 LLM 中的 FlashAttention](decoding-flash-attention.md)
- [Transformer 中的多头注意力](multi-head-attention-in-transformers.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
