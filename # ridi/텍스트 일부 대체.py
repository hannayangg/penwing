# 대체하기
# re.sub(pattern, new_text, text)
# text에서 pattern에 맞는 부분을 new_text으로 대체하라.

# 1)
text = "123abc456"
text_substituted = re.sub(r'[1-3]', '', text)
# 123abc456 에사 r'[1-3]'이라는 패턴을 찾아 공백('')으로 바꾼다.
print("1: ", text_substituted)

# 2)
text = "Bob did it."
text_substituted = re.sub(r'[^\w]', '', text) # r'[^\w]' -> '' 대체
print("2: ", text_substituted)

# 여기서 주의할 점.
# Bob --- did 사이의 공백 또한 문자가 아니므로 대체할 대상에 들어간다.
# ''으로 대체할 경우, 공백 부분도 사라진다.
# ' '으로 대체할 경우, 공백 부분은 공백으로 대체된다.
# 즉, 공백을 그대로 두고 싶다면, '' 이 아니라 ' '으로 대체해야 한다.

# 3)
text = "Bob did it."
text_substituted = re.sub(r'[^\w]', ' ', text) # r'[^\w]' -> '' 대체
print("3: ", text_substituted)


# 4) 소문자로 바꾼다.
text = "Bob did it."
text_substituted = re.sub(r'[^\w]', ' ', text).lower()
print("lower: ", text_substituted)

# 5) split을 이용해 단어를 쪼개어 리스트에 담는다.
text = "Bob did it."
text_substituted = re.sub(r'[^\w]', ' ', text).lower().split()
print("split: ", text_substituted)



para = "Bob hit a ball, the hit BALL flew far after it was hit."
import re
words = re.sub(r'[^\w]', ' ', para).lower().split()
print(words)

# 딕셔너리를 만들어서 하는 대신 counter 사용함.
import collections
counts = collections.Counter(words)
print(counts.most_common(1)) # most_common(1) 흔한 단어의 가장 첫번째 값
print(counts.most_common(1)[0])
print(counts.most_common(1)[0][0])