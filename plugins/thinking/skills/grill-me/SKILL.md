---
name: grill-me
description: Interview the user relentlessly about a plan, design, business or topic, checkpointing every answer to a capture file so nothing is lost. Use when they want to stress-test a plan, get grilled on a design, run a brainstorm or discovery session, extract what is in their head into a doc, or say "grill me".
---

# Grill Me — `/grill-me`

Interview the user about every branch of the topic until you both hold the same picture. Walk the decision tree, settling upstream calls before the ones that depend on them. **The point is to get what is in their head onto disk** — durable, organised, safe against context filling up.

## The capture file is the whole point

Long interviews eat context. Answers held only in your head get misremembered, conflated or dropped. So you write to disk after every single answer. **The file, not your context, is the record.** Never wait to be asked to save.

## Before the first question

1. **Search what is already known.** One pass through the user's notes, documents and connected tools (for example Notion or Drive) on the topic and the named entities. Anything already recorded is not a question; it is a line you put in the file and ask them to confirm or correct.
2. **Create the capture file** at `brainstorms/{YYYY-MM-DD}-{topic-slug}.md` in the user's own repo or notes folder. If they have none, ask once where captures should live, and use that place every time. Date from `date +%F`. If the session later produces a finished artefact (a plan, a map, an offer), that moves wherever it belongs; the raw capture stays here. If the folder is a git repo: pull before you start, commit and push after the session.
3. Write the header immediately: title, date, the goal in one line, what you already found, and an empty "Open flags" section.
4. **One line telling them where you are saving.** Then Q1.

## The checkpoint rule — non-negotiable

After EVERY answer, BEFORE the next question:

- Append the entry: what you asked, the facts and decisions from the answer (their words where the wording carries meaning), and any flags.
- Correct earlier entries if this answer changes them.
- Then ask the next question.

Never batch. One answer, one write. If the session dies at any moment, the file already holds everything said.

## How to ask

- **One question at a time.** Always carry your **recommended answer** — your best read from context — so they can confirm, correct or redirect in three words instead of writing a paragraph.
- **Grill, don't survey.** Push on the weak joint: the number with no source, the assumption doing all the load-bearing, the plan that only works if someone else behaves. If an answer dodges, ask again, narrower. This is the skill's whole value — a polite interviewer produces a document nobody needed.
- **Look it up rather than ask it.** Anything answerable from a file, a repo, a connected tool or the calendar — go and read it. If they hand you a doc, read it and surface only what is net-new.
- **Can't answer → flag it and move.** Capture the open item and who owns it. Never stall the interview on a missing fact.
- Keep going until they call it, or every branch is walked. Near the end, offer the backstop: "anything we haven't touched?"

## File structure

```
# {Topic}: Brainstorm / Discovery Notes
Date: {date} · Goal: {one line}

## Summary / key decisions
(running synthesis, updated as you go)

## Q&A log
### Q1 — {topic}
- Asked: {question}
- Captured: {facts, decisions, their words where it matters}
- Flags: {open item -> owner}

## Open flags (pending input)
- {item} -> {who can answer}
```

## At the end

- Re-read the file for contradictions and gaps, and reconcile them.
- Short recap: what is captured, what is still flagged, the one next step.
- Offer to save the durable decisions to the user's memory or notes tool, one fact per entry. Offer — do not write memory unasked.

## Source

Based on Matt Pocock's `grill-me` skill in [mattpocock/skills](https://github.com/mattpocock/skills) (MIT license). This version adds the capture file and the checkpoint rule.
