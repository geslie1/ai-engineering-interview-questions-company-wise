# 组相对策略优化（GRPO）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Group Relative Policy Optimization (GRPO)](https://outcomeschool.com/blog/group-relative-policy-optimization-grpo)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 GRPO 对同一问题采样多个答案，用组内奖励构造相对优势，减少对独立价值模型的依赖。

## 面试解析

组内归一化的直观形式是 A_i=(r_i−mean(r))/(std(r)+ε)。奖励可来自学习模型或可验证规则；没有价值网络不等于不需要奖励设计。

## 常见误区与边界

全部答案同分时，组内相对信号可能消失。还应关注验证器被钻空子、长答案偏置和采样成本；KL 等其他损失项可能仍有作用。

## 面试追问

为什么扩大组大小可能改善优势估计，却不一定提高单位算力收益？

## 相关阅读

- [基于人类反馈的强化学习（RLHF）](reinforcement-learning-from-human-feedback-rlhf.md)
- [近端策略优化（PPO）](proximal-policy-optimization-ppo.md)
- [大型推理模型（LRM）](large-reasoning-models.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
