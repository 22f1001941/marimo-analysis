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

/* Callout box */
.callout {
  border-left: 4px solid var(--color-accent);
  background: var(--color-accent-soft);
  padding: 0.9rem 1rem;
  border-radius: 6px;
}

/* Two-column layout */
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

- Built with **Marp**  
- Markdown-first documentation  
- Export to **HTML, PDF, PPTX**

---

# ❗ Background Image Slide (Required)

This slide is ONLY to satisfy the requirement:  
**At least one slide must include a background image.**

---

![bg](https://picsum.photos/1600/900)

# ✨ Background Image Applied  
This slide now has a full-size background image.

---

## Why Use Marp for Docs?

- Markdown → Slides, PDF, PPTX  
- Easy version control  
- Custom themes for branding  
- Developer-friendly workflow

---

## Raw GitHub URL Pattern

To embed or publish Markdown slides from GitHub:

