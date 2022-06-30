# goal
hyper-paramter optimization:
understand the probablity of certain hyper-parameters for the ML model given the evidence. 
and the evidence is given by the generalization error of the ML model given certain hyper-parameters.

# in math
a model specifies P(data|parameters) and the prior P(parameters) --->
poserior P(parameters|data)

#
Bayes's rule gets us from the prior P(A) to the posterior (conditional) distribution P(A|B) when focusing on a specific value of B

P(A|B): conditional on B 
P(B|A): conditional on A 
P(A) & P(B): unconditional

P(A|B) = P(A,B) / P(B)
P(B|A) = P(A,B) / P(A)

P(A|B) = P(B|A) * P(A) / P(B) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         Bayes's rule          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

******************************************************* How to calculate P(B) *********************************************************
P(B) = sum[P(A,B)] 
     = sum[P(A|B)*P(B)] = sum[P(B|A)*P(A)]
     = sum[P(A1,B),P(A2,B),P(A3,B)........] *******************************************************************************************
