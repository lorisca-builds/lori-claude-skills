# ml-business-insight

**Use it when** your EDA is done and you need to know what to model and why.

Step 2 of 4 in the [ML notebook set](../README.md#ml-notebook-workflow).

## The problem

My notebooks had a gap between "I explored the data" and "here are my models." The business framing was either missing or made of empty phrases like "gain valuable insights for stakeholders." A model with no decision behind it has no way to choose a metric.

## What it does

It runs once, after cleaning and EDA and before the first model. It produces one block under 300 words that you paste above the modeling section.

1. **The decision**, in one fixed shape: "If [a specific role] knew [the target] in advance, they would [do what differently]." It has to name a person you can picture, what they do today, and what they would do instead.
2. **The one constraint** in the data that drives everything after it, with its number.
3. **Two metrics**, each justified by that constraint.
4. **The model family**, decided by the type of target.
5. **A capped plan**: three model rungs at most, one improvement lever, and a stopping condition stated up front.

## What it won't do

- Use a number that isn't in the output you pasted.
- Invent a business case. If the data doesn't support a decision anyone would act on, it says so and suggests another target or another dataset.
- Use words like "robust" or "powerful" with no comparison number behind them.

## Limits

- It needs your EDA numbers printed. Charts alone are not enough.
- It includes a prompt you can paste into Gemini in Colab if you're working there.
