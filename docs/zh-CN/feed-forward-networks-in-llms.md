# LLM 中的前馈网络

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Feed-Forward Networks in LLMs](https://outcomeschool.com/blog/feed-forward-networks-in-llms)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文把 FFN 描述为逐 token 的非线性特征变换，与负责跨 token 信息交互的注意力互补，并介绍扩维再降维的结构。

## 面试解析

普通 FFN 可写为 W₂σ(W₁x)。门控版本另有一条投影分支并逐元素相乘；比较 SwiGLU 与普通 FFN 时，应在相近参数或计算预算下讨论。

## 常见误区与边界

同层 FFN 通常对位置共享权重，但各 token 的输入不同。不能把注意力完全称为“关系库”、FFN 完全称为“事实库”，两者作用并非如此严格分离。

## 面试追问

移除激活函数后，两层线性映射的表达能力发生什么变化？

## 相关阅读

- [混合专家模型详解](mixture-of-experts.md)
- [RMSNorm（均方根层归一化）](rmsnorm-root-mean-square-layer-normalization.md)
- [解析 Transformer 架构](decoding-transformer-architecture.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
