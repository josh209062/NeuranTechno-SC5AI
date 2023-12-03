# 🥛 Remilk Go: Various of milk Types Detection for Automated Smart Retail Monitoring System 🥛



## Project Description
Milk is a drink that is liked by many people, from children to adults. Milk is available in all existing supermarkets and minimarkets. Currently, the distribution of supermarkets and minimarkets is very wide, where we can find them on almost every street. Of the many activities carried out in supermarkets and minimarkets, the one that is often carried out by sales or employees is checking the availability of goods in supermarkets or minimarkets, one of which is milk products. Checking the availability of a dairy product in supermarkets, minimarkets or shops is an activity that is often carried out. Where in this activity, errors often occur when checking the stock of a dairy product. Moreover, when there is too much stock of dairy products being checked, this can result in human error. Of course, this will have a direct impact on operational efficiency and income in supermarkets and minimarkets. Therefore, we need a program or application that utilizes computer vision, such as object detection, to automatically detect what milk products are available on a minimarket or supermarket shelf.



## Contributor
| Full Name                   | Affiliation                          | Email                     | LinkedIn                                                          | Role        |
|-----------------------------|--------------------------------------|---------------------------|--------------------------------------------------------------     |-------------|
| Reynaldi Tangkearung | Universitas Dipa Makassar | reynaldi.fcb@gmail.com | [link](https://www.linkedin.com/in/reynaldi-tangkearung/) | Team Lead |
| Joshua Immanuel Fransisko Manurung | Universitas Sumatera Utara | joshuamanurung2609@gmail.com | [link](https://www.linkedin.com/in/joshua-immanuel-fransisko-manurung/) | Team Member |
| Dhea Amanda Ramadhan | Universitas Riau | dheadilla2002@gmail.com | [link](https://www.linkedin.com/in/dhea-amanda-ramadhan-b57b1725b/) | Team Member |
| Moh. Darirul Anwar | Universitas Trunojoyo | mohdarirula99@gmail.com | [link]() | Team Member |
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
| | |
|---------|---------|
| GPU | NVIDIA A100-SXM4-40GB|
| ROM | 200 GB |
| RAM | 40 GB |
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
| **ResNet-50** | **100** | **0.01** | **32** | **SGD** | **0.734** | **0.776** | **0.823** | ***0.725** |

#### 2. Ablation Study


#### 3. Training/Validation Curve
![Result Plot](https://github.com/josh209062/NeuranTechno-SC5AI/assets/85721003/01095fe3-3c96-43b4-a958-0ea1165f1750)
In the training/validation curve above we can see that the model we built **fit** the dataset we created.
 
### Testing
Show some implementations (demos) of this model. Show **at least 10 images** of how your model performs on the testing data.

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
