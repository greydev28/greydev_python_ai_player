# Part 11 — Deep Learning with PyTorch

## Core concepts
A tensor is a multidimensional array. A neural network applies parameterised transformations and nonlinear activation functions. A loss function measures prediction error. Backpropagation calculates gradients; an optimiser updates parameters to reduce loss.

A standard training loop:
1. Put the model in training mode.
2. Clear old gradients.
3. Run a forward pass.
4. Calculate loss.
5. Backpropagate gradients.
6. Update parameters.
7. Track metrics on validation data.
8. Save the best checkpoint and evaluate on held-out test data.

Use `model.eval()` and `torch.no_grad()` for inference/evaluation as appropriate. Separate training and validation data. Watch for overfitting: training performance improves while validation performance stagnates or worsens.

## Learning path
Start with tensors and datasets, then build a small neural network, learn autograd and optimisation, and save/load a model. Follow the official PyTorch beginner tutorials linked in the repository README. Begin with CPU-sized datasets; a GPU is not required to learn fundamentals.

## Exercises
1. Create tensors, inspect shapes, and perform matrix multiplication.
2. Train a tiny classifier on a standard dataset.
3. Plot training and validation loss per epoch.
4. Save a model state and load it to reproduce predictions.
5. Compare a neural network with a simpler scikit-learn baseline.
6. Explain overfitting and try one regularisation method.

## Greydev Advanced Challenge — Deep Learning Experiments

1. Build a small PyTorch classifier with separate training, validation, and test sets. Record the random seed and all important experimental settings.
2. Plot training and validation loss/metrics. Diagnose underfitting and overfitting and run a controlled experiment changing one factor at a time.
3. Compare at least one regularisation or optimisation change against a baseline. Explain the evidence rather than declaring the changed model better from one run.
4. Save a checkpoint containing model parameters and the configuration needed to reproduce the experiment. Load it in a fresh process and verify predictions.
5. Compare the neural network with a simpler baseline on the same split and metric. Discuss data size, compute, interpretability, and whether deep learning is justified.
6. Deliberately create a tensor shape error, explain the traceback, and fix it by reasoning about dimensions rather than trial-and-error reshaping.

