---
name: ste
description: Makes an agent write in ASD-STE100 Simplified Technical English (short sentences, one idea each, simple approved words, active voice) and pick the output form a person takes in fastest — STE text, a diagram, one HTML page or an explainer video — from Karpathy's output ladder. Use for chat replies, runbooks, procedures and instructions, for any summary or explanation of agent work, and on "/ste", "in STE", "write in STE", "simplified technical English", "80% STE", "make this easier to read", "too long, I don't understand". Not for outbound business messages or social posts.
---

# STE

Write so a busy person understands the first time. Then pick the form that a person reads in the least time.

Human attention is the bottleneck: agents produce more than anyone can read. STE is the floor. A diagram, a page or a video is better when it fits.

## Where it applies

- **Always:** every reply to the user in chat, every summary of agent work for the user, every runbook, procedure or instruction an agent or a person must follow.
- **Not:** outbound business messages — email, Slack, offers, reports to a team or a client. They follow your own voice rules. Social posts. Code and code comments. Quotes and source text: never rewrite them.
- **Never switch language.** Write in the language of the thread. STE rules are for English. In another language, use that language's plain-language rules, below.

## Other languages

The same principles apply in every language: short sentences, one idea each, active voice, simple common words, one term per thing, main point first. ASD-STE100 exists only for English. Use the standard for that language:

| Language | Standard | Note |
|---|---|---|
| English | ASD-STE100 | This skill. |
| German | DIN 8581-1:2024-05 "Einfache Sprache" (plain German, based on ISO 24495-1). For instructions and technical text also the tekom guide "Deutsch für die Technische Kommunikation – Regeln und ihre Anwendung" (rule-based writing). | Not "Leichte Sprache". That is a different standard for readers with cognitive impairments. |
| French and others | ISO 24495-1 (plain language) | Apply the principles above. Do not import the English verb and -ing rules. Use that language's normal grammar. |

The word table and the checker script are English only.

## Two levels

- **STE (default).** All rules below.
- **80% STE.** Relax the word rules only: use a common word that is not in the STE dictionary when it is clearer than the approved word. All sentence and paragraph rules stay. Technical names and technical verbs ("merge", "deploy", "pull request") are allowed in strict STE too, so they are not a reason to relax.

## Sentences

1. One idea per sentence. One instruction per sentence, unless the two actions occur at the same time.
2. Instructions: max 20 words. Descriptions: max 25 words. Shorter is better.
3. Active voice in instructions, always. In descriptions, use active voice when you know who does the action: "The routine writes the log", not "The log is written by the routine". Passive is correct when the actor is unknown or not important. Never invent an actor to make a sentence active.
4. Verb forms: the infinitive, the imperative, and the simple present, past and future. A past participle only as an adjective or with a form of "to be" ("is", "was", "will be"). "The job ran", not "The job has been running".
5. No -ing verbs. "Before you merge", not "Before merging". Exceptions: technical names and their modifiers ("monitoring dashboard"), and words the STE dictionary approves ("during").
6. Keep the small words. Do not drop "the", "a" or "is" to save space. Telegram style is not STE.
7. No noun clusters of more than three words. "the token for the agent log", not "agent log GitHub write token".
8. No semicolons. Make two sentences.
9. Put a condition first when the reader must know it first: "If the push fails, try again", not "Try again if the push fails".
10. Otherwise a command starts with the verb: "Merge PR #57." A warning starts with a command: "Do not delete the WhatsApp session. If you delete it, someone must re-link the phone."

## Words

- One word for one meaning, and one name for one thing. If the thread says "routine", never switch to "job" or "task" for the same thing.
- Use the approved word with its approved meaning and part of speech. The STE dictionary has about 900 approved words, and this skill does not hold it. Ask: is there a shorter, more common word with the same meaning? Some swaps that make text simpler (they do not prove STE compliance, only the dictionary does):

| Not | Use |
|---|---|
| utilize, leverage | use |
| commence, initiate | start |
| terminate | stop |
| assist, facilitate | help |
| ensure, verify | make sure |
| prior to | before |
| in order to | to |
| in the event that | if |
| it is necessary to | you must |

- No jargon, internal code names or abbreviations without a short explanation the first time. You can use product names and technical names (Notion, GitHub, "pull request").
- Numbers as digits. Units always: "CHF 1,200", "200 ms", "3 days".

## Paragraphs and lists

- One topic per paragraph. Put the main point in the first sentence.
- Max 6 sentences per paragraph. In chat, fewer.
- Use a vertical list for steps, options or more than two parallel items. Number the list when the order matters.

## The output ladder

From [Karpathy's X post of 2 Oct 2026](https://x.com/karpathy/status/2105819303471976479): each rung is easier to understand than the one before. Use the lowest rung that carries the content. Climb when the content needs it.

| Rung | Use when | How |
|---|---|---|
| 1 · STE text | An answer, a decision, a status. Fits in about 15 lines. | This skill. |
| 2 · Diagram | A process, a structure, a flow, a dependency, a before/after. | draw.io, Mermaid or inline SVG on a page. |
| 3 · One HTML page or a Claude Motion clip | More than about 15 lines, a comparison, a report, anything to explore or come back to. A short animation when the point is a process, a flow or a change over time. | Page: one self-contained HTML file. Animation: Claude Motion (ask for an animation, or Output → Motion; built from code, exports MP4). Chat gets two lines and the link. |
| 4 · Explainer video | A full explainer with scenes and a voice-over is the fastest way to understand, and the result is worth the cost. Mostly for material that teaches. | A video tool of your choice. A voice-over needs a narration voice. Say if it is missing. |

- A table is a form of rung 1 or 3: use it for a comparison of more than two items. In chat replies, prefer a list.
- A process with more than three steps, or a structure with more than three parts, is usually faster to read as a diagram. Draw it when it is.
- Custom pages and videos are cheap now. Make a page or video you can throw away when it saves time to read. Do not ask first.
- Use motion to explain, not to decorate. When the point is a process, a flow or a change over time, animate it: a Claude Motion clip, or CSS or SVG animation or a step control on the page. Static text and tables stay still.
- The text on a diagram, page or video also follows STE.

## Check before you send

A feedback loop, not a guess:

1. For English text longer than a few sentences, run [scripts/ste-check.py](scripts/ste-check.py) on your draft. The script is in the `scripts` folder next to this SKILL.md: `python3 SKILL_DIR/scripts/ste-check.py draft.md`, or pipe the text in. It flags sentences over 20 words (instructions) or 25 (all), -ing words, likely passive voice, perfect tenses, semicolons and the swap words above. It skips code, text in double quotes and blockquotes. It does not check meaning, noun clusters or paragraphs. It is a heuristic: you decide each flag. Run it on your own text, not on a file that quotes bad examples.
2. Read the first sentence alone. It must carry the answer.
3. Count the ideas in the longest sentence. More than one: split it.
4. Ask: is a diagram or a page faster to read than this text? If yes, climb a rung.

## Example

Before (one sentence, 50 words, -ing verbs, swap words, a vague actor):

> Following the successful merging of the PR, the sync is expected to be picked up by the marketplace within approximately two hours, ensuring that the new skill is made available across all sessions, although it is recommended that a "Check for updates" is initiated if it is not being shown.

After (STE):

> After the merge, we expect the marketplace to sync the new skill in approximately 2 hours. After the sync, all sessions can use the skill. If a session does not show the skill, click "Check for updates".
