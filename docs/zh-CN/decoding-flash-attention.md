# 解析 LLM 中的 FlashAttention

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Decoding Flash Attention in LLMs](https://outcomeschool.com/blog/decoding-flash-attention)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文将 FlashAttention 的核心归结为分块计算、在线 softmax 和减少 HBM 数据往返，而非近似删减注意力连接。

## 面试解析

回答性能题时区分 FLOPs、HBM 读写和片上存储：避免把完整 n×n 中间矩阵写回 HBM，能降低内存流量；反向传播还可用重计算换存储。

## 常见误区与边界

数学上仍计算完整注意力，浮点舍入可能与其他实现不同。收益受硬件、序列长度、数据类型及内核支持影响，不应承诺固定倍数。

## 面试追问

为什么额外重计算有时反而让训练更快？

## 相关阅读

- [注意力中 √dₖ 缩放因子的数学原理](scaling-dot-product-attention.md)
- [注意力的数学原理：Q、K 和 V](math-behind-attention-qkv.md)
- [GPU 如何用于深度学习？](how-does-a-gpu-work-for-deep-learning.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
