# LLM 中的 N-gram 推测

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[N-gram Speculation in LLMs](https://outcomeschool.com/blog/n-gram-speculation-in-llms)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍用已有文本中的 n-gram 匹配提出候选续写，再由目标模型验证，以减少逐 token 解码的开销。

## 面试解析

可将当前后缀与输入或历史中的片段匹配，把后续 token 作为候选块。收益取决于复用程度、候选长度、接受率以及验证成本，代码局部修改是值得测量的场景。

## 常见误区与边界

分布等价需要正确的验证与接受规则，不能直接输出检索到的片段。低接受率时额外查找和验证可能拖慢推理；“总能加速”并不成立。

## 面试追问

如何动态调整候选长度，使重复率低的请求不会因推测而明显变慢？

## 相关阅读

- [字节对编码（BPE）](bpe-in-llms.md)
- [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md)
- [推测解码](speculative-decoding.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
