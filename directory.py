import os
import requests

# --- CONFIGURATION ---
NV_API_KEY = "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" 
MODEL_NAME = "mistralai/mistral-small-4-119b-2603"
URL = "https://integrate.api.nvidia.com/v1/chat/completions"

headers = {"Authorization": f"Bearer {NV_API_KEY}", "Content-Type": "application/json"}

prompt = """
Write a complete Remotion video in TypeScript for a 25-second preview.
File: src/remotion/index.ts

Requirements:
1. Imports: { AbsoluteFill, Audio, Img, interpolate, spring, useCurrentFrame, useVideoConfig, registerRoot, Composition, staticFile }.
2. Duration: Exactly 750 frames (25 seconds at 30fps).
3. Media: 
   - Use staticFile('voiceover.mp3') for Audio.
   - Loop through images in 'public/assets/'.
4. Export 'RemotionRoot' with <Composition id="DynamicComp" component={MainScene} durationInFrames={750} fps={30} width={1920} height={1080} />.
5. Call registerRoot(RemotionRoot) at the end.
6. Return ONLY code. No markdown.
"""

payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.2,
    "extra_body": {"reasoning_effort": "high"}
}

print("🚀 Generating 25-second test edit...")
try:
    response = requests.post(URL, headers=headers, json=payload)
    if response.status_code == 200:
        video_code = response.json()['choices'][0]['message']['content']
        
        # Clean up any markdown code blocks
        for tag in ["```tsx", "```typescript", "```"]:
            video_code = video_code.replace(tag, "")
        
        os.makedirs("src/remotion", exist_ok=True)
        with open("src/remotion/index.ts", "w", encoding="utf-8") as f:
            f.write(video_code.strip())
        print("✅ 25-second logic generated in src/remotion/index.ts!")
    else:
        print(f"❌ Error: {response.text}")
except Exception as e:
    print(f"⚠️ Connection Error: {e}")