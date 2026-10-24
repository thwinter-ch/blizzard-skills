# Engagement Page — workflow

Do the steps in this order. Stop where a step says stop. The rules are in [SKILL.md](SKILL.md).

- [ ] 1. Talk the concept through with the page owner, get their go
- [ ] 2. Propose the landing, get the page owner's confirmation
- [ ] 3. Check what exists
- [ ] 4. Build
- [ ] 5. Check before the publish
- [ ] 6. Show it, get the page owner's yes
- [ ] 7. Commit, then publish
- [ ] 8. Report

## 1. Talk the concept through, then stop

Never skip it, also when the brief looks complete. Propose your answer for each point:

1. **Audience:** the organisation and the named people who will read the page.
2. **Type:** customer room, pitch or point page.
3. **The one point:** the one sentence the reader must take away.
4. **Sources:** the notes, the offer, the deck that the text comes from.
5. **Language:** the language and the spelling of the audience.
6. **Animation:** none, or what it must show.

Then propose the story in order: the sections and what each one says. Stop. Go on only when the page owner agrees.

## 2. Propose the landing, then stop

Send one short message:

- **Source folder:** for example `customers/acme/pages/2026-10-talk-pitch/`.
- **Address:** `/<client>/` for the first page, `/<client>/<yyyy-mm-dd-slug>/` when the client already has a page. The readable address if the user has a domain. Never a generated label.
- **here.now:** a new slug, or the existing slug of the client's site.
- **Access:** "Protect it, and for whom, or public?" For a protected page, propose the named email addresses plus your own domain. Name a whole customer domain only when the page owner asks.

Example:

> Pitch page "Agents in the back office", `customers/acme/pages/2026-10-talk-pitch/`, address `pages.example.com/acme/`, new slug, access: protect for jane@acme.com and your own domain, or public?

Stop. Go on after a yes or a correction.

## 3. Check what exists

1. Pull the repo. Read `<client>/README.md`. If the client already has a site, add to it. Do not make a second site.
2. If the page exists on here.now but not in the repo, pull the live files into the source folder first and commit them as they are.
3. If this is the second page of the client, grow the tree:
   1. Move the first page from `index.html` to `<yyyy-mm-dd-slug>/index.html`, with the date of the first page. Fix its relative links.
   2. Write a new `index.html` as the landing page. It lists both pages, newest first.
   3. Add the back link at the top of both pages.
   4. Tell the page owner that `/<client>/` now shows the landing page, and give the new address of the first page.

## 4. Build

1. Copy the repo's `base.html` to `<page>/index.html`. If there is none yet, build the first page plain, then save its style as `base.html`.
2. Replace every placeholder. Delete the blocks the page type does not use.
3. Write from the sources only. Every number, price and date comes from a source. A missing fact stays a visible gap, marked as such.
4. Put every file the page links to (PDF, image) in the page folder. Use relative links.
5. For a customer room, add each document as a dated folder or file, and one entry in the list, newest first.
6. Add animation only per the rules in SKILL.md.

## 5. Check before the publish

1. Search the page for leftover placeholders. There must be none.
2. Open `index.html` at 1280 px, at 390 px and at one width between them. No horizontal scroll, no cut text, no overlap.
3. Look at every line break at all three widths. Fix every single word alone on a last line and every label that overlaps.
4. Turn on reduced motion. All content must be visible.
5. Click every link and every file. With a landing page, check the navigation: back links, every page listed, next links where the order matters.
6. Check contrast, spacing and the closing line: no harsh block, no text tight under a block, no reference to anything not on the page.
7. Read the footer: the data protection notice is there. No notice, no publish.

If the session has design skills for web pages, run them on a new page or layout now, fix what they find, and do this check again. A new document in an existing room does not need the pass.

A page you did not see is not done.

## 6. Show it, then stop

Send the page owner a screenshot or a local preview. Stop. Go on after a yes, or make the changes and show it again.

## 7. Commit, then publish

1. Commit the page folder and the updated `<client>/README.md`, and push. Follow the repo's own rules for the merge.
2. Publish the whole page folder with the here.now skill. A publish replaces the whole site. On a republish, use the same slug.
3. On the first publish, set the readable address with a domain route, if the user has a domain.
4. Set the access from step 2: `restricted` with the guests, or public. On an existing page, read the access list first and keep the guests the page owner added by hand.
5. Open the readable address and do the check of step 5 again on the live page.

Work that never reaches the repo reaches nobody; if it cannot, say so.

## 8. Report

Send the page owner: the address, the access (public, or the guests), the commit or pull request link, and what is open. Do not send the link to the audience. The page owner does that.
