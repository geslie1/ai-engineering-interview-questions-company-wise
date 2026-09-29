# RNN 与 Transformer 有何区别？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How do RNNs and Transformers differ?](https://outcomeschool.com/blog/how-do-rnns-and-transformers-differ)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文对比 RNN 的递归状态更新与 Transformer 的注意力机制，讨论训练并行性、长距离依赖和资源开销。

## 面试解析

比较时要区分训练与生成：Transformer 可并行处理训练序列中的多个位置，但自回归生成通常仍逐 token 进行。RNN 的状态较紧凑，注意力则能直接访问更丰富的历史表示。

## 常见误区与边界

不能把“Transformer 更并行”理解为输出 token 可全部同时生成。小数据、低功耗、持续流处理等场景也可能适合循环结构。

## 面试追问

对无限长度的数据流，固定状态与持续增长的 KV 缓存各有什么取舍？

## 相关阅读

- [什么是 LLM 中的 KV 缓存？](kv-cache-in-llms.md)
- [解析 Transformer 架构](decoding-transformer-architecture.md)
- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [循环神经网络（RNN）](recurrent-neural-network.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
