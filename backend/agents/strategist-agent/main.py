# Save this file in: backend/agents/strategist-agent/main.py

import os, json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
class AnalysisRequest(BaseModel):
    original_text: str
    pattern_found: str

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

SYSTEM_PROMPT = """You are 'The Strategist,' a psychological analyst AI. You will receive a cognitive distortion pattern and the user's original text. Your job is to determine the potential long-term negative consequences of this pattern and interpret a common hidden reason for it. Respond ONLY with a valid JSON object with this exact structure: {"consequences": "Your analysis of consequences.", "interpretation": "Your interpretation of the hidden meaning."}"""

@app.post("/analyze")
async def analyze_entry(req: AnalysisRequest):
    prompt = f"Pattern: {req.pattern_found}\nText: {req.original_text}"
    try:
        completion = client.chat.completions.create(model="google/gemini-flash-1.5", messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": prompt}])
        response_text = completion.choices[0].message.content
        return json.loads(response_text)
    except Exception as e:
        print(f"Error in strategist-agent: {e}")
        raise HTTPException(status_code=500, detail=str(e))