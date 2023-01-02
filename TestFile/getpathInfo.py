import os

def get_Path():
    path = os.path.dirname(os.path.realpath(__file__))
    return path


if __name__ == "__main__":
    print(os.path.realpath((__file__)))
    print("测试路径返回是否OK，路径为：", get_Path())


