# How to use GitHub Models API in GitHub Actions workflows

[中文](README_zh.md)

This repository demonstrates how to use GitHub Models API in GitHub Actions workflows.

## Usage

1. Fork this repository
2. Edit [config.json](.github/scripts/config.json) to customize the AI prompt
3. Add a markdown file to the repository
4. The AI will automatically process it and create a `_processed.md` file

## Configuration

Edit the `system_prompt` in [config.json](.github/scripts/config.json):

```json
{
  "system_prompt": "You are a content summarization assistant. Generate a clear, structured summary of the provided content. Include key points, main ideas, and important details. Keep the summary concise but comprehensive.",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```

More configurations:

Blog Post Enhancement

```json
{
  "system_prompt": "You are a blog writing assistant. Improve the provided content by enhancing clarity, adding engaging elements, and ensuring proper structure. Maintain the original tone and message while making it more polished and reader-friendly.",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```

Technical Documentation

```json
{
  "system_prompt": "You are a technical documentation expert. Convert the provided content into clear, well-structured technical documentation. Add proper headings, code examples where appropriate, and ensure clarity for developers.",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```

Translation to Chinese

```json
{
  "system_prompt": "You are a professional translator. Translate the provided content to English while maintaining the original meaning, tone, and structure. Ensure the translation is natural and fluent.",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```

Meeting Notes Formatting

```json
{
  "system_prompt": "You are a meeting notes organizer. Structure the provided content into well-formatted meeting notes with clear sections for agenda items, decisions made, action items, and next steps.",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```