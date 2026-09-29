# LLM 推理优化

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文是推理优化资料导航，串联 KV 缓存、分页、FlashAttention、GQA、推测解码、批处理与推理引擎等主题。

## 面试解析

先区分显存容量、内存带宽、算力、通信和排队瓶颈，再选择对应方法。例如分页改善分配效率，前缀缓存减少重复预填充，两者不能互相替代。

## 常见误区与边界

任何优化都需要说明适用负载和成本：更大批处理可能增加等待，推测解码可能有草稿开销。不要把多个单项加速比直接相乘。

## 面试追问

如何设计一个同时比较质量、吞吐、尾延迟和每请求成本的基准？

## 相关阅读

- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [vLLM 如何工作？](how-does-vllm-work.md)
- [推测解码](speculative-decoding.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
