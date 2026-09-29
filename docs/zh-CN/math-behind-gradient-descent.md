# 梯度下降的数学原理

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Math Behind Gradient Descent](https://outcomeschool.com/blog/math-behind-gradient-descent)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍梯度下降依据损失梯度更新参数，并区分批量、随机和小批量更新，说明学习率对训练轨迹的影响。

## 面试解析

基本更新是 w ← w − η∇L(w)。梯度给出局部变化方向，学习率决定步长；特征尺度和损失曲率会影响稳定性，可结合学习曲线与梯度范数诊断训练。

## 常见误区与边界

非凸目标下不能保证找到全局最优。损失波动不一定意味着实现错误，也可能来自小批量噪声；应在受控小例子上检查梯度和更新符号。

## 面试追问

训练损失突然发散时，你会按什么顺序排查学习率、输入尺度和数值精度？

## 相关阅读

- [交叉熵损失的数学原理](math-behind-cross-entropy-loss.md)
- [机器学习中的正则化：L1 与 L2](regularization-in-machine-learning.md)
- [反向传播的数学原理](math-behind-backpropagation.md)
- [线性回归与逻辑回归](linear-regression-vs-logistic-regression.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
