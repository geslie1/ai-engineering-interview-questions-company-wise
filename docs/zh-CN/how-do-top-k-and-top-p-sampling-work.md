# top-k 和 top-p 采样如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How do Top-k and Top-p Sampling work?](https://outcomeschool.com/blog/how-do-top-k-and-top-p-sampling-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文区分固定候选数量的 top-k 与固定累计概率阈值的 top-p，两者都先筛选候选 token，再按重新归一化的概率采样。

## 面试解析

top-p 要保留使累计概率首次达到阈值的边界 token。实现时先确定温度与过滤器的应用顺序，再测试极尖锐分布、均匀分布和只有一个有效候选的情况。

## 常见误区与边界

不同服务的组合顺序与默认值可能不同；top-k=1 近似贪心，top-p=1 仅表示该过滤器不裁剪，不能忽略温度和其他约束。

## 面试追问

如何写一个测试，发现 top-p 实现误删了跨越阈值的 token？

## 相关阅读

- [温度如何控制 LLM 输出？](how-does-temperature-control-llm-output.md)
- [LLM 评估](llm-evaluation.md)
- [token 流式传输如何工作？](how-does-token-streaming-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
