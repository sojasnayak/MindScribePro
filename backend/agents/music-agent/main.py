# Save this file in: backend/agents/music-agent/main.py

import os, json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
class Entry(BaseModel): text: str

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

SYSTEM_PROMPT = """You are a music sommelier AI. Analyze the mood of the user's text and suggest a specific song that fits the mood. Respond ONLY with a valid JSON object with this exact structure: {"mood": "The primary mood identified.", "song_suggestion": "Artist - Song Name"}"""

@app.post("/analyze")
async def analyze_entry(entry: Entry):
    try:
        completion = client.chat.completions.create(model="google/gemini-flash-1.5", messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": entry.text}])
        response_text = completion.choices[0].message.content
        return json.loads(response_text)
    except Exception as e:
        print(f"Error in music-agent: {e}")
        raise HTTPException(status_code=500, detail=str(e))