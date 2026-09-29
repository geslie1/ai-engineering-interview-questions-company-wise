# 直接偏好优化（DPO）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Direct Preference Optimization (DPO)](https://outcomeschool.com/blog/direct-preference-optimization-dpo)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 DPO 直接使用同一提示下的偏好答案对训练策略，省去单独拟合奖励模型和在线 PPO 优化循环的常见步骤。

## 面试解析

理解目标中的两组差值：策略对优选与拒选答案的 log probability 差，再减去参考模型的对应差。训练推动相对偏好，而不是简单提高所有长答案概率。

## 常见误区与边界

DPO 仍依赖偏好数据覆盖和一致性。β 需要结合实现与数据调节，不能仅凭单个默认值判断偏离程度；离线数据不充分时还要考虑分布偏移。

## 面试追问

偏好对中“被拒绝答案”其实也正确，会怎样影响训练？

## 相关阅读

- [解析 InstructGPT](decoding-instructgpt.md)
- [基于人类反馈的强化学习（RLHF）](reinforcement-learning-from-human-feedback-rlhf.md)
- [近端策略优化（PPO）](proximal-policy-optimization-ppo.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
