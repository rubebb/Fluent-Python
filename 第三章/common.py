# 实例 3-8 StrKeyDict0 在查找键时把非字符串键转换成字符串（见示例3-7中的测试）

# class StrKeyDict0(dict):

    # def __missing__(self, key):
    #     if isinstance(key, str):
    #         raise KeyError(key)
    #     return self[str(key)]
    #
    # def get(self, key, default=None):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         return default
    #
    # def __contains__(self, key):
    #     return key in self.keys() or str(key) in self.keys

# 实例 3-9 StrKeyDict0 在插入、更新、查找时，始终把非字符串键转换成str类型
from collections import UserDict

class StrKeyDict0(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data
        # return key in self.keys() or str(key) in self.

    def __setitem__(self, key, item):
        self.data[str(key)] = item
