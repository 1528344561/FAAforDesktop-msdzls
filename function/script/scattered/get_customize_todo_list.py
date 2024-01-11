import os

from function.get_paths import paths


def get_customize_todo_list(with_extension):
    """
    :param with_extension: Include extension name
    :return: a list of battle plan
    """
    my_list = os.listdir(paths["customize_todo"] + "\\")

    # 只保留json
    new_list = []
    for i in range(len(my_list)):
        if my_list[i].split(".")[-1] == "json":
            new_list.append(my_list[i])
    my_list = new_list

    # 根据参数 是否保留后缀
    if with_extension:
        return my_list
    else:
        for i in range(len(my_list)):
            my_list[i] = my_list[i].split(".")[0]
        return my_list

if __name__ == '__main__':
    def main():
        my_list = get_customize_todo_list(with_extension=False)
        print(my_list)

    main()