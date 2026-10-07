# Audience modes - who is actually going to read this

The single most expensive mistake this skill can make is producing a technically flawless
artifact aimed at nobody in particular. A notebook that teaches machine learning to a
vice-president of marketing wastes their time; a notebook that assumes fluency in overfitting
loses a student who needed the explanation; a notebook that skips the reasoning chain to stay
crisp throws away rubric marks.

The content is often identical. **The structure, the voice, and the cut-list are not.**

So the audience is decided first, out loud, before a single cell is written - and stated in the
artifact itself so no reader has to guess who it was built for.

---

## The three modes

### STUDENT - the user is learning this material

**Reader:** The user, or someone at their level, working to understand the material well enough to be
examined on it and to explain it to someone else.

**What they want:** comprehension. They need to be able to defend every choice, not just repeat
it. A cartoon version they can't defend is worse than useless.

**Voice:** everything in `references/narrative-style.md`. Zero assumed background, every term
defined in the same breath it's used, analogies where they clarify the mechanism.

**Structure:** the full chronological arc in `references/notebook-structure.md`. The journey *is*
the content - understand before cleaning, clean before modeling, baseline before comparing.

**What gets cut:** nothing. Length is not the enemy here; unexplained jumps are.

**Deliverable:** one executed `.ipynb`.

**Self-check:** could someone with zero ML background read this and explain the dataset's story
back in their own words - what it predicts, why that metric, why the winner won?

---

### GRADER - a professor is marking this

**Reader:** the instructor, with a rubric in hand, reading perhaps twenty of these.

**What they want:** evidence that the reasoning happened. The grader already knows what boosting
is. They are not reading to learn - they are reading to check whether *you* know, and whether the
choices were justified rather than defaulted into.

**Voice:** the same plain-language rules as STUDENT. This surprises people, but it's correct: an
explanation clear enough to teach with is also the clearest possible evidence of understanding.
Compressing it to sound sophisticated reads as hand-waving and loses marks.

**Structure:** STUDENT's arc, plus the rubric-facing scaffolding in
`references/graded-assignment-checklist.md` - team-name placeholder, rubric self-check, the
no-AI-disclosure rule.

**What gets cut:** nothing, and be careful here. The instinct to "tighten it up for submission" is
usually an instinct to delete the justifications the rubric is specifically paying for. The
diagnostic detours - a model that lost, a metric that misled, a tuning pass that barely moved -
are among the *highest*-value content in this mode, because they demonstrate judgement rather
than recipe-following.

**Deliverable:** one executed `.ipynb`, plus whatever the assignment separately requires.

**Self-check:** read the actual current rubric line by line against the finished notebook, every
top-band criterion. State any place you're not certain it lands, and why.

---

### EXECUTIVE - someone is deciding whether to act on this

**Reader:** a decision-maker. A marketing director, a business owner, a panel. They have limited
time, no ML background, and - this is the part that changes everything - **no obligation to
acquire any.** They are not the audience for a teaching notebook written faster. They are a
different audience entirely.

**What they want:** the answer, what it's worth, how much to trust it, what could go wrong, and
what you're asking them to approve. In that order.

**Voice:** plain business language with **zero algorithm vocabulary in the main body.** Not
simplified ML terms - *absent* ML terms. No decision trees, no boosting, no F1, no ROC-AUC, no
overfitting, no hyperparameters, no `max_depth`. If a sentence can't survive the removal of the
method's name, rewrite the sentence.

Numbers appear in business units: buyers reached, budget saved, share of sales captured, lift
over current practice. "0.688 F1" means nothing to this reader. "Catches roughly three-quarters
of likely buyers" means something.

**Structure - inverted, never chronological.** The STUDENT/GRADER arc walks forward through the
work. This one starts at the destination:

1. **The finding** - one sentence, quantified, in business terms.
2. **What it's worth** - the concrete payoff against what they do today.
3. **How much to trust it** - tested on data never used to build it, stated without jargon.
4. **What could go wrong** - the honest risks, named specifically. Do not soften this; a decision-
   maker who later discovers a hidden caveat stops trusting everything else you said.
5. **The ask** - what you want them to approve, and what would prove it worked.

**What gets cut:** the entire method narrative. Which models were tried and lost, why one metric
was chosen over another, what the tuning grid showed, how the data was encoded. All of it goes to
an appendix nobody opens unless they challenge point 3.

**A worked example of how violently this cuts.** In the online-shoppers analysis, the most
interesting finding in the whole notebook was that a one-question decision tree scored a better F1
than tuned XGBoost - because the default 0.50 cutoff flattered it, while ROC-AUC showed the
opposite. That is the single highest-value passage in GRADER mode: it demonstrates real
diagnostic reasoning and would earn marks. In EXECUTIVE mode it is **deleted entirely.** Not
shortened - deleted. The executive does not care which model won or how the cutoff was chosen;
they care that targeting the top 20% of visits reaches 79% of buyers.

Same true finding. Highest-value content for one reader, zero-value for the other. When those two
pull in opposite directions, the audience declaration is what resolves it.

**Deliverable - and this is the important structural difference: an executive does not receive a
notebook.** This mode produces **two** artifacts:

- **The brief** - the primary deliverable. A short deck (roughly five slides) or a one-page memo,
  built to the inverted structure above. This is what gets presented.
- **The notebook** - still built, still executed, still verified, but demoted to *appendix*. Its
  job is to make every number in the brief defensible if challenged. Its markdown can be lean -
  the executive isn't reading it - but the numbers rule still applies absolutely.

**Self-check:** hand the brief to someone who has never heard of a decision tree. Can they say
what the recommendation is, what it's worth, and what the main risk is, without asking a single
follow-up question? If any slide needs you standing next to it to make sense, it isn't finished.

---

## Deciding the mode

Read it from the request. Signals:

- **GRADER** - a named assignment, "team assignment," a due date, "rubric," "submit," team member names, an
  assignment brief in the conversation or project knowledge.
- **STUDENT** - "practice," "exam prep," "session prep," "just want to try this," "I'm testing
  this," no deadline, no grading language.
- **EXECUTIVE** - "present this," "pitch," "for the client," "for my manager," "stakeholders,"
  "make the case," "business audience," or any framing where someone is being asked to *decide*
  rather than to *evaluate the work*.

**If it's genuinely ambiguous, ask.** Getting this wrong means rebuilding structural parts of the
artifact - not rewording it - which costs far more than one question up front.

**Two audiences can both be real.** "Build the assignment notebook and I'll present the findings to the
class" is GRADER *and* EXECUTIVE - build both artifacts rather than compromising into an
artifact that serves neither well. Say plainly which one is which when delivering them.

## State the choice in the artifact

Whichever mode is chosen, say so where the reader will see it - a line in the notebook's title
cell, or the brief's footer:

> *Written for: a reader with no machine-learning background who is deciding whether to fund a
> pilot. Method detail is in the appendix notebook.*

This costs one sentence and removes every later argument about whether the tone was right, because
the tone was declared rather than inferred.
