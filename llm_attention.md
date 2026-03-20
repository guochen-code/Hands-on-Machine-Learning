Input:
(B, T) tokens

→ embedding + positional
(B, T) → (B, T, C)

→ linear projection → Q, K, V
(B, T, C) → (B, T, C) each

→ reshape/split into heads
(B, T, C) → (B, T, h, A) → (B, h, T, A)

→ attention (per head):
Q: (B, h, T, A)
K: (B, h, T, A)
V: (B, h, T, A)

Q @ K^T:
(B, h, T, A) @ (B, h, A, T)
→ (B, h, T, T)

→ / sqrt(A)
→ softmax (along last dim)

→ @ V:
(B, h, T, T) @ (B, h, T, A)
→ (B, h, T, A)

→ merge heads:
(B, h, T, A) → (B, T, h·A) = (B, T, C)



| Perspective          | Focus         | What it explains                                                      |
| -------------------- | ------------- | --------------------------------------------------------------------- |
| Variance / magnitude | Forward pass  | Without scaling, logits grow with head_size → softmax becomes peaky   |
| Gradient stability   | Backward pass | Without scaling, softmax saturation → small gradients → slow learning |



✅ So, both explanations are correct, just highlighting different aspects:

- Variance perspective → “why logits explode as d grows”

- Gradient perspective → “why exploding logits cause slow training”

- 

A scientific mindset here is:

separate what the model should learn

from how the computation behaves numerically

remove dependencies on arbitrary parameterization

preserve invariances

→ final linear:
(B, T, C) @ (C, C)
→ (B, T, C)

= attention output
