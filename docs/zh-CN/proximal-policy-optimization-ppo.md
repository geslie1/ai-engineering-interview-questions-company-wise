# 近端策略优化（PPO）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Proximal Policy Optimization (PPO)](https://outcomeschool.com/blog/proximal-policy-optimization-ppo)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 PPO 用新旧策略概率比和裁剪目标控制更新幅度，并说明它在奖励反馈训练中的作用及与 KL 约束的区别。

## 面试解析

常见裁剪目标为 min(rA, clip(r,1−ε,1+ε)A)，r 是新旧策略概率比，A 是优势。解释时要分别讨论正、负优势下何种更新会被限制。

## 常见误区与边界

裁剪不是对所有参数变化的硬限制，也不保证训练永远稳定。RLHF 中相对参考模型的 KL 项与相对采样策略的 PPO 裁剪承担不同职责。

## 面试追问

为什么需要记录生成样本时旧策略的 log probability？

## 相关阅读

- [基于人类反馈的强化学习（RLHF）](reinforcement-learning-from-human-feedback-rlhf.md)
- [直接偏好优化（DPO）](direct-preference-optimization-dpo.md)
- [组相对策略优化（GRPO）](group-relative-policy-optimization-grpo.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
