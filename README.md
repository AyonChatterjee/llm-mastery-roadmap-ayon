# 🧠 LLM Complete Roadmap & Resources
> From Transformers to Production-Grade LLM Systems
> Curated for someone who has completed ML, DL, NLP, and Transformer Architecture

---

## 🗺️ The Full Learning Path

```
Phase 1: LLM Fundamentals       (Weeks 1–3)
Phase 2: Fine-Tuning & Alignment (Weeks 4–6)
Phase 3: RAG                    (Weeks 7–9)
Phase 4: Agents & LangGraph     (Weeks 10–12)
Phase 5: Knowledge Graphs       (Weeks 13–15)
Phase 6: Production & MLOps     (Weeks 16+)
```

---

## 📌 Phase 1 — LLM Fundamentals

### 🎥 YouTube (Free)

| Channel | Playlist / Video | Notes |
|---|---|---|
| **CampusX** | [GenAI Roadmap End-to-End 2025](https://www.youtube.com/watch?v=pSVk-5WemQ0) | Best starting point, Nitish Sir |
| **CampusX** | [Generative AI using LangChain Playlist](https://www.youtube.com/@campusx-official/playlists) | Hands-on, very practical |
| **Andrej Karpathy** | [Let's build GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY) | THE best deep dive into GPT internals |
| **Andrej Karpathy** | [Neural Networks: Zero to Hero playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | Absolute gold for fundamentals |
| **Umar Jamil** | [Coding LLaMA from scratch](https://www.youtube.com/watch?v=oM4VmoabDAI) | Great for coding transformers from scratch |
| **Umar Jamil** | [Coding Attention from scratch](https://www.youtube.com/watch?v=bCz4OMemCcA) | Deep attention mechanism walkthrough |
| **1littlecoder** | LLM + HuggingFace tutorials | Quick practical demos |
| **Sentdex** | GPT/LLM from scratch series | Very beginner-friendly implementation |

### 📄 Research Papers (Must-Read)

| Paper | Link | Why It Matters |
|---|---|---|
| Attention Is All You Need (2017) | [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) | You already have this ✅ |
| GPT-2: Language Models are Unsupervised Multitask Learners | [OpenAI Blog](https://openai.com/research/language-unsupervised) | Decoder-only pretraining |
| GPT-3: Language Models are Few-Shot Learners | [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) | Scaling + few-shot prompting |
| BERT: Pre-training of Deep Bidirectional Transformers | [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) | Encoder-only, embeddings |
| InstructGPT (RLHF) | [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) | How ChatGPT was born — MUST READ |
| Chinchilla Scaling Laws | [arXiv:2203.15556](https://arxiv.org/abs/2203.15556) | Compute-optimal training |
| LLaMA 2 | [arXiv:2307.09288](https://arxiv.org/abs/2307.09288) | Open-source LLM architecture |

### 📝 Blogs & Free Courses

| Resource | Link | Type |
|---|---|---|
| **Hugging Face NLP Course** | [huggingface.co/learn/nlp-course](https://huggingface.co/learn/nlp-course) | Free, best HF intro |
| **DeepLearning.AI Short Courses** | [deeplearning.ai/short-courses](https://www.deeplearning.ai/short-courses/) | Free, industry-standard |
| **Lilian Weng's Blog (OpenAI)** | [lilianweng.github.io](https://lilianweng.github.io) | The best technical blog in AI |
| **Sebastian Raschka's Newsletter** | [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com) | Very detailed ML/LLM articles |
| **Jay Alammar's Blog** | [jalammar.github.io](https://jalammar.github.io) | Visual explanations of transformers/GPT |
| **The Illustrated Transformer** | [jalammar.github.io/illustrated-transformer](https://jalammar.github.io/illustrated-transformer/) | Best visual transformer explanation |

---

## 📌 Phase 2 — Fine-Tuning & Alignment

### 🎥 YouTube (Free)

| Channel | What to Watch |
|---|---|
| **CampusX** | Fine-tuning with HuggingFace PEFT |
| **Maxime Labonne** | [LLM Fine-Tuning playlist](https://www.youtube.com/@maximelabonne) — excellent LoRA/QLoRA content |
| **1littlecoder** | QLoRA fine-tuning on Colab tutorials |
| **Shaw Talebi** | Fine-tuning LLMs series |

### 📄 Research Papers

| Paper | Link | Why |
|---|---|---|
| LoRA | [arXiv:2106.09685](https://arxiv.org/abs/2106.09685) | Parameter-efficient fine-tuning |
| QLoRA | [arXiv:2305.14314](https://arxiv.org/abs/2305.14314) | Fine-tune 70B on a single GPU |
| RLHF / InstructGPT | [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) | Alignment via human feedback |
| DPO (Direct Preference Optimization) | [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) | Simpler alternative to RLHF |

### 📝 Blogs & Tools

| Resource | Link |
|---|---|
| HuggingFace PEFT Library Docs | [huggingface.co/docs/peft](https://huggingface.co/docs/peft) |
| Maxime Labonne's LLM Notebooks | [github.com/mlabonne/llm-course](https://github.com/mlabonne/llm-course) |
| Axolotl (fine-tuning framework) | [github.com/OpenAccess-AI-Collective/axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) |
| Unsloth (faster fine-tuning) | [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth) |

### 🛠️ Practice Target
> Fine-tune **Mistral 7B** or **LLaMA 3 8B** on a custom dataset using QLoRA on Google Colab (free tier works).

---

## 📌 Phase 3 — RAG (Retrieval Augmented Generation)

### What Is RAG?
```
User Query
    ↓
Embed query → search Vector DB
    ↓
Retrieve top-k relevant chunks
    ↓
Inject as context into LLM prompt
    ↓
LLM generates grounded answer (no hallucination)
```

### 🎥 YouTube (Free)

| Channel | What to Watch |
|---|---|
| **CampusX** | RAG pipeline from scratch — LangChain + ChromaDB |
| **Sam Witteveen** | RAG techniques deep dives |
| **Prompt Engineering (channel)** | Advanced RAG techniques |
| **James Briggs** | Vector databases + RAG hands-on |
| **AI Jason** | RAG + Agents projects |

### 📄 Research Papers

| Paper | Link |
|---|---|
| RAG original paper (Facebook AI) | [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) |
| Self-RAG | [arXiv:2310.11511](https://arxiv.org/abs/2310.11511) |
| HyDE (Hypothetical Document Embedding) | [arXiv:2212.10496](https://arxiv.org/abs/2212.10496) |
| RAGAS Evaluation | [arXiv:2309.15217](https://arxiv.org/abs/2309.15217) |

### 📝 Free Courses & Blogs

| Resource | Link |
|---|---|
| DeepLearning.AI — LangChain Chat with Data | [deeplearning.ai/short-courses](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/) |
| DeepLearning.AI — Building and Evaluating RAG | [deeplearning.ai](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) |
| LlamaIndex Docs | [docs.llamaindex.ai](https://docs.llamaindex.ai) |
| LangChain Docs | [python.langchain.com](https://python.langchain.com) |
| Pinecone Learning Center | [pinecone.io/learn](https://www.pinecone.io/learn/) |
| RAGAS Docs | [docs.ragas.io](https://docs.ragas.io) |

### 🛠️ Tools to Learn (in order)

```
FAISS (local vector search) → ChromaDB (local DB) → Pinecone (cloud)
Sentence Transformers → OpenAI Embeddings → BGE Embeddings
LlamaIndex → LangChain → Custom pipelines
```

---

## 📌 Phase 4 — LangChain, LangGraph & Agents

### 🔧 Tool Breakdown

| Tool | What It Is | When to Use |
|---|---|---|
| **LangChain** | Framework for LLM app building (chains, memory, tools) | General LLM apps, RAG |
| **LangGraph** | Stateful multi-agent workflows as graphs — nodes + edges | Complex agents, loops, multi-step reasoning |
| **LangFuse** | Observability / monitoring for LLM apps | Production apps — track latency, cost, traces |
| **LangSmith** | LangChain's own tracing/eval tool | Debugging LangChain pipelines |
| **LlamaIndex** | Data-centric framework, strong RAG tooling | Document Q&A, Knowledge Graphs |
| **DSPy** | Program LLMs, not just prompt them | Advanced, research-oriented pipelines |
| **Instructor** | Structured JSON outputs from LLMs using Pydantic | When you need reliable structured output |
| **CrewAI** | High-level multi-agent framework | Quick multi-agent apps with roles |
| **Ollama** | Run LLMs locally (Mistral, LLaMA, Gemma) | Local development |
| **vLLM** | Production LLM inference server | Serving at scale |

### 🎥 YouTube (Free)

| Channel | What to Watch |
|---|---|
| **CampusX** | [LangChain full playlist](https://www.youtube.com/@campusx-official/playlists) — very comprehensive |
| **CampusX** | LangGraph playlist (Dec 2025 updated) |
| **Greg Kamradt** | LangChain tutorials — OG channel for LC |
| **Sam Witteveen** | LangGraph + Agents deep dives |
| **LangChain Official** | [@LangChain on YouTube](https://www.youtube.com/@LangChain) |
| **AI Makerspace** | Agents + LangGraph hands-on |

### 📄 Research Papers (Agents)

| Paper | Link |
|---|---|
| ReAct: Reasoning + Acting | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) |
| Toolformer | [arXiv:2302.04761](https://arxiv.org/abs/2302.04761) |
| HuggingGPT / Jarvis | [arXiv:2303.04848](https://arxiv.org/abs/2303.04848) |
| AutoGPT / AgentGPT concepts | [arXiv:2304.11490](https://arxiv.org/abs/2304.11490) |

### 📝 Docs & Blogs

| Resource | Link |
|---|---|
| LangGraph Docs (official) | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/) |
| LangFuse Docs | [langfuse.com/docs](https://langfuse.com/docs) |
| LangChain Expression Language (LCEL) | [python.langchain.com/docs/expression_language](https://python.langchain.com/docs/expression_language/) |
| DeepLearning.AI — AI Agents in LangGraph | [deeplearning.ai/short-courses/ai-agents-in-langgraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) |

---

## 📌 Phase 5 — Knowledge Graphs & GraphRAG

### What Is a Knowledge Graph?
```
Instead of storing raw text chunks (like normal RAG),
you extract ENTITIES and RELATIONSHIPS and store as a graph:

[Elon Musk] --CEO of--> [Tesla]
[Tesla]      --makes--> [Electric Vehicles]
[Elon Musk]  --founded--> [SpaceX]

LLM can now do MULTI-HOP reasoning:
"What kind of vehicles does the CEO of SpaceX's other company make?"
```

### 🎥 YouTube (Free)

| Channel | What to Watch |
|---|---|
| **Neo4j** | [GraphRAG playlist](https://www.youtube.com/@neo4j) — official, very good |
| **CampusX** | Knowledge Graph + LLM sessions |
| **Rabbitmetrics** | Neo4j + LangChain tutorials |
| **PyBay 2024** | [Practical GraphRAG talk](https://www.youtube.com/watch?v=XNneh6-eyPg) — excellent 26 min walkthrough |

### 📄 Research Papers

| Paper | Link |
|---|---|
| Microsoft GraphRAG | [arXiv:2404.16130](https://arxiv.org/abs/2404.16130) |
| LightRAG | [arXiv:2410.05779](https://arxiv.org/abs/2410.05779) |
| HippoRAG | [arXiv:2405.14831](https://arxiv.org/abs/2405.14831) |
| Survey of GraphRAG | [arXiv:2501.13958](https://arxiv.org/abs/2501.13958) |

### 📝 Courses & Blogs

| Resource | Link |
|---|---|
| **DeepLearning.AI — Knowledge Graphs for RAG** | [deeplearning.ai/short-courses/knowledge-graphs-rag](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/) |
| Neo4j GraphRAG Python Package Docs | [neo4j.com/docs/neo4j-graphrag-python](https://neo4j.com/docs/neo4j-graphrag-python/current/) |
| Microsoft GraphRAG GitHub | [github.com/microsoft/graphrag](https://github.com/microsoft/graphrag) |
| LlamaIndex Knowledge Graph Tutorial | [docs.llamaindex.ai](https://docs.llamaindex.ai/en/stable/examples/index_structs/knowledge_graph/KnowledgeGraphDemo/) |
| IBM GraphRAG Tutorial | [ibm.com/think/tutorials/knowledge-graph-rag](https://www.ibm.com/think/tutorials/knowledge-graph-rag) |
| Awesome-GraphRAG (curated list) | [github.com/DEEP-PolyU/Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) |

### 🛠️ Tools

```
Neo4j          → Industry standard graph database (free community edition)
FalkorDB       → Ultra-fast graph DB, great GraphRAG SDK
LlamaIndex KG  → Built-in Knowledge Graph support
spaCy          → Entity extraction to build graphs
```

---

## 📌 Phase 6 — Production, Optimization & LLMOps

### 🎥 YouTube

| Channel | What to Watch |
|---|---|
| **Weights & Biases (W&B)** | LLMOps course, experiment tracking |
| **Hamel Husain** | Production LLM engineering |
| **Full Stack Deep Learning** | [fullstackdeeplearning.com](https://fullstackdeeplearning.com) — LLM bootcamp |

### 📝 Tools & Docs

| Tool | Link | What It Does |
|---|---|---|
| **vLLM** | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) | High-throughput LLM inference |
| **Ollama** | [ollama.ai](https://ollama.ai) | Run models locally |
| **LangFuse** | [langfuse.com](https://langfuse.com) | Monitoring, traces, cost tracking |
| **RAGAS** | [docs.ragas.io](https://docs.ragas.io) | Evaluate RAG pipeline quality |
| **Weights & Biases** | [wandb.ai](https://wandb.ai) | Experiment tracking |
| **Quantization (GPTQ/AWQ)** | [github.com/AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ) | Run big models on small GPUs |

### 📄 Papers

| Paper | Link |
|---|---|
| FlashAttention-2 | [arXiv:2307.08691](https://arxiv.org/abs/2307.08691) |
| Speculative Decoding | [arXiv:2211.17192](https://arxiv.org/abs/2211.17192) |
| vLLM (PagedAttention) | [arXiv:2309.06180](https://arxiv.org/abs/2309.06180) |

---

## 🔑 Key YouTube Channels — Master List

| Channel | Strength |
|---|---|
| **CampusX** | Your home base — Hindi explanations, end-to-end, LangChain/LangGraph/RAG all covered |
| **Andrej Karpathy** | Deep internals, GPT from scratch — no one beats this |
| **Umar Jamil** | Coding LLMs from scratch (LLaMA, Mistral, BERT) |
| **Sam Witteveen** | RAG + Agents, very practical |
| **1littlecoder** | Quick demos, HuggingFace, fine-tuning on Colab |
| **Maxime Labonne** | Fine-tuning, LoRA, quantization |
| **Shaw Talebi** | Beginner-friendly LLM tutorials |
| **AI Jason** | RAG projects + agent apps |
| **Greg Kamradt** | LangChain deep dives |
| **AI Makerspace** | Agents + production pipelines |
| **Neo4j** | GraphRAG, Knowledge Graphs — official |
| **DeepLearning.AI** | Short courses companion content |
| **LangChain Official** | Latest LangChain/LangGraph features |
| **Full Stack Deep Learning** | LLM bootcamp, production mindset |
| **LLM Agents MOOC (Berkeley)** | [YouTube Playlist](https://www.youtube.com/playlist?list=PLS01nW3RtgopsNLeM936V4TNSsvvVglLc) — university level |

---

## 📰 Top Blogs to Follow (Free)

| Blog | URL | What's Special |
|---|---|---|
| **Lilian Weng (OpenAI)** | [lilianweng.github.io](https://lilianweng.github.io) | The best technical AI blog, period |
| **Jay Alammar** | [jalammar.github.io](https://jalammar.github.io) | Visual explanations — Transformers, GPT, BERT |
| **Sebastian Raschka** | [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com) | Deep LLM articles |
| **Eugene Yan** | [eugeneyan.com](https://eugeneyan.com) | Applied ML/LLM in production |
| **The Batch (Andrew Ng)** | [deeplearning.ai/the-batch](https://www.deeplearning.ai/the-batch/) | Weekly AI news |
| **Hugging Face Blog** | [huggingface.co/blog](https://huggingface.co/blog) | Latest models, techniques |
| **Towards Data Science** | [towardsdatascience.com](https://towardsdatascience.com) | Community articles on LLMs |
| **Chip Huyen's Blog** | [huyenchip.com/blog](https://huyenchip.com/blog) | Production ML, LLMOps |

---

## 🔬 Where to Find Research Papers

| Platform | URL |
|---|---|
| **arXiv (AI section)** | [arxiv.org/list/cs.AI/recent](https://arxiv.org/list/cs.AI/recent) |
| **Papers With Code** | [paperswithcode.com](https://paperswithcode.com) |
| **Semantic Scholar** | [semanticscholar.org](https://www.semanticscholar.org) |
| **Google Scholar** | [scholar.google.com](https://scholar.google.com) |
| **Hugging Face Papers** | [huggingface.co/papers](https://huggingface.co/papers) |

---

## 🏗️ The One Project That Ties Everything Together

> Build a **Multi-Agent Research Assistant**:

```
Step 1: User gives a research topic
Step 2: Agent 1 (Research Agent) → searches web, extracts info
Step 3: Store extracted knowledge in Neo4j Knowledge Graph
Step 4: Agent 2 (QA Agent) → answers questions using GraphRAG
Step 5: Agent 3 (Writer Agent) → writes a structured report
Step 6: Whole pipeline monitored via LangFuse
```

**Tech stack:** LangGraph + Neo4j + LlamaIndex + LangFuse + Mistral/LLaMA

This touches every concept in this roadmap. Put this on GitHub — it's **portfolio gold**.

---

## 📅 Week-by-Week Plan

| Week | Focus | Deliverable |
|---|---|---|
| 1–2 | GPT-2/3 papers + HuggingFace basics + Ollama locally | Run inference on a local model |
| 3–4 | Fine-tune LLaMA 3 8B with QLoRA on Colab | Custom fine-tuned model |
| 5–6 | Basic RAG app — LlamaIndex + ChromaDB + PDF Q&A | PDF chatbot |
| 7–8 | RAGAS evaluation, improve chunking & retrieval | Evaluated RAG pipeline |
| 9–10 | LangGraph — build a multi-step agent | Working agent with tools |
| 11–12 | Knowledge Graph — Neo4j + entity extraction | Graph from your own dataset |
| 13–14 | GraphRAG with Microsoft GraphRAG / LlamaIndex | GraphRAG Q&A system |
| 15–16 | LangFuse monitoring + vLLM serving basics | Production-ready app |
| 17+ | DSPy, multi-agent systems with CrewAI/LangGraph | The portfolio project above |

---

## 🔗 CampusX Specific Resources

Since you've already followed CampusX for ML/DL/NLP:

| Resource | Link |
|---|---|
| GenAI End-to-End Course 2025 | [YouTube Video](https://www.youtube.com/watch?v=pSVk-5WemQ0) |
| LangChain Full Playlist | [CampusX Playlists](https://www.youtube.com/@campusx-official/playlists) |
| LangGraph Playlist | [campusx-official GitHub](https://github.com/campusx-official) |
| CrewAI Masterclass | [campusx-official GitHub](https://github.com/campusx-official) |
| LangGraph Memory Repo | [campusx-official GitHub](https://github.com/campusx-official) |

> Nitish Sir has LangChain, LangGraph, RAG, and CrewAI all covered. Stick with CampusX for practical implementation — it's the best Hindi resource for this stack.

---

*Last updated: May 2026 | Covers LLMs, RAG, Knowledge Graphs, LangGraph, LangFuse, Agents*
