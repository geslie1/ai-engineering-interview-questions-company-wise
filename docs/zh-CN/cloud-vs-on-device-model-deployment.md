# 云端与端侧模型部署

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Cloud vs On-Device Model Deployment](https://outcomeschool.com/blog/cloud-vs-on-device-model-deployment)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文比较云端和端侧部署在网络依赖、隐私、资源、成本与模型更新上的差异，并介绍混合部署方式。

## 面试解析

先列出离线要求、延迟预算、设备容量和数据流向，再选择部署位置。混合方案可本地处理常见任务，复杂请求经授权转交云端，同时提供断网降级。

## 常见误区与边界

端侧不自动意味着数据安全，云端也不必然更慢。应实际测量模型计算、网络往返、散热降频与更新成本；边缘服务器也不等同于用户设备。

## 面试追问

如何为一款需要离线可用的语音助手划分端侧和云端能力？

## 相关阅读

- [模型量化如何工作？](how-does-model-quantization-work.md)
- [设计实时语音 AI 智能体](design-a-real-time-voice-ai-agent.md)
- [小语言模型（SLM）](small-language-models-slms.md)
- [GPU 如何用于深度学习？](how-does-a-gpu-work-for-deep-learning.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
