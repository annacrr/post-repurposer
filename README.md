# ✦ Post Repurposer

A minimal AI-powered content repurposing tool that turns one long-form text into platform-ready posts for **LinkedIn**, **Instagram**, and **Twitter/X**.

Built with **Python**, **Streamlit**, and an API-ready structure for **Claude**.

---

## 🌿 Project Overview

Creating content once is already a lot of work.

But turning that same idea into different formats for different platforms takes even more time. A LinkedIn post needs one tone. An Instagram caption needs another. Twitter/X needs to be sharper, shorter, and more direct.

**Post Repurposer** was built to solve that problem.

The tool takes a long-form text and prepares it to become platform-specific social content, using different rules for tone, length, structure, formatting, and style.

The goal is not just to generate text.

The goal is to simulate a real content workflow and show how AI can support marketing, content strategy, and repeatable creative systems.

---

## ✨ What It Does

Post Repurposer allows users to:

- Paste long-form content into a clean input box
- Choose a tone for the output
- Select which platforms they want to generate content for
- Prepare platform-specific prompts for:
  - LinkedIn
  - Instagram
  - Twitter/X
- Display results in a minimal, editorial-style interface
- Use a Claude API-ready structure for future real generation

---

## 🧠 Why I Built This

This project was created as part of my portfolio to show how I can combine:

- Content marketing strategy
- Prompt engineering
- Python development
- AI API integration
- Product thinking
- User interface design

I wanted to build something practical, not just a technical demo.

This is a tool I could actually use when creating content for social media, portfolio updates, LinkedIn posts, project announcements, or content distribution workflows.

---

## 🖥️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core app logic |
| Streamlit | Interactive web interface |
| Claude API | API-ready AI content generation |
| python-dotenv | Environment variable management |
| HTML/CSS | Custom styling inside Streamlit |

---

## 🎨 Design Direction

The interface was designed to feel:

- Minimal
- Editorial
- Soft
- Bookish
- Clean
- Portfolio-friendly

The visual style uses a warm off-white background, serif typography, rounded input/output boxes, navy accents, and subtle borders.

The goal was to make the tool feel less like a generic dashboard and more like a polished creative AI workspace.

---

## 📱 Platform Logic

Each platform has its own content rules.

### LinkedIn

LinkedIn outputs are designed to feel:

- Professional
- Human
- Reflective
- Conversational
- Easy to skim

The structure encourages short paragraphs, a strong opening hook, natural emojis when useful, and a soft closing thought or question.

### Instagram

Instagram outputs are designed to feel:

- Short
- Visual
- Warm
- Skimmable
- Caption-friendly

The structure uses short blocks, relevant emojis, and a small number of specific hashtags when useful.

### Twitter/X

Twitter/X outputs are designed to feel:

- Direct
- Punchy
- Curious
- Compact
- Shareable

The structure focuses on strong hooks, short sentences, and clear value without overexplaining.

---

## ⚙️ Current Project Status

The app currently includes:

- Streamlit interface
- Custom visual styling
- Tone selector
- Platform selector
- Long-form content input
- Prompt builder function
- Claude API-ready structure
- Placeholder outputs while API mode is turned off

The API integration is prepared in the code, but disabled by default:

```python
USE_API = False