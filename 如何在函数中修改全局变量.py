#
# v = 10
#
# def f():
#     global v
#     v = 100
#
# f()
# print(v)

# def func(**kwargs):
#    for i in kwargs:
#        print(i,kwargs[i])
# func(a=1,b=2,c=7)

# def squares(n):
#    i=1
#    while(i<=n):
#        yield i**2
#        print(i,"000")
#        i+=1
# for i in squares(5):
#     print(i)

# def coin(n):
#     f = [2**31 for _ in range(n+1)]
#     f[0] = 0
#     for i in range(1, n+1):
#         if i - 1 >= 0:
#             f[i] = min(f[i-1]+1, f[i])
#         if i - 5 >= 0:
#             f[i] = min(f[i - 5] + 1, f[i])
#         if i - 11 >= 0:
#             f[i] = min(f[i - 11] + 1, f[i])
#
#
#     return f
#
#
# print(coin(110))

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
