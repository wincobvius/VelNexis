# VelNexis

**Live site:** https://velnexis.netlify.app

Tech fix guides and honest rumor checks — 330 articles across 20 categories, built as a fully static site.

## What is this

VelNexis is a tech publication covering Windows, Android, iPhone, printers, WiFi, battery, AI tools and viral tech rumors — every guide written to be useful first: step-by-step fixes, checkable sources, and plain-English verdicts.

## How it is built

A custom static site generator in a single Python file — no frameworks, no dependencies.

- `build.py` — the generator: parses frontmatter Markdown, renders 362 HTML pages, builds JSON-LD structured data (Article, HowTo, FAQPage, BreadcrumbList, CollectionPage, Person, Organization), sitemap.xml, llms.txt, robots.txt and a client-side search index
- `content/` — 330 article files, 20 category files, 6 site pages (all Markdown)
- `assets/` — minified CSS, fonts, images
- `netlify.toml` — security headers + cache rules

```bash
python3 build.py
```

Run the build and the complete static site is generated in place.

## Author

**Abdul Rafay** — founder and author. Computer Science student, Rawalpindi, Pakistan.
GitHub: https://github.com/wincobvius
