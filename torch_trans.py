torch.manual_seed(1337)
batch_size = 4 # how many independent sequences will we process in parallel?
block_size = 8 # what is the maximum context length for predictions?

def get_batch(split):
    # generate a small batch of data of inputs x and targets y
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x, y                                                      # x is input to transformer !!!!!!!!!!

############################################################################################################
ix = torch.randint(len(data) - block_size, (batch_size,))

# torch.randint(low=0, high, size, .....)
# Returns a tensor filled with random integers generated uniformly between low (inclusive) and high (exclusive)
'''
>>> torch.randint(3, 5, (3,))
tensor([4, 3, 4])

>>> torch.randint(10, (2, 2))
tensor([[0, 2],
        [5, 5]])

>>> torch.randint(3, 10, (2, 2))
tensor([[4, 5],
        [6, 7]])
'''
############################################################################################################
x = torch.stack([data[i:i+block_size] for i in ix])

# Concatenates a sequence of tensors along a new dimension.
# All tensors need to be of the same size.
train_data ---> tensor([18, 47, 56,  ..., 43, 56, 43])
train_data[0:5] ---> tensor([18, 47, 56, 57, 58])
torch.stack([train_data[0:5],train_data[0:5]]) --->  tensor([[18, 47, 56, 57, 58],[18, 47, 56, 57, 58]])

############################################################################################################
