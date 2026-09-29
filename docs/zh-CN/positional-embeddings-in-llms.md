# LLM 中的位置嵌入

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Positional Embeddings in LLMs](https://outcomeschool.substack.com/p/positional-embeddings-in-llms)
- 来源平台：outcomeschool.substack.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文说明，仅凭词向量不足以表达顺序，需要额外的位置表示，让 Transformer 区分相同词语的不同排列。

## 面试解析

面试中可先说明不含位置信息的自注意力对输入置换具有相应的等变性质，再区分添加绝对位置向量与在注意力计算中引入相对位置的做法。

## 常见误区与边界

“位置嵌入加到输入上”是常见方案之一，不代表所有现代 LLM 都这样实现。RoPE 等方法作用于 Q、K，不能与加法式位置嵌入混为一谈。

## 面试追问

位置编码存在，是否就能保证训练长度之外的效果？

## 相关阅读

- [RoPE（旋转位置嵌入）的数学原理](math-behind-rope-rotary-position-embedding.md)
- [解析 Transformer 架构](decoding-transformer-architecture.md)
- [LLM 中的上下文窗口](post-context-window.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
