# 预填充与解码：LLM 推理优化

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Prefill vs Decode: LLM Inference Optimization](https://outcomeschool.com/blog/prefill-vs-decode-llm-inference-optimization)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文区分预填充和解码阶段，并把首 token 延迟、逐 token 延迟、吞吐量及多种推理优化手段对应到不同瓶颈。

## 面试解析

预填充并行处理输入，解码复用 KV 缓存逐步生成。小批量解码常受带宽限制，长输入预填充更容易利用算力；实际瓶颈仍需通过测量确认。

## 常见误区与边界

TTFT 还包含排队、检索、网络等时间；不能全部算到模型预填充。报告性能时固定输入输出长度分布、并发、硬件和质量条件。

## 面试追问

首 token 快但后续输出断断续续，应检查哪些阶段和指标？

## 相关阅读

- [LLM 中的连续批处理](continuous-batching-in-llms.md)
- [推测解码](speculative-decoding.md)
- [LLM 推理中的预填充与解码分离](prefill-decode-disaggregation.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
