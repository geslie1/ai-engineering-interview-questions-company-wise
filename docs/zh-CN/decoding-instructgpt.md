# 解析 InstructGPT

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Decoding InstructGPT](https://outcomeschool.com/blog/decoding-instructgpt)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文回顾 InstructGPT 通过示范数据微调、偏好奖励建模和强化学习改进指令遵循，并讨论对齐收益与通用能力之间的取舍。

## 面试解析

回答时把目标与训练信号对应起来：SFT 学习示范，奖励模型拟合相对偏好，策略优化提高偏好得分。KL 约束用于控制策略偏离参考模型的程度。

## 常见误区与边界

参数规模、语言建模损失与用户偏好不是同一指标。偏好改善也不意味着所有任务或所有人群都同步获益，应保留独立能力和安全评估。

## 面试追问

为什么训练偏好奖励模型通常使用答案比较，而非只标注单个答案分数？

## 相关阅读

- [基于人类反馈的强化学习（RLHF）](reinforcement-learning-from-human-feedback-rlhf.md)
- [近端策略优化（PPO）](proximal-policy-optimization-ppo.md)
- [直接偏好优化（DPO）](direct-preference-optimization-dpo.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
