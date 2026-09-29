# LLM 中的连续批处理

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Continuous Batching in LLMs](https://outcomeschool.com/blog/continuous-batching-in-llms)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍按迭代动态接纳与移除请求的连续批处理，使短请求结束后空出的容量不必等待整批长请求完成。

## 面试解析

调度器需要管理等待队列、运行集合、每步 token 预算和 KV 容量。把“完成后立即补位”理解为调度边界上的决策，而不是任意时刻改动正在执行的 GPU 内核。

## 常见误区与边界

吞吐量最大不等于每位用户延迟最好。长预填充可能阻塞解码，应结合分块预填充、公平性和拥塞控制评估尾延迟。

## 面试追问

新请求很多时，怎样避免已有长对话长期抢不到计算资源？

## 相关阅读

- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [LLM 中的分页注意力](paged-attention-in-llms.md)
- [vLLM 如何工作？](how-does-vllm-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
