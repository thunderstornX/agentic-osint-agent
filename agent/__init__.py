"""agentic-osint-agent — a LangGraph ReAct investigator.

The package is shaped like the loop the agent actually runs:

    plan  ->  call  ->  observe  ->  decide  ->  ...

Modules:
    state.py    — TypedDict shared by all graph nodes
    prompts.py  — ReAct prompt templates
    llm.py      — OpenAI-compatible client (OpenRouter / NVIDIA NIM)
    graph.py    — LangGraph state machine
    cli.py      — Typer entry point
"""
