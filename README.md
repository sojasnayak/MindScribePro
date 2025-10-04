# MindScribe Pro

> Your AI-powered partner for deep reflection and growth. MindScribe Pro is an intelligent journaling app that uses a collaborative team of AI agents to provide deep, psychological insights based on your thoughts.

---

![MindScribe Pro Screenshot](link-to-your-screenshot.png)
*(Replace the link above with a screenshot of your running application!)*

## Inspiration

Journaling is a powerful tool, but sometimes we get stuck in our own thought patterns. It's hard to see the forest for the trees. We were inspired to build MindScribe Pro to solve this problem. What if your journal could do more than just store your thoughts? What if it could act as an intelligent partner, providing you with a fresh perspective, challenging your assumptions, and helping you understand the hidden psychological meanings behind your feelings?

## What It Does

MindScribe Pro transforms a simple journal entry into a multi-layered, insightful reflection. Here's how it works:

* **Analyzes Your Thoughts:** You write down what's on your mind, and our system kicks off a sophisticated analysis.
* **Identifies Thought Patterns:** A specialized AI agent, **"The Reflector,"** analyzes your entry to identify common cognitive distortions based on principles from Cognitive Behavioral Therapy (CBT).
* **Reveals Long-Term Consequences:** If a pattern is found, **"The Strategist"** agent reveals the potential long-term, real-world consequences of that pattern, providing a powerful "reality check."
* **Suggests a Mood-Matching Song:** A **"Music Sommelier"** agent analyzes the mood of your entry and suggests a fitting song to complement your reflective state.
* **Delivers a Synthesized Insight:** Finally, **"The Challenger"** agent takes all of this information and synthesizes it into a single, coherent, and actionable piece of feedback that is both empathetic and empowering.

## How We Built It

MindScribe Pro is built as a modern microservice application, orchestrated with Docker to ensure scalability and separation of concerns.

### Tech Stack

| Component         | Technology / Framework       | Purpose                                                    |
| ----------------- | ---------------------------- | ---------------------------------------------------------- |
| **Frontend** | React.js (with Vite) & Axios | To build a fast, modern, and interactive user interface.   |
| **Backend Agents**| Python & FastAPI             | To create our four distinct, high-performance AI services. |
| **Gateway** | NGINX                        | To act as a reverse proxy and the single entry point.      |
| **Containerization**| Docker & Docker Compose      | To package and manage all our services cohesively.       |
| **AI Models** | OpenRouter, MistralAI        | To power the intelligence of our specialized agents.       |

### The AI Agent Assembly Line

Our unique architecture is what makes MindScribe Pro so powerful. Instead of relying on a single AI, we use a multi-step workflow orchestrated by our gateway:

**User Entry → Reflector → Strategist → Music Agent → Challenger → Final Insight**

This "assembly line" approach allows each agent to perform its specialized task, building on the analysis of the previous agents to create a final output that is far richer and more insightful than a single AI could ever achieve.

## Sponsor Technology Showcase: Docker MCP Gateway

For the Docker prize, we focused on the **most creative usage** of the Docker MCP Gateway. We transformed it from a simple router into the **intelligent "brain" and "factory floor manager"** of our entire application.

* **Standard Use:** Most applications use a gateway as a simple, stateless traffic cop.
* **Our Creative Use:** In MindScribe Pro, the gateway is an **AI Process Manager**. It orchestrates the entire multi-step "assembly line" of analysis. It receives the initial request and then intelligently directs the flow of data between our specialized AI agents, managing the state of the analysis from raw text to a final, synthesized insight. This stateful workflow management is what enables our agents to collaborate, making the gateway a fundamental and creative part of the application's core logic.

## Getting Started (Running Locally)

Follow these steps to get MindScribe Pro running on your machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[sojasnayak]/mindscribepro-v2.git
    cd mindscribepro-v2
    ```

2.  **Create your environment file:**
    Create a `.env` file in the root of the project. Add your OpenRouter API key to it:
    ```
    OPENROUTER_API_KEY=sk-or-v1-your-key-here
    ```

3.  **Build and run the application:**
    This single command will build all the services and start the application.
    ```bash
    docker-compose up --build
    ```

4.  **Open the application:**
    * The frontend will be available at **`http://localhost:5173`**.
    * The gateway is listening at `http://localhost:9999`.

## Future Work

* **Adaptive Personality Gateway:** Allow the gateway to learn from user feedback (e.g., "This was too harsh") and adapt its routing choices over time.
* **More Psychological Models:** Integrate agents based on other frameworks, like Stoicism or Positive Psychology.
* **Long-Term Memory:** Implement a vector database to give the agents a "memory" of the user's past entries, allowing them to spot patterns over weeks or months.

## Team

* [Sojas Nayak
   Somya Tambi]