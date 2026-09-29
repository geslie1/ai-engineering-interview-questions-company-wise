# 上下文压缩如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does context compaction work?](https://outcomeschool.com/blog/how-does-context-compaction-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍用摘要压缩较早的对话历史，让长任务在有限上下文中继续，并比较直接丢弃历史的滑动窗口方式。

## 面试解析

可将目标、约束、已完成操作、未解决事项和证据路径分开保存；保留近期消息及必要的原始引用，接近预算阈值时再压缩，并为后续工具输出预留空间。

## 常见误区与边界

摘要可能丢失关键细节或引入错误，不能保证只丢无关信息。尤其要保留否定条件、操作是否已成功和授权范围，避免压缩后重复产生副作用。

## 面试追问

如何设计长任务回归用例，检测压缩后忘记限制或重复执行已完成操作的问题？

## 相关阅读

- [LLM 的“中间信息丢失”问题](lost-in-the-middle-problem-in-llms.md)
- [AI 智能体循环](ai-agent-loop.md)
- [AI 智能体记忆](ai-agent-memory.md)
- [AI 智能体可观测性](ai-agent-observability.md)
- [上下文工程](context-engineering.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
