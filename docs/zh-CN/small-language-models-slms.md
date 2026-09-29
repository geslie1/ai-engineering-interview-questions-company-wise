# 小语言模型（SLM）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Small Language Models (SLMs)](https://outcomeschool.com/blog/small-language-models-slms)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文讨论小语言模型在窄领域、低成本和端侧场景中的价值，以及数据质量、蒸馏和微调对能力的影响。

## 面试解析

先建立目标任务的质量下限，再比较模型在目标硬件上的内存、速度、能耗与并发。可把容易的请求交给小模型，难题转交更强模型，但路由本身也需评测。

## 常见误区与边界

“小模型”没有统一参数阈值。参数更少不保证端到端更快：算子支持、量化方式、输入长度和 KV 缓存都可能改变结果。

## 面试追问

怎样证明一个专用小模型能替代通用大模型，而不是只在少量演示上表现相近？

## 相关阅读

- [模型量化如何工作？](how-does-model-quantization-work.md)
- [微调如何工作？](how-does-fine-tuning-work.md)
- [知识蒸馏如何工作？](how-does-knowledge-distillation-work.md)
- [LLM 路由](llm-routing.md)
- [云端与端侧模型部署](cloud-vs-on-device-model-deployment.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
