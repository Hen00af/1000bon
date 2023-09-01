def word_bi_gram(s):
  word_list=s.split();
  result=[]
  for i in range(len(word_list)-1):
    result.append(" ".join([word_list[i],word_list[i+1]]))
  return result
sentence="i like an apple!!"

print("words: ", word_bi_gram(sentence))
