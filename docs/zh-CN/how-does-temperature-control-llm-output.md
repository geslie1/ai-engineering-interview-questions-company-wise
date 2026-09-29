# 温度如何控制 LLM 输出？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Temperature control LLM output?](https://outcomeschool.com/blog/how-does-temperature-control-llm-output)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文解释温度通过缩放 logits 改变采样分布的集中程度：较低温度更集中，较高温度更分散，但不会增加模型知识。

## 面试解析

对 T>0 使用 p_i=softmax(z_i/T)。改变温度通常不改变 logits 排序，却会改变低概率 token 的采样机会；T=0 通常由服务实现为贪心选择，而非直接除以零。

## 常见误区与边界

低温度不保证事实正确，也不保证跨硬件、批处理及服务版本逐字一致。调参应结合任务成功率和输出多样性，而非把随机性等同于质量。

## 面试追问

保持 top-p 不变时降低温度，会怎样影响实际候选集？

## 相关阅读

- [top-k 和 top-p 采样如何工作？](how-do-top-k-and-top-p-sampling-work.md)
- [LLM 评估](llm-evaluation.md)
- [使用 LLM 作为裁判](llm-as-a-judge.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
