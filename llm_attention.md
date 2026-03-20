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

→ final linear:
(B, T, C) @ (C, C)
→ (B, T, C)

= attention output
