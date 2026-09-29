# 前缀微调如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Prefix Tuning work?](https://outcomeschool.com/blog/how-does-prefix-tuning-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍前缀微调：冻结模型，训练参与各层注意力计算的连续前缀表示，并将其与输入层的提示微调区分。

## 面试解析

前缀是可学习向量，不是人工编写的自然语言。比较 PEFT 方法时，可从注入位置、可训练参数、额外上下文计算和多任务切换成本入手。

## 常见误区与边界

前缀参数少不意味着推理完全没有额外开销。它和提示词缓存只是中文名称接近，一个是训练适配方法，一个是推理复用技术。

## 面试追问

为什么输入层 prompt tuning 与各层 prefix tuning 的参数量和作用不同？

## 相关阅读

- [提示词缓存如何工作？](how-does-prompt-caching-work.md)
- [LoRA：LLM 的低秩适配](lora-low-rank-adaptation-of-llms.md)
- [微调如何工作？](how-does-fine-tuning-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
