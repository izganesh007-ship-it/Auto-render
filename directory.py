import os
import requests

# --- CONFIGURATION ---
NV_API_KEY = "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" # <--- MAKE SURE TO PUT YOUR REAL KEY HERE
MODEL_NAME = "mistralai/mistral-small-4-119b-2603"
URL = "https://integrate.api.nvidia.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {NV_API_KEY}",
    "Content-Type": "application/json"
}

# --- THE PROMPT ---
prompt = """
Write a high-end Remotion video file using React.
Target: src/remotion/index.ts
Required: Export a composition with the ID "DynamicComp".

Instructions:
1. Use 'public/voiceover.mp3' for audio.
2. Implement 'Ken Burns' effect (Scale 1.0 to 1.15) for images in 'public/assets/'.
3. Use a navy blue (#000080) and gold (#D4AF37) color palette.
4. The main component MUST be exported as: 
   export const RemotionVideo = () => { 
     return <Composition id="DynamicComp" ... />; 
   };
5. Return ONLY the code. No talking.
"""

payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.1,
    "max_tokens": 8192,
    "extra_body": { "reasoning_effort": "high" }
}

print(f"🚀 Consulting Mistral Small 4...")

try:
    response = requests.post(URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        video_code = data['choices'][0]['message']['content']
        video_code = video_code.replace("```tsx", "").replace("```typescript", "").replace("```", "")
        
        # FIX: Save to the correct location for the GitHub Action
        os.makedirs("src/remotion", exist_ok=True)
        with open("src/remotion/index.ts", "w", encoding="utf-8") as f:
            f.write(video_code.strip())
        print("✅ Documentary code generated in src/remotion/index.ts!")
    else:
        print(f"❌ API Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"⚠️ Error: {e}")