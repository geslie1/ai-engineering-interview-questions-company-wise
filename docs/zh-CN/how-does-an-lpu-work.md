# LPU 如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does an LPU work?](https://outcomeschool.com/blog/how-does-an-lpu-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文以 LPU 推理芯片为例，介绍片上存储、编译期调度和多芯片数据流如何服务语言模型生成。

## 面试解析

讨论专用硬件时应比较可支持模型、内存容量、互联开销、批量与尾延迟，而不只比较单用户输出速度。还要计入模型变更后编译和部署的成本。

## 常见误区与边界

原文的架构描述和性能判断不能推广到所有专用加速器。生成是否受带宽限制取决于批量和模型，具体芯片能力应以对应产品资料与实测为准。

## 面试追问

一个低延迟推理系统在大并发下优势消失，可能是哪些资源成为瓶颈？

## 相关阅读

- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [LLM 中的连续批处理](continuous-batching-in-llms.md)
- [云端与端侧模型部署](cloud-vs-on-device-model-deployment.md)
- [GPU 如何用于深度学习？](how-does-a-gpu-work-for-deep-learning.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
