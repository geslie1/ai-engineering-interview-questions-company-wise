# 机器学习中的正则化：L1 与 L2

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Regularization in Machine Learning: L1 vs L2](https://outcomeschool.com/blog/regularization-in-machine-learning)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 L1 与 L2 通过对权重增加不同形式的惩罚来抑制过拟合，并指出正则强度控制拟合与约束之间的取舍。

## 面试解析

L1 使用绝对值和，常产生稀疏解；L2 使用平方和，倾向于平滑收缩。特征量纲影响惩罚效果，因此通常需要在训练数据上拟合缩放方式。

## 常见误区与边界

正则化不替代验证集，也不自动解决数据泄漏。选择强度应使用验证或交叉验证，且注意偏置项是否被纳入惩罚。

## 面试追问

高度相关的两个特征，在 L1 与 L2 下可能呈现怎样不同的系数行为？

## 相关阅读

- [精确率与召回率](precision-vs-recall.md)
- [梯度下降的数学原理](math-behind-gradient-descent.md)
- [机器学习中的特征工程](feature-engineering.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
