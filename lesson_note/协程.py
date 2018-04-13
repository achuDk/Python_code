def f():
    print("ok")
    s = yield 6
    print(s)
    print("ok2")
    yield 12

gen = f()
res = gen.__next__()
print(res)
ret = gen.send(5)
print(ret)