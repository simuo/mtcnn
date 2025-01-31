import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from src.MtcnnTrain import trainer
from src.myNet import R24Net

if __name__ == '__main__':
    trainer = trainer(R24Net(), '../models/rnet.pth', r'F:\celeba3\24', '../log/Rlog.txt')
    trainer.train()
