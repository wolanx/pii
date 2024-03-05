- 回归
    - [x] 线性回归 y = kx + b
        - 为什么需要..(实现不了)，怎么做..
    - [x] 多维多项式回归 https://baike.baidu.com/item/多项式回归/21505384
    - [ ] nn
        - nn回归 https://playground.tensorflow.org/
- 优化
    - ga
        - [x] 极值问题
        - [ ] case：怎么吃最省钱
    - 思考
        - [ ] case：卡路里达标情况下，怎么吃最省钱
        - [ ] case：泳池灌水，规定（T，V）下，怎么开pump能耗最低
    - or
- 框架库
    - [ ] flowable
    - [ ] torch
    - [ ] torch ext
- other

## ga-demo

```shell
rule = {
    "direction": "min",
    "run": "x[0] * x[0] + x[1] * x[1] + 2 * x[0] - 6 * x[1] + x[0] * 100",
    "data_x_last": [2],
    "data_c_range": [[-100, 100, 0.001], [-100, 100, 0.001]],
    "constraints": [
        ["=", "x[0] * x[0]", "1"],
        [">", "x[1]", "4"],
    ],
}
```
