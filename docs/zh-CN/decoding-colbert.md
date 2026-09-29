# ColBERT：后期交互检索详解

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[ColBERT - Late Interaction Retrieval Explained](https://outcomeschool.com/blog/decoding-colbert)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 ColBERT 对查询和文档分别生成 token 级表示，通过后期交互打分，兼顾离线索引与细粒度匹配。

## 面试解析

典型 MaxSim 对每个查询向量寻找最相似的文档向量，再把这些最大相似度求和。文档表示可预计算，但多向量存储和查询运算比单向量检索更重。

## 常见误区与边界

后期交互不等于把整个查询与文档一起送入交叉编码器。效果、索引体积和延迟应在同一候选集与硬件条件下比较，不能直接套用文章的历史基准。

## 面试追问

若检索库规模扩大十倍，你会从压缩、候选裁剪和重排预算哪些方面优化？

## 相关阅读

- [混合搜索如何工作？](how-does-hybrid-search-work.md)
- [重排序器如何工作？](how-does-a-reranker-work.md)
- [近似最近邻（ANN）搜索如何工作？](how-does-approximate-nearest-neighbor-ann-search-work.md)
- [向量数据库如何工作？](how-does-a-vector-database-work.md)
- [什么是对比学习？](contrastive-learning.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
