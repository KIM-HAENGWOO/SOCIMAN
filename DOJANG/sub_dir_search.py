import os

# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]  # [1]도 동일한 결과? 
#                 if ext == '.py':
#                     print(full_filename)
#     except PermissionError:
#         pass

# search("/Users/haengwoomac/CloudStation/SOCIMAN/DOJANG")

for (path, dir, files) in os.walk('/Users/haengwoomac/CloudStation/SOCIMAN/DOJANG'):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))
            