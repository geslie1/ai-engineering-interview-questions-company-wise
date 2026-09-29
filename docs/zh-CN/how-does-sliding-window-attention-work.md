# 滑动窗口注意力如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Sliding Window Attention work?](https://outcomeschool.com/blog/how-does-sliding-window-attention-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍每个位置只关注有限邻域的滑动窗口注意力，降低长序列开销，并通过多层传播扩大间接可见范围。

## 面试解析

固定窗口宽度 w 时，注意力交互数约随 n×w 增长。流式实现可使用滚动 KV 缓冲，但要匹配模型训练时的局部或全局层结构。

## 常见误区与边界

有限层数下间接传播不等于无损访问所有历史。不要把为全注意力模型直接删缓存，与原生采用滑动窗口的模型混为一谈。

## 面试追问

模型混合局部层与全局层时，显存估算为什么不能只使用一个窗口长度？

## 相关阅读

- [什么是 LLM 中的 KV 缓存？](kv-cache-in-llms.md)
- [KV 缓存压缩](kv-cache-compression.md)
- [LLM 的“中间信息丢失”问题](lost-in-the-middle-problem-in-llms.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
