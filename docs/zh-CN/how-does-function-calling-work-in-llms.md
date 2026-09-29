# LLM 中的函数调用如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文强调函数调用中模型提出工具名和参数，真正执行由应用程序负责，并区分工具调用、JSON 输出和结构化结果。

## 面试解析

工具 schema 应给出精确名称、参数类型、必填项和错误语义。运行时再做格式验证、权限检查、业务约束检查和结果封装，不能把参数有效等同于操作获准。

## 常见误区与边界

结构化输出保证的是形式约束的一部分，不保证业务事实正确。工具结果应绑定调用 ID，并处理拒绝、超时与部分成功。

## 面试追问

为什么“退款金额必须小于限额”不能只写在工具描述里？

## 相关阅读

- [AI 智能体循环](ai-agent-loop.md)
- [什么是 MCP（模型上下文协议）？](what-is-mcp-model-context-protocol.md)
- [LLM 中的提示词注入](prompt-injection-in-llms.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
