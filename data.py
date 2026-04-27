LESSONS = [
    {
        "num": 1,
        "title": "Tokens 101",
        "subtitle": "What are tokens and why do they matter?",
        "sections": [
            {
                "heading": "What is a token?",
                "body": "A token is a basic unit of data \u2014 a piece of a word, a full word, or punctuation \u2014 that serves as either input or output to a large language model. LLMs don't read characters; they read tokens."
            },
            {
                "heading": "How does token optimization work?",
                "body": "Token optimization strategies are techniques that reduce unnecessary token consumption without changing the nature or quality of the work being done. Think of it as trimming the fat from your prompts."
            },
            {
                "heading": "How much do we have with Claude Pro?",
                "body": "Claude Pro users get approximately 44,000 tokens per 5-hour usage window. In practice, this allows for roughly 10\u201340 prompts in Claude Code \u2014 depending on how heavy each prompt is. Running out mid-project is a real problem."
            }
        ],
        "meme_caption": "When you realize you burned 40,000 tokens asking Claude to refactor your README...",
        "meme_alt": "Person realizing the mistake they just made"
    },
    {
        "num": 2,
        "title": "Right Model, Right Job",
        "subtitle": "Haiku vs. Sonnet vs. Opus \u2014 don't pay for what you don't need",
        "sections": [
            {
                "heading": "Claude's model tiers",
                "body": "Claude has three main tiers: Haiku (fast, cheap, great for simple tasks), Sonnet (balanced, the everyday workhorse), and Opus (most powerful, most token-expensive). Using Opus for a README is like hiring a brain surgeon to make toast."
            },
            {
                "heading": "When to use Haiku",
                "body": "Use Haiku for quick, well-defined tasks: generating boilerplate, writing short documentation, formatting code, simple file ops. It consumes far fewer tokens and returns answers faster."
            },
            {
                "heading": "When to use Sonnet or Opus",
                "body": "Use Sonnet or Opus when reasoning depth matters: debugging complex systems, designing architecture, working across large codebases. Save Opus for tasks where you genuinely need it."
            }
        ],
        "meme_caption": "Using Claude Opus to generate a .gitignore file. Bro really called in a consultant for a sticky note.",
        "meme_alt": "Overpowered solution to a trivial problem"
    },
    {
        "num": 3,
        "title": ".claudeignore & /compact",
        "subtitle": "Control what Claude sees \u2014 and what it remembers",
        "sections": [
            {
                "heading": "What is a .claudeignore file?",
                "body": "A .claudeignore file sits in your project root and tells Claude which files and directories to exclude from its context window. Similar to .gitignore, it prevents Claude from reading node_modules, build artifacts, test fixtures, or any other noise that inflates your token count without helping Claude do its job."
            },
            {
                "heading": "Where does it go?",
                "body": "Always place .claudeignore in your project root directory \u2014 the same level as your .gitignore. Claude scans for it there automatically. Putting it anywhere else will cause it to be ignored."
            },
            {
                "heading": "/compact and /clear commands",
                "body": "Claude reads your entire context window on every response. /clear wipes it completely \u2014 great when you're starting a new task and don't need prior context. /compact summarizes the conversation into a compressed form, preserving important instructions while cutting token overhead."
            }
        ],
        "meme_caption": "Claude reading your node_modules before answering a CSS question.",
        "meme_alt": "Someone reading a phonebook to answer a simple question"
    },
    {
        "num": 4,
        "title": "Timing Your Chats",
        "subtitle": "Anthropic gives you more tokens when the grid is quiet",
        "sections": [
            {
                "heading": "Why does timing matter?",
                "body": "Why does timing matter?\nDuring peak hours on weekdays, user demand far exceeds available GPU capacity, forcing Anthropic to constrain usage to maintain service stability. During off-peak hours and weekends, server load is lighter, so Anthropic can offer more generous limits without risking system overload."
            },
            {
                "heading": "When are peak hours?",
                "body": "Peak hours are weekdays from 5 AM to 11 AM PT (1 PM \u2013 7 PM GMT). During these hours, usage limits are tighter because grid demand is highest and model inference costs more."
            },
            {
                "heading": "The off-peak advantage",
                "body": "Outside of peak hours and on weekends, Anthropic often doubles usage limits. If your workflow is flexible, doing your heavy Claude Code sessions at night or on weekends can effectively double your available token budget \u2014 for free."
            }
        ],
        "meme_caption": "Using Claude Opus at 2pm on a Tuesday. This is not going to end well.",
        "meme_alt": "Someone walking confidently toward inevitable disaster"
    }
]

QUIZ_QUESTIONS = [
    {
        "num": 1,
        "question": "You need to generate a README.md for a small database project you just finished. Which Claude model is most appropriate?",
        "type": "single",  # one correct answer
        "options": [
            "Claude Haiku",
            "Claude Sonnet",
            "Claude Opus",
            "It doesn't matter \u2014 all models produce identical output"
        ],
        "correct": [0],  # index of correct answer(s)
        "explanation": "Haiku is ideal for well-defined, low-complexity tasks like generating documentation for a small project. Using Sonnet or Opus wastes tokens on unnecessary reasoning depth."
    },
    {
        "num": 2,
        "question": "You're deploying a backend with multiple microservices, debugging cross-service authentication failures, and working across 15+ files. Which model should you use?",
        "type": "single",
        "options": [
            "Claude Haiku \u2014 it's faster",
            "Claude Sonnet or Opus \u2014 complex reasoning required",
            "Any model, just use /compact first",
            "None \u2014 use GPT-4 instead"
        ],
        "correct": [1],
        "explanation": "Complex, multi-file debugging with architectural implications is exactly when Sonnet or Opus earns its cost. The reasoning depth matters here."
    },
    {
        "num": 3,
        "question": "Where should you place your .claudeignore file?",
        "type": "single",
        "options": [
            "In the .git folder",
            "In the same folder as your .env file",
            "In the project root directory",
            "Claude finds it automatically anywhere in the project"
        ],
        "correct": [2],
        "explanation": "The .claudeignore file must be in the project root \u2014 the same level as your .gitignore. Claude only scans for it there."
    },
    {
        "num": 4,
        "question": "When should you use /clear? Select ALL that apply.",
        "type": "multi",  # multiple correct answers possible
        "options": [
            "When starting a completely new, unrelated task",
            "When you want to erase bugs from your code",
            "When your context window is full of irrelevant earlier conversation",
            "When you want Claude to use a smaller model"
        ],
        "correct": [0, 2],
        "explanation": "/clear wipes the context window. Use it when switching tasks or when accumulated context is doing more harm than good. It does not affect your code or model selection."
    },
    {
        "num": 5,
        "question": "When are Anthropic's peak usage hours (when limits are tightest)?",
        "type": "single",
        "options": [
            "9 AM \u2013 5 PM Monday through Saturday",
            "Weekdays 5 AM \u2013 11 AM PT (1 PM \u2013 7 PM GMT)",
            "2 PM \u2013 5 PM every day",
            "Peak hours don't exist \u2014 limits are always the same"
        ],
        "correct": [1],
        "explanation": "Peak hours are weekdays 5 AM\u201311 AM PT. Outside these windows and on weekends, Anthropic often doubles usage limits. Schedule heavy work accordingly."
    }
]
