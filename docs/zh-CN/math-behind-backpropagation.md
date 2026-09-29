# 反向传播的数学原理

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Math Behind Backpropagation](https://outcomeschool.com/blog/math-behind-backpropagation)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍反向传播利用链式法则复用中间梯度，从损失沿计算图反向求导，并与参数更新步骤区分。

## 面试解析

反向传播计算梯度，优化器根据梯度更新参数。共享参数出现在多条路径时，应累加各路径贡献；数值梯度检查可验证小规模实现。

## 常见误区与边界

梯度为零可能来自饱和激活、断开的计算图或初始化，不一定是学习率问题。自动微分也无法纠正错误的前向目标。

## 面试追问

为什么在多次小批量反向传播之间，是否清空梯度会改变训练行为？

## 相关阅读

- [RMSNorm（均方根层归一化）](rmsnorm-root-mean-square-layer-normalization.md)
- [交叉熵损失的数学原理](math-behind-cross-entropy-loss.md)
- [梯度下降的数学原理](math-behind-gradient-descent.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
