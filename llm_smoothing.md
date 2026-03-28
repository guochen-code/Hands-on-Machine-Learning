Sure:

---

Our count-based bigram model assigns exactly zero probability to any bigram that never appeared in training data. This becomes a problem at evaluation time — if the validation or test set contains even one unseen bigram, the NLL becomes `inf` and you can no longer use it to rank or compare models.

**Why zero probability for unseen bigrams:**

The model learns probabilities by counting transitions and normalising:

```
P(a | q) = count(qa) / count(q?)
```

If `qa` never appeared in training, `count(qa) = 0`, so `P(a | q) = 0`. The model has no way to assign any probability to transitions it never saw.

**Why one zero makes the entire sequence's NLL inf:**

Likelihood is a product of all bigram probabilities in the sequence:

```
likelihood = P(b1) × P(b2) × P(b3) × ... × P(bn)
```

One zero anywhere kills the entire product regardless of how good every other term is:

```
0.3 × 0.5 × 0.0 × 0.8 × 0.4 = 0
```

Taking the log:

```
log(0) = -inf
NLL = -log(0) = inf
```

And since NLL is a sum of individual bigram NLLs:

```
NLL = -log(P(b1)) + -log(P(b2)) + -log(0) + ...
    = finite + finite + inf + ...
    = inf
```

One unseen bigram anywhere in the sequence makes the entire sequence's NLL `inf`, regardless of how well the model handles every other transition.

**Why inf NLL breaks model comparison:**

```
validation set contains "qzara" — unseen bigram qz

model A (trained on more data, generally better): NLL = inf
model B (trained on less data, generally worse):  NLL = inf
```

Both score `inf`. You cannot tell which model is better. `inf` swallows all information — it doesn't matter how good or bad everything else is, the score is stuck at `inf` the moment any unseen bigram appears. This makes your evaluation metric completely useless for model selection or measuring improvement.

**The fix — Laplace smoothing:**

Add a small constant (typically 1) to all counts before normalising:

```
# without smoothing
P(a | q) = 0 / count(q?) = 0

# with smoothing
P(a | q) = (0 + 1) / (count(q?) + 27) = tiny but nonzero
```

Common bigrams are barely affected — adding 1 to a count of 500 changes the probability negligibly. Unseen bigrams get a small but nonzero probability instead of zero. NLL stays finite across the entire validation set, and you can meaningfully compare models again.

---
