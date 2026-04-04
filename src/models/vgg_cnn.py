import torch
import torch.nn as nn

class VGGTelemetery(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1=nn.Conv2d(1,32,kernel_size=3,padding=1)
        self.bn1=nn.BatchNorm2d(32)
        self.pool1=nn.MaxPool2d(kernel_size=(1,2))

        self.conv2=nn.Conv2d(32,64,kernel_size=3,padding=1)
        self.bn2=nn.BatchNorm2d(64)
        self.pool2=nn.MaxPool2d(kernel_size=(1,2))

        self.fc1=nn.Linear(64*5*5,256)
        self.dropout1=nn.Dropout(0.5)
        self.fc2=nn.Linear(256,2)
    
 
        


