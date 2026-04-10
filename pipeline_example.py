import urllib.request
import json
import os

# ==========================================
# Configuration: Replace with your details
# ==========================================
PAID_API_KEY = os.getenv("PAID_API_KEY", "your-paid-api-key-here")
PAID_API_URL = "https://api.anthropic.com/v1/messages" # Example: Anthropic endpoint
LOCAL_LLM_URL = "http://127.0.0.1:1234/v1/chat/completions" # Example: LM Studio endpoint
PROJECT_DIR = "./sample_project_folder"

def call_paid_api(prompt):
    """Phase 2: Calls the expensive, high-intelligence model (e.g., Claude, GPT-4)."""
    headers = {
        "x-api-key": PAID_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    data = {
        "model": "claude-3-5-sonnet-latest",
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": prompt}]
    }
    req = urllib.request.Request(PAID_API_URL, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    res = urllib.request.urlopen(req)
    return json.loads(res.read().decode('utf-8'))['content'][0]['text']

def call_local_slm(prompt):
    """Phase 1 & 3: Calls the free, local SLM (e.g., Gemma, Llama 3)."""
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "local-model",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }
    try:
        req = urllib.request.Request(LOCAL_LLM_URL, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
        res = urllib.request.urlopen(req)
        return json.loads(res.read().decode('utf-8'))['choices'][0]['message']['content']
    except Exception as e:
        print(f"Local LLM Error: Ensure your local server is running. ({e})")
        return ""

def run_sandwich_pipeline():
    print("=== Sandwich-LLM Pipeline Example ===")
    
    # [Phase 1] Local SLM Compresses Context (Assuming compressor.py was run, or mock data)
    print("\n>> Phase 1: Loading Compiled Context...")
    compressed_context = "[Char|Alice: Hero, Brave, Level 5] [Event|Forest: Found magical sword]" 
    print(f"Dense Context Loaded: {compressed_context}")
    
    # [Phase 2] Paid API Executes Task with dense context
    print("\n>> Phase 2: Paid API generating high-quality output...")
    prompt = f"""Use the following compressed context to write a short story scene.
    
    [Compiled Context]
    {compressed_context}
    
    [Task]
    Alice enters the dark cave and encounters a goblin. Describe her reaction based on her character traits.
    """
    # output = call_paid_api(prompt) # Uncomment when API key is set
    output = "(Mock Output) Alice boldly stepped into the cave, her magical sword gleaming..."
    print(f"Output generated successfully.")

    # [Phase 3] Local SLM Extracts State Changes to update Database
    print("\n>> Phase 3: Local SLM extracting state changes from the new output...")
    update_prompt = f"Extract any state changes (new items, level ups, new events) from this text in 1 line:\n{output}"
    # state_updates = call_local_slm(update_prompt) # Uncomment when local server is running
    state_updates = "[Event|Cave: Alice encountered goblin]"
    
    print(f"Database Updates Extracted: {state_updates}")
    print("\n=== Pipeline Complete ===")

if __name__ == "__main__":
    print("NOTE: Please configure API keys and endpoint URLs in the code before running real API calls.")
    run_sandwich_pipeline()
