import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[5,6],[7,8]])
variable = Variable(tensor, True)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)

print(t_out)
print(v_out)