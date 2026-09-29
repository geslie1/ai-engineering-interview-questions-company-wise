# 混合搜索如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Hybrid Search work?](https://outcomeschool.com/blog/how-does-hybrid-search-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍联合关键词与语义检索，并通过排名融合或分数归一化后的加权组合形成候选列表。

## 面试解析

关键词检索适合精确标识与术语，向量检索有助于匹配语义改写。RRF 按排名而非原始分数融合，可写为各路 1/(c+rank) 的求和。

## 常见误区与边界

不同检索器的分数通常不可直接相加。混合检索也不保证所有任务都变好，应分别检查精确查询、语义查询和权限过滤后的召回。

## 面试追问

产品型号与自然语言描述混在一个问题里，如何判断哪一路检索贡献了收益？

## 相关阅读

- [重排序器如何工作？](how-does-a-reranker-work.md)
- [近似最近邻（ANN）搜索如何工作？](how-does-approximate-nearest-neighbor-ann-search-work.md)
- [语义搜索如何工作？](how-does-semantic-search-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
