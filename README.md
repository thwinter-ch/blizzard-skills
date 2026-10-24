# blizzard-skills

A public skills marketplace from Blizzard Ventures, by [Thomas Winter](https://www.linkedin.com/in/thomaswinter/). Add it once, and every skill and every update reaches you by itself. The layout follows Anthropic's [plugin marketplace format](https://code.claude.com/docs/en/plugin-marketplaces): one marketplace, packs as plugins, skills inside each pack.

## Install

### In the Claude app (web or desktop)

1. In the left sidebar, open **Customize**, then the **Plugins** tab.
2. Click **Add**, then **Add marketplace**, then **Add from a repository**.
3. Enter `thwinter-ch/blizzard-skills` and confirm.
4. In **Plugins**, open **Discover**, pick a pack (`thinking` or `communication`) and click **Add**.

Done. Updates arrive by themselves. Plugins need a paid Claude plan (Pro, Max, Team or Enterprise). Official steps: [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

### In ChatGPT or another AI tool

Open the skill's `SKILL.md` below, copy its text and paste it into a project as instructions. Copy any `workflow.md` next to it too. Updates do not arrive by themselves.

### In Claude Code (terminal)

```
/plugin marketplace add thwinter-ch/blizzard-skills
/plugin install thinking@blizzard-skills
/plugin install communication@blizzard-skills
```

## Packs

### thinking

Raise the ask, think an idea through, get grilled.

| Skill | What it does |
|---|---|
| [`higher-and-better`](./plugins/thinking/skills/higher-and-better) | Raises an ask (higher, deeper, wider, one hard target), has a test or another model judge the result, keeps the report small. |
| [`concept-page`](./plugins/thinking/skills/concept-page) | Thinks an idea through on one web page (idea, concept, build idea), source in your repo, published on here.now. |
| [`grill-me`](./plugins/thinking/skills/grill-me) | Interviews you about a plan, one question at a time, and saves every answer to a file. |

### communication

Write so people get it the first time, lead with the decision, and give each customer one page.

| Skill | What it does |
|---|---|
| [`ste`](./plugins/communication/skills/ste) | Plain writing: ASD-STE100 for English, DIN 8581-1 «Einfache Sprache» for German. Picks the fastest form: text, diagram, page or video. |
| [`scipab`](./plugins/communication/skills/scipab) | Structures a data dump into a 7-part SCIPAB decision brief (Situation → Risk). |
| [`engagement-page`](./plugins/communication/skills/engagement-page) | One web page for a named outside audience (customer room, pitch, point page), source in your repo, published on here.now, public or protected. |

## Credits

| Skill | Built on |
|---|---|
| higher-and-better | Felix Rieseberg, [How to be more ambitious](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) (13.10.2026) · Anthropic Economics, [How employment is changing at Anthropic](https://www.anthropic.com/research/employment-at-anthropic) (16.10.2026) · Andrej Karpathy, [output ladder](https://x.com/karpathy/status/2105819303471976479) (2.10.2026) |
| grill-me | Matt Pocock, [mattpocock/skills](https://github.com/mattpocock/skills) (MIT license, © Matt Pocock) |
| ste | [ASD-STE100](https://www.asd-ste100.org/) · DIN 8581-1 · ISO 24495-1 · Karpathy's output ladder |
| scipab | [SCIPAB® by Mandel Communications](https://www.mandel.com/scipab-messaging-tool); unofficial, not affiliated |

## How skills work

Every skill is a directory containing a `SKILL.md` with frontmatter that tells Claude when to invoke it. Read [the skill docs](https://code.claude.com/docs/en/skills) for the full spec.

## License

MIT — use, fork, modify, redistribute. Attribution appreciated, not required.

## Contact

Built by Thomas Winter. Find me on [LinkedIn](https://www.linkedin.com/in/thomaswinter/) or open an issue here.
