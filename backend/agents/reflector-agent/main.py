# Save this in: backend/agents/reflector-agent/main.py

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
        completion = client.chat.completions.create(model="mistralai/mistral-7b-instruct", messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": entry.text}])
        response_text = completion.choices[0].message.content
        
        # --- BULLETPROOF JSON PARSING ---
        # Find the start and end of the JSON object in the AI's response
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1
        json_string = response_text[json_start:json_end]
        
        return json.loads(json_string)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in reflector-agent: {e}")