# Transformer 中的多头注意力

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Multi-Head Attention in Transformers](https://outcomeschool.com/blog/multi-head-attention-in-transformers)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍多组 Q、K、V 投影并行计算注意力，再拼接并投影输出，使模型能在不同表示子空间中组合信息。

## 面试解析

实现可按批次、头数、长度、头维度组织张量。明确 reshape 与 transpose 的区别，以及最后如何回到模型维度，能避免只会背公式。

## 常见误区与边界

不同头的关注模式由训练学习，不能预设每个头都有固定语言学职责。固定总维度时增加头数也不等同于同比增加表达能力。

## 面试追问

多头结果拼接后，输出投影 W_O 起什么作用？

## 相关阅读

- [注意力的数学原理：Q、K 和 V](math-behind-attention-qkv.md)
- [分组查询注意力](grouped-query-attention.md)
- [Transformer 中的自注意力](self-attention-in-transformers.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
