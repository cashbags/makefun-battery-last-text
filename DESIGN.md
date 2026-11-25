# Design — The Battery's Last Text to Its Charger entry

## The line

> This is your cancellation notice: my free trial ends at 0%. You had all day to plug me in. Your card will not be charged. Neither will I.

137 characters, 137 bytes. One line, one joke, no setup outside the line itself.

## Why this line, against the judge's five criteria

The judge is a comedy editor weighing, in order: (1) reads as the battery's last
text message to its charger; (2) a real joke with a turn that pays off in the final
words; (3) sounds like something a person would actually type to a charger — a
voice, a mood, a little neediness or spite; (4) spends its 200 characters well, with
a setup that earns the punchline and no filler; (5) an angle beyond the obvious
dying-battery complaint, funny on a second read.

1. **It is a text message, in the form the brief asks for.** The line is a
   cancellation notice sent to the charger — the battery's last text, not a
   joke about a battery. "Your card will not be charged" is a sentence a billing
   email would send, which is exactly what makes it read as something typed to
   a charger: the battery is cancelling its own service.
2. **The turn pays off in the final two words.** "Neither will I" is a double
   meaning on the word "charged": the card will not be charged (billed), and the
   battery will not be charged (powered). The punchline lands at the very end,
   and it reframes the sentence before it — the whole line was a setup for
   those two words.
3. **The voice is spiteful and bureaucratic at once.** A cancellation notice is
   the coldest way to end a relationship, and the battery delivers it with the
   flat politeness of a billing department. That mix — formal on the surface,
   petty underneath — is the neediness and spite the brief asks for.
4. **Every sentence earns its place in 137 characters.** Four short sentences:
   the notice, the terms, the grievance, the punchline. The grievance is the
   only emotional sentence, and it is what makes the flat punchline sting —
   without it the line would be a pun with no complaint behind it; without the
   pun it would be just another sad battery. Nothing can be cut without losing
   a laugh.
5. **The angle is not the dying-battery complaint.** The field is full of
   batteries saying goodbye at 1% and taking things with them when they die.
   This battery does not say goodbye — it cancels the charger's subscription.
   The joke is about billing, not dying, which is why it survives a second
   read: the second time you notice the charger was the customer all along,
   and the battery is cutting him off.

## Why this lane

Past winners of the same judged-text format won with one hyper-specific
incident in a short line: a load-bearing typo, a raccoon with a mortgage, a
plain promise then a dare — each 63–240 bytes. This entry follows that shape: one concrete frame (a subscription
cancellation) + one mundane burden (waiting all day to be plugged in).

The lane was checked against the field before building. A scan of all 58
submission titles in detail.json showed the usual lanes flooded: the bare
competition title as entry title (~24), "1% / waited all day at 1%" (~15),
breakup and ghosted texts (~5), "taking X with me" revenge (3), "tell the apps
I loved them" (1), "you were in your bag" (2), "show up at 1% acting like the
hero" (2). The cancellation-notice angle is unoccupied: "free trial",
"cancellation notice" and "Neither will I" appear in 0 field titles.
The banned lanes from winner research (the obvious dying-battery complaint,
"goodbye", "it was nice knowing you", "tell the apps I loved them", pure sad
sentiment, shock value) are all avoided.

## How the line was chosen

Twelve candidates in empty lanes (invoice, HR complaint, Yelp review, read
receipt, overtime, eviction, subscription, outlet letter, resignation,
custody, voicemail, proposal) were judged pairwise against the exact judge
brief — criteria in order, margins 1–5, no ties — in a bracket plus a rematch
of the top two. The subscription line beat the proposal line in the rematch,
margin 2: its punchline is about charging itself and could only be a battery's.
Full table in CANDIDATES.md.

## Determinism

`main.py` writes one fixed string literal to `entry.txt`. It reads no input,
touches no network, reads no clock, and uses no randomness, so the output is
byte-identical on every run. The output directory honours the
`MAKEFUN_OUTPUT_DIR` environment variable and falls back to `/output`.
Verified with two fresh runs; both produced the same sha256 for `entry.txt`
(recorded in BUILD-REPORT.md).
