# 线性回归与逻辑回归

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Linear Regression vs Logistic Regression](https://outcomeschool.com/blog/linear-regression-vs-logistic-regression)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文比较线性回归与逻辑回归：前者预测连续值，后者通过 sigmoid 表示二分类概率，并使用不同损失目标。

## 面试解析

线性回归常用平方误差，逻辑回归常用二元交叉熵。概率预测与最终决策是两步：阈值应根据类别比例和误判成本选择，不必固定为 0.5。

## 常见误区与边界

逻辑回归损失的凸性不意味着任何数据上都有有限的无正则最优参数；线性可分时参数可能持续增大。正则化和数值稳定实现仍然重要。

## 面试追问

如果业务要求减少漏报，应该调整训练目标、分类阈值，还是同时考虑二者？

## 相关阅读

- [交叉熵损失的数学原理](math-behind-cross-entropy-loss.md)
- [机器学习中的正则化：L1 与 L2](regularization-in-machine-learning.md)
- [精确率与召回率](precision-vs-recall.md)
- [梯度下降的数学原理](math-behind-gradient-descent.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
