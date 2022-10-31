# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import torch

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    a = torch.tensor([1,2,3], dtype=torch.float64)
    print(f"A Pytorch Tensor -> {a}")

    b = torch.tensor([2,2,2], dtype=torch.float64)
    print(f"B Pytorch Tensor -> {b}")

    print(f"A + B -> {a + b}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('From Inside the Repository')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
