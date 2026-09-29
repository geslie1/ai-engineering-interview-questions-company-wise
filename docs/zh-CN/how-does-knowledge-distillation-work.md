# 知识蒸馏如何工作？

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[How does Knowledge Distillation work?](https://outcomeschool.com/blog/how-does-knowledge-distillation-work)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍教师—学生蒸馏，通过软标签或其他教师信号训练更小模型，并说明软概率携带类别间关系。

## 面试解析

区分白盒 logits 蒸馏与仅能调用 API 的输出蒸馏。前者可匹配概率分布，后者通常使用教师生成的数据；两者需要的接口与训练信号不同。

## 常见误区与边界

教师错误可能被学生继承，不能把蒸馏当成自动净化。使用真实标签、数据过滤和独立测试，并确认学生在目标硬件上的实际成本收益。

## 面试追问

只有教师生成文本、拿不到 logits 时，蒸馏流程要怎样变化？

## 相关阅读

- [温度如何控制 LLM 输出？](how-does-temperature-control-llm-output.md)
- [微调如何工作？](how-does-fine-tuning-work.md)
- [小语言模型（SLM）](small-language-models-slms.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
