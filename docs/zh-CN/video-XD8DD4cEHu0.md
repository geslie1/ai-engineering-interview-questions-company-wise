# LLM 中的首 token 延迟问题

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 视频主题解析；未取得字幕，不是视频摘要或全文翻译。

- 原文来源：[The First-Token Latency Problem in LLMs](https://www.youtube.com/watch?v=XD8DD4cEHu0)
- 来源平台：www.youtube.com
- 获取日期：2026-09-29
- 获取状态：未取得可用字幕或正文

## 获取状态

未取得该视频的可用字幕或正文，因此不对视频内容作摘要。此页整理首 token 延迟的诊断思路，相关阅读提供可读取的文章笔记。

## 面试解析

把 TTFT 拆为网络、鉴权、排队、检索与上下文组装、预填充、首包传输。为每段记录时间，先定位占比最大的退化项，再决定缓存、调度或模型优化。

## 常见误区与边界

客户端看到的首字延迟可能包含缓冲，不等同于 GPU 计算结束时间。指标应同时观察 p50、p95、p99 和负载水平。

## 面试追问

模型没变但 TTFT 翻倍，如何用一条请求调用链缩小排查范围？

## 相关阅读

- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [提示词缓存如何工作？](how-does-prompt-caching-work.md)
- [token 流式传输如何工作？](how-does-token-streaming-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
