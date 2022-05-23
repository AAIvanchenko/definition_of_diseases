import torch
import torch.nn as nn
import cv2 as cv
import numpy as np
from torchvision import models, transforms
import os


def model_resnet18():
    device = torch.device("cuda") if torch.cuda.is_available else torch.device("cpu")
    resnet18 = models.resnet18(pretrained=True)
    # Выключаем подсчет градиентов для слоев, которые не будем обучать
    for param in resnet18.parameters():
        param.requires_grad = False

    # Выключаем подсчет градиентов для слоев, которые не будем обучать
    for param in resnet18.parameters():
        param.requires_grad = False
    # разморозили три слоя слой
    for param in resnet18.layer2.parameters():
        param.requires_grad = True
    for param in resnet18.layer3.parameters():
        param.requires_grad = True
    for param in resnet18.layer4.parameters():
        param.requires_grad = True

    resnet18.fc = nn.Sequential(nn.Linear(in_features=512,
                                          out_features=2,
                                          bias=True),
                                nn.Softmax(dim=1))

    resnet18_two = resnet18.to(device)
    return resnet18_two


def model_load(model, name):
    """
    Загрузка весов модели.

    :name: название файла с расширением .pth
    :return: загруженная модель
    """
    model.load_state_dict(torch.load(name))
    model.eval()
    return model


def get_img_by_path(img):
    """
    Получение картинки по её пути.

    :img_path: путь до картинки
    :return: картинка, состаящая из массива цифр
    """

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = np.array(img)
    return img


def img_to_tensor(img_path):
    """
    Преобразование картинки в tensor.
    :param img_path:
    :return:
    """
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize(size=244)])

    img = get_img_by_path(img_path)
    return transform(img)


def load_img():
    images = []
    path = '../web/media/images/'
    for dirs, _, files in os.walk(path):
        for file in files:
            images.append(img_to_tensor(get_img_by_path(cv.imread(path+file))).unsqueeze(0).cuda())

    return images


def start_model():
    title_list = []
    result_list = []
    model = model_load(model_resnet18(), "../data/resnet18_20.pth")

    images = load_img()

    for img in images:
        pred_list = model(img)
        print(pred_list)

        if pred_list[0][1] == 1:
            prob_class = round(pred_list[0][1].item(), 1)
            title_list.append('Класс больное')
        else:
            prob_class = round(pred_list[0][0].item(), 4)
            title_list.append('Класс здоровое')
        result_list.append('Вероятность {}'.format(prob_class*100))

    return title_list, result_list
