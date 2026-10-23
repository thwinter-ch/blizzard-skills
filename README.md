# Skills

A growing collection of [Claude Code](https://docs.claude.com/claude-code) skills by [Thomas Winter](https://www.linkedin.com/in/thomaswinter/).

A public skills marketplace from Blizzard Ventures. Add it once, and every skill and every update reaches you by itself.

## Install

**Claude app:** add the marketplace `thwinter-ch/blizzard-skills` under plugins, then install the plugin `blizzard`.

**Claude Code:**

```
/plugin marketplace add thwinter-ch/blizzard-skills
/plugin install blizzard@blizzard-skills
```

**ChatGPT or another tool:** open the skill's `SKILL.md` and paste its text into a project as instructions.

## Available skills

| Skill | What it does |
|---|---|
| [`ste`](./plugins/blizzard/skills/ste) | Plain writing: ASD-STE100 for English, DIN 8581-1 «Einfache Sprache» for German. Picks the fastest form: text, diagram, page or video. |
| [`concept-page`](./plugins/blizzard/skills/concept-page) | Thinks an idea through on one web page (idea, concept, build idea), source in your repo, published on here.now. |
| [`grill-me`](./plugins/blizzard/skills/grill-me) | Interviews you about a plan, one question at a time, and saves every answer to a file. |
| [`scipab`](./plugins/blizzard/skills/scipab) | Structures a data dump into a 7-part SCIPAB decision brief (Situation → Risk). |

## How skills work

Every skill is a directory containing a `SKILL.md` with frontmatter that tells Claude when to invoke it. Read [the skill docs](https://docs.claude.com/claude-code/skills) for the full spec.

## License

MIT — use, fork, modify, redistribute. Attribution appreciated, not required.

## Contact

Built by Thomas Winter. Find me on [LinkedIn](https://www.linkedin.com/in/thomaswinter/) or open an issue here.
