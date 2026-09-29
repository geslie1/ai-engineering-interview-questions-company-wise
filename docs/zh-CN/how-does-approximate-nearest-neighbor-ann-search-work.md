# 近似最近邻（ANN）搜索如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Approximate Nearest Neighbor (ANN) search work?](https://outcomeschool.com/blog/how-does-approximate-nearest-neighbor-ann-search-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文比较多种 ANN 路线，包括分区、哈希、倒排聚类和近邻图，用部分召回损失换取更低搜索成本。

## 面试解析

建立精确搜索基线，再测 recall@k、延迟、内存和构建成本。HNSW 的搜索宽度、IVF 的探测簇数都应通过代表性查询调优。

## 常见误区与边界

ANN 的 recall@k 衡量对精确近邻的恢复程度，不等同于业务相关性。过滤条件、数据分布变化和更新频率都会影响最终效果。

## 面试追问

向量数量增加十倍时，你怎样判断应该调参数、分片还是换索引？

## 相关阅读

- [混合搜索如何工作？](how-does-hybrid-search-work.md)
- [向量数据库如何工作？](how-does-a-vector-database-work.md)
- [语义搜索如何工作？](how-does-semantic-search-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
