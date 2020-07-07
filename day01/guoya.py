# print(list())
# # 列表转元组
# f = open("aaa.txt",'w')
# f.write("Hello")
# f.close()
#
#
# a = "abcdefghijklmnopqrstuvwxyz"
# print(a[0])
# print(a[2:-5:4])
#
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d X %d = %d"%(j,i,i*j), end="\t")
#     print()
#
#
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{} X {} = {}".format(j,i,i*j), end="\t")
#     print()

d = {"name":"小米","age":18,"sex":"男"}

d.update({"addr":"上海闵行","学历":"本科"})
print(d)
