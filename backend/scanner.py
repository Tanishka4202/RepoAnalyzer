import os
import ast
from metrics import get_complexity


def get_loc(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return len(f.readlines())
    except:
        return 0


def get_python_dependencies(filepath):
    dependencies = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):
                for alias in node.names:
                    dependencies.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    dependencies.append(node.module)

    except:
        pass

    return dependencies


def scan_repository(path):

    nodes = []
    edges = []

    allowed_extensions = (".py",)

    for root, dirs, files in os.walk(path):

        for file in files:

            if not file.endswith(allowed_extensions):
                continue

            filepath = os.path.join(root, file)

            nodes.append({
    "id": file,
    "label": file,
    "loc": get_loc(filepath),
    "complexity": get_complexity(filepath)
})
            dependencies = get_python_dependencies(filepath)

            for dep in dependencies:

                target = dep + ".py"

                edges.append({
                    "source": file,
                    "target": target
                })

    return {
        "nodes": nodes,
        "edges": edges
    }