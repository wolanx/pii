# llm 大语言模型

> 2024年02月分别运行了，“我想去上海旅游，有什么推荐嘛？”

- Mistral-7B-Instruct-v0.1 gpu显存30G，中文不理想
- Qwen1.5-7B-Chat 运行失败，gpu显存超过32G
- Qwen1.5-4B-Chat 可以
- Qwen1.5-1.8B-Chat 这也可以

## 模型评价 https://www.superclueai.com/

- gpt4 第一，86分
- qwen1.5-72B-Chat 开源第一，79分
- Qwen1.5-7B-Chat 61分

```python
import time

from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto
#device = "cpu"

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen1.5-1.8B-Chat",
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-7B-Chat")

model.to(device)

prompt = "Give me a short introduction to large language model."
messages = [
    # {"role": "user", "content": "What is your favourite condiment?"},
    # {
    #     "role": "assistant",
    #     "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!",
    # },
    {"role": "user", "content": "我想去上海旅游，有什么推荐嘛?"},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(response)
```

```text title="Qwen1.5-1.8B-Chat 效果超出想象"
(base) root@ECS-GIMC-GPU-CSH-G:/www/lla# python main.py
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
当然可以！上海是中国的经济、文化、金融中心之一，拥有众多值得一游的地方。以下是一些在上海旅游的推荐：

1. 外滩：外滩是上海最具有历史和文化底蕴的地区之一，也是上海的标志性建筑之一。您可以在这里欣赏到黄浦江两岸的美景，包括东方明珠电视塔、南京路步行街、豫园等著名景点。

2. 上海博物馆：作为中国最大的综合性博物馆，上海博物馆展示了丰富的中国古代文物和现代艺术品，涵盖了自然、历史、艺术等多个领域。此外，您还可以在这里学习了解中国的文化和历史。

3. 虎丘：虎丘是中国四大名山之一，以其秀美的风景和深厚的历史底蕴吸引了大量的游客。这里有许多古代建筑和墓地，如剑池、寒山寺等，您可以进行历史文化研究或感受苏州园林的魅力。

4. 田子坊：田子坊是一个充满复古风情的创意街区，充满了各种手工艺品店、咖啡馆、画廊等特色小店，这里的艺术氛围浓厚，是摄影爱好者的好去处。

5. 陆家嘴金融区：这里是上海的核心商业区，汇集了国内外各大金融机构和跨国企业，如世界500强公司、国际大都会等。在这里您可以看到现代化的高楼大厦和传统的洋楼，体验现代化与传统相结合的都市生活。

6. 长城饭店：长城饭店位于上海的市中心，被誉为“全球最美的酒店之一”。这里的餐饮服务和住宿环境都非常出色，尤其是餐厅提供的菜品和酒水丰富多样，让您在品尝美食的同时也能享受豪华的服务。

7. 南京路步行街：南京路步行街是中国最著名的购物街之一，汇聚了许多国际品牌和本土知名品牌，是购物和娱乐的首选之地。这里还有许多精致的小吃和咖啡店，让您在逛街之余也能品味上海的饮食文化。

以上就是我为您推荐的一些上海旅游地点，希望对您的旅行有所帮助！如果您需要更多的具体信息或者有其他特殊需求，请随时告诉我，我会为您提供更详细和个性化的建议。祝您在上海度过一个愉快而充实的旅程！
```
