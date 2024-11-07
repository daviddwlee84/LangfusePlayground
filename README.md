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

- http://localhost/playground - For Streamlit Playground
- http://localhost - For Langfuse

## Todo

- [ ] Basic chat with Langfuse callback
- [ ] Able to fetch and select prompt from Langfuse
- [ ] Locate placeholders from prompt for user to input
- [X] Use Traefik so we only need to export single port
  - [Try Traefik · Issue #1 · daviddwlee84/Nginx-DockerCompose](https://github.com/daviddwlee84/Nginx-DockerCompose/issues/1)
  - [Traefik Getting Started Quickly - Traefik](https://doc.traefik.io/traefik/getting-started/quick-start/)
  - [**HTTP routing with Traefik | Docker Docs**](https://docs.docker.com/guides/traefik/)
  - [Traefik Docker Routing Documentation - Traefik](https://doc.traefik.io/traefik/routing/providers/docker/)
  - [Traefik Docker Documentation - Traefik](https://doc.traefik.io/traefik/user-guides/docker-compose/basic-example/)
  - [Traefik Routers Documentation - Traefik](https://doc.traefik.io/traefik/routing/routers/)
  - [dockersamples/easy-http-routing-with-traefik: Repo to support the HTTP routing with Traefik use case guide on docs.docker.com](https://github.com/dockersamples/easy-http-routing-with-traefik)
  - [How can I deploy multiple Streamlit apps on different subdomains? - Streamlit Docs](https://docs.streamlit.io/knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains)
    - [How to proxy web apps using nginx?](https://gist.github.com/soheilhy/8b94347ff8336d971ad0)
    - `--server.baseUrlPath` `STREAMLIT_SERVER_BASE_URL_PATH`

## Resources

[Langfuse](https://langfuse.com/)

- [langfuse/langfuse: 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with LlamaIndex, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23](https://github.com/langfuse/langfuse)
- [Langfuse Cloud](https://cloud.langfuse.com/)

---

Prompt Playground & Prompt Versioning/Management

- [LangSmith](https://www.langchain.com/langsmith)
- [PromptHub Features: Prompt Versioning](https://www.prompthub.us/features/prompt-versioning)
