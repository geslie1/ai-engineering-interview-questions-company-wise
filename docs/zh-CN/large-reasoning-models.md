# 大型推理模型（LRM）

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Large Reasoning Models (LRMs)](https://outcomeschool.com/blog/large-reasoning-models)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文将大型推理模型解释为投入更多推理阶段计算来处理复杂问题的语言模型，并介绍相应训练、应用场景及成本取舍。

## 面试解析

比较普通生成和推理模式时，应固定任务集，记录成功率、总 token、工具调用、延迟与成本。数学题和开放式写作的收益可能不同，适合按任务难度分配预算。

## 常见误区与边界

输出更长不等于推理更可靠，增加计算也不保证单调改善。可验证的答案、测试结果与证据比要求暴露内部思考过程更适合验收。

## 面试追问

如何判断一道题值得增加推理预算，还是应该调用外部工具验证？

## 相关阅读

- [思维链（CoT）提示如何工作？](how-does-chain-of-thought-prompting-work.md)
- [近端策略优化（PPO）](proximal-policy-optimization-ppo.md)
- [组相对策略优化（GRPO）](group-relative-policy-optimization-grpo.md)
- [LLM 路由](llm-routing.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
