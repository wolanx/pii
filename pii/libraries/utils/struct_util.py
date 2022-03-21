class DictUtil:
    @staticmethod
    def merge(a, b, path=None):
        """
        merges b into a
        dict1 = {1:{"a":{A}}, 2:{"b":{B}}}
        dict2 = {2:{"c":{C}}, 3:{"d":{D}}
        dict3 = {1:{"a":{A}}, 2:{"b":{B},"c":{C}}, 3:{"d":{D}}}
        """
        if path is None:
            path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    DictUtil.merge(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass  # same leaf value
                else:
                    raise Exception("Conflict at %s" % ".".join(path + [str(key)]))
            else:
                a[key] = b[key]
        return a


class DotDict(dict):
    def get(self, k, default=None):
        v = super().get(k)
        if v is None:
            try:
                v = self.gets(k)
            except AttributeError:
                v = default
            self.__setitem__(k, v)
        return v if v is not None else default

    def gets(self, name):
        arr = name.split(".")
        i_ = 0
        l_ = len(arr)
        d_ = super()
        while i_ < l_:
            d_ = d_.get(arr[i_])
            i_ = i_ + 1

        return d_


if __name__ == "__main__":
    # with open(r"./a.yml") as file:
    #     data = yaml.load(file, Loader=yaml.FullLoader)
    data = DotDict({"server": {"port": 123123}, "info": "qweqwe"})

    print(data.get("server.port"))
    print(data.get("info"))
