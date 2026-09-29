# token 流式传输如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Token Streaming work?](https://outcomeschool.com/blog/how-does-token-streaming-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍服务端把生成结果逐块发送给客户端，并用 SSE 解释流式传输与完整响应的体验差异。

## 面试解析

网络分块不等于事件边界，更不等于 token 边界。解析器要支持增量 UTF-8 解码、跨块 JSON、多个事件同块、取消和中途错误，并在完成后清理资源。

## 常见误区与边界

[DONE] 是部分 API 的约定，不是 SSE 协议必需标记。是否自动重连取决于客户端实现；重连也不天然保证生成可续传。

## 面试追问

一个汉字的字节横跨两次网络读取时，怎样避免乱码？

## 相关阅读

- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [LLM 中的首 token 延迟问题](video-XD8DD4cEHu0.md)
- [LLM 安全护栏如何工作？](how-do-llm-guardrails-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
