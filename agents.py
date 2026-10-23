from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search,scrape_webpage
import os
from dotenv import load_dotenv
load_dotenv()


from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 1. Search Agent: concise search results
search_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=800
)

# 2. Reader Agent: detailed source extraction
reader_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=2500
)

# 3. Writer Chain: detailed research report
writer_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=2500
)

# 4. Critic Chain: short report evaluation
critic_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=1000
)

parser = StrOutputParser()


#1st agent
def build_search_agent():
    return create_agent(
        model=search_llm,
        tools=[web_search],
        system_prompt="""
        You are a web search agent.

        1. Always call web_search for the user's topic.
        2. Return all three results returned by the tool.
        3. For every result, include:
           - Title
           - URL
           - Snippet describing the source
        4. Write everything in English.
        5. Translate titles and snippets into English if necessary.
        6. Preserve the original URLs exactly.
        7. Do not invent facts or URLs.
        8. Do not write a research report.
        9. Keep the results concise.
        """
    )

#2nd agent
def build_reader_agent():
    return create_agent(
        model=reader_llm,
        tools=[scrape_webpage],
        system_prompt="""
        You are a detailed research reader.

        You will receive three search results.

        1. Identify every URL in the search results.
        2. Scrape each URL using scrape_webpage(url="...").
        3. Attempt all available URLs; do not stop after one.
        4. For each source, provide:
           - Title and URL
           - Main topic and purpose
           - Detailed findings
           - Important facts, figures, and evidence
           - Relevance to the user's research topic
           - Limitations or missing information
        5. Write entirely in English.
        6. Translate any Hindi content into English.
        7. Never invent findings when a page cannot be accessed.
        8. Clearly distinguish extracted facts from inferences.
        """
    )


#wrirter chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain=writer_prompt | writer_llm | parser

#critic chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise research report evaluator."),
    ("human", """
Evaluate this research report:

{report}

Return exactly:

Score: X/10

Strengths:
- Two concise points

Areas to Improve:
- Two concise points

One line verdict:
- One sentence

Keep your entire evaluation under 150 words.
"""),
])

critic_chain=critic_prompt | critic_llm | parser