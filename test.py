import jieba
#
# with open('天龙八部.txt', errors='ignore', encoding='utf-8') as fp:
#    lines = fp.readlines()
#    for line in lines:
#        seg_list = jieba.cut(line)
#        with open('分词后的天龙八部.txt', 'a', encoding='utf-8') as ff:
#            ff.write(' '.join(seg_list))  # 词汇用空格分开

from gensim.models import word2vec

# 加载语料
sentences = word2vec.Text8Corpus('分词后的天龙八部.txt')

# 训练模型
model = word2vec.Word2Vec(sentences)
# print(type(model))
# 选出最相似的10个词
for e in model.wv.most_similar(positive=['乔峰'], topn=10):
   print(e[0], e[1])
# model.save('天龙八部.model')
# 加载模型
model = word2vec.Word2Vec.load('天龙八部.model')
# 计算两个词的相似度
print(model.wv.similarity('乔峰', '慕容复'))
# 计算两个集合的相似度
list1 = ['乔峰', '慕容复']
list2 = ['萧远山', '慕容博']
print(model.wv.n_similarity(list1, list2))
# 选出集合中不同类的词语
list3 = ['乔峰', '段誉', '虚竹', '丁春秋']
print(model.doesnt_match(list3))

# 查看词的向量值
print(type(model['乔峰']))  # 输出 <class 'numpy.ndarray'>
print(len(model['乔峰']))  # 输出 100
print(model['乔峰'])  # 输出 一行100列的向量 [-0.64503133  0.7794444 ...]