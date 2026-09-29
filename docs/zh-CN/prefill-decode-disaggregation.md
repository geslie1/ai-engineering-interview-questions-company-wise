# LLM 推理中的预填充与解码分离

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Prefill-Decode Disaggregation in LLM Inference](https://outcomeschool.com/blog/prefill-decode-disaggregation)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文说明把预填充与解码放在不同工作池，能够分别扩容并减少阶段间干扰，但需要跨设备传输 KV 缓存。

## 面试解析

先估算每请求的 KV 传输量，再用带宽与额外排队计算交接延迟。比较分离部署与同机分块预填充，在真实长短输入混合流量下验证收益。

## 常见误区与边界

传输、路由和双工作池调度都增加复杂度。低负载或慢互连下可能得不偿失，不能仅以“预填充算力密集、解码带宽密集”决定架构。

## 面试追问

输入长度增长四倍时，哪个环节可能使分离方案失去优势？

## 相关阅读

- [什么是 LLM 中的 KV 缓存？](kv-cache-in-llms.md)
- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [LLM 中的连续批处理](continuous-batching-in-llms.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
