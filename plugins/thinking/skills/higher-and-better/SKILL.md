---
name: higher-and-better
description: Raises an ask before the work starts, or raises the bar on a finished result that is not good enough — higher (the outcome behind the task), deeper (what a top expert would do, from raw material, with expert tools), wider (the methods of other fields, one of them adversarial), against one hard, measurable target — then has a test or a different model judge the result, and reports it in the form the reader takes in fastest. Use on "/higher-and-better", "higher and better", "aim higher", "go deeper", "be more ambitious", "what would a top expert do here", "this is not good", "not good enough, go higher", "redo this better", or when a task will lead to a meeting or a decision, repeats every week, or is worth a day of agent time. Not for lookups, small fixes or rewording.
---

# Higher and better

Make the ask bigger in the right direction — before the work starts, or after, on a result that is not good enough. Then prove the result with a judge that is not you, and keep the report small.

Run it as the workflow in [workflow.md](workflow.md); if you cannot read it, say so and stop.

## Two ways in

- **Before:** a new ask. Raise it, then do the work (workflow steps 1–7).
- **After:** a finished result the user is not happy with — yours, another agent's, or a human's. First name the ask the result actually answered, and where it fell short of each move (too low, too shallow, too narrow, no target, self-judged). Raise that ask with the four moves. Then redo the work against the raised ask, not a polish of the old result. The judge compares old and new against the target. Workflow step 0, then steps 2–7.

## When it fits

- **Fits:** outcome work — a decision, a meeting, a job that repeats, a system that must stay healthy. Tell: there will be a meeting about it.
- **Fits partly:** creative work. Use Deeper and Wider; skip Higher.
- **Does not fit:** speed work — a lookup, a small fix, a tone change. Do it fast and stop.

## The four moves

On outcome work, Higher, Target and the judge apply every time; on creative work, skip Higher. Deeper and Wider are lenses: use the parts that change the work, and say which you skipped.

1. **Higher (altitude).** Ask what must happen after this task. Name the goal beyond the goal in one sentence ("fix this crash" → "keep the apps crash-free"). If access is missing — a connector, a repo, raw data, a machine to test on — name it. Never quietly shrink the goal to fit the access you have. Higher often needs a setup step first.
2. **Deeper (depth).** Answer: (1) what a top professional does here that nobody asked for; (2) the rawest material they start from, not the digested version; (3) their methods and tools; (4) what, other than you or the user, shows the result is right. Then use those tools — a database, a script, a statistical test — not a markdown table that only sounds expert. Where it matters, test one thing the user believes against the raw data. A new finding counts only when it holds up on data it was not built from, or a test or an independent source confirms it; otherwise label it a hypothesis.
3. **Wider (range).** Restate the noun as verbs: "an offer" → "make a sceptical board believe one cause-and-effect story and sign in one meeting". From the verbs, pick the other fields that help — one adversarial (short seller, forensic accountant, procurement officer). Do what each field does to its material. Never write in its voice: role-play is a failure.
4. **Target.** Set one hard, specific target on the outcome, with its baseline and how you measure it: "page load 5 s → 200 ms, measured on the live site", not "three insights". Never a count of output. Treat it as solvable. A miss is reported as the measured gap.

**Scope gate.** If the higher goal changes what the user asked for, it is their call: show them the old ask and the new one in three lines, and continue on the original ask until they answer. No setup for the new ask before their go.

**Stop rule.** Set a budget before you start (time or agent runs). When access cannot be had, or the target cannot be measured, report that and stop raising. Never go round in circles on a gap.

## The outside judge

Never grade your own work. Use the highest rung you can reach, and name it in the report:

1. **A test or a measurement** that runs without you deciding the answer — a test suite, a live check, a reconcile against a number you did not produce.
2. **A different model.** Claude's work goes to Codex; Codex's work goes to Claude. A chat bot asks a second model. The commands are in workflow.md, step 5.
3. **A fresh subagent** briefed to attack. Same model, same blind spots — the lowest rung.

A judge finds problems; you decide what changes. After you fix, check again: the same judge, on the changed result.

## Report

Human attention is the bottleneck. A bigger ask makes more output, so the report gets smaller, not bigger.

- Answer first. At most three decisions per message, ranked; if more decisions are the user's, say how many wait and batch them. Never take a decision that is theirs to keep the count low.
- Write the report by the `ste` skill (communication pack): its wording rules and its output ladder.
- Work in the open. Write each decision to a log, a repo issue or a shared page, so the next agent sees it. If a doc you read is stale, flag it.

## Never

- Take a step that cannot be undone — mail, production, money — because the goal got higher. The go stays with the user.
- Make the report longer because the ambition grew.

## Copy-paste prompt

For a chat bot, or any agent without this skill. It carries the same gates. After the fact, put this line in front: "This result is not good enough. Name the ask it answered and where it fell short, then redo it, not polish it."

> Higher and better, not bigger. If this is a lookup, a small fix or a rewording, just do it and skip the rest. Before you start: (1) name the outcome behind this task, and the access you lack to reach it (skip this for creative work); (2) say what a top expert would do that I did not ask for — from which raw material, with which tools; (3) if it helps, restate the task as verbs and pick the fields that help, one adversarial — do what they do, no role-play; (4) set one hard target on the outcome, with baseline and measurement. If the outcome changes my ask, show me old and new in three lines and wait for my go on the new one. Take no step that cannot be undone without my go. Set a budget; if access or measurement fails, report and stop. A test or a different model judges the result, never you; fix, then check again. Report in STE: answer first, at most three decisions (say how many more wait for me), plus a diagram or one HTML page if it is complex.

## Sources

Built from three articles, October 2026:

- Felix Rieseberg (Anthropic), [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/), 13 October 2026. Altitude, depth and range (here: higher, deeper, wider), and never letting a model judge its own work.
- Anthropic Economics team (Wilmers, Catipon, Massenkoff, McCrory), [How employment is changing at Anthropic](https://www.anthropic.com/research/employment-at-anthropic), 16 October 2026. Human attention is the bottleneck for agent output; hence the small report.
- Andrej Karpathy, [post on the output ladder](https://x.com/karpathy/status/2105819303471976479), 2 October 2026. STE text, diagram, HTML page, explainer video: the report form (see the `ste` skill).

The hard target, the scope gate, the stop rule and the rungs of the judge ladder are additions of this skill.
