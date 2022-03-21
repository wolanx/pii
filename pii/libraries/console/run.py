import argparse
from importlib import import_module

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("script", nargs="?", type=str)
    args = parser.parse_args()

    script: str = args.script
    scriptArr = script.split(".")

    pkg_name = "{0}.{1}".format(scriptArr[0], scriptArr[1])
    cls_name = scriptArr[2]
    func_name = scriptArr[3]

    pkg = import_module(pkg_name)
    cls = getattr(pkg, cls_name)
    obj = cls()
    func = getattr(obj, func_name)
    func()
