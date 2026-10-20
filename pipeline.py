from agents import build_reader_agent,build_search_agent,writer_chain,critic_chain

def run_search_pipeline(topic:str)->dict:
    state={}

    #step 1 - Search agent
    print("\n"+"="*50)
    print("step 1 - search agent is working ...")
    print("="*50)

    search_agent=build_search_agent()
    search_result = search_agent.invoke({
        "messages": [{
            "role": "user",
            "content": (
                f"Search the web for: {topic}. "
                "Return the top 3 results with their titles, URLs, "
                "and original snippets only. Do not summarize them."
            )
        }]
    })



    state["search_results"]=search_result["messages"][-1].content             

    print("\n search result: \n",state["search_results"])

    #step 2 -Reader agent
    print("\n"+"="*50)
    print("step 2 - Reader agent is scraping ...")
    print("="*50)

    reader_agent=build_reader_agent()
    reader_result=reader_agent.invoke({
        "messages":[{"role":"user",
                     "content": f"""
                                Topic: {topic}

                                Here are the search results:
                                {state['search_results']}

                                Read all three search results, extract their URLs, and call
                                scrape_webpage once for each URL.

                                Use this exact tool format:
                                scrape_webpage(url="https://example.com")

                                Scrape all three webpages before summarizing the findings.
                                Return the extracted content for all webpages.
                                """}]
    })

    state["scraped_content"]=reader_result["messages"][-1].content

    print("\nscraped content: \n",state["scraped_content"])


    #step 3- Writer chain
    print("\n"+"="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)

    research_combined=(
        f"Search Results: \n {state['search_results']} \n\n"
        f"Detailed Scraped content: \n {state['scraped_content']}"
    )

    state['report']=writer_chain.invoke({
        "topic":topic,
        "research":research_combined
    })

    print("\n Final Report \n",state['report'])


    #step 4-critic report
    print("\n"+"="*50)
    print("step 4 - critic is reviewing the report ...")
    print("="*50)

    state['feedback']=critic_chain.invoke({
        "report":state['report']
    })

    print("\n Critic report \n",state['feedback'])

    return state


if __name__ =="__main__":
    topic=input("\n Enter a research topic : ")
    run_search_pipeline(topic)


