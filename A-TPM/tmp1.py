def expand_groups(groups, total_boxes=6):
    """
    根据传入的 groups 列表自动扩展分组方案，以确保总箱子数为 total_boxes。
    如果 groups 的总箱子数超过 total_boxes，则截取多余的部分。

    参数:
        groups (list): 用户传入的初始分组。
        total_boxes (int): 总箱子数，默认是6。

    返回:
        list: 完整的分组方案，确保总箱子数为 total_boxes。
    """
    current_count = sum(groups)

    # 如果当前分组总箱子数超过 total_boxes，截取前面的部分使其等于 total_boxes
    if current_count > total_boxes:
        trimmed_groups = []
        box_count = 0
        for group_size in groups:
            if box_count + group_size > total_boxes:
                # 截取最后一组的部分，使总数刚好等于 total_boxes
                trimmed_groups.append(total_boxes - box_count)
                break
            trimmed_groups.append(group_size)
            box_count += group_size
        return trimmed_groups

    # 如果当前分组已涵盖所有箱子，直接返回
    if current_count == total_boxes:
        return groups[:]

    # 计算剩余箱子数量，并用最后一个组大小填充
    remaining_boxes = total_boxes - current_count
    last_group_size = groups[-1]
    expanded_groups = groups + [last_group_size] * (remaining_boxes // last_group_size)

    # 如果有剩余箱子不足以形成一个完整组，单独加一个组
    if sum(expanded_groups) < total_boxes:
        expanded_groups.append(total_boxes - sum(expanded_groups))

    return expanded_groups


def calculate_distances(groups):
    """
    计算每个箱子的移动距离，组间和组内均有偏移。

    参数:
        groups (list): 用户传入的初始分组。

    返回:
        list: 每个箱子移动的距离。
    """
    expanded_groups = expand_groups(groups)

    distances = []
    base_distance = 200  # 组间的初始距离
    increment = 100  # 每组的距离递增
    intra_group_offset = 5  # 组内偏移

    for i, group_size in enumerate(expanded_groups):
        group_distance = base_distance + increment * i  # 每组的初始距离
        # 为当前组的每个箱子计算偏移量
        for j in range(group_size):
            distances.append(group_distance + intra_group_offset * j)

    return distances


# 示例调用
groups = [2, 3, 3]  # 希望的分组数，原本有8个箱子，应自动截取至6个
distances = calculate_distances(groups)
print("每个箱子移动的距离:", distances)
