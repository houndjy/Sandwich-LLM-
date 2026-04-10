import sys
import urllib.request
import json
import os

# Set your local SLM endpoint (e.g., LM Studio, Ollama)
LOCAL_LLM_URL = "http://127.0.0.1:1234/v1/chat/completions"

def compress_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Skip compression for very short files to avoid overhead
    if len(content) < 500:
        print(f"INFO: Text is too short to compress. ({len(content)} chars)")
        out_path = file_path + ".compiled"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        sys.exit(0)

    print(f">> [Local SLM] Compressing context... ({len(content)} chars)")
    
    prompt = f"""You are an expert Prompt Compiler. Compress the following text into highly dense, structured YAML-like Key-Value tags. 
- Remove all conversational grammar, filler words, and redundant info. 
- Retain ALL technical facts, logic, and core meanings.
- If it is code, summarize the architecture and key functions instead of printing full logic.

[Original Text]
{content}
"""
    
    data = {
        "model": "local-model", # Replace with your local model name if needed
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    
    try:
        req = urllib.request.Request(LOCAL_LLM_URL, data=json.dumps(data).encode('utf-8'), headers={"Content-Type": "application/json"}, method='POST')
        res = urllib.request.urlopen(req)
        compiled = json.loads(res.read().decode('utf-8'))['choices'][0]['message']['content']
        
        out_path = file_path + ".compiled"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(compiled)
            
        print(f"SUCCESS: Compiled context saved to {out_path}")
        print(f"Stats: Original {len(content)} chars -> Compiled {len(compiled)} chars")
        
    except Exception as e:
        print(f"ERROR: Local LLM compression failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 compressor.py <file_path>")
        sys.exit(1)
        
    target_file = sys.argv[1]
    compress_file(target_file)
