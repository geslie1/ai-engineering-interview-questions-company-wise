# 机器学习中的特征工程

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Feature Engineering in Machine Learning](https://outcomeschool.com/blog/feature-engineering)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍特征工程如何利用领域知识构造、变换和选择输入特征，并通过例子说明它对模型表现的影响。

## 面试解析

先确保特征在预测时真实可用，再讨论表达能力。标准化、缺失值填充和类别编码应只在训练数据上拟合；时间序列特征需要遵守事件发生时的信息边界。

## 常见误区与边界

看似极强的特征可能泄露结果。除了离线指标，还要检查训练与线上计算是否一致、分布是否漂移，以及缺失模式是否改变。

## 面试追问

某个特征加入后离线分数大幅上升、上线却失效，你会如何定位泄漏或时间错位？

## 相关阅读

- [LLM 评估](llm-evaluation.md)
- [机器学习中的正则化：L1 与 L2](regularization-in-machine-learning.md)
- [精确率与召回率](precision-vs-recall.md)
- [线性回归与逻辑回归](linear-regression-vs-logistic-regression.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
