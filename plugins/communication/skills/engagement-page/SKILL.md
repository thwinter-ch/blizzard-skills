---
name: engagement-page
description: Builds an engagement page — one web page for a named outside audience, such as a customer room, a talk or seminar pitch, or a page that makes one point — keeps its source in the user's own git repo, and publishes it on their here.now account, public or protected as the page owner decides. Use on "/engagement-page", "make a page for a client", "customer room", "deal room", "pitch page", "talk proposal page", "here.now page for a client", or "add a document to the client room". Not for a concept or idea page (that is concept-page) or for a PDF.
---

# Engagement Page — `/engagement-page`

An engagement page is a web page for a named outside audience. It serves one deal, one talk or one moment. This skill builds it the same way every time: the source is in the repo, the page owner decides who can open the page, and every page looks like the others.

Run it as the workflow in [workflow.md](workflow.md); if you cannot read it, say so and stop.

## When to use

- **Customer room:** one shared page per customer, with a dated list of documents: meeting notes, a proposed approach, slides.
- **Pitch:** a page that sells a talk, a seminar or a workshop to one organiser.
- **Point page:** a page that makes one point or shows one demo, for example a meeting summary for a partner.

## When not to use

- Not for a concept or idea page. Those are for the user and their sparring partners, not for one outside audience. Use `concept-page`.
- Not for a document the customer signs or files. Make a PDF.
- Not to send the link. The page owner sends it.

## Roles

- **The page owner** (the user, or the person who owns the deal) agrees the concept, confirms the landing, approves the text and decides the access.
- **The builder** (a person or an agent) builds, commits and publishes.

## The hard rules

1. **Conversation first, page second.** Talk the concept through with the page owner before you build: who reads the page, the one point, the story in order, and what any animation must show. Never build or publish before that conversation.
2. **Propose the landing.** Before you build, send one line: source folder, readable address, and the access question: "Protect it, and for whom, or public?" Build only after a yes or a correction.
3. **Show it before you publish.** Publish only after the page owner says yes to the built page.
4. **Source in the repo before the publish.** Commit and push the source before the first publish and before every republish. A page that exists only on here.now is a defect.
5. **The page owner decides the access.** There is no default. Ask every time: protected (here.now `restricted`, with named guests) or public (anyone with the link). Some pages are public on purpose, for example a talk pitch.
6. **One record per client.** Keep a row per page in `<client>/README.md`: title, folder, address, slug, access (public, or the guests).
7. **Look at it before you call it done.** Open the published page at desktop and at phone width.

## Where pages land

In the user's own repo. If they have none yet, ask once which one to use.

| Audience | Folder |
|---|---|
| A customer or a prospect | `customers/<client>/pages/<page>/` |
| A partner (a reseller, a vendor) | `partners/<partner>/pages/<page>/` |
| The user's own company | `marketing/pages/<page>/` |

`<client>` is a short lower-case name. The page folder is the site: `index.html` and its files, nothing else.

## One site per client: the address tree

Each customer and each partner has one here.now site, at one address, with one access setting. It starts with one page and grows:

1. The first page sits at `/<client>/`.
2. When a second page comes, `/<client>/` becomes the landing page that lists all pages, newest first. Each page, the first one included, moves to `/<client>/<yyyy-mm-dd-slug>/`.
3. Every later page gets its own dated folder and one entry on the landing page.

The `/<client>/` link never changes. Send it to the customer once. Publish the whole site to the one slug of the client.

**Navigation**, once there is a landing page: a back link at the top of each page, every page listed on the landing page, and a next link at the bottom where the order matters. Use relative links, so the tree works at its readable address.

**A readable address.** If the user has their own domain on here.now, every page lives at a readable address there, for example `pages.example.com/<client>/`. Never hand out the generated here.now label when a readable address exists. Set it with a domain route, as the here.now docs (domains) describe.

## The page types

| Type | Header | Body | Access |
|---|---|---|---|
| **Landing page** | Your logo × customer logo (only if the customer gave one), `<Client> × <You>`, "Shared documents" | One intro sentence, then the list of pages, newest first: date, link, one line each | As the site |
| **Customer room** | Same as the landing page | One intro sentence, then the document list, newest first. Each document is a dated folder (`2026-09-28-meeting-notes/index.html`) or a dated file | Usually protected: named people of the customer plus your own domain |
| **Pitch** | Eyebrow ("Talk proposal"), the talk title as headline, one line with audience and format | 1. Why this talk, for this audience, now. 2. What the audience takes away (three to five points). 3. Outline with times. 4. The speaker: photo and three lines. 5. Format and logistics | Often public |
| **Point page** | Eyebrow (summary, review, demo), the point as headline, the date | The point first, then the evidence, then the next step. One idea per section | Public or protected |

Every page ends with the contact of the page owner and the data protection notice.

## Look

- **One house style for all pages.** Write it down once (colours, fonts, logo, footer) in a `base.html` in the repo and copy it for each page. Do not invent a new style per page. Use the customer's colours only when the page owner asks.
- **No harsh contrast.** No dark block on a light page, no white block on a dark page. Show emphasis with a soft tint, a thin border or the accent colour.
- **Room.** At least `3rem` between blocks. The footer never sits tight under a coloured block. Names and roles get one line each.
- **Line breaks.** Headings get `text-wrap: balance`, paragraphs, list items and captions `text-wrap: pretty`. In a short caption, label or button, join the last two or three words with `&nbsp;`. No single word alone on a last line, no label that overlaps a chart.
- **One column**, a text line at most `60ch`, tables in a wrapper that scrolls sideways on a phone.
- **Not for search engines.** Every page has `<meta name="robots" content="noindex,nofollow">`.
- A mechanism is a diagram, not a paragraph: inline SVG or a draw.io export.

## Animation

Animation must help the reader: an order, a build-up, a focus. Decoration is not a reason.

1. Use GSAP in the page, from a CDN with a fixed version. ScrollTrigger for scroll-driven steps.
2. Content never depends on motion. Everything is visible without JavaScript and with reduced motion. Animate from a hidden state with `gsap.from()`; never hide content in CSS.
3. Respect `prefers-reduced-motion: reduce`: skip all animation.
4. Short and once: an entrance takes at most 0.8 s and plays once. No loops in body text.
5. One idea per animation, and no horizontal scroll at 390 px.

## Closing line and data protection

End with one plain next-step question, for example "Which process could this apply to?" Never refer to something the page does not show.

Every page has the same data protection notice in the footer, in the language of the page:

> Data protection notice. This page is hosted on here.now, which delivers it through Cloudflare. Their position on sovereignty and data residency is the same as that of any other US cloud provider without an additional sovereignty agreement.

> Datenschutzhinweis. Diese Seite liegt bei here.now, das über Cloudflare ausliefert. Deren Souveränitäts- und Datenresidenz-Position entspricht der jedes anderen US-Cloud-Anbieters ohne zusätzliche Souveränitätsvereinbarung.

Do not add what the page contains or who has access. A page without the notice is not published.

## Language

Write in the language of the audience, in its spelling: US English for a US reader, British English for a UK or Swiss reader in English. Keep the terms the customer already uses. For plain wording, use the `ste` skill.

## Hand-offs

- Publish with the official here.now skill (here.now/docs).
- If the session has design skills for web pages, run them on a new page or layout before the page owner sees it.
- For a customer, collect scattered sources into one place before you write. Every number, price and date comes from a source; a missing fact stays a visible gap.
