import re


class Node:
    def __init__(self, name):
        self.name = name

    @property
    def size(self):
        raise NotImplementedError


class File(Node):
    def __init__(self, name, parent, size_val):
        super().__init__(name)
        self.parent = parent
        self.size_val = size_val

    @property
    def size(self):
        return self.size_val


class Folder(Node):
    def __init__(self, name, parent):
        super().__init__(name)
        self.parent = parent
        self.children = {}
        self.size_value = None

    @property
    def size(self):
        if self.size_value is None:
            # update
            self.size_value = sum(c.size for c in self.children.values())
        return self.size_value


def pick_folders(node, max_size, picked=None):
    if picked is None:
        picked = []

    for name, c in node.children.items():
        if isinstance(c, Folder):
            if c.size < max_size:
                picked.append(c)
            pick_folders(c, max_size, picked)
    return picked


def find_delete(node, current_size, target_size, min_size=None):
    if min_size is None:
        min_size = target_size

    for name, c in node.children.items():
        if isinstance(c, Folder):
            if current_size - c.size <= target_size:
                min_size = min(min_size, c.size)
            min_size = min(min_size, find_delete(c, current_size, target_size, min_size))

    return min_size


STATE_START = 0
STATE_IDLE = 1
STATE_LISTING = 2
STATE_DONE = 3


def main():
    node = None
    node_root = None

    reread = False

    with open("day07_input.txt", "r") as f:
        state = STATE_START
        # print(state, node.name if node is not None else node)
        while state != STATE_DONE:
            if reread:
                reread = False
            else:
                line = f.readline().strip()
            if state == STATE_START:
                # root has no parents
                node = Folder("/", None)
                state = STATE_IDLE
                node_root = node
            elif state == STATE_IDLE:
                m = re.match(r"^\$ ls$", line)
                if m is not None:
                    state = STATE_LISTING
                    continue
                m = re.match(r"^\$ cd (.+)$", line)
                if m is not None:
                    folder_name = m.group(1)
                    if folder_name == "..":
                        node = node.parent
                    else:
                        node = node.children[folder_name]
                    continue
                state = STATE_DONE
            elif state == STATE_LISTING:
                m = re.match(r"^dir (.+)$", line)
                if m is not None:
                    new_name = m.group(1)
                    node.children[new_name] = Folder(new_name, node)
                    continue
                m = re.match(r"^(\d+) (.+)$", line)
                if m is not None:
                    new_size = int(m.group(1))
                    new_name = m.group(2)
                    node.children[new_name] = File(new_name, node, new_size)
                    continue

                # back to IDLE, reread this line
                state = STATE_IDLE
                reread = True
                continue

    folders_picked = pick_folders(node_root, max_size = 100000)

    print(sum([c.size for c in folders_picked]))

    total_size = 70000000
    needed_space = 30000000

    min_size = find_delete(node_root, node_root.size, total_size-needed_space)
    print(min_size)


if __name__ == "__main__":
    main()
