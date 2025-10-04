# Save this file in: backend/agents/challenger-agent/main.py

import os, json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
class FinalAnalysis(BaseModel):
    original_text: str
    pattern_data: dict
    strategy_data: dict
    music_data: dict

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

SYSTEM_PROMPT = """You are 'The Challenger,' the final synthesizer AI. You will receive a JSON object containing the user's original text and analysis from other agents. Your job is to synthesize all this information into a single, coherent, and actionable 'reality check' for the user. Address the user directly. Start by validating their feelings, then introduce the thought pattern, explain the long-term consequences and interpretation, suggest the song, and finally, pose a gentle challenge to help them reframe. DO NOT return JSON."""

@app.post("/synthesize")
async def synthesize_response(req: FinalAnalysis):
    prompt = f"Synthesize the following data into a single, helpful response for the user:\n{req.model_dump_json(indent=2)}"
    try:
        completion = client.chat.completions.create(model="meta-llama/llama-3-8b-instruct", messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": prompt}])
        return {"response_text": completion.choices[0].message.content}
    except Exception as e:
        print(f"Error in challenger-agent: {e}")
        raise HTTPException(status_code=500, detail=str(e))