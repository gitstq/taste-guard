<div align="center">

# 🛡️ TasteGuard

**AI Content Quality Guardian**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)](https://github.com/gitstq/taste-guard/releases)

[English](#english) | [简体中文](#简体中文) | [繁體中文](#繁體中文)

</div>

---

<a name="english"></a>
## 🎉 Introduction

**TasteGuard** is a Python CLI tool that evaluates and optimizes AI-generated content quality. Inspired by the trending [taste-skill](https://github.com/Leonxlnx/taste-skill) project, TasteGuard helps content creators, developers, and writers produce **unique, engaging, and non-generic** text outputs.

### Why TasteGuard?

In the era of AI-generated content, "AI slop" — generic, repetitive, and soulless text — is everywhere. TasteGuard acts as your content quality guardian, detecting:

- 🎯 Overused generic phrases ("in today's world", "leverage synergy")
- 📉 Weak modifiers that dilute meaning ("very", "really", "quite")
- 🔄 Repetitive sentence structures and transition words
- 📊 Overall content engagement and readability metrics

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔍 **Generic Phrase Detection** | Identifies 50+ common AI-generated expressions |
| 📈 **Vocabulary Diversity** | Measures lexical richness and bigram variety |
| 💬 **Engagement Scoring** | Evaluates sensory words, questions, and active voice |
| 📖 **Readability Analysis** | Flesch Reading Ease and Grade Level metrics |
| 💡 **Smart Suggestions** | Actionable recommendations for improvement |
| 🎨 **Rich CLI Output** | Beautiful terminal formatting with color-coded results |

### 🚀 Quick Start

#### Requirements

- Python 3.8 or higher
- pip package manager

#### Installation

```bash
pip install taste-guard
```

#### Usage

```bash
# Analyze text content
taste-guard analyze "Your text here..."

# Analyze from file
taste-guard analyze -f article.txt --verbose

# Compare two texts
taste-guard compare "Text A..." "Text B..."

# Get optimization suggestions
taste-guard optimize "Your draft text..."

# Output as JSON
taste-guard analyze "Text..." --json
```

### 📖 Detailed Usage Guide

#### Analyze Command

The `analyze` command provides comprehensive content quality analysis:

```bash
# Basic analysis
taste-guard analyze "In today's world, we need to leverage synergy."

# Verbose mode with detailed detection
taste-guard analyze -f blog_post.md --verbose

# JSON output for programmatic use
taste-guard analyze "Text..." --json
```

**Output Metrics:**

- **Overall Score**: 0-100 quality rating
- **Generic Phrases**: Count and density of overused expressions
- **Vocabulary Diversity**: Unique word ratio and bigram variety
- **Sentence Variation**: Pattern diversity and length variation
- **Engagement Score**: Interactive elements and active voice ratio
- **Readability**: Flesch metrics for comprehension difficulty

#### Compare Command

Compare two pieces of content side-by-side:

```bash
taste-guard compare "AI-generated text..." "Human-written text..."
```

#### Optimize Command

Get targeted suggestions for improvement:

```bash
taste-guard optimize -f draft.txt
```

### 💡 Design Philosophy

TasteGuard was designed with these principles:

1. **Privacy First**: All analysis runs locally — no data sent to external services
2. **Fast & Lightweight**: Pure Python with minimal dependencies
3. **Actionable Insights**: Not just scores, but specific improvement suggestions
4. **Developer Friendly**: JSON output mode for CI/CD integration

### 📦 Development & Deployment

#### From Source

```bash
git clone https://github.com/gitstq/taste-guard.git
cd taste-guard
pip install -e .
```

#### Running Tests

```bash
make test
# or
pytest tests/ -v
```

#### Building

```bash
make build
```

### 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<a name="简体中文"></a>
## 🎉 项目介绍

**TasteGuard** 是一款 Python CLI 工具，用于评估和优化 AI 生成内容的质量。灵感来源于热门的 [taste-skill](https://github.com/Leonxlnx/taste-skill) 项目，TasteGuard 帮助内容创作者、开发者和写作者产出**独特、引人入胜、非通用**的文本内容。

### 为什么选择 TasteGuard？

在 AI 生成内容的时代，"AI 垃圾"——千篇一律、重复乏味、毫无灵魂的文本——无处不在。TasteGuard 作为您的内容质量守护者，能够检测：

- 🎯 过度使用的通用短语（"在当今世界"、"利用协同效应"）
- 📉 弱化语义的修饰词（"非常"、"真的"、"相当"）
- 🔄 重复的句子结构和过渡词
- 📊 整体内容互动性和可读性指标

### ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🔍 **通用短语检测** | 识别 50+ 种常见 AI 生成表达 |
| 📈 **词汇多样性** | 测量词汇丰富度和双词组多样性 |
| 💬 **互动性评分** | 评估感官词汇、疑问句和主动语态 |
| 📖 **可读性分析** | Flesch 阅读难度和年级水平指标 |
| 💡 **智能建议** | 提供可操作的改进建议 |
| 🎨 **丰富的 CLI 输出** | 彩色编码结果的精美终端格式 |

### 🚀 快速开始

#### 环境要求

- Python 3.8 或更高版本
- pip 包管理器

#### 安装

```bash
pip install taste-guard
```

#### 使用

```bash
# 分析文本内容
taste-guard analyze "您的文本内容..."

# 从文件分析
taste-guard analyze -f article.txt --verbose

# 比较两段文本
taste-guard compare "文本 A..." "文本 B..."

# 获取优化建议
taste-guard optimize "您的草稿文本..."

# 输出 JSON 格式
taste-guard analyze "文本..." --json
```

### 📖 详细使用指南

#### Analyze 命令

`analyze` 命令提供全面的内容质量分析：

```bash
# 基础分析
taste-guard analyze "在当今世界，我们需要利用协同效应。"

# 详细检测模式
taste-guard analyze -f blog_post.md --verbose

# JSON 输出，便于程序化处理
taste-guard analyze "文本..." --json
```

**输出指标：**

- **整体评分**：0-100 质量评级
- **通用短语**：过度使用的表达的数量和密度
- **词汇多样性**：独特词汇比例和双词组多样性
- **句子变化度**：模式多样性和长度变化
- **互动性评分**：互动元素和主动语态比例
- **可读性**：Flesch 理解难度指标

#### Compare 命令

并排比较两段内容：

```bash
taste-guard compare "AI 生成的文本..." "人工编写的文本..."
```

#### Optimize 命令

获取针对性的改进建议：

```bash
taste-guard optimize -f draft.txt
```

### 💡 设计理念

TasteGuard 遵循以下设计原则：

1. **隐私优先**：所有分析在本地运行——数据不会发送到外部服务
2. **快速轻量**：纯 Python 实现，依赖最小化
3. **可操作洞察**：不仅提供分数，还有具体的改进建议
4. **开发者友好**：JSON 输出模式，便于 CI/CD 集成

### 📦 开发与部署

#### 从源码安装

```bash
git clone https://github.com/gitstq/taste-guard.git
cd taste-guard
pip install -e .
```

#### 运行测试

```bash
make test
# 或
pytest tests/ -v
```

#### 构建

```bash
make build
```

### 🤝 贡献指南

欢迎贡献！请遵循以下准则：

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

### 📄 开源协议

本项目采用 MIT 协议 - 详情请查看 [LICENSE](LICENSE) 文件。

---

<a name="繁體中文"></a>
## 🎉 專案介紹

**TasteGuard** 是一款 Python CLI 工具，用於評估和優化 AI 生成內容的品質。靈感來源於熱門的 [taste-skill](https://github.com/Leonxlnx/taste-skill) 專案，TasteGuard 幫助內容創作者、開發者和寫作者產出**獨特、引人入勝、非通用**的文字內容。

### 為什麼選擇 TasteGuard？

在 AI 生成內容的時代，「AI 垃圾」——千篇一律、重複乏味、毫無靈魂的文字——無處不在。TasteGuard 作為您的內容品質守護者，能夠檢測：

- 🎯 過度使用的通用短語（「在當今世界」、「利用協同效應」）
- 📉 弱化語義的修飾詞（「非常」、「真的」、「相當」）
- 🔄 重複的句子結構和過渡詞
- 📊 整體內容互動性和可讀性指標

### ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🔍 **通用短語檢測** | 識別 50+ 種常見 AI 生成表達 |
| 📈 **詞彙多樣性** | 測量詞彙豐富度和雙詞組多樣性 |
| 💬 **互動性評分** | 評估感官詞彙、疑問句和主動語態 |
| 📖 **可讀性分析** | Flesch 閱讀難度和年級水平指標 |
| 💡 **智能建議** | 提供可操作的改進建議 |
| 🎨 **豐富的 CLI 輸出** | 彩色編碼結果的精美終端格式 |

### 🚀 快速開始

#### 環境要求

- Python 3.8 或更高版本
- pip 套件管理器

#### 安裝

```bash
pip install taste-guard
```

#### 使用

```bash
# 分析文字內容
taste-guard analyze "您的文字內容..."

# 從檔案分析
taste-guard analyze -f article.txt --verbose

# 比較兩段文字
taste-guard compare "文字 A..." "文字 B..."

# 獲取優化建議
taste-guard optimize "您的草稿文字..."

# 輸出 JSON 格式
taste-guard analyze "文字..." --json
```

### 📖 詳細使用指南

#### Analyze 命令

`analyze` 命令提供全面的內容品質分析：

```bash
# 基礎分析
taste-guard analyze "在當今世界，我們需要利用協同效應。"

# 詳細檢測模式
taste-guard analyze -f blog_post.md --verbose

# JSON 輸出，便於程式化處理
taste-guard analyze "文字..." --json
```

**輸出指標：**

- **整體評分**：0-100 品質評級
- **通用短語**：過度使用的表達的數量和密度
- **詞彙多樣性**：獨特詞彙比例和雙詞組多樣性
- **句子變化度**：模式多樣性和長度變化
- **互動性評分**：互動元素和主動語態比例
- **可讀性**：Flesch 理解難度指標

#### Compare 命令

並排比較兩段內容：

```bash
taste-guard compare "AI 生成的文字..." "人工編寫的文字..."
```

#### Optimize 命令

獲取針對性的改進建議：

```bash
taste-guard optimize -f draft.txt
```

### 💡 設計理念

TasteGuard 遵循以下設計原則：

1. **隱私優先**：所有分析在本地運行——資料不會發送到外部服務
2. **快速輕量**：純 Python 實現，依賴最小化
3. **可操作洞察**：不僅提供分數，還有具體的改進建議
4. **開發者友好**：JSON 輸出模式，便於 CI/CD 整合

### 📦 開發與部署

#### 從原始碼安裝

```bash
git clone https://github.com/gitstq/taste-guard.git
cd taste-guard
pip install -e .
```

#### 執行測試

```bash
make test
# 或
pytest tests/ -v
```

#### 建置

```bash
make build
```

### 🤝 貢獻指南

歡迎貢獻！請遵循以下準則：

1. Fork 本倉庫
2. 建立功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟 Pull Request

### 📄 開源協議

本專案採用 MIT 協議 - 詳情請查看 [LICENSE](LICENSE) 檔案。
