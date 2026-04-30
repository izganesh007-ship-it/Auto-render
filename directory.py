import os
import requests

# --- CONFIGURATION ---
NV_API_KEY = "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" 
MODEL_NAME = "mistralai/mistral-small-4-119b-2603"
URL = "https://integrate.api.nvidia.com/v1/chat/completions"

headers = {"Authorization": f"Bearer {NV_API_KEY}", "Content-Type": "application/json"}

prompt = """
Write a single-file Remotion video in TypeScript (src/remotion/index.ts).
Required Imports: { AbsoluteFill, Audio, Img, useCurrentFrame, registerRoot, Composition, staticFile }.

Logic:
1. Composition ID: "DynamicComp", Duration: 750 frames.
2. Background: Navy blue (#000080).
3. Images: Use an array: const images = ['image1.jfif', 'image2.jfif', 'image3.jfif', 'image4.jfif', 'image5.jfif'];
4. Audio: Use staticFile('voiceover.mp3').
5. Use double curly braces for styles: style={{ backgroundColor: '#000080' }}.

Return ONLY the raw TypeScript code. No markdown backticks.
"""

payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.1
}

print("🚀 Regenerating...")
try:
    response = requests.post(URL, headers=headers, json=payload)
    if response.status_code == 200:
        video_code = response.json()['choices'][0]['message']['content']
        
        # Safer cleanup loop
        for junk in ["```tsx", "```typescript", "```"]:
            video_code = video_code.replace(junk, "")
        
        os.makedirs("src/remotion", exist_ok=True)
        with open("src/remotion/index.ts", "w", encoding="utf-8") as f:
            f.write(video_code.strip())
        print("✅ Success! src/remotion/index.ts updated.")
    else:
        print(f"❌ Error: {response.status_code}")
except Exception as e:
    print(f"⚠️ Error: {e}")