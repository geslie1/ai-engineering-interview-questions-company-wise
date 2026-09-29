# 分组查询注意力

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[Grouped Query Attention](https://outcomeschool.com/blog/grouped-query-attention)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文比较 MHA、MQA 与 GQA：GQA 保留多个查询头，但让一组查询头共享键和值，在缓存成本和表示能力之间折中。

## 面试解析

固定层数、长度和头维度时，KV 载荷与 H_kv 成正比。若查询头为 32、KV 头为 8，相比对应 MHA，KV 载荷约为四分之一；这是本笔记的简化算例。

## 常见误区与边界

GQA 是模型结构选择，不能只改配置就保证预训练权重质量不变。转换现有 MHA 模型需要权重处理及后续训练验证。

## 面试追问

当 KV 头数等于 1 或查询头数时，分别退化成哪种结构？

## 相关阅读

- [什么是 LLM 中的 KV 缓存？](kv-cache-in-llms.md)
- [KV 缓存压缩](kv-cache-compression.md)
- [Transformer 中的多头注意力](multi-head-attention-in-transformers.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
