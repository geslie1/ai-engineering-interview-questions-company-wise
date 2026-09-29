# 交叉熵损失的数学原理

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Math Behind Cross-Entropy Loss](https://outcomeschool.com/blog/math-behind-cross-entropy-loss)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文解释交叉熵通过预测分布为真实标签分配的概率衡量损失，并讨论与 softmax、梯度和困惑度的联系。

## 面试解析

对 one-hot 标签，损失为 −log p_y；softmax 交叉熵对 logits 的梯度为 p−y。固定目标分布时，交叉熵等于目标熵加 KL 散度。

## 常见误区与边界

准确率为 100% 不表示损失为零。语言模型困惑度通常是平均 token 负对数似然的指数，比较时必须保持分词和评估条件一致。

## 面试追问

两个分类器准确率相同，但置信度不同，交叉熵为什么会不同？

## 相关阅读

- [基于人类反馈的强化学习（RLHF）](reinforcement-learning-from-human-feedback-rlhf.md)
- [反向传播的数学原理](math-behind-backpropagation.md)
- [线性回归与逻辑回归](linear-regression-vs-logistic-regression.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
