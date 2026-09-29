# 为什么 LLM 的上下文窗口有限？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 视频主题解析；未取得字幕，不是视频摘要或全文翻译。

- 原文来源：[Why is the context window limited in LLMs?](https://www.youtube.com/watch?v=CGIhxIaOg3M&lc)
- 来源平台：www.youtube.com
- 获取日期：2026-09-29
- 获取状态：未取得可用字幕或正文

## 获取状态

未取得该视频的可用字幕或正文，因此不对视频内容作摘要。此页补充上下文长度的工程约束，相关笔记提供可核对的学习路径。

## 面试解析

窗口限制来自训练配置、位置表示、运行时资源与产品约束等多方面。全注意力计算和 KV 存储的增长规律不同，应分别分析，而不是只说“显存不够”。

## 常见误区与边界

修改一个最大长度配置不保证模型能可靠处理更长文本。应验证位置外推、长距离证据利用、实际延迟和并发容量。

## 面试追问

同样支持长窗口的两个模型，为什么长文问答质量仍可能差很多？

## 相关阅读

- [什么是 LLM 中的 KV 缓存？](kv-cache-in-llms.md)
- [RoPE（旋转位置嵌入）的数学原理](math-behind-rope-rotary-position-embedding.md)
- [LLM 的“中间信息丢失”问题](lost-in-the-middle-problem-in-llms.md)
- [滑动窗口注意力如何工作？](how-does-sliding-window-attention-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
