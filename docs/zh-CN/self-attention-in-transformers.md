# Transformer 中的自注意力

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Self Attention in Transformers](https://outcomeschool.com/blog/self-attention-in-transformers)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍自注意力从同一序列生成 Q、K、V，根据相关性加权聚合各位置的信息，并与交叉注意力作区分。

## 面试解析

同源输入不代表 Q、K、V 完全相同，它们使用不同投影。全自注意力的训练可并行，但因果生成仍有序列依赖，缓存改变的是重复计算方式。

## 常见误区与边界

是否能看所有位置取决于掩码和架构。注意力权重也不自动构成忠实的解释，不能仅凭热力图证明模型采用了某条因果依据。

## 面试追问

把图像特征作为 K、V，而文本作为 Q，这属于哪种注意力？

## 相关阅读

- [注意力的数学原理：Q、K 和 V](math-behind-attention-qkv.md)
- [注意力中的因果掩码](causal-masking-in-attention.md)
- [Transformer 中的多头注意力](multi-head-attention-in-transformers.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
