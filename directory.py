import os
import requests

# --- CONFIGURATION ---
NV_API_KEY = "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" 
MODEL_NAME = "mistralai/mistral-small-4-119b-2603"
URL = "https://integrate.api.nvidia.com/v1/chat/completions"

headers = {"Authorization": f"Bearer {NV_API_KEY}", "Content-Type": "application/json"}

# I've simplified the styling instructions to prevent syntax errors
prompt = """
Write a single-file Remotion video in TypeScript (src/remotion/index.ts).
Required Imports: { AbsoluteFill, Audio, Img, interpolate, spring, useCurrentFrame, useVideoConfig, registerRoot, Composition, staticFile }.

Logic:
1. Create a 'MainScene' component. 
2. Use a navy blue background: <AbsoluteFill style={{backgroundColor: '#000080', justifyContent: 'center', alignItems: 'center'}}>
3. Display images from 'public/assets/' one by one using <img> tags.
4. Add <Audio src={staticFile('voiceover.mp3')} />.
5. Duration: 750 frames.
6. Export 'RemotionRoot' with <Composition id="DynamicComp" component={MainScene} durationInFrames={750} fps={30} width={1920} height={1080} />.
7. Call registerRoot(RemotionRoot).

IMPORTANT: Ensure all JSX tags are closed correctly. Do not use complex CSS-in-JS libraries. Use standard React 'style' objects. Return ONLY code.
"""

payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.1, # Lower temperature = more stable code
    "extra_body": {"reasoning_effort": "high"}
}

print("🚀 Fixing syntax and regenerating 25s preview...")
try:
    response = requests.post(URL, headers=headers, json=payload)
    if response.status_code == 200:
        video_code = response.json()['choices'][0]['message']['content']
        
        # Clean up tags
        for tag in ["```tsx", "```typescript", "```"]:
            video_code = video_code.replace(tag, "")
        
        os.makedirs("src/remotion", exist_ok=True)
        with open("src/remotion/index.ts", "w", encoding="utf-8") as f:
            f.write(video_code.strip())
        print("✅ Clean code generated in src/remotion/index.ts!")
    else:
        print(f"❌ Error: {response.text}")
except Exception as e:
    print(f"⚠️ Connection Error: {e}")