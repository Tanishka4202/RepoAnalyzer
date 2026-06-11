from radon.complexity import cc_visit


def get_complexity(filepath):

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        result = cc_visit(code)

        total = sum(item.complexity for item in result)

        return total

    except:
        return 0