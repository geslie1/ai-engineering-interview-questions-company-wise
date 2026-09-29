# LoRA：LLM 的低秩适配

[资料目录](README.md) · [返回中文题库](../../README.zh-CN.md)

> 中文简要摘要与原创面试解析；不是原文的全文翻译。

- 原文来源：[LoRA - Low-Rank Adaptation of LLMs](https://outcomeschool.com/blog/lora-low-rank-adaptation-of-llms)
- 来源平台：outcomeschool.com
- 获取日期：2026-09-29
- 获取状态：已读取正文

## 原文摘要

原文介绍 LoRA 冻结基础权重，通过低秩矩阵学习增量，并讨论适配层选择、秩和合并部署。

## 面试解析

若 W 为 d_out×d_in，可令 ΔW=BA，其中 B 为 d_out×r、A 为 r×d_in，新增参数为 r(d_in+d_out)。按任务复杂度和验证效果选择秩及目标层。

## 常见误区与边界

减少可训练参数不等于训练显存按同一比例减少，基础权重和激活仍占空间。QLoRA 还涉及基础模型量化；多适配器部署也有调度开销。

## 面试追问

为什么零初始化一个因子能保持初始输出，而两个因子都为零会影响梯度？

## 相关阅读

- [模型量化如何工作？](how-does-model-quantization-work.md)
- [微调如何工作？](how-does-fine-tuning-work.md)
- [前缀微调如何工作？](how-does-prefix-tuning-work.md)

---

原文及其版权归原作者或权利人所有。本页摘要仅供学习定位；“面试解析”“常见误区与边界”“面试追问”为本项目补充，不代表原作者观点。
