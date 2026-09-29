# 什么是对比学习？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[What is Contrastive Learning?](https://outcomeschool.com/blog/contrastive-learning)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍对比学习通过拉近相关样本表示、区分不相关样本来学习嵌入，并讨论正负样本构造与常见应用。

## 面试解析

先定义“相似”对下游任务意味着什么，再设计数据增强和样本配对。检索任务可用查询与相关文档配对，难负例能够提高区分力，但需要检查其是否其实相关。

## 常见误区与边界

对比学习既可以自监督，也可以使用人工标签。错误的增强或假负例会破坏语义；不能仅凭训练损失下降就断定检索质量提高。

## 面试追问

同一问题存在多篇正确答案时，如何避免批内负例把正确文档推远？

## 相关阅读

- [混合搜索如何工作？](how-does-hybrid-search-work.md)
- [重排序器如何工作？](how-does-a-reranker-work.md)
- [图像嵌入如何工作？](how-do-image-embeddings-work.md)
- [语义搜索如何工作？](how-does-semantic-search-work.md)
- [ColBERT：后期交互检索详解](decoding-colbert.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
