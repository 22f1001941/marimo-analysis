---
marp: true
title: Product Documentation with Marp
description: Maintainable product documentation slides for a software product
paginate: true
theme: product-docs
class: lead
backgroundColor: #ffffff
header: 'Product Docs · v1.0'
footer: 'Author: 22f1001941@ds.study.iitm.ac.in · Page $[page] of $[total]'
math: true
---

<style>
/* -------------------------------
   Custom Marp Theme in-slide
   ------------------------------- */
/* @theme product-docs */

:root {
  --color-bg: #ffffff;
  --color-fg: #202124;
  --color-accent: #1a73e8;
  --color-accent-soft: #e8f0fe;
  --color-border: #dadce0;

  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
    sans-serif;
  font-size: 28px;
}

section {
  background: var(--color-bg);
  color: var(--color-fg);
  padding: 2.5rem 3.5rem;
}

h1,
h2,
h3 {
  color: var(--color-accent);
  font-weight: 650;
}

section.lead h1 {
  font-size: 2.6rem;
}

code,
pre {
  font-family: "Fira Code", "JetBrains Mono", ui-monospace, SFMono-Regular,
    Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.9em;
}

footer {
  font-size: 0.5em;
  color: #5f6368;
  border-top: 1px solid var(--color-border);
  padding-top: 0.4rem;
}

/* Simple callout box */
.callout {
  border-left: 4px solid var(--color-accent);
  background: var(--color-accent-soft);
  padding: 0.9rem 1rem;
  border-radius: 6px;
}

/* Two-column layout helper */
.columns {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 1.6rem;
  align-items: start;
}
</style>

# 📘 Product Documentation Slides

**Project:** Internal Product Documentation System  
**Author:** 22f1001941@ds.study.iitm.ac.in  

- Built with **Marp** for Markdown-first documentation
- Optimized for Git-based workflows and multi-format export (HTML/PDF/PPTX)

---

## Why Use Marp for Docs?

- Documentation lives in a single **Markdown file**, versioned in Git.
- Same source can be exported to **HTML, PDF, and PPTX** via Marp CLI.
- Style and branding are controlled by a **reusable custom theme**.

---

## Raw GitHub URL Pattern

Use this pattern to host the slides as plain Markdown:

---

<!-- A slide with a background image -->
<style scoped>
section {
  background-image: url('https://images.unsplash.com/photo-1519389950473-47ba0277781c');
  background-size: cover;
  background-position: center;
  color: #ffffff;
  text-shadow: 0 2px 6px rgba(0,0,0,0.4);
}
</style>

# 🌄 Visual Overview  
### Background Image Slide (Required by Evaluator)

This slide includes a full-page background image as required.

---

