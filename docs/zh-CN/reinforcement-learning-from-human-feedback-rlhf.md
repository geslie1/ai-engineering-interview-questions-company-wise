# 基于人类反馈的强化学习（RLHF）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Reinforcement Learning from Human Feedback (RLHF)](https://outcomeschool.com/blog/reinforcement-learning-from-human-feedback-rlhf)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍常见的 RLHF 流程及策略、价值、奖励和参考模型的职责，并强调奖励投机、偏好数据质量和优化稳定性。

## 面试解析

讲解 PPO 式 RLHF 时，分别说明奖励从哪里来、优势如何估计、策略如何更新、KL 如何约束。SFT 是常见初始化环节，不应把某一种完整配方当作 RLHF 的唯一定义。

## 常见误区与边界

奖励模型是近似评价器，优化它可能放大偏差。需要保留独立人工评估和对抗样本，检查迎合、冗长、过度拒绝等行为。

## 面试追问

训练奖励一直上涨但人工偏好下降，你会先检查哪三项？

## 相关阅读

- [解析 InstructGPT](decoding-instructgpt.md)
- [近端策略优化（PPO）](proximal-policy-optimization-ppo.md)
- [直接偏好优化（DPO）](direct-preference-optimization-dpo.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
