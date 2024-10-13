# Hey All,

My interactions with AI are a little different, as I have experimented with it in the past. I have experimented with AI Tools/Agents for a few years now and have a few of my own that I've built, localized, and trained.

The files I attached were made in Notepad++ so it takes a little bit longer to open them. The summary file takes about 30-40 seconds. Please be patient with the files opening, as I feel like it makes my discussion post make more sense.

## Topic 2: Explore this week's AI Playground and share your experience with the class.

### Which tool(s) did you use?
Claude 3.5 sonnet

### What are some prompt(s) that you used?
I used the anthropic prompt guidelines to create an effective prompt to tailor my chat with Claude to provide specific information about "Python Career Opportunities." I will include my initial prompt below for those interested in reading as well as a list of prompt commands to tailor the AI agent chat and a schema that I typically use for creating prompts.

The prompts I used after tailoring Claude were:
- %USER%["What career options are available to me?"]
- %USER%["Which of these job opportunities have entry level positions?"]
- %USER%["Provide a list of resume skills that will assist in getting these jobs."]
- %USER%["Provide a template for a resume to these entry level positions."]
- %USER%["Suggest projects to complete for a portfolio that relate to these entry level positions."]
- %USER%["What are the current statistics of availability and projected growth for these entry level positions?"]
- %USER%["Give this data to me in a graphical format that includes an educated guess on growth and availability for the next 2 years given trends as of April, 2024."]

### Was the information received useful?
Yes.

### Did it help you understand this week's topics?
Yes.

### Was the information at an appropriate level that you understood?
Yes.

### Was the information accurate?
Yes. Accurate to the extent of Claude's knowledge cut off (April, 2024).

### Was the information complete?
Yes.

### Did you use the tool to suggest challenge projects and if so did you try them?
Yes. I did not try the projects but will likely include 1 or 2 of them in my current portfolio.

### Did you use the tool to quiz yourself and if so did it help you focus on areas that you would like to improve in?
No.

### Share your thoughts with the class. Would you recommend using AI tools for learning? Were some tools better than others? Do you have any tips for refining prompts?
Yes, with caveats. AI tools *can* be effective at assisting in learning. But the effectiveness is entirely dependent upon the %USER%. The tool, regardless of which one (Copilot, Claude, GPT, Perplexity), will begin its interaction with you as if it were a new employee with no experience. If you do not provide effective guidelines for the AI tool to operate within and adhere to, then it will create them for itself.

There are obvious issues that come from the tool generating its own operating parameters, the biggest of which is AI Hallucination. If you have not implemented effective %FALLBACK% and %EXCEPTION% parameters, then the tool, if in a situation where it does not have an effective knowledge base to solve a query, will "hallucinate" a solution that is equivalent to someone guessing about a topic they have no prior knowledge of.

Here is a description of this directly from Copilot:
- %USER%["explain ai hallucination"]
- %RESPONSE%["AI hallucination occurs when an AI model generates information that is not grounded in the data it was trained on. Essentially, the AI "hallucinates" details or facts that aren't true or verifiable. This can happen for various reasons, like the AI trying to fill in gaps, misinterpreting ambiguous inputs, or combining unrelated pieces of information in an incorrect way. For instance, if you ask an AI about a specific event that it doesn't have accurate data on, it might fabricate details based on similar events or contexts. While the AI's response might seem plausible, it's not reliable. This is why verifying information from trusted sources is crucial, even when it comes from an AI."]

I have attached 4 documents. The first is the prompt I used to get career information. The second is a list of AI Tool Commands for tailoring a prompt. The third document is a generic schema I use for creating prompts; some tools have extra commands you can look up, but this schema covers the generic ones that work across all AI Tools/Agents. The last document is my conversation with Claude. At the end of the conversation, you will see an example of me using prompt commands to make Claude do something it refused to do twice. Below all of that is the graphical representation Claude generated of the entry-level job market trends.

Hope you all enjoy reading through this and that it can be informative to you.
