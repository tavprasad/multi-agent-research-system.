# 🤖 Multi-Agent Research System

An AI-powered research application that uses multiple LLM agents, web search, and webpage content extraction to gather information and generate structured research reports.

🌐 **Live Demo:** [Multi-Agent Research System](https://multi-agent-research-system-6sbtm78hsculvjmy2au5fb.streamlit.app/)

## 📌 Project Overview

Researching a topic online often requires searching multiple sources, reading webpages, extracting relevant information, and organizing findings into a useful report.

The **Multi-Agent Research System** aims to simplify this process by combining Large Language Models (LLMs), web search, and webpage scraping in an interactive application.

The system uses specialized AI agents and tools to search for relevant information, analyze webpage content, and assist in generating research results through a Streamlit interface.

The project includes:

✅ Multi-Agent AI Architecture  
✅ LLM Integration using Groq API  
✅ Web Search using Tavily API  
✅ Webpage Content Extraction using BeautifulSoup  
✅ Tool Calling and Agent Workflows  
✅ Streamlit Interactive Frontend  
✅ Environment Variable Management for API Keys  

## 🚀 Features

### 🤖 Multi-Agent System

- Multiple AI agents designed for research-related tasks.
- LLM-powered reasoning and information processing.
- Agent interaction with external tools.
- Automated research workflow.

### 🔎 Web Search and Information Retrieval

- Search for relevant information using the Tavily API.
- Retrieve useful webpages related to a research query.
- Identify relevant sources for further analysis.

### 🌐 Webpage Content Extraction

- Extract webpage text using BeautifulSoup.
- Retrieve readable content from supported URLs.
- Provide webpage content to the AI agents for analysis.

### 🧠 LLM-Powered Research

- Process user research queries.
- Analyze retrieved information using language models.
- Generate organized research results.
- Combine web search and content extraction in a single workflow.

### 🎨 Interactive Web Application

- User-friendly Streamlit interface.
- Enter research queries directly through the application.
- View research results without running commands manually.
- Access the application through a live deployment.

## 🏗️ System Architecture

The application follows a tool-assisted multi-agent research workflow.

```text
              User Research Query
                      |
                      ▼
             Streamlit Frontend
                      |
                      ▼
             Research Workflow
                      |
             ┌────────┴────────┐
             ▼                 ▼
        Research Agent    Analysis Agent
             |                 |
             ▼                 ▼
         Tavily API       BeautifulSoup
         Web Search      Webpage Extraction
             |                 |
             └────────┬────────┘
                      ▼
              Research Findings
                      |
                      ▼
              Final Research Output
                      |
                      ▼
              Streamlit Interface
```

*Note: This diagram represents the conceptual workflow. The exact execution order depends on the implementation of the agents and tools in the codebase.*

## 🛠️ Tech Stack

### Artificial Intelligence & LLMs

- 🧠 Large Language Models (LLMs)
- ⚡ Groq API
- 🔗 LangChain
- 🤖 AI Agents and Tool Calling

### Search & Web Scraping

- 🔎 Tavily API
- 🌐 BeautifulSoup
- 📡 Requests

### Frontend Development

- 🎨 Streamlit

### Programming & Configuration

- 🐍 Python
- 🔑 Python-dotenv
- 📦 pip
- 🔐 Environment Variables

## 🔄 Research Workflow

1. **User Input:** The user enters a research topic through the Streamlit application.
2. **Web Search:** The research workflow uses Tavily to discover relevant webpages.
3. **Content Extraction:** BeautifulSoup extracts readable content from accessible webpages.
4. **Agent Analysis:** The AI agents process the retrieved information according to their assigned responsibilities.
5. **Research Output:** The application presents the generated research results to the user.

## 📂 Project Structure

```text
Multi-Agent-Research-System/
│
├── streamlit_app.py       # Streamlit Frontend
├── agents.py              # Agent Definitions (if applicable)
├── tools.py               # Search and Scraping Tools (if applicable)
├── requirements.txt       # Python Dependencies
├── .env                   # Local API Keys (not committed)
├── .gitignore             # Files Excluded from Git
└── README.md              # Project Documentation
```

*The structure above is illustrative. Adjust the filenames to match the actual files in your repository.*

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the repository URL with your actual GitHub repository URL.

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholders with your own API keys.

**Security:** Never commit your `.env` file or expose your API keys in source code. Keep `.env` in `.gitignore`.

### 5️⃣ Run the Application

```bash
streamlit run streamlit_app.py
```

Open the local application at:

http://localhost:8501

## 🌐 Live Application

Try the deployed application here:

**[Launch Multi-Agent Research System](https://multi-agent-research-system-6sbtm78hsculvjmy2au5fb.streamlit.app/)**

The application is hosted on Streamlit Community Cloud.

## 🎯 Key Learnings

Through this project, I gained practical experience in:

- Generative AI application development.
- Multi-agent system design.
- LLM integration using Groq.
- Tool calling and agent workflows with LangChain.
- Web search using the Tavily API.
- Web scraping and content extraction using BeautifulSoup.
- Prompt engineering and information processing.
- Building interactive applications with Streamlit.
- Managing API keys and environment variables.
- Deploying a Python application to the cloud.

## 🔮 Future Improvements

- 🔗 Advanced agent orchestration using LangGraph.
- 📚 Retrieval-Augmented Generation (RAG).
- 📑 Research report export to PDF and Markdown.
- 🔍 Source citations and reference management.
- 🗄️ PostgreSQL integration for research history.
- 📊 Research quality evaluation and source relevance scoring.
- 🐳 Docker containerization.
- ☁️ Deployment automation using GitHub Actions.
- 🧠 Improved error handling, retries, and rate-limit management.

## ⚠️ Limitations

- Research quality depends on the relevance and reliability of retrieved sources.
- Some webpages may block automated requests or restrict content extraction.
- LLM API rate limits and service availability may affect execution.
- Generated findings should be verified against the original sources.

## 👨‍💻 Author

**Tavprasad Singh**

- Aspiring AI/ML Engineer
- Generative AI and Agentic AI Enthusiast
- Interested in building intelligent applications using LLMs and AI agents

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

Feedback and suggestions for improvement are always welcome.
