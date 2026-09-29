# 什么是 MCP（模型上下文协议）？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[What is MCP (Model Context Protocol)?](https://outcomeschool.com/blog/what-is-mcp-model-context-protocol)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 MCP 通过共同协议连接 AI 应用与外部工具、数据，并区分宿主、客户端、服务器及函数调用的职责。

## 面试解析

可以按“应用宿主管理交互与授权，客户端维护连接，服务器暴露能力并访问后端”解释。模型选工具与应用通过协议调用工具是两个不同层次。

## 常见误区与边界

协议统一不等于权限自动正确。发现工具后仍要验证来源、用户授权及数据访问范围；具体传输和认证实现须遵循所用协议版本。

## 面试追问

一个 MCP 工具能返回数据，但用户在源系统已失去权限，应在哪一层拒绝？

## 相关阅读

- [LLM 中的函数调用如何工作？](how-does-function-calling-work-in-llms.md)
- [AI 编排](ai-orchestration.md)
- [LLM 中的提示词注入](prompt-injection-in-llms.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
