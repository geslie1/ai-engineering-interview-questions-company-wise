# AI 工程面试中文资料库

[返回中文题库](../../README.zh-CN.md) · [English](../../README.md)

这里按主题整理题库中的 **105 项独立参考资料**，供 310 处答案链接复用。每篇笔记提供来源、简要摘要或获取状态、原创面试解析、常见误区、追问和相关笔记。

**这是一份摘要与学习解析资料库，不是外链文章的全文译本。** 英文题库保留原始外链，中文题库的答案链接指向本目录；每篇笔记顶部都可以跳转原文。

## 阅读范围与状态

- 98 篇文章与 1 篇帖子：已读取正文，提供简短中文摘要。
- 1 篇帖子：仅概括可见文字，未解读附图。
- 5 个视频：未取得可用字幕或正文，仅提供独立主题解析与相关阅读，不宣称概括视频内容。
- 获取日期：2026-09-29。工具、模型与硬件介绍存在版本边界，第三方文章不等同于官方实现保证。

## 按主题阅读

- [LLM 架构与分词（21 篇）](#topic-1)
- [推理优化与硬件（22 篇）](#topic-2)
- [RAG 与检索（10 篇）](#topic-3)
- [智能体与上下文工程（15 篇）](#topic-4)
- [微调、后训练与对齐（10 篇）](#topic-5)
- [评估与可观测性（4 篇）](#topic-6)
- [安全与防护（2 篇）](#topic-7)
- [多模态与语音（4 篇）](#topic-8)
- [产品与部署设计（7 篇）](#topic-9)
- [机器学习基础（10 篇）](#topic-10)

<a id="topic-1"></a>

## LLM 架构与分词

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [注意力中 √dₖ 缩放因子的数学原理](scaling-dot-product-attention.md) | 文章摘要与解析 |
| [注意力的数学原理：Q、K 和 V](math-behind-attention-qkv.md) | 文章摘要与解析 |
| [分组查询注意力](grouped-query-attention.md) | 文章摘要与解析 |
| [字节对编码（BPE）](bpe-in-llms.md) | 文章摘要与解析 |
| [大语言模型（LLM）中的分词](video-sK2s9I84EVI.md) | 视频主题解析，无字幕 |
| [LLM 中的位置嵌入](positional-embeddings-in-llms.md) | 文章摘要与解析 |
| [RoPE（旋转位置嵌入）的数学原理](math-behind-rope-rotary-position-embedding.md) | 文章摘要与解析 |
| [混合专家模型详解](mixture-of-experts.md) | 文章摘要与解析 |
| [LLM 的“中间信息丢失”问题](lost-in-the-middle-problem-in-llms.md) | 文章摘要与解析 |
| [RMSNorm（均方根层归一化）](rmsnorm-root-mean-square-layer-normalization.md) | 文章摘要与解析 |
| [LLM 中的前馈网络](feed-forward-networks-in-llms.md) | 文章摘要与解析 |
| [解析 Transformer 架构](decoding-transformer-architecture.md) | 文章摘要与解析 |
| [注意力中的因果掩码](causal-masking-in-attention.md) | 文章摘要与解析 |
| [Transformer 中的多头注意力](multi-head-attention-in-transformers.md) | 文章摘要与解析 |
| [Transformer 中的自注意力](self-attention-in-transformers.md) | 文章摘要与解析 |
| [滑动窗口注意力如何工作？](how-does-sliding-window-attention-work.md) | 文章摘要与解析 |
| [LLM 中的上下文窗口](post-context-window.md) | 帖子可见文字摘要 |
| [为什么 LLM 的上下文窗口有限？](video-CGIhxIaOg3M.md) | 视频主题解析，无字幕 |
| [DeepSeek-V4 架构详解](decoding-deepseek-v4.md) | 文章摘要与解析 |
| [大型推理模型（LRM）](large-reasoning-models.md) | 文章摘要与解析 |
| [Transformer 中的编码器与解码器](encoder-vs-decoder-in-transformers.md) | 文章摘要与解析 |

<a id="topic-2"></a>

## 推理优化与硬件

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [什么是 LLM 中的 KV 缓存？](kv-cache-in-llms.md) | 文章摘要与解析 |
| [KV 缓存压缩](kv-cache-compression.md) | 文章摘要与解析 |
| [解析 LLM 中的 FlashAttention](decoding-flash-attention.md) | 文章摘要与解析 |
| [温度如何控制 LLM 输出？](how-does-temperature-control-llm-output.md) | 文章摘要与解析 |
| [top-k 和 top-p 采样如何工作？](how-do-top-k-and-top-p-sampling-work.md) | 文章摘要与解析 |
| [预填充与解码：LLM 推理优化](prefill-vs-decode-llm-inference-optimization.md) | 文章摘要与解析 |
| [LLM 中的连续批处理](continuous-batching-in-llms.md) | 文章摘要与解析 |
| [LLM 中的分页注意力](paged-attention-in-llms.md) | 文章摘要与解析 |
| [vLLM 如何工作？](how-does-vllm-work.md) | 文章摘要与解析 |
| [推测解码](speculative-decoding.md) | 文章摘要与解析 |
| [提示词缓存如何工作？](how-does-prompt-caching-work.md) | 文章摘要与解析 |
| [模型量化如何工作？](how-does-model-quantization-work.md) | 文章摘要与解析 |
| [LLM 中的首 token 延迟问题](video-XD8DD4cEHu0.md) | 视频主题解析，无字幕 |
| [SGLang 如何工作？](how-does-sglang-work.md) | 文章摘要与解析 |
| [TensorRT-LLM 如何工作？](how-does-tensorrt-llm-work.md) | 文章摘要与解析 |
| [LLM 推理优化](video-jV2sCj4lHYk.md) | 视频主题解析，无字幕 |
| [LLM 推理优化](llm-inference-optimization.md) | 文章摘要与解析 |
| [LLM 推理中的预填充与解码分离](prefill-decode-disaggregation.md) | 文章摘要与解析 |
| [token 流式传输如何工作？](how-does-token-streaming-work.md) | 文章摘要与解析 |
| [GPU 如何用于深度学习？](how-does-a-gpu-work-for-deep-learning.md) | 文章摘要与解析 |
| [LPU 如何工作？](how-does-an-lpu-work.md) | 文章摘要与解析 |
| [LLM 中的 N-gram 推测](n-gram-speculation-in-llms.md) | 文章摘要与解析 |

<a id="topic-3"></a>

## RAG 与检索

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [RAG 分块策略](chunking-strategies-for-rag.md) | 文章摘要与解析 |
| [混合搜索如何工作？](how-does-hybrid-search-work.md) | 文章摘要与解析 |
| [重排序器如何工作？](how-does-a-reranker-work.md) | 文章摘要与解析 |
| [HyDE 在 RAG 中如何工作？](how-does-hyde-work.md) | 文章摘要与解析 |
| [智能体式 RAG](agentic-rag.md) | 文章摘要与解析 |
| [近似最近邻（ANN）搜索如何工作？](how-does-approximate-nearest-neighbor-ann-search-work.md) | 文章摘要与解析 |
| [向量数据库如何工作？](how-does-a-vector-database-work.md) | 文章摘要与解析 |
| [语义搜索如何工作？](how-does-semantic-search-work.md) | 文章摘要与解析 |
| [ColBERT：后期交互检索详解](decoding-colbert.md) | 文章摘要与解析 |
| [GraphRAG](graphrag.md) | 文章摘要与解析 |

<a id="topic-4"></a>

## 智能体与上下文工程

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [ReAct 智能体](react-agent.md) | 文章摘要与解析 |
| [思维链（CoT）提示如何工作？](how-does-chain-of-thought-prompting-work.md) | 文章摘要与解析 |
| [AI 智能体循环](ai-agent-loop.md) | 文章摘要与解析 |
| [LLM 中的函数调用如何工作？](how-does-function-calling-work-in-llms.md) | 文章摘要与解析 |
| [AI 工程详解：LLM、RAG、MCP、智能体、微调与量化](video-lnfWvX66FUk.md) | 视频主题解析，无字幕 |
| [什么是 MCP（模型上下文协议）？](what-is-mcp-model-context-protocol.md) | 文章摘要与解析 |
| [多智能体系统](multi-agent-systems.md) | 文章摘要与解析 |
| [AI 编排](ai-orchestration.md) | 文章摘要与解析 |
| [AI 智能体记忆](ai-agent-memory.md) | 文章摘要与解析 |
| [修复 AI 智能体中的无限循环](post-agent-infinite-loop.md) | 帖子摘要与解析 |
| [AI 运行框架工程（Harness Engineering）](harness-engineering-in-ai.md) | 文章摘要与解析 |
| [计算机操作智能体如何工作？](how-do-computer-use-agents-work.md) | 文章摘要与解析 |
| [AI 子智能体](ai-subagents.md) | 文章摘要与解析 |
| [上下文工程](context-engineering.md) | 文章摘要与解析 |
| [上下文压缩如何工作？](how-does-context-compaction-work.md) | 文章摘要与解析 |

<a id="topic-5"></a>

## 微调、后训练与对齐

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [解析 InstructGPT](decoding-instructgpt.md) | 文章摘要与解析 |
| [基于人类反馈的强化学习（RLHF）](reinforcement-learning-from-human-feedback-rlhf.md) | 文章摘要与解析 |
| [近端策略优化（PPO）](proximal-policy-optimization-ppo.md) | 文章摘要与解析 |
| [直接偏好优化（DPO）](direct-preference-optimization-dpo.md) | 文章摘要与解析 |
| [组相对策略优化（GRPO）](group-relative-policy-optimization-grpo.md) | 文章摘要与解析 |
| [LoRA：LLM 的低秩适配](lora-low-rank-adaptation-of-llms.md) | 文章摘要与解析 |
| [微调如何工作？](how-does-fine-tuning-work.md) | 文章摘要与解析 |
| [前缀微调如何工作？](how-does-prefix-tuning-work.md) | 文章摘要与解析 |
| [LLM 中的持续学习](continual-learning-in-llms.md) | 文章摘要与解析 |
| [知识蒸馏如何工作？](how-does-knowledge-distillation-work.md) | 文章摘要与解析 |

<a id="topic-6"></a>

## 评估与可观测性

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [LLM 评估](llm-evaluation.md) | 文章摘要与解析 |
| [使用 LLM 作为裁判](llm-as-a-judge.md) | 文章摘要与解析 |
| [AI 智能体可观测性](ai-agent-observability.md) | 文章摘要与解析 |
| [AI 智能体评估](ai-agent-evaluation.md) | 文章摘要与解析 |

<a id="topic-7"></a>

## 安全与防护

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [LLM 中的提示词注入](prompt-injection-in-llms.md) | 文章摘要与解析 |
| [LLM 安全护栏如何工作？](how-do-llm-guardrails-work.md) | 文章摘要与解析 |

<a id="topic-8"></a>

## 多模态与语音

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [多模态 AI](multimodal-ai.md) | 文章摘要与解析 |
| [解析视觉 Transformer（ViT）](decoding-vision-transformer-vit.md) | 文章摘要与解析 |
| [设计实时语音 AI 智能体](design-a-real-time-voice-ai-agent.md) | 文章摘要与解析 |
| [图像嵌入如何工作？](how-do-image-embeddings-work.md) | 文章摘要与解析 |

<a id="topic-9"></a>

## 产品与部署设计

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [Cursor 如何工作？](how-does-cursor-work.md) | 文章摘要与解析 |
| [Claude Code 如何工作？](how-does-claude-code-work.md) | 文章摘要与解析 |
| [LLM 路由](llm-routing.md) | 文章摘要与解析 |
| [语义缓存如何工作？](how-does-semantic-caching-work.md) | 文章摘要与解析 |
| [走进 ChatGPT：按下回车后发生了什么](inside-chatgpt-what-happens-after.md) | 文章摘要与解析 |
| [小语言模型（SLM）](small-language-models-slms.md) | 文章摘要与解析 |
| [云端与端侧模型部署](cloud-vs-on-device-model-deployment.md) | 文章摘要与解析 |

<a id="topic-10"></a>

## 机器学习基础

| 笔记 | 类型与阅读范围 |
| --- | --- |
| [交叉熵损失的数学原理](math-behind-cross-entropy-loss.md) | 文章摘要与解析 |
| [机器学习中的正则化：L1 与 L2](regularization-in-machine-learning.md) | 文章摘要与解析 |
| [反向传播的数学原理](math-behind-backpropagation.md) | 文章摘要与解析 |
| [精确率与召回率](precision-vs-recall.md) | 文章摘要与解析 |
| [梯度下降的数学原理](math-behind-gradient-descent.md) | 文章摘要与解析 |
| [线性回归与逻辑回归](linear-regression-vs-logistic-regression.md) | 文章摘要与解析 |
| [什么是对比学习？](contrastive-learning.md) | 文章摘要与解析 |
| [循环神经网络（RNN）](recurrent-neural-network.md) | 文章摘要与解析 |
| [机器学习中的特征工程](feature-engineering.md) | 文章摘要与解析 |
| [RNN 与 Transformer 有何区别？](how-do-rnns-and-transformers-differ.md) | 文章摘要与解析 |

## 内容与来源说明

摘要用于帮助判断原文是否值得进一步阅读，不覆盖原文全部论证、示例、代码或图片。其后的面试解析和追问是本项目补充，不能视为原作者观点，也不保证覆盖引用它的每一道题的完整答案。

外部原文的著作权和许可仍由原作者或权利人保留；仓库许可证不自动授予外部原文的复制、翻译或再发布权。本目录未收录外部文章全文、图片副本或视频字幕。

[来源清单（JSON）](sources.json)记录原始链接、获取日期、阅读状态和对应文件，便于核对及维护。

## 本地检查

在仓库根目录运行：

```bash
python3 scripts/validate-docs.py
```

检查题库答案与来源清单的对应关系、105 篇笔记的来源标注、相关笔记链接，以及 Markdown 本地链接和锚点。
