# Langfuse Playground

Playground build around Langfuse

> Motivation: Self Hosted LLM Playground only support for Enterprise Edition
>
> - [Will Playground be available for self-hosted? · langfuse · Discussion #2073](https://github.com/orgs/langfuse/discussions/2073)
> - [LLM Playground - Langfuse](https://langfuse.com/docs/playground)

## Getting Started

```bash
docker compose up --build
```

## Todo

- [ ] Basic chat with Langfuse callback
- [ ] Able to fetch and select prompt from Langfuse
- [ ] Locate placeholders from prompt for user to input
- [ ] Use Traefik so we only need to export single port
  - [Try Traefik · Issue #1 · daviddwlee84/Nginx-DockerCompose](https://github.com/daviddwlee84/Nginx-DockerCompose/issues/1)

## Resources

[Langfuse](https://langfuse.com/)

- [langfuse/langfuse: 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with LlamaIndex, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23](https://github.com/langfuse/langfuse)
- [Langfuse Cloud](https://cloud.langfuse.com/)

---

Prompt Playground & Prompt Versioning/Management

- [LangSmith](https://www.langchain.com/langsmith)
- [PromptHub Features: Prompt Versioning](https://www.prompthub.us/features/prompt-versioning)
