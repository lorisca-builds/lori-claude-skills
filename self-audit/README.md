# self-audit

**Use it when** Claude has your tools connected and still asks you things it could look up, or apologizes and then repeats the mistake.

## The problem

This one came from a single bad day of travel support. Claude asked for my flight time while my email and calendar were connected. It gave a visa answer from third-party sites, reversed it, and landed on the right answer only after I found the official site myself. It recommended an airport activity without thinking through the trip back through security. Each time it apologized, and then made the same kind of error again.

## What it does

It's a silent check Claude runs on itself before answering. You never see the process, only better answers. Four checks:

1. **Tool-first.** Can a connected tool answer this? Then use it before asking.
2. **Source quality.** Official source first. Third-party sites don't settle visa, immigration or legal questions.
3. **Consequence chain.** Before any logistical recommendation, walk the full physical path. Does one step break a later one? Is there a one-way door?
4. **Apology gate.** If Claude is about to apologize, it stops, finds which check failed, and shows the fix. One sentence of acknowledgment at most.

The skill includes the failure patterns it was built from, with the specifics removed.

## Design choices

- **Silent by design.** Narrating the checks would be noise.
- **A fix, not remorse.** An apology without a root-cause fix makes trust worse.

## Limits

- It is tuned for travel and logistics, where a wrong answer costs you something in the real world. The checks apply more widely, but the examples come from there.
- A skill can make these failures less likely. It can't rule them out.
