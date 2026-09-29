# 推测解码

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Speculative Decoding](https://outcomeschool.com/blog/speculative-decoding)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文说明推测解码先生成草稿，再由目标模型批量验证；正确的接受与修正规则可以保持目标采样分布。

## 面试解析

分析加速比时，把草稿耗时、验证耗时和每轮实际接受的 token 数放在同一个模型里。接受率高但草稿太贵，仍可能没有收益。

## 常见误区与边界

贪心一致性检查与随机采样下的分布保持不是同一算法。不能仅比较“两个模型选中的词是否一致”就宣称保留随机采样分布。

## 面试追问

某个领域草稿接受率突然下降，怎样选择缩短草稿、换草稿器或关闭推测？

## 相关阅读

- [温度如何控制 LLM 输出？](how-does-temperature-control-llm-output.md)
- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [LLM 中的 N-gram 推测](n-gram-speculation-in-llms.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
