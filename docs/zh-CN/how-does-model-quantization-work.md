# 模型量化如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍低精度表示、缩放与零点，以及 PTQ、QAT、权重量化和激活量化之间的区别，并讨论异常值带来的误差。

## 面试解析

先估算权重载荷，再把量化元数据、KV 和运行时开销加回去。选择位宽后，需要确认目标硬件存在有效内核，并用代表性数据检验精度与延迟。

## 常见误区与边界

更少 bit 不必然更快：解量化、内核覆盖和访存方式可能抵消收益。权重量化也不会自动缩小未量化的 KV 缓存。

## 面试追问

4 bit 模型能装进显存但推理反而更慢，优先检查什么？

## 相关阅读

- [KV 缓存压缩](kv-cache-compression.md)
- [LoRA：LLM 的低秩适配](lora-low-rank-adaptation-of-llms.md)
- [云端与端侧模型部署](cloud-vs-on-device-model-deployment.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
