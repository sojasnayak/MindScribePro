// Save this file in: frontend/src/App.jsx

import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

// Configure the base URL for our gateway
const apiClient = axios.create({
  baseURL: 'http://localhost:9999/api',
});

function App() {
  const [entry, setEntry] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleAnalyze = async () => {
    if (!entry.trim()) {
      setError("Please write something in your journal first.");
      return;
    }

    setIsLoading(true);
    setResponse('');
    setError('');

    try {
      // --- THE AI ASSEMBLY LINE ---
      
      // Step 1: Call the Reflector and Music agents in parallel
      const [reflectorRes, musicRes] = await Promise.all([
        apiClient.post('/reflector', { text: entry }),
        apiClient.post('/music', { text: entry })
      ]);
      const patternData = reflectorRes.data;
      const musicData = musicRes.data;

      // Step 2: If a pattern was found, call the Strategist
      let strategyData = {};
      if (patternData.pattern_found) {
        const strategistRes = await apiClient.post('/strategist', {
          original_text: entry,
          pattern_found: patternData.pattern_found
        });
        strategyData = strategistRes.data;
      }

      // Step 3: Bundle everything and call the final Challenger for synthesis
      const finalPayload = {
        original_text: entry,
        pattern_data: patternData,
        strategy_data: strategyData,
        music_data: musicData
      };

      const challengerRes = await apiClient.post('/challenger', finalPayload);
      
      // The final, synthesized response is ready!
      setResponse(challengerRes.data.response_text);

    } catch (err) {
      console.error("Full error object:", err);
      const errorMessage = err.response ? JSON.stringify(err.response.data) : err.message;
      setError(`An error occurred in the analysis pipeline: ${errorMessage}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header>
        <h1>MindScribe Pro</h1>
        <p>Your AI partner for deep reflection and growth.</p>
      </header>

      <div className="journal-entry">
        <textarea
          value={entry}
          onChange={(e) => setEntry(e.target.value)}
          placeholder="What's on your mind today?"
        />
      </div>

      <button className="analyze-button" onClick={handleAnalyze} disabled={isLoading}>
        {isLoading ? 'Analyzing...' : "Get My Insight"}
      </button>

      {isLoading && <div className="loading-spinner"></div>}
      {error && <p className="error-message">{error}</p>}

      {response && (
        <div className="response-container">
          <div className="response-box">
            <h3>Your Insightful Reflection</h3>
            {/* Using <pre> tag to respect whitespace and newlines from the AI's response */}
            <pre style={{ whiteSpace: 'pre-wrap', fontFamily: 'inherit', fontSize: '1.1rem' }}>{response}</pre>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;