# GPU 如何用于深度学习？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does a GPU work for Deep Learning?](https://outcomeschool.com/blog/how-does-a-gpu-work-for-deep-learning)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 GPU 如何利用并行计算和矩阵运算加速深度学习，并讨论显存、带宽、低精度运算及多卡协作。

## 面试解析

分析性能可先看算术强度，即计算量相对数据搬运量的比例，再判断主要受算力还是带宽限制。训练还需保存梯度与优化器状态，推理则应关注 KV 与并发。

## 常见误区与边界

模型不一定必须完整放进单卡显存，也可以分片或卸载，但会增加通信成本。更高峰值算力不会自动加速受内存或同步限制的任务。

## 面试追问

同一块 GPU 上，增大 batch 为什么可能提高吞吐，却恶化单个请求延迟？

## 相关阅读

- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [LLM 中的连续批处理](continuous-batching-in-llms.md)
- [模型量化如何工作？](how-does-model-quantization-work.md)
- [LPU 如何工作？](how-does-an-lpu-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
