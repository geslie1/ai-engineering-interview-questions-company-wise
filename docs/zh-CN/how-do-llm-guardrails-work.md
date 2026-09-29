# LLM 安全护栏如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How do LLM guardrails work?](https://outcomeschool.com/blog/how-do-llm-guardrails-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍输入与输出侧的安全护栏，包括规则和模型检查，并说明误判、绕过及额外延迟等限制。

## 面试解析

按风险设置不同检查点：输入筛查、检索权限、工具参数验证、输出隐私检查。每层都定义失败时的处理方式，并用正常与对抗样本测误拒率、漏检率。

## 常见误区与边界

输出过滤无法撤销已经执行的工具副作用。流式输出若先发后查，也可能让敏感片段已经离开系统；因此要明确缓冲与放行策略。

## 面试追问

安全模型不可用时，哪些任务可以降级，哪些必须暂停？

## 相关阅读

- [LLM 中的函数调用如何工作？](how-does-function-calling-work-in-llms.md)
- [LLM 中的提示词注入](prompt-injection-in-llms.md)
- [token 流式传输如何工作？](how-does-token-streaming-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
