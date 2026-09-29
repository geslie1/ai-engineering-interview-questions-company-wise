# LLM 的“中间信息丢失”问题

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[The Lost in the Middle Problem in LLMs](https://outcomeschool.com/blog/lost-in-the-middle-problem-in-llms)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文讨论长上下文中信息位置影响任务表现的问题：能接收很多 token，不代表能同样可靠地利用各个位置的证据。

## 面试解析

设计位置敏感评测：保持问题和事实不变，移动证据位置，分别测首部、中部、尾部的准确率；再改变干扰材料数量，区分位置效应与总长度效应。

## 常见误区与边界

优化可从减少无关片段、重排序和明确证据引用入手。不要将所有遗忘归因于同一种机制，也不要仅扩大窗口而不测效果。

## 面试追问

如何证明一次 RAG 改进修复了中间信息利用问题，而不是碰巧换了更容易的样本？

## 相关阅读

- [RAG 分块策略](chunking-strategies-for-rag.md)
- [重排序器如何工作？](how-does-a-reranker-work.md)
- [上下文工程](context-engineering.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
