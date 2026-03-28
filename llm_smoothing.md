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


Good question. Let me build it from scratch.

**What "too confident" means:**

Without smoothing, the model says:
```
P(qz) = 0        ← absolutely impossible, 100% confident
P(ma) = 0.3      ← seen many times
```

Assigning exact zero means the model is infinitely confident that `qz` can never happen. But that's not justified — just because it didn't appear in training doesn't mean it's truly impossible. The model is **overfitting to the training data** by treating "never seen" as "can never exist."

---

**How smoothing fixes overconfidence:**

```
P(qz) = tiny but nonzero   ← possible, just unlikely
P(ma) = 0.3 - tiny         ← slightly less than before
```

You're essentially saying "I'm not 100% sure about anything — even unseen things have some small chance." This is more honest about the model's uncertainty.

---

**How this connects to neural network regularisation:**

In neural networks, regularisation (L2/dropout) prevents the model from becoming too confident about its training data specifically:

```
without regularisation: model memorises training data exactly → overfits
with regularisation:    model is forced to be slightly less certain → generalises better
```

Smoothing does the same thing for count-based models:

```
without smoothing: model memorises "unseen = impossible" → breaks on new data
with smoothing:    model hedges slightly → handles new data gracefully
```

Both are trading a tiny bit of accuracy on known cases to gain robustness on unknown cases. That's the conceptual connection — they're both solutions to overconfidence, just in different model types.
