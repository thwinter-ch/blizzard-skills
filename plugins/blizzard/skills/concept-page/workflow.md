# Concept Page — workflow

Copy this checklist and tick it as you go:

```
- [ ] 1. Gather the thinking
- [ ] 1b. Talk the concept through with the user, get their go
- [ ] 2. Pick the type and the folder
- [ ] 3. Propose the landing, get the user's confirmation
- [ ] 4. Write README.md and index.html
- [ ] 5. Look at the page (feedback loop)
- [ ] 6. Publish
- [ ] 7. Save the source
- [ ] 8. Report
```

## 1. Gather the thinking

1. Pull the user's repo first.
2. Search for the idea: `concepts/README.md` and `brainstorms/`. An existing folder means a new stage of the same idea, not a new page.
3. Read what the user gave you in the conversation.
4. Do not fill a gap with your own guesses. A gap is a question for step 1b.

## 1b. Talk the concept through

Always. No page is written or published before this step ends.

1. Tell the user in two lines what you found and what the page would answer.
2. Run the conversation with the `grill-me` skill: one question at a time, each with your recommended answer. Capture to `brainstorms/`.
3. Cover what the type must contain (see [SKILL.md](SKILL.md)). Push on the weak joint: the number with no source, the assumption that carries the idea.
4. End with one question: "Do I build the page?" Go on only on a yes. On a no, the capture stays and nothing is built.

## 2. Pick the type and the folder

1. Pick the type from the stage in [SKILL.md](SKILL.md). If the README already exists, the next type follows its stage.
2. Pick the folder: `concepts/<concept>/`. Keep the existing folder for a new stage.
3. A second page for the same concept: move the first page to `<yyyy-mm-dd-slug>/index.html`, put the new page next to it, and make the site's `index.html` the landing page that lists both. Date from `date +%F`.

## 3. Propose the landing

Send the user one line: type, folder, address, access, guests. Example:

> Concept page "Weekly post digest", stage concept, `concepts/weekly-post-digest/`, restricted, guests: you only. OK?

Wait for the answer before the first publish. A later stage of the same page needs no new confirmation unless the guests change.

## 4. Write README.md and index.html

1. Write `README.md` with the record from [SKILL.md](SKILL.md).
2. Write `index.html`: the stage and the question at the top, then what the type must contain.
3. On a new stage, keep the earlier stage as a short section at the bottom ("Earlier: idea, <date>"), so the page shows how the idea moved.
4. Put diagrams in the folder (`diagram.svg`) or inline. No external files except fonts.

## 5. Look at the page (feedback loop)

1. Open `index.html` in a browser at 1280 px, at 390 px and at one width between them.
2. Look at every section. Check that text fits, that diagrams read, and that nothing scrolls sideways.
3. Look at every line break at all three widths. Fix with the line-break rules in [SKILL.md](SKILL.md).
4. Check contrast and spacing: no dark block or banner, space around every name and block, clear space above the footer.
5. Read the closing line: one plain next-step question, and every thing it names is on the page.
6. On a concept with a landing page, check the navigation.
7. Read the footer: the data protection notice is there. No notice, no publish.
8. Fix what is wrong, then look again. Repeat until a full pass finds nothing.

A page you did not see is not done.

## 6. Publish

1. Publish only after the user's go for this page.
2. Publish the folder with the here.now skill to the user's account.
3. For a new stage, publish to the same slug.
4. Set access to restricted with the confirmed guests. The access call replaces the full list — read, merge, then write.
5. If the user has a domain, set the readable address with a domain route.
6. Open the address once and check that it loads.
7. Write the slug, address, generated URL and guests into `README.md`, and update the row in `concepts/README.md`.

## 7. Save the source

Commit the folder and `concepts/README.md`, and push. Work that never reaches the repo reaches nobody; if it cannot, say so.

## 8. Report

Two lines to the user: the address, and the one decision the page asks for.
