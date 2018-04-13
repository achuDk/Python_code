# test = "aleX"
# v1 = test.capitalize()
# print(v1)
# v2 = test.swapcase()
# print(v2)
# v3 = test.lower()
# print(v3)
# v4 = test.casefold()
# print(v4)
# v5 = test.upper()
# print(v5)

# test = "aleX"
# v1 = test.center(20,"*")
# print(v1)
# v2 = test.ljust(20,"*")
# print(v2)
# v3 = test.rjust(20,"*")
# print(v3)
# v4 = test.zfill(20)
# print(v4)
#
# test = "aleXxelaaleX"
# v1 = test.count("eX")
# print(v1)
# v2 = test.count('X',2,-1)
# print(v2)
#
# test = "tomcat"
# v1 = test.startswith("to")
# print(v1)
# v2 = test.startswith("T")
# print(v2)
# v3 = test.endswith("at")
# print(v3)

# test = "id\tusername\tage\n1\ttom\t12\n2\tjerry\t13"
# v = test.expandtabs(10)
# print(v)

# test = "alexxelaeaasdfkjales"
# v1 = test.find("le")
# print(v1)
# v2 = test.find("ax")
# print(v2)

# test = "alexxelaalxe"
# v1 = test.index("al")
# print(v1)

# test = "i am {name} , age {n}"
# v1 = test.format(name="tom",n=18)
# v2 = test.format_map({"name":"jerry","n":19})
# print(v1,"\n",v2)

# test = "{name} is {describe}"
# v1 = test.format(name="tom", describe="friendly")
# v2 = test.format(name="jerry", describe="kind")
# print(v1, "\n", v2)

# test = "{0} is a {2} {1}"
# v = test.format("alex", "teacher", "good")
# print(v)
#
# test = "{0} {1} {2} {3}"
# v1 = test.format("where", "are", "you","from")
# v2 = test.format("you",",", "a", "damn", "fool")
# print(v1, "\n", v2)

# test = "2②二"
# v = test.isnumeric()
# print(v)

# test = "abc12你3好"
# v = test.isalnum()
# print(v)
#
# test = "ab\nc"
# v = test.isprintable()
# print(v)

# test = " \t\n "
# v = test.isspace()
# print(v)

# test = "Abc Are Alpha"
# v = test.istitle()
# print(v)

# test1 = "你是风儿我是沙"
# test2 = "**"
# v = test2.join(test1)
# print(v)

# test = "aleX"
# v = test.islower()
# print(v)
# test = "aleX"
# test = test.lower()
# v = test.islower()
# print(v)

# test = "alExz"
# v1 = test.strip("bzcawxlde")
# print(v1)
# v2 = test.strip("lE")
# print(v2)

# test1 = "\nabc"
# test2 = "abc\t"
# test3 = "  abc  "
# v1 = test1.lstrip()
# v2 = test2.rstrip()
# v3 = test3.strip()
# print(v1,"\n",v2,"\n",v3)

# test1 = "alknv,zxcvl;kajwpijklansnzxc,vnlk;wejrqoin"
# test2 = test1.maketrans("aeiounlk;,","12345789 _")
# v = test1.translate(test2)
# print(v)

# test = "asdfasdfasdf"
# v = test.rpartition("s")
# print(v)

# test = "asdfasdfasdf"
# v1 = test.split("s")
# print(v1)
# v2 = test.split("sd")
# print(v2)
# v3 = test.split("s",2)
# print(v3)

# test = "asdf\nasdf\nwetahfhgh\n"
# v1 = test.splitlines(True)
# v2 = test.splitlines(False)
# print(v1,"\n",v2)

# test = "abcdef"
# v1 = test.startswith("ab")
# v2 = test.endswith("fg")
# print(v1,v2)

# test1 = "abc_123"
# test2 = "a b c*123"
# v1 = test1.isidentifier()
# v2 = test2.isidentifier()
# print(v1,v2)

test = "abcdef"
v = test.replace("bcd","xxyyzz+-*")
print(v)





# li = [11,22,33,44,55]
# v = li.append([66,77])
# v = li.extend([88,99])
# v = li.extend("不得了")
# print(li)
