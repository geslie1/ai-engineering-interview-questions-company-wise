# 上下文工程

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Context Engineering](https://outcomeschool.com/blog/context-engineering)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文把上下文工程描述为对指令、历史、检索材料、工具信息等输入进行组织和管理，并讨论预算、选择与压缩。

## 面试解析

可为不同信息分配 token 预算，记录来源和时效，把当前目标、已确认约束和执行状态放在稳定位置。检索内容与工具输出作为证据处理，避免混入高优先级指令。

## 常见误区与边界

上下文更多不一定更好，模型也并非只受当前文字影响：训练得到的能力和推理配置同样重要。上下文策略需要通过真实任务和失败案例验证。

## 面试追问

怎样证明一次上下文裁剪保留了关键约束，而不仅是让提示变短？

## 相关阅读

- [LLM 的“中间信息丢失”问题](lost-in-the-middle-problem-in-llms.md)
- [AI 智能体记忆](ai-agent-memory.md)
- [LLM 中的提示词注入](prompt-injection-in-llms.md)
- [AI 运行框架工程（Harness Engineering）](harness-engineering-in-ai.md)
- [上下文压缩如何工作？](how-does-context-compaction-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
