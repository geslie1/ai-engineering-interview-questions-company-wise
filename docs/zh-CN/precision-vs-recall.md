# 精确率与召回率

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Precision vs Recall](https://outcomeschool.com/blog/precision-vs-recall)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文通过混淆矩阵说明精确率与召回率的区别，并讨论阈值、F1 分数以及不同误判成本下的指标选择。

## 面试解析

精确率为 TP/(TP+FP)，召回率为 TP/(TP+FN)。例如告警审核资源有限时，要同时报告误报负担与漏报损失，并在验证集上按业务成本选择阈值。

## 常见误区与边界

改变阈值通常带来取舍，但更好的模型可以同时改善两项指标。F1 不包含真负例；类别严重不平衡时，仅报告准确率容易掩盖问题。

## 面试追问

在召回率至少为 95% 的约束下，你会如何选择阈值并报告不确定性？

## 相关阅读

- [LLM 评估](llm-evaluation.md)
- [机器学习中的正则化：L1 与 L2](regularization-in-machine-learning.md)
- [线性回归与逻辑回归](linear-regression-vs-logistic-regression.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
