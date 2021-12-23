from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertModel, BertForMaskedLM
import csv
import pandas as pd
import os
import torch
import pandas as pd
import sklearn
from transformers import BertModel, BertTokenizer
import numpy as np
import torch.nn as nn


# media:1 , green group:2 , government:3 , subcontractor:4 , political party:5 , NGO:6
# worker:7 , consultant:8 , surveyor:9 , environmental group:10 , community:11 , resident:12
# designer:13 , contractor:14

def read_data_from_csv(path):
    assert os.path.exists(path), f'File not found: {path}!'
    assert os.path.splitext(path)[
               -1] == '.csv', f'Unsupported file type {os.path.splitext(path)[-1]}!'

    data = pd.read_csv(path)
    data.dropna()
    column_list = data.columns.values.tolist()

    if 'label' in column_list:
        column_list.remove('label')
        X = data[column_list].values
        y = data['label'].astype('int').values
        return X, y
    else:
        X = data[column_list].values
        return X


# 采用bert微调策略,在反向传播时一同调整BERT和线性层的参数，使bert更加适合分类任务
class BertClassfication(nn.Module):
    def __init__(self):
        super(BertClassfication, self).__init__()
        self.model_name = 'hfl/chinese-bert-wwm'
        self.model = BertModel.from_pretrained(self.model_name)
        self.tokenizer = BertTokenizer.from_pretrained(self.model_name)
        self.fc = nn.Linear(768, 14)  # 768取决于BERT结构，2-layer, 768-hidden, 12-heads, 110M parameters

    def forward(self, x):  # 这里的输入是一个list
        batch_tokenized = self.tokenizer.batch_encode_plus(x, add_special_tokens=True,
                                                           max_length=148,
                                                           pad_to_max_length=True)  # tokenize、add special token、pad
        input_ids = torch.tensor(batch_tokenized['input_ids'])
        attention_mask = torch.tensor(batch_tokenized['attention_mask'])
        hiden_outputs = self.model(input_ids, attention_mask=attention_mask)
        outputs = hiden_outputs[0][:, 0, :]  # [0]表示输出结果部分，[:,0,:]表示[CLS]对应的结果
        output = self.fc(outputs)
        return output

model = BertClassfication()
X, Y = read_data_from_csv('data.csv')
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.2)
batch_size = 64
batch_count = int(len(Xtrain) / batch_size)
batch_train_inputs, batch_train_targets = [], []
for i in range(batch_count):
    batch_train_inputs.append(Xtrain[i * batch_size: (i + 1) * batch_size])
    batch_train_targets.append(Ytrain[i * batch_size: (i + 1) * batch_size])

# print(batch_train_inputs)
# 定义训练过程
bertClassfication = BertClassfication()
lossFuction = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(bertClassfication.parameters(), lr=2e-5)
epoch = 5
batch_count = batch_count
print_every_batch = 5
for _ in range(epoch):
    print_avg_loss = 0
    for i in range(batch_count):
        inputs = batch_train_inputs[i]
        targets = torch.tensor(batch_train_targets[i])
        optimizer.zero_grad()
        outputs = bertClassfication(inputs)
        loss = lossFuction(outputs, targets)
        loss.backward()
        optimizer.step()

        print_avg_loss += loss.item()
        if i % print_every_batch == (print_every_batch - 1):
            print("Batch: %d, Loss: %.4f" % ((i + 1), print_avg_loss / print_every_batch))
            print_avg_loss = 0

# 验证
hit = 0
total = len(Xtest)
for i in range(total):
    outputs = model([Xtest[i]])
    _, predict = torch.max(outputs, 1)
    if predict == Ytest[i]:
        hit += 1
print('准确率为%.4f' % (hit / len(Xtest)))
