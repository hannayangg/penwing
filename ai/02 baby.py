import numpy as np
X = [[0.56821476],[0.30541418],[0.35010836],[0.44191363],[0.45326883],
     [0.54870102],[0.50402217],[0.55111746],[0.50937959],[0.44867542],
     [0.56906268],[0.4975468 ],[0.43701401],[1.        ],[0.27261929],
     [0.6737199 ],[0.47905837],[0.56340487],[0.30353893],[0.31730837],
     [0.01097152],[0.01406849],[0.00549036],[0.00792982],[0.00403473],
     [0.        ],[0.00545068],[0.03441932],[0.16156788],[0.16157684],
     [0.15829597],[0.13953834],[0.144235  ],[0.05382088],[0.06238467],
     [0.05558972],[0.06395295],[0.06336643],[0.04250992],[0.06120087]]
y = np.zeros((40,1))
y[:20,:]=1

# 랜덤 beta0,1

def Sigmoid(X):
    return 1 / (1+np.exp(-X))

def cost(X,y):
    delta = 1e-7
    temp = beta0 + np.dot(X,beta1)
    f = Sigmoid(temp)
    return -np.sum(y*np.log(f+delta) + (1-y)*np.log(1-f+delta))

def numerical_derivative(f, x):
  delta_x = 1e-4
  grad = np.zeros_like(x)
  it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
  while not it.finished:
    idx = it.multi_index        
    tmp_val = x[idx]
    x[idx] = float(tmp_val) + delta_x
    fx1 = f(x)
    x[idx] = tmp_val - delta_x 
    fx2 = f(x) 
    grad[idx] = (fx1 - fx2) / (2*delta_x)
    x[idx] = tmp_val 
    it.iternext()          
  return grad

def predict(X):
    temp = beta0 + np.dot(X,beta1)
    f = Sigmoid(temp)
    if f >= 0.79:
        return 1
    else:
        return 0

# 학습률
learning_rate = 0.01
beta0 = np.random.rand(1)
beta1 = np.random.rand(1,1)
F = lambda x : cost(X,y)

# cost함수의 최솟값을 만드는 beta1,0 찾기
for step in range(10001):
    beta1 -= learning_rate*numerical_derivative(F,beta1)
    beta0 -= learning_rate*numerical_derivative(F, beta0)
print(beta0, beta1)

# 찾아낸 beta1,0을 넣은 예측함수로 예측해보기
# float 을 안하면 0.003이 아니라 "0.003"문자로 인식함
X = float(input("0과 1 사이 숫자입력"))
X = [X]
print(predict(X))