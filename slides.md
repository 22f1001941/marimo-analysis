---
marp: true
title: Product Documentation Presentation
paginate: true
theme: my-custom-theme
class: lead
---

<!--
Author: 22f1001941@ds.study.iitm.ac.in
-->

<style>
/* -------- Custom Theme -------- */
section {
  font-family: "Segoe UI", sans-serif;
}

h1 {
  color: #007acc;
  font-weight: 700;
}

code {
  background: #f2f2f2;
  padding: 2px 6px;
  border-radius: 4px;
}

footer {
  content: attr(data-footer);
}
</style>

<!-- Theme definition -->
<style>
@theme my-custom-theme {
  backgroundColor: #ffffff;
  color: #333333;
  header: {
    color: #007acc;
    font-size: 0.8rem;
  }
  footer: {
    color: #999999;
    font-size: 0.7rem;
  }
}
</style>

# Product Documentation  
### Powered by Marp  
**Contact:** 22f1001941@ds.study.iitm.ac.in

---

# Overview  
This presentation demonstrates:

- Custom Marp theme  
- Background images  
- Page numbers  
- Mathematical equations  
- Developer-friendly documentation practices  

---

<!-- Slide with background image -->
<!-- Use any public image URL or a relative path -->
<!-- Example using Unsplash -->
![bg](https://images.unsplash.com/photo-1518770660439-4636190af475)

# System Architecture  
Our system uses a microservices architecture with:

- API Gateway  
- Auth Service  
- Data Processing Engine  
- ML Service Layer  

---

# Mathematical Model  

To describe algorithmic behavior:

\[
T(n) = O(n \log n)
\]

And recursively:

\[
T(n) = 2T\left(\frac{n}{2}\right) + n
\]

This corresponds to **merge sort** complexity.

---

# Custom Styled Slide

<style scoped>
h2 {
  color: #d63384;
  font-size: 2rem;
}
p {
  font-size: 1.1rem;
}
</style>

## Custom Styling Example

This slide uses **scoped CSS** to override theme rules locally.

---

# Version Control Best Practices

- Keep documentation in a `docs/` folder  
- Use Markdown for portability  
- Prefer Marp for presentations  
- Use GitHub Actions for automated PDF export  

---

# Thank You  
Reach out anytime:  
**22f1001941@ds.study.iitm.ac.in**
