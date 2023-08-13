################################################################################################################################ save and load model
# save model 
torch.save(model.state_dict(),'model.pth.tar')

# load model
import torch
from your_model_module import YourModelClass

# Load the model's state dictionary
model = YourModelClass()
model.load_state_dict(torch.load('model.pth.tar'))

# Set the model to evaluation mode
model.eval()

'''
In PyTorch, calling model.eval() is important when you want to set the model in evaluation mode rather than training mode. This is necessary because certain layers and operations behave differently during training and evaluation, and you want to ensure that the model behaves as expected when making predictions on new data. Here's why model.eval() is used after loading the model state dictionary:

Batch Normalization and Dropout: During training, layers like Batch Normalization and Dropout apply different operations compared to evaluation. Batch Normalization uses batch statistics during training and population statistics during evaluation. Dropout randomly drops units during training but does nothing during evaluation. Setting the model in evaluation mode ensures that these layers behave as intended during inference.

Inference Consistency: If you don't set the model to evaluation mode after loading its state dictionary, the model might produce inconsistent results during inference due to the differences in layer behavior mentioned above.

Gradients and Autograd: When the model is set to evaluation mode, the requires_grad attribute of model parameters remains unchanged. This is important because during evaluation, you don't want the model's parameters to accumulate gradients, which could affect memory consumption and performance.

However, in TensorFlow, there is no direct equivalent to PyTorch's model.eval() when loading a model. This is because TensorFlow's layers and operations inherently behave the same way during both training and inference, unlike in PyTorch where some layers have different behaviors depending on the mode.

TensorFlow's layers and operations are designed to automatically adapt to the inference mode when you call them after loading a saved model. 

There's no need for an equivalent of model.eval() in TensorFlow. The loaded model is ready for inference without any additional steps.
'''

################################################################################################################################ stop and resume training
model = CNN().cuda()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
checkpoint={'epoch':1,
            'model_state_dict':model.state_dict(),
            'optimizer_state_dict':optimizer.state_dict(),
            'loss':0.2}
torch.save(checkpoint, 'model.pth.tar')

model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']

# if testing
model.eval()
# if resume training
model.train()
            
            



























