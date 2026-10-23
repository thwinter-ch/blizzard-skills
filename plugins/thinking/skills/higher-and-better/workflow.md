# Higher and better workflow

Copy this checklist and tick it off:

```
Higher and better progress:
- [ ] 0. After the fact only — diagnose the result
- [ ] 1. Fit check — outcome, creative or speed work?
- [ ] 2. Raise the ask — the moves that change the work, in writing; set the budget
- [ ] 3. Scope gate and access
- [ ] 4. Do the work
- [ ] 5. Judge — highest rung reachable, never yourself
- [ ] 6. Fix, then judge again
- [ ] 7. Report and log
```

**0. After the fact only — diagnose the result.** Read the finished result in full. Write, one line each: the ask it actually answered; where it fell short on Higher, Deeper, Wider, Target and the judge; the one shortfall that matters most. Show the user these lines only if the raised ask changes their goal (scope gate). Then go to step 2 and redo against the raised ask; keep the old result as the baseline the judge compares against.

**1. Fit check.** Use SKILL.md → "When it fits". Speed work: stop here and just do it. Creative work: skip Higher in step 2.

**2. Raise the ask.** Write it down, one line each, and leave out the lenses that change nothing (say which):

```
Goal beyond the goal: <one sentence>
Expert move nobody asked for: <one line>
Raw material: <source>
Methods and tools: <names>
Verbs and fields: <the task as verbs> — <field: what it does>, <adversarial field: what it does>
Target: <baseline → target, how measured>
Judge: <rung and how>
Budget: <time or agent runs>
```

**3. Scope gate and access.** Apply SKILL.md → "Scope gate" first: no setup for a changed ask before the user's go. Then list the access the ask needs. Set up what you can (connector, repo checkout, data export, test machine). For what you cannot, name it in one line. If the budget runs out on access or measurement, report and stop (SKILL.md → "Stop rule").

**4. Do the work.** Use the methods and tools from step 2. Do what each field does; no role-play. Measure against the target; a miss is the measured gap, not more work past the budget.

**5. Judge.** Pick the highest rung from SKILL.md → "The outside judge". For rung 2 in Claude Code with the Codex plugin:

- **Changes in a repo:** `/codex:adversarial-review <what to attack: the goal, the assumption, the weakest claim>` reviews the uncommitted working tree; add `--base <the branch it will merge into>` to review a whole branch. It sees the diff only, so make sure every change you want judged is in it.
- **A document, or anything that is not a diff:** `/codex:rescue` with the brief: "Read <file>. Attack it: wrong claims, missing evidence, the weakest decision. Do not fix anything. List findings, worst first."
- Long reviews: add `--background`, then wait for the completion notice before `/codex:result`. Do not poll. Rescue may ask whether to resume an old thread: answer `--fresh` for a new judgment.
- Keep the Codex output word for word: in the log, and linked from the report. Your summary goes beside it, never instead of it.

Without the plugin, a terminal run works the same: `codex exec --sandbox read-only -C <repo> "<the brief>"`. This counts as rung 2 only when Claude did the work. When Codex did the work, Claude is the judge: `claude -p "<the brief>"` in a fresh session.

**6. Fix, then judge again.** Fix what the judge proves; answer the rest with one line each. Run the same judge on the changed result. Stop when it finds nothing new that changes a decision, or the budget runs out.

**7. Report and log.** Use SKILL.md → "Report". State baseline, target and result as numbers, the judge rung, and how many findings you fixed and waived. Write the decisions to a log, a repo issue or a shared page. Flag any stale doc you found.
