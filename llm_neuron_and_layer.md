# Neurons and Layers

## A Neuron

A neuron does exactly one thing: a weighted sum of its inputs plus a bias, producing a single scalar.

```
inputs:  [x1, x2, x3]
weights: [w1, w2, w3]
output:  w1x1 + w2x2 + w3x3 + b  ← one scalar
```

**The weight count is forced by the input.** A neuron needs exactly one weight per input, so `nin` inputs → `nin` weights. No choice involved.

---

## A Layer

A layer is a collection of neurons that all receive the **same input vector** and each independently produce a scalar output.

- Neurons share no weights — each neuron has its own independent weight vector and bias
- They are grouped together only because they operate on the same input
- `nout` neurons → `nout` independent dot products → `nout` scalar outputs

**Two numbers fully determine a layer:**

| Number | Determined by | Controls |
|---|---|---|
| `nin` | Your data | How many weights each neuron has |
| `nout` | Your design choice | How many outputs the layer produces |

Everything else — matrix shapes, transposes, storage layout — is just a consequence of these two numbers.

---

## The Core Insight: Everything is Dot Products

Matrix multiply is just "run all dot products simultaneously" — pure computational efficiency. The underlying operation is always:

```
1 neuron  = 1 dot product → 1 scalar
4 neurons = 4 dot products → 4 scalars
```

---

## From Dot Products to Matrix Multiply

For matrix multiply to equal running all dot products at once, **each neuron's weights must occupy one column** in the matrix at multiply time. This is the only constraint — everything else follows from it.

```
x (3,) @ W (3,4):

column 0: [w00,w01,w02]  ← neuron 0's weights → dot(x, col0) = scalar0
column 1: [w10,w11,w12]  ← neuron 1's weights → dot(x, col1) = scalar1
column 2: [w20,w21,w22]  ← neuron 2's weights → dot(x, col2) = scalar2
column 3: [w30,w31,w32]  ← neuron 3's weights → dot(x, col3) = scalar3

result: (4,)  ← one scalar per neuron ✓
```

---

## Two Ways to Store the Weight Matrix

You have 4 neurons each with 3 weights. There are two natural ways to arrange them:

**Option A — neurons as columns `(nin, nout)` = `(3,4)`:**
```
W (3,4):
col 0: [w00,w10,w20,w30]  ← all weights for neuron 0 spread down a column
col 1: [w01,w11,w21,w31]  ← all weights for neuron 1
col 2: [w02,w12,w22,w32]  ← all weights for neuron 2
col 3: [w03,w13,w23,w33]  ← all weights for neuron 3
```

Math works directly — neurons are already columns:
```
x @ W  →  (3,) @ (3,4)  →  (4,)  ✓  no transpose needed
```

But indexing is awkward: `W[:, 2]` to get neuron 2's weights (a column slice).

---

**Option B — neurons as rows `(nout, nin)` = `(4,3)`:**
```
W (4,3):
W[0] = [w00, w01, w02]  ← neuron 0's weights, all in one row
W[1] = [w10, w11, w12]  ← neuron 1's weights
W[2] = [w20, w21, w22]  ← neuron 2's weights
W[3] = [w30, w31, w32]  ← neuron 3's weights
```

Indexing is clean: `W[2]` gives you neuron 2's weights directly. Rows are also contiguous in memory — one fast read.

But neurons are now rows, not columns, so a transpose is needed before multiplying:
```
x @ W.T  →  (3,) @ (3,4)  →  (4,)  ✓  transpose required
```

---

**PyTorch chose Option B** — neurons as rows `(nout, nin)` — for readability and indexing convenience, and handles the transpose transparently inside `nn.Linear`:

```python
# What you write:
nn.Linear(3, 4)

# What PyTorch does internally:
output = x @ W.T + b    # W is (4,3), W.T is (3,4), x is (3,) → output is (4,)
```

---

## Shape Summary

```
input:         (3,)     ← 1 sample, 3 features
each neuron:   (3,)     ← one weight per feature, produces 1 scalar
weight matrix: (4,3)    ← 4 neurons stacked as rows  (PyTorch storage)
output:        (4,)     ← one scalar per neuron
```

| Thing | Shape | Why |
|---|---|---|
| Input vector | `(nin,)` | flat, one value per feature |
| Weight matrix stored | `(nout, nin)` | neurons as rows, for readability |
| Weight matrix at multiply time | `(nin, nout)` | neurons as columns, for dot products |
| Output vector | `(nout,)` | one scalar per neuron |

---

## Mental Model in Two Lines

- **input features → weights per neuron** (forced by data, no choice)
- **number of neurons → output size** (your design choice)

`nn.Linear(nin, nout)` stores `nout` weight vectors of length `nin`, stacked as rows into a `(nout, nin)` matrix, then computes `x @ W.T + b` — giving you all `nout` dot products at once.
