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

---

## The Core Insight: Everything is Dot Products

Matrix multiply is just "run all dot products simultaneously" — pure computational efficiency. The underlying operation is always:

```
1 neuron  = 1 dot product → 1 scalar
4 neurons = 4 dot products → 4 scalars
```

---

## From Dot Products to Matrix Multiply

For matrix multiply to equal running all dot products at once, **each neuron's weights must occupy one column** in the matrix at multiply time:

```
x (3,) @ W (3,4):

column 0: [w00,w01,w02]  ← neuron 0's weights → dot(x, col0) = scalar0
column 1: [w10,w11,w12]  ← neuron 1's weights → dot(x, col1) = scalar1
column 2: [w20,w21,w22]  ← neuron 2's weights → dot(x, col2) = scalar2
column 3: [w30,w31,w32]  ← neuron 3's weights → dot(x, col3) = scalar3

result: (4,)  ← one scalar per neuron ✓
```

This is the only constraint. Everything else follows from it.

---

## PyTorch's Storage Convention

PyTorch stores the weight matrix as `(nout, nin)` — neurons as **rows**, not columns:

```
W (4,3):
W[0] = [w00, w01, w02]  ← neuron 0
W[1] = [w10, w11, w12]  ← neuron 1
W[2] = [w20, w21, w22]  ← neuron 2
W[3] = [w30, w31, w32]  ← neuron 3
```

**Why rows?** Readability and indexing convenience. `W[i]` gives you neuron i's weights in one clean index. Rows are also contiguous in memory, so it's a fast read.

**The tradeoff:** neurons-as-rows requires a transpose before multiplying. PyTorch handles this transparently inside `nn.Linear`:

```
# What you write:
nn.Linear(3, 4)

# What PyTorch does internally:
output = x @ W.T + b    # W is (4,3), W.T is (3,4), x is (3,) → output is (4,)
```

---

## Shape Summary

| Thing | Shape | Why |
|---|---|---|
| Input vector | `(nin,)` | flat, no row/column concept |
| Weight matrix stored | `(nout, nin)` | neurons as rows, for readability |
| Weight matrix at multiply time | `(nin, nout)` | neurons as columns, for dot products |
| Output vector | `(nout,)` | one scalar per neuron |

---

## `nn.Linear(nin, nout)` in One Line

It stores `nout` weight vectors of length `nin`, stacked as rows into a `(nout, nin)` matrix, then computes `x @ W.T + b` — giving you all `nout` dot products at once.




---
---


input:        (3,)        ← 1 sample, 3 features
                                    
each neuron:  (3,)        ← one weight per feature, produces 1 scalar
                                    
weight matrix (4,3)       ← 4 neurons stacked, each row is one neuron
                                    
output:       (4,)        ← one scalar per neuron



- Neuron shape = (nin,) — forced by input, one weight per feature
- Layer weight shape = (nout, nin) — just nout neurons stacked as rows
- Layer output shape = (nout,) — one scalar per neuron

The number of neurons is purely your design choice. It controls how many different "summaries" of the input you want. The input dimension is forced by your data. Everything else is just a consequence of those two numbers.



That's the complete mental model in two lines:

- input features → weights per neuron (forced by data, no choice)
- number of neurons → output size (your design choice)
