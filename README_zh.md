# 如何在 GitHub Actions 工作流中使用 GitHub Models API

[English](README.md)

此仓库演示如何在 GitHub Actions 工作流中使用 GitHub Models API。

## 使用方法

1. Fork 此仓库
2. 编辑 `.github/scripts/config.json` 自定义 AI 提示词
3. 向仓库添加 markdown 文件
4. AI 会自动处理并创建 `_processed.md` 文件

## 配置

编辑 `config.json` 中的 `system_prompt`：

```json
{
  "system_prompt": "你是内容摘要助手。为提供的内容生成清晰、结构化的摘要。包括关键点、主要想法和重要细节。保持摘要简洁但全面。",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```

更多配置参考：


博客文章优化

```json
{
  "system_prompt": "你是博客写作助手。通过增强清晰度、添加吸引人的元素和确保适当的结构来改进提供的内容。在使内容更加精美和读者友好的同时，保持原始语调和信息。",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```

技术文档整理

```json
{
  "system_prompt": "你是技术文档专家。将提供的内容转换为清晰、结构良好的技术文档。添加适当的标题，在合适的地方添加代码示例，并确保对开发者来说清晰易懂。",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```

中文翻译

```json
{
  "system_prompt": "你是专业翻译员。将提供的内容翻译成中文，同时保持原始含义、语调和结构。确保翻译自然流畅。",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```

会议记录格式化

```json
{
  "system_prompt": "你是会议记录整理员。将提供的内容结构化为格式良好的会议记录，包含议程项目、决定事项、行动项目和后续步骤等清晰部分。",
  "model": "gpt-4o-mini",
  "max_tokens": 1000,
  "temperature": 0.3
}
```