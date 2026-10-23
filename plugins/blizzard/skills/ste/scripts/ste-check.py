#!/usr/bin/env python3
"""Flag likely ASD-STE100 breaches in English text. A heuristic: the writer decides each flag.

Usage: python3 ste-check.py DRAFT.md   or   echo "text" | python3 ste-check.py
Skips code, blockquotes and text in double quotes. Does not check meaning, noun clusters or paragraphs.
Exit code 0 = no flags, 1 = flags found.
"""
import re
import sys

MAX_INSTRUCTION = 20
MAX_DESCRIPTION = 25
SWAPS = {  # exact word forms -> STE word
    "utilize": "use", "utilizes": "use", "utilized": "use", "utilise": "use", "utilised": "use",
    "leverage": "use", "leverages": "use", "leveraged": "use",
    "commence": "start", "commences": "start", "commenced": "start",
    "initiate": "start", "initiates": "start", "initiated": "start",
    "terminate": "stop", "terminates": "stop", "terminated": "stop",
    "assist": "help", "assists": "help", "assisted": "help",
    "facilitate": "help", "facilitates": "help", "facilitated": "help",
    "ensure": "make sure", "ensures": "make sure", "ensured": "make sure",
    "verify": "make sure", "verifies": "make sure", "verified": "make sure",
    "prior to": "before", "in order to": "to", "in the event that": "if",
    "it is necessary to": "you must",
}
# -ing words that are nouns, adjectives or approved words, not verbs
ING_OK = {"thing", "things", "something", "nothing", "anything", "everything", "string",
          "strings", "during", "morning", "evening", "ceiling", "spring", "king", "ring",
          "wing", "bring", "sing", "swing", "sting", "meeting", "meetings", "building",
          "buildings", "setting", "settings", "pricing", "logging", "briefing", "heading",
          "headings", "warning", "warnings", "timing", "staging", "ping", "missing",
          "opening", "openings", "meaning", "meanings", "training", "drawing", "drawings",
          "wiring", "bearing", "bearings", "housing", "fitting", "fittings", "marking",
          "markings", "lighting", "routing", "booking", "onboarding", "billing", "reporting",
          "monitoring", "packaging", "wording", "spacing", "padding", "coding"}
BE = {"am", "is", "are", "was", "were", "be", "been", "being"}
PARTICIPLE = r"(\w{3,}ed|made|done|shown|given|taken|written|sent|run|built|set|kept|seen|known|found|put|held|left|gone|broken|chosen|driven|begun|lost|paid|read|told|bought|brought|thought|got|gotten)"
PASSIVE = re.compile(rf"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?{PARTICIPLE}\b", re.I)
PERFECT = re.compile(rf"\b(has|have|had)\s+(\w+ly\s+)?(been|{PARTICIPLE})\b", re.I)
WORD = re.compile(r"[A-Za-z0-9][\w'’%-]*")


def strip_markup(text):
    text = re.sub(r"```.*?```", "\n\n", text, flags=re.S)   # code blocks
    text = re.sub(r"`[^`]*`", "X", text)                    # inline code
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)    # links
    text = re.sub(r"https?://\S+", "URL", text)
    return text


def blocks(text):
    """Join wrapped lines into blocks. A blank line, a list item, a heading or a table row starts a new block."""
    cur = []
    for line in text.splitlines():
        raw = line.strip()
        if raw.startswith(">"):  # a quote is source text: never rewrite it
            raw = ""
        starts_new = not raw or re.match(r"^([#|*-]|\d+[.)]|>\s*$)", raw)
        if starts_new and cur:
            yield " ".join(cur)
            cur = []
        raw = re.sub(r"^([#>*-]+|\d+[.)])\s*", "", raw)
        if raw.startswith("|"):
            yield from (c.strip() for c in raw.strip("|").split("|") if c.strip(" -:"))
            continue
        if raw:
            cur.append(raw)
    if cur:
        yield " ".join(cur)


def sentences(text):
    for block in blocks(strip_markup(text)):
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", block):
            if s.strip():
                yield s.strip()


def after_be(words, i):
    """True if a form of "to be" comes just before word i, perhaps with one -ly word between."""
    prev = [x.lower() for x in words[max(0, i - 2):i]]
    return bool(prev) and (prev[-1] in BE or (len(prev) == 2 and prev[-1].endswith("ly") and prev[0] in BE))


def check(text):
    flags = []
    for s in sentences(text):
        bare = re.sub(r"[\"“][^\"”]*[\"”]", " ", s)  # text in quotes is not checked
        n = len(WORD.findall(bare))
        short = s if len(s) <= 90 else s[:87] + "..."
        if n > MAX_DESCRIPTION:
            flags.append(f"LONG ({n} words, limit 25): {short}")
        elif n > MAX_INSTRUCTION:
            flags.append(f"LONG FOR AN INSTRUCTION ({n} words, limit 20): {short}")
        if ";" in re.sub(r"[\"“][^\"”]*[\"”]", " ", s):
            flags.append(f"SEMICOLON: {short}")
        words = WORD.findall(bare)
        ing = [w for i, w in enumerate(words) if w.lower().endswith("ing") and len(w) > 4
               and (i == 0 or not w[0].isupper())
               and (w.lower() not in ING_OK or after_be(words, i))]
        if ing:
            flags.append(f"-ING ({', '.join(ing)}): {short}")
        m = PASSIVE.search(bare)
        if m:
            flags.append(f"PASSIVE? ({m.group(0)}): {short}")
        m = PERFECT.search(bare)
        if m:
            flags.append(f"PERFECT TENSE ({m.group(0)}): {short}")
        low = bare.lower()
        for bad, good in SWAPS.items():
            if re.search(rf"\b{bad}\b", low):
                flags.append(f"WORD '{bad}' -> a form of '{good}': {short}")
    return flags


def main():
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    flags = check(text)
    for f in flags:
        print(f)
    print(f"{len(flags)} flag(s).")
    sys.exit(1 if flags else 0)


if __name__ == "__main__":
    main()
