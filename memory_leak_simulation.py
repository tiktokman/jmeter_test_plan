import os
import psutil
import time

# 获取系统总内存量（MB）
TOTAL_MEMORY_MB = psutil.virtual_memory().total / (1024 * 1024)
# 目标内存使用率（%）
TARGET_USAGE_PERCENT = 90
# 目标内存量（MB）
TARGET_MEMORY_MB = TOTAL_MEMORY_MB * (TARGET_USAGE_PERCENT / 100)

# 用来存储大量数据的列表，模拟内存泄漏
memory_hog = []


def system_memory_usage():
    """
    获取系统整体内存使用情况的百分比
    """
    mem = psutil.virtual_memory()
    return mem.percent


def allocate_memory(target_mb):
    """
    分配内存直到达到目标内存使用量。
    """
    total_allocated = 0

    while total_allocated < target_mb:
        current_usage = system_memory_usage()  # 使用系统内存使用率
        if current_usage < 85:
            allocation_mb = 500  # 达到85%之前，每次分配500MB
        else:
            allocation_mb = 50  # 达到85%之后，每次分配50MB

        allocate_mb = min(allocation_mb, target_mb - total_allocated)  # 确保不超过目标内存

        try:
            memory_hog.append(' ' * int(allocate_mb * 1024 * 1024))  # 分配内存
            total_allocated += allocate_mb
            current_usage = system_memory_usage()  # 使用系统内存使用率
            print(f"Allocated {total_allocated:.2f} MB, Current memory usage: {current_usage:.2f}%")
        except MemoryError:
            print("MemoryError: Unable to allocate more memory, stopping allocation.")
            break

        time.sleep(0.5)  # 短暂等待后继续分配

    print("Reached target memory usage or hit memory limit.")


def maintain_memory_usage():
    """
    维持在目标内存使用率水平。
    """
    allocation_size_mb = 50  # 在接近目标时，使用50MB的块调整
    release_size_mb = 50  # 每次释放的内存块大小
    while True:
        current_usage = system_memory_usage()  # 使用系统内存使用率
        print(f"Current memory usage: {current_usage:.2f}%")

        if current_usage < TARGET_USAGE_PERCENT - 1:
            print(f"Memory usage is below target. Allocating more memory...")
            try:
                memory_hog.append(' ' * int(allocation_size_mb * 1024 * 1024))  # 每次分配50MB
            except MemoryError:
                print("MemoryError during maintenance: Unable to allocate more memory.")
        elif current_usage > TARGET_USAGE_PERCENT + 1:
            print(f"Memory usage is above target. Reducing memory...")
            release_count = 0
            while current_usage > TARGET_USAGE_PERCENT + 1 and memory_hog:
                for _ in range(release_size_mb // 50):  # 释放多个内存块
                    if memory_hog:
                        memory_hog.pop(0)  # 释放第一个分配的内存块（FIFO）
                        release_count += 1
                        print(f"Released {release_count * 50} MB, Current memory usage after release: {current_usage:.2f}%")
                current_usage = system_memory_usage()
                time.sleep(0.1)  # 更频繁地检查

        time.sleep(0.5)  # 每0.5秒检查一次


if __name__ == "__main__":
    # 快速分配内存达到目标
    allocate_memory(TARGET_MEMORY_MB)

    # 维持在目标内存使用率
    maintain_memory_usage()
