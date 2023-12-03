# 🥛 Remilk Go: Various of milk Types Detection for Automated Smart Retail Monitoring System 🥛



## Project Description
Milk is a drink that is liked by many people, from children to adults. Milk is available in all existing supermarkets and minimarkets. Currently, the distribution of supermarkets and minimarkets is very wide, where we can find them on almost every street. Of the many activities carried out in supermarkets and minimarkets, the one that is often carried out by sales or employees is checking the availability of goods in supermarkets or minimarkets, one of which is milk products. Checking the availability of a dairy product in supermarkets, minimarkets or shops is an activity that is often carried out. Where in this activity, errors often occur when checking the stock of a dairy product. Moreover, when there is too much stock of dairy products being checked, this can result in human error. Of course, this will have a direct impact on operational efficiency and income in supermarkets and minimarkets. Therefore, we need a program or application that utilizes computer vision, such as object detection, to automatically detect what milk products are available on a minimarket or supermarket shelf.



## Contributor
| Full Name                   | Affiliation                          | Email                     | LinkedIn                                                          | Role        |
|-----------------------------|--------------------------------------|---------------------------|--------------------------------------------------------------     |-------------|
| Reynaldi Tangkearung | Universitas Dipa Makassar | reynaldi.fcb@gmail.com | [link](https://www.linkedin.com/in/reynaldi-tangkearung/) | Team Lead |
| Joshua Immanuel Fransisko Manurung | Universitas Sumatera Utara | joshuamanurung2609@gmail.com | [link](https://www.linkedin.com/in/joshua-immanuel-fransisko-manurung/) | Team Member |
| Dhea Amanda Ramadhan | Universitas Riau | dheadilla2002@gmail.com | [link](https://www.linkedin.com/in/dhea-amanda-ramadhan-b57b1725b/) | Team Member |
| Moh. Darirul Anwar | Universitas Trunojoyo | mohdarirula99@gmail.com | [link](https://www.linkedin.com/in/moh-darirul-anwar-02b89b274/) | Team Member |
| Nirmala Arumningtyas | Universitas PGRI Yogyakarta | nirmalaarumningtyas2@gmail.com | [link](https://www.linkedin.com/in/nirmala-arumningtyas-40571428b/) | Team Member |
| Purnomo Hernaoli | Universitas Sebelas Maret | Purnomohernaoli021000@gmail.com | [link](https://www.linkedin.com/in/purnomo-hernaoli-68326a222/) | Team Member |
| M. Haswin Anugrah Pratama | Startup Campus, AI Track | haswinpratama21@gmail.com | [link](https://www.linkedin.com/in/haswinpratama/) | Supervisor |

## Setup
### Prerequisite Packages (Dependencies)
- pandas>=1.1.4
- seaborn>=0.11.0
- python==3.9.13
- torch>=1.7.0
- torchvision>=0.8.1
- streamlit==1.29.0
- matplotlib>=3.2.2
- numpy>=1.18.5
- Pillow>=7.1.2
- PyYAML>=5.3.1
- requests>=2.23.0

### Environment
🧿 Google Collab Environment
| | |
|---------|---------|
| GPU | NVIDIA A100-SXM4-40GB|
| ROM | 200 GB |
| RAM | 40 GB |
| OS | Microsoft Windows 10 |

💻 Local Environment
| | |
|---------|---------|
| CPU | AMD Ryzen 5 2500U |
| GPU | AMD Radeon Vega 8 Mobile Graphics |
| ROM | 256 GB |
| RAM | 8 GB |
| OS | Microsoft Windows 10 |

## Dataset
The dataset we use in this project is images of Frisian flag dairy products with a total of 12 classes as follows:
- Kental Manis Omela 
- Milky zuzhu UHT chocolate 
- Milky zuzhu HT Strawberry 
- Susu Kental Full Cream Gold
- Susu Kental Manis Vanilla 
- Susu bubuk kompleta cokelat 
- Susu bubuk kompleta vanilla
- Susu kental manis cokelat 
- UHT Full Cream 946 ml 
- UHT LOw Fat Belgian Chocolate 225 ml
- UHT Strawberry 225 ml
- UHT Swiss Chocolate 946 ml

This dataset was taken directly at a retail store.
- Link: [Dataset Roboflow](https://universe.roboflow.com/neurantechno-1yd1n/various-milk-types-detection/dataset/6)

## Results
### Model Performance
In this project we carried out several experiments and modifications using several models in yolov5, by changing the backbone architecture. After conducting a series of training data using the model we chose, we found that the Yolov5 model using the Resnet-50 architecture performed well using the dataset we had.

#### 1. Metrics

| model | epoch | learning_rate | batch_size | optimizer | Precision | Recall | mAP50 | mAP50-95 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------| 
| Custom Yolov5s | 300 |  0.01 | 32 | SGD | 0.65 | 0.807 | 0.765 | 0.631 |
| MobileNet V3 | 300 | 0.01 | 32 | SGD | 0.577 | 0.699 | 0.691 | 0.57 |
| VGG-16 | 300 | 0.01 | 32 | SGD | 0.699 | 0.731 | 0.802 | 0.689 |
| **ResNet-50** | **100** | **0.01** | **32** | **SGD** | **0.734** | **0.776** | **0.823** | ***0.725** |

#### 2. Ablation Study
In this project we use the custom Yolov5 model using the architecture from Resnet50 which we got from [GitHub](https://github.com/WangRongsheng/BestYOLO). This repository provides a resnet50 model with the following architecture:
```
# Parameters
nc: 2  # number of classes
depth_multiple: 0.33  # model depth multiple
width_multiple: 0.25  # layer channel multiple
anchors:
  - [10,13, 16,30, 33,23]  # P3/8
  - [30,61, 62,45, 59,119]  # P4/16
  - [116,90, 156,198, 373,326]  # P5/32

# YOLOv5 v6.0 backbone
backbone:
  # [from, number, module, args]
  [[-1, 1, resnet501, [512]],  # 0
   [-1, 1, resnet502, [1024]],  # 1
   [-1, 1, resnet503, [2048]],  # 2
   [-1, 1, SPPF, [1024, 5]],  # 3
  ]

# YOLOv5 v6.0 head
head:
  [[-1, 1, Conv, [512, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 1], 1, Concat, [1]],  # cat backbone P4
   [-1, 3, C3, [512, False]],  # 7

   [-1, 1, Conv, [256, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 0], 1, Concat, [1]],  # cat backbone P3
   [-1, 3, C3, [256, False]],  # 11 (P3/8-small)

   [-1, 1, Conv, [256, 3, 2]],
   [[-1, 7], 1, Concat, [1]],  # cat head P4
   [-1, 3, C3, [512, False]],  # 14 (P4/16-medium)

   [-1, 1, Conv, [512, 3, 2]],
   [[-1, 3], 1, Concat, [1]],  # cat head P5
   [-1, 3, C3, [1024, False]],  # 17 (P5/32-large)

   [[11, 14, 17], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)
  ]
```

in our model we modify the **nc** from ```nc:2``` to ```nc: {num_classes}``` and add **SPP** module, **BottleneckCSP** at the end of the backbone.

so the final backbone like this:
```
# YOLOv5 v6.0 backbone
backbone:
  # [from, number, module, args]
  [[-1, 1, resnet501, [512]],  # 0
   [-1, 1, resnet502, [1024]],  # 1
   [-1, 1, resnet503, [2048]],  # 2
   [-1, 1, SPPF, [1024, 5]],  # 5
   [-1, 1, SPP, [1024, [5, 9, 13]]],
   [-1, 3, BottleneckCSP, [1024, False]]
  ]
```

#### 3. Training/Validation Curve
![Result Plot](https://github.com/josh209062/NeuranTechno-SC5AI/assets/85721003/01095fe3-3c96-43b4-a958-0ea1165f1750)
In the training/validation curve above we can see that the model we built **fit** the dataset we created.
 
### Testing
In this testing we provide 10 images that can access by this [Link](https://drive.google.com/drive/folders/1A880u-IJMFvRGYKjrh4ciLMAbN5d1Npr?usp=drive_link).

And the result of testing images can be access by this [Link](https://drive.google.com/drive/folders/1X1oPvUbU5BzGRPiDy4nCyJvQwrOrIAy2?usp=drive_link).



### Deployment (Optional)
Describe and show how you deploy this project (e.g., using Streamlit or Flask), if any.

## Supporting Documents
### Presentation Deck
- Link: https://...

### Business Model Canvas
Provide a screenshot of your Business Model Canvas (BMC). Give some explanations, if necessary.

### Short Video
Provide a link to your short video, that should includes the project background and how it works.
- Link: https://...

## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://...
- Link: https://...
- Link: https://...

## Additional Comments
Provide your team's additional comments or final remarks for this project. For example,
1. ...
2. ...
3. ...

## How to Cite
If you find this project useful, we'd grateful if you cite this repository:
```
@article{
...
}
```

## License
For academic and non-commercial use only.

## Acknowledgement
This project entitled <b>"YOUR PROJECT TITLE HERE"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.
