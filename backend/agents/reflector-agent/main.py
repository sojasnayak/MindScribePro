# Save this file in: backend/agents/reflector-agent/main.py

import os, json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
class Entry(BaseModel): text: str

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

SYSTEM_PROMPT = """You are 'The Reflector,' a CBT-based AI. Your only job is to analyze text and identify a single, primary cognitive distortion. Respond ONLY with a valid JSON object with this exact structure: {"pattern_found": "Name of Pattern" or null, "pattern_explanation": "A brief, one-sentence explanation of the pattern."}"""

@app.post("/analyze")
async def analyze_entry(entry: Entry):
    try:
        completion = client.chat.completions.create(model="cerebras/cerebras-gpt-13b", messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": entry.text}])
        response_text = completion.choices[0].message.content
        return json.loads(response_text)
    except Exception as e:
        print(f"Error in reflector-agent: {e}")
        raise HTTPException(status_code=500, detail=str(e))