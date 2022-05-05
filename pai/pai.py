import torch


class Pai:
    @staticmethod
    def isGpu() -> bool:
        # device = "cuda" if torch.cuda.is_available() else "cpu"
        # print(f"Using {device} device")
        return torch.cuda.is_available()
