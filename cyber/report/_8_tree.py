import os
from graphviz import Digraph
import argparse

def generate_file_tree(path, max_files=10):
    tree = {}
    if os.path.isdir(path):
        tree[os.path.basename(path)] = []
        files = os.listdir(path)
        if len(files) > max_files:
            tree[os.path.basename(path)].extend(files[:5])
            tree[os.path.basename(path)].append("...")
            tree[os.path.basename(path)].extend(files[-5:])
        else:
            for file in files:
                file_path = os.path.join(path, file)
                if os.path.isdir(file_path):
                    tree[os.path.basename(path)].append(generate_file_tree(file_path))
                else:
                    tree[os.path.basename(path)].append(file)
    return tree

def visualize_file_tree(tree, graph=None, depth=0, ellipsis_count=0):
    colors = ['#FFD700', '#FFDA40', '#FFDD80', '#FFE0BF', '#FFE3FF']
    if graph is None:
        graph = Digraph()
        graph.attr(rankdir='LR')  # 设置文件树方向为从左到右
    for key in tree:
        color = colors[min(depth, len(colors)-1)]
        graph.node(key, style='filled', fillcolor=color)
        for value in tree[key]:
            if isinstance(value, dict):
                sub_key = list(value.keys())[0]
                graph.edge(key, sub_key)
                _, ellipsis_count = visualize_file_tree(value, graph, depth+1, ellipsis_count)
            elif value == "...":
                ellipsis_id = f"ellipsis_{ellipsis_count}"
                graph.node(ellipsis_id, label="...", style='filled', fillcolor=color)
                graph.edge(key, ellipsis_id)
                ellipsis_count += 1
            else:
                graph.node(value, style='filled', fillcolor='#ADD8E6')
                graph.edge(key, value)
    return graph, ellipsis_count

def main()
    parser = argparse.ArgumentParser(description='Get script info')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing scripts')
    parser.add_argument('output', type=str, help='Path to the output HTML file')
    args = parser.parse_args()
    tree = generate_file_tree(args.folder_path)
    graph, _= visualize_file_tree(tree)
    graph.render(args.output, view=False)

if __name__ == '__main__':
    main()