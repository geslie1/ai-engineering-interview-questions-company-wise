# 混合专家模型详解

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍稀疏 MoE：路由器为每个 token 选择少数专家，扩大总参数容量，同时限制每次前向的激活计算量。

## 面试解析

区分总参数、激活参数与系统开销：总参数影响权重存储，激活参数影响计算，而跨设备路由带来通信和负载均衡问题。容量更大不等于单机显存需求更小。

## 常见误区与边界

不能假设每个专家天然对应某个学科。评估路由要检查专家负载、溢出处理和 all-to-all 通信，不能只看理论 FLOPs。

## 面试追问

为什么一个稀疏模型的单 token 计算较少，实际延迟仍可能更高？

## 相关阅读

- [KV 缓存压缩](kv-cache-compression.md)
- [组相对策略优化（GRPO）](group-relative-policy-optimization-grpo.md)
- [DeepSeek-V4 架构详解](decoding-deepseek-v4.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
