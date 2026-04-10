# 🥪 Sandwich-LLM

> Slash your Claude/GPT API costs by 70% with Local SLM Context Compression.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)

## 💡 What is this?
Long prompts cost money. Providing large context (lorebooks, system logs, vast codebases) to paid LLMs like Claude 3.5 Sonnet or GPT-4o drains your API budget quickly. 

**Sandwich-LLM** introduces a "Sandwich Architecture" (`Local SLM` $\rightarrow$ `Paid LLM` $\rightarrow$ `Local SLM`). It uses a free, local model (like Gemma 27B or Llama 3 via LM Studio/Ollama) to compress verbose natural language into highly dense, YAML-like structured tags. You send only this compressed core to the expensive LLM, drastically reducing token usage while maintaining high accuracy.

## 🚀 The 3-Phase Architecture

1. **Phase 1: Compile (Local SLM - $0)** 🍞 *(Top Bread)*
   - The local model reads your massive context (e.g., 5,000 words of story lore or chat history).
   - It strips all conversational grammar and outputs extremely dense Key-Value tags. (Compression rate: 40~70%).
2. **Phase 2: Execute (Paid API - $$$)** 🥩 *(The Meat)*
   - The paid, highly intelligent model (Claude/Gemini/GPT) receives the compressed YAML context + the current task.
   - It executes the task brilliantly without hallucination, using only a fraction of the tokens.
3. **Phase 3: De-compile & Update (Local SLM - $0)** 🍞 *(Bottom Bread)*
   - The local model reads the newly generated output, extracts only the state changes (new events, logic updates), and appends them to your database.

## 📊 Example: Structural Compression
**[Original Raw Text - 70 Tokens]**
> "Alice is the guild master of the Rank 1 guild. She acts as Bob's legal shield. She misunderstands his indifferent behavior as a caring gesture to protect her."

**[Compiled Context - 15 Tokens]**
> `[Char|Alice: Rank1_Master, LegalShield, Delusion(Misunderstands Bob)]`

## 🛠️ Use Cases
- **AI Novel Writing Automation:** Keep track of massive story bibles without paying massive token fees on every new chapter.
- **Log Analysis:** Compress daily chat logs or server logs locally before asking a paid AI to analyze them.
- **Agentic Memory (RAG):** Retrieve memories in a highly compressed format instead of fetching raw, verbose text.

## 💻 How to Run (Quick Start)
1. Run a local SLM via [LM Studio](https://lmstudio.ai/) or Ollama (Default: `http://127.0.0.1:1234/v1`).
2. Add your Anthropic/OpenAI API key in the scripts.
3. Run the compiler or the full pipeline:
```bash
# Compress a large text file
python3 compressor.py ./your_massive_lorebook.md

# Run the 3-phase sandwich pipeline example
python3 pipeline_example.py
```

## 📜 License
MIT License. Free to use and modify!
