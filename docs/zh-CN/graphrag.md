# GraphRAG

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[GraphRAG](https://outcomeschool.com/blog/graphrag)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 GraphRAG 利用实体、关系和图结构补充检索，并讨论局部查询、全局归纳以及建图与更新成本。

## 面试解析

适合多跳关系问题时，可把图中的关系路径与原始证据片段一起返回。每条关系应保留出处、时间和置信信息，更新文档时也要处理旧关系和相关摘要。

## 常见误区与边界

图结构不会自动消除抽取错误或幻觉。GraphRAG 是一类方法，具体实现不都具有相同社区摘要机制；简单事实查询可能无需付出建图成本。

## 面试追问

当两份文档对同一组织关系给出不同时间的描述时，图应怎样表示并检索？

## 相关阅读

- [RAG 分块策略](chunking-strategies-for-rag.md)
- [智能体式 RAG](agentic-rag.md)
- [向量数据库如何工作？](how-does-a-vector-database-work.md)
- [语义搜索如何工作？](how-does-semantic-search-work.md)
- [上下文工程](context-engineering.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
