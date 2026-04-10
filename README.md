# 🥪 Sandwich-LLM

> Slash your Claude/GPT API costs by 70% with Local SLM Context Compression.
> 로컬 소형 모델(SLM)을 활용해 컨텍스트를 고밀도로 압축하고, 유료 API(Claude/GPT) 비용을 획기적으로 절감하는 하이브리드 파이프라인.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)

## 💡 What is this? (이게 뭔가요?)
Long prompts cost money. Providing large context (lorebooks, logs, codebases) to paid LLMs like Claude 3.5 Sonnet or GPT-4o drains your API budget quickly. 

**Sandwich-LLM** introduces a "Sandwich Architecture" (Local SLM $\rightarrow$ Paid LLM $\rightarrow$ Local SLM). It uses a free, local model (like Gemma 27B via LM Studio) to compress verbose natural language into highly dense, YAML-like structured tags. You send only this compressed core to the expensive LLM.

방대한 자연어 컨텍스트를 무료 로컬 모델(`LM Studio` + `gemma`)을 이용해 초고밀도 YAML/태그 형식으로 1차 압축(Compile)한 뒤, 비싼 유료 모델에게 전달하는 비용 최적화 파이프라인입니다.

## 🚀 The 3-Phase Architecture

1. **Phase 1: Compile (Local SLM - $0)** 🍞 (Top Bread)
   - The local model reads your massive context (e.g., 5,000 words of story lore) and strips all natural language grammar.
   - It outputs extremely dense Key-Value tags. (Compression rate: 40~70%).
2. **Phase 2: Execute (Paid API - $$$)** 🥩 (Meat/Core)
   - The paid model (Claude/Gemini) receives the compressed YAML context + the current task.
   - It executes the task brilliantly without hallucination, using a fraction of the tokens.
3. **Phase 3: De-compile & Update (Local SLM - $0)** 🍞 (Bottom Bread)
   - The local model reads the newly generated output, extracts only the state changes (new events, character updates), and appends them to your database.

## 📊 Example: Structural Compression
**[Original Raw Text - 70 Tokens]**
> "Seo Ha-yun is the guild master of the Rank 1 guild. She acts as Lee-jun's legal shield. She misunderstands his indifferent behavior as a caring gesture to protect her."

**[Compiled Context - 15 Tokens]**
> `[Char|Ha-yun: Rank1_Master, LegalShield, Delusion(Misunderstands Lee-jun)]`

## 🛠️ Use Cases
- **AI Novel Writing Automation:** Keep track of massive story bibles without paying massive token fees.
- **Log Analysis:** Compress daily chat logs or server logs locally before asking an AI to analyze them.
- **Agentic Memory (RAG):** Retrieve memories in a highly compressed format instead of raw text.

## 💻 How to Run (Quick Start)
1. Run a local SLM via [LM Studio](https://lmstudio.ai/) (Default: `http://127.0.0.1:1234/v1`).
2. Add your Anthropic/OpenAI API key in the scripts.
3. Run the compiler:
```bash
python3 compressor.py ./your_massive_lorebook.md
# Generates ./your_massive_lorebook.md.compiled
```

## 📜 License
MIT License. Free to use and modify!
