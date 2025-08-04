# Solving the inference problem for open source AI projects with GitHub Models

AI features can make an open source project shine. At least, until setup asks for a paid inference API key. Requiring contributors or even casual users to bring their own large language model (LLM) key stops adoption in its tracks:

```javascript
$ my-cool-ai-tool
Error: OPENAI_API_KEY not found
```

Developers may not want to buy a paid plan just to try out your tool, and self hosting a model can be too heavy for laptops or GitHub Actions runners.

GitHub Models solves that friction with a free, OpenAI-compatible inference API that every GitHub account can use with no new keys, consoles, or SDKs required. In this article, we’ll show you how to drop it into your project, run it in CI/CD, and scale when your community takes off.

Let’s jump in.

## The hidden cost of “just add AI”

AI features feel ubiquitous today, but getting them running locally is still a challenge for a few reasons:

- **Paid APIs:** The simplest path is to ask users for an OpenAI or Anthropic key. That’s a non-starter for many hobbyists and students because paid APIs are too expensive.
- **Local models:** Running a 2 B-parameter LLM can work for lightweight tasks, but anything that requires more intelligence will quickly blow past typical laptop memory — let alone the 14 GB container that backs a GitHub Actions runner.
- **Docker images and weights:** You can bundle a model with your app, but distributing multi-gigabyte weights balloons install size and slows CI.

Every additional requirement filters out potential users and contributors. What you need is an inference endpoint that’s:

1. Free for public projects
2. Compatible with existing OpenAI SDKs
3. Available wherever your code runs, like your laptop, server, or Actions runner

That’s what GitHub Models provides.

### GitHub Models in a nutshell

- **What it is:** A REST endpoint that speaks the chat/completions spec you already know.
- **What you get:** A curated set of models (GPT-4o, DeepSeek-R1, Llama 3, and more) hosted by GitHub.
- **Who can call it:** Anyone with a GitHub Personal Access Token (PAT), or a repository’s built-in GITHUB\_TOKEN when you opt-in via permissions.
- **How much it costs:** Free tier for all personal accounts and OSS orgs; metered paid tier unlocks higher throughput and larger context windows.

Because the API mirrors OpenAI’s, any client that accepts a baseURL will work without code changes. This includes OpenAI-JS, OpenAI Python, LangChain, llamacpp, or your own curl script.

## How to get started with GitHub Models

Since GitHub Models is compatible with the OpenAI `chat/completions` API, almost every inference SDK can use it. To get started, you can use the OpenAI SDK:

```php
import OpenAI from "openai";

const openai = new OpenAI({
  baseURL: "https://models.github.ai/inference/chat/completions",
  apiKey: process.env.GITHUB_TOKEN  // or any PAT with models:read
});

const res = await openai.chat.completions.create({
  model: "openai/gpt-4o",
  messages: [{ role: "user", content: "Hi!" }]
});
console.log(res.choices[0].message.content);
```

If you write your AI open source software with GitHub Models as an inference provider, all GitHub users will be able to get up and running with it just by supplying a GitHub Personal Access Token (PAT).

And if your software runs in GitHub Actions, your users won’t even need to supply a PAT. By requesting the `models: read` permission in your workflow file, the built-in GitHub token will have permissions to make inference requests to GitHub Models. This means you can build a whole array of AI-powered Actions that can be shared and installed with a single click. For instance:

- Code review or PR triage bots
- Smart issue tagging workflows
- Weekly repository activity report generators
- And anything else that a GitHub Action can do

Plus, using GitHub Models makes it easy for your users to set up AI inference. And that has another positive effect: it’s easier for your *contributors* to set up AI inference as well. When anyone with a GitHub account can run your code end to end, you’ll be able to get contributions from the whole range of GitHub users, not just the ones with an OpenAI key.

### Zero-configuration CI with GitHub Actions

Publishing an Action that relies on AI used to require users to add their inference API key as a GitHub Actions secret. Now you can ship a one-click install:

```javascript
yaml 

# .github/workflows/triage.yml
permissions:
  contents: read
  issues: write
  models: read   # 👈 unlocks GitHub Models for the GITHUB_TOKEN

jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Smart issue triage
        run: node scripts/triage.js
```

The runner’s `GITHUB_TOKEN` carries the `models:read` scope, so your Action can call any model without extra setup. This makes it well suited for:

- Automated pull request summaries
- Issue deduplication and tagging
- Weekly repository digests
- Anything else you can script in an Action

## Scaling when your project takes off

The GitHub Models inference API is free for everyone. But if you or your users want to do more inference than the free rate limits allow, you can turn on [paid inference](https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-models) in your settings for significantly larger context windows and higher requests-per-minute.

When your community grows, so will traffic. So it’s important to consider the following:

- **Requests per minute (RPM)**: While the free tier offers default limits, the paid tier offers multiples higher.
- **Context window**: Free tier tops out at standard model limits; paid enables 128k tokens on supported models.
- **Latency**: The paid tier runs in its own separate deployment, so you’re not in the same queue as free tier users.

To get started, you can enable paid usage in **Settings > Models** for your org or enterprise. Your existing clients and tokens will keep working (but they’ll be faster and support bigger contexts).

## Take this with you

LLMs are transforming how developers build and ship software, but requiring users to supply their own paid API key can be a barrier to entry. The magic only happens when the first `npm install`, `cargo run`, or `go test` just works.

If you maintain an AI-powered open source codebase, you should consider adding GitHub Models as a default inference provider. Your users already have free AI inference via GitHub, so there’s little downside to letting them use it with your code. That’s doubly true if your project is able to run in GitHub Actions. The best API key is no API key!

By making high-quality inference a free default for every developer on GitHub, GitHub Models gets rid of the biggest blocker to OSS AI adoption. And that opens the door to more contributions, faster onboarding, and happier users.

## Tags:

## Written by

## Related posts

[AI & ML](https://github.blog/ai-and-ml/)

### Onboarding your AI peer programmer: Setting up GitHub Copilot coding agent for success

Learn how to configure Copilot coding agent’s environment, optimize project structure, use custom instructions, and extend its capabilities with MCP servers.

[AI & ML](https://github.blog/ai-and-ml/)

### A practical guide on how to use the GitHub MCP server

Upgrade from a local MCP Docker image to GitHub’s hosted server and automate pull requests, continuous integration, and security triage in minutes — no tokens required.

[AI & ML](https://github.blog/ai-and-ml/)

### How to build secure and scalable remote MCP servers

More context can mean more attack surfaces for your projects. Be prepared for what lies ahead with this guide.
