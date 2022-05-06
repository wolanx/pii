"""
torchvision 实现
    https://github.com/pytorch/vision/blob/main/torchvision/models/resnet.py
    torchvision.models.resnet18(pretrained=True)
"""
import gradio as gr
import torch
import torch.nn.functional as F
import torchvision.models
from torchvision import transforms

torch.hub.download_url_to_file(
    "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt",
    "imagenet_classes.txt",
)
torch.hub.download_url_to_file(
    "https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg"
)

# model = torch.hub.load("pytorch/vision:v0.10.0", "resnet18", pretrained=True)  # hub 上拿模型
model = torchvision.models.resnet18(pretrained=True)  # vision 上拿模型
model.eval()


def inference(input_image):
    preprocess = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    input_tensor = preprocess(input_image)
    # create a mini-batch as expected by the model
    input_batch = input_tensor.unsqueeze(0)

    if torch.cuda.is_available():
        input_batch = input_batch.to("cuda")
        model.to("cuda")

    with torch.no_grad():
        output = model(input_batch)

    # The output has un-normalized scores. To get probabilities, you can run a softmax on it.
    probabilities = F.softmax(output[0], dim=0)

    # Read the categories
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]

    # Show top categories per image
    top5_prob, top5_cid = torch.topk(probabilities, 5)
    ret = {}
    for i in range(top5_prob.size(0)):
        ret[categories[top5_cid[i]]] = top5_prob[i].item()

    return ret


inputs = gr.inputs.Image(type="pil")
outputs = gr.outputs.Label(type="confidences", num_top_classes=5)
examples = [["dog.jpg"]]

# http://localhost:7860/
gr.Interface(
    inference,
    title="ResNet",
    description="Gradio demo for ResNet",
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    analytics_enabled=False,
).launch()
