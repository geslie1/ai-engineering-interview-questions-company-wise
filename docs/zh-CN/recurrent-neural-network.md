# 循环神经网络（RNN）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Recurrent Neural Network (RNN)](https://outcomeschool.com/blog/recurrent-neural-network)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍循环神经网络通过隐藏状态沿序列传递信息，解释其时序建模用途以及长距离依赖中的梯度困难。

## 面试解析

RNN 在时间步之间共享参数，处理当前输入并更新状态。训练常通过时间反向传播计算梯度；截断可降低内存和计算开销，但限制直接学习的依赖跨度。

## 常见误区与边界

LSTM 和 GRU 有助于缓解梯度问题，并不保证无限记忆。固定大小状态也可能压缩掉细节，模型选择仍应结合任务所需历史与实时约束。

## 面试追问

持续到来的传感器流是否适合 RNN？你会如何设置状态重置和训练窗口？

## 相关阅读

- [反向传播的数学原理](math-behind-backpropagation.md)
- [梯度下降的数学原理](math-behind-gradient-descent.md)
- [RNN 与 Transformer 有何区别？](how-do-rnns-and-transformers-differ.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
