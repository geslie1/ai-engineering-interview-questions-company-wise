# 向量数据库如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does a Vector Database work?](https://outcomeschool.com/blog/how-does-a-vector-database-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍向量、元数据和相似度查询，以及 HNSW、IVF、PQ 等索引或压缩方法，说明向量存储如何支撑检索。

## 面试解析

生产设计除相似度算法外，还要涵盖增量写入、删除、版本、权限过滤、备份和嵌入模型迁移。归一化后内积与余弦的关系可用于检查度量是否匹配。

## 常见误区与边界

向量数据库不自动解决内容权限与证据真实性。关系数据库也可通过扩展提供向量检索，应根据一致性、规模和运维需求选型。

## 面试追问

更换嵌入模型后，旧向量和新向量为什么通常不能直接混用？

## 相关阅读

- [RAG 分块策略](chunking-strategies-for-rag.md)
- [近似最近邻（ANN）搜索如何工作？](how-does-approximate-nearest-neighbor-ann-search-work.md)
- [语义搜索如何工作？](how-does-semantic-search-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
