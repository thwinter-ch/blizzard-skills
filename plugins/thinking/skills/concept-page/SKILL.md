---
name: concept-page
description: Builds one web page that thinks an idea through — an idea, a concept or a build idea — keeps its source in the user's own git repo, and publishes it on their here.now account with restricted access. Use on "/concept-page", "concept page", "idea page", "make a page for this idea", "write up the concept", "put the concept on a page", "build idea", "page for the build", or when a brainstorm or grill-me session ends and the user wants something to look at or share. Not for customer or pitch pages.
---

# Concept Page — `/concept-page`

A concept page helps the user think an idea through and decide. It is for them and the people they invite to spar, never for a customer.

Run it as the workflow in [workflow.md](workflow.md); if you cannot read it, say so and stop.

**Always from this skill.** Read the skill and follow it. Never build a concept page from memory.

**Conversation first, page second.** Every concept page starts with a conversation with the user about the concept. Never write or publish a page before that conversation, and never before the user says the page can be built. This holds for every stage, also a new stage of an existing page.

## Three types, one per stage

An idea moves through stages. Each stage has its own page type. The page shows its stage at the top.

| Type | It answers | Must contain |
|---|---|---|
| **Idea** | Is this worth thinking about? | The problem, why now, a first guess at the solution, open questions. One screen. |
| **Concept** | How would it work, and do we do it? | How it works (a diagram), who it is for, what it costs, the risks, the one decision the user must make. |
| **Build idea** | What exactly do we build first? | The smallest first version, what is out, where the code goes, the first task to open. |

The last stage is **done** or **dropped**. A dropped page stays, with one line that says why.

## Where it lands

- **Source first, page second.** The source lands in the user's own git repo before anything is published, never only on here.now. If they have no repo yet, ask once which one to use.
  - Every concept: `concepts/<concept>/`, at the repo root.
  - `concepts/README.md` is the index: one row per concept with its stage and URL. Update it with every page.
  - The raw brainstorm stays in `brainstorms/` (the `grill-me` skill). The concept page links to it.
- **Published**: the user's here.now account, access **restricted**. Never public without the user's go for that page.
- **One slug per idea.** A new stage republishes to the same slug, so the link the user shared keeps working.
- **A readable address.** If the user has their own domain on here.now, the page lives at a readable address there. Never hand out the generated here.now label when a readable address exists. Set it with a domain route, as the here.now docs (domains) describe.
- **An address tree.** A concept starts with one page and can grow:
  1. The first page sits at `/<concept>/`.
  2. When a second page comes, `/<concept>/` becomes the landing page that lists the pages. Each page moves to `/<concept>/<yyyy-mm-dd-slug>/`.
  3. The `/<concept>/` link never changes. The user can share it from day one.
- **Navigation.** Once the concept has a landing page: each page below it has a link back to the landing page at the top; the landing page lists every page; where the order matters, each page links to the next one at the bottom. Use relative links.

Before the first publish, propose the landing — folder, address, access, guests — in one line. The user confirms or corrects it. Do not guess the guest list.

## The record

Each folder has a `README.md`. With `concepts/README.md` it is the whole record; there is no database.

```
# <Title>
Stage: idea | concept | build idea | done | dropped
Started: <yyyy-mm-dd> · Updated: <yyyy-mm-dd>
Slug: <slug> · Address: <readable address> · Generated URL: <here.now URL>
Access: restricted · Guests: <emails or domains>
Brainstorm: <link to brainstorms/...md, if any>
Decision: <the one decision this page asks for, and the answer when it comes>
```

## The page

- One self-contained `index.html` in the folder. Plain and readable.
- Lead with the stage and the one question the page answers. Then the content the type must contain.
- A mechanism is a diagram, not a paragraph: inline SVG or a draw.io export.
- Every number and claim names its source, or says it is a guess.
- No motion by default. Motion only when it explains a mechanism, and never when the reader asks for reduced motion.
- Short sentences. One idea per sentence. People read on a phone.

### Line breaks

A single word alone on the last line, or a label that runs into a diagram, looks broken. Prevent both in the CSS and check them by eye.

1. Give headings `text-wrap: balance`. Give paragraphs, list items and captions `text-wrap: pretty`.
2. In a short caption, a label or a button, join the last two or three words with non-breaking spaces (`&nbsp;`).
3. Put a diagram label where it has room: above the line, or at the end of it. Give it a background only when it must cross a line, never when it crosses a bar.
4. Check at 1280 px, at 390 px and at one width between them. Fix every single word alone on a last line, and every label that overlaps.

### Contrast and spacing

1. Use no dark blocks or banners on a light page. Show emphasis with a soft tint of the accent colour.
2. Leave enough space between blocks and around names. Text never sits tight against the edge of a box.
3. Leave clear space between the last coloured block and the footer.

### The footer: data protection

Every page ends with the same data protection notice in the footer, in the language of the page:

> Data protection notice. This page is hosted on here.now, which delivers it through Cloudflare. Their position on sovereignty and data residency is the same as that of any other US cloud provider without an additional sovereignty agreement.

> Datenschutzhinweis. Diese Seite liegt bei here.now, das über Cloudflare ausliefert. Deren Souveränitäts- und Datenresidenz-Position entspricht der jedes anderen US-Cloud-Anbieters ohne zusätzliche Souveränitätsvereinbarung.

### The closing line

End with one plain question about the next step, for example "Which process could this apply to?" Never refer to something the page does not show.

### Language

Write in the language of the audience, in its spelling. When the user invites no guests, write the language they used in the conversation. For plain wording, use the `ste` skill.

## Reuse, no copies

- Publish with the official here.now skill (here.now/docs).
- Run the conversation with the `grill-me` skill. A page does not replace the thinking.
- If the session has design skills for web pages, run them before the user sees the page. The page stays plain.
