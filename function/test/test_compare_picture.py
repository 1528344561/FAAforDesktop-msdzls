import cProfile

from function.common.bg_p_compare import find_p_in_w
from function.get_paths import paths
from function.script.scattered.gat_handle import faa_get_handle


def f_test():
    handle = faa_get_handle(channel="深渊之下 | 锑食", mode="flash")
    target_path = paths["picture"]["common"] + "\\底部菜单\\跳转_竞技场.png"
    # target_path = cv2.imdecode(np.fromfile(target_path, dtype=np.uint8), -1)
    for i in range(100):
        find_p_in_w(
            raw_w_handle=handle,
            # raw_range=[0, 0, 2000, 2000],
            raw_range=[0, 0, 950, 600],
            target_path=target_path,
            target_tolerance=0.95
        )


cProfile.run("f_test()")

"""
裁剪与否的性能提升:
完全不裁剪, 从[1425 x 894]找[113 x 45] 1000次
4通道每次耗时 68s
3通道每次耗时 56s

进行裁剪, 从[900 x 600]找[113 x 45] 1000次
4通道每次耗时 34s
3通道每次耗时 28s

计算方法:
结论 通过减少比对的像素数量 能成正比减少运算时间

预加载图像文件对性能的提升 从[900 x 600]找[113 x 45] 1000次
不预加载:38.5s
预加载:37.5s
"""
