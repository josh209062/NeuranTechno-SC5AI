# 🥛 Remilk Go: Various of milk Types Detection for Automated Smart Retail Monitoring System 🥛



## Project Description
Please describe your Startup Campus final project here. You may should your <b>model architecture</b> in JPEG or GIF.

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
- Link: https://universe.roboflow.com/neurantechno-1yd1n/various-milk-types-detection/dataset/6

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
Inform your model validation performances, as follows:
- For classification tasks, use **Precision and Recall**.
- For object detection tasks, use **Precision and Recall**. Additionaly, you may also use **Intersection over Union (IoU)**.
- For image retrieval tasks, use **Precision and Recall**.
- For optical character recognition (OCR) tasks, use **Word Error Rate (WER) and Character Error Rate (CER)**.
- For adversarial-based generative tasks, use **Peak Signal-to-Noise Ratio (PNSR)**. Additionally, for specific GAN tasks,
  - For single-image super resolution (SISR) tasks, use **Structural Similarity Index Measure (SSIM)**.
  - For conditional image-to-image translation tasks (e.g., Pix2Pix), use **Inception Score**.

Feel free to adjust the columns in the table below.

| model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | 1000 |  0.0001 | 32 | Adam | 0.093 | 88.34% | 84.15% | ... |
| vit_l_32 | 2500 | 0.00001 | 128 | SGD | 0.041 | 90.19% | 87.55% | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | 

#### 2. Ablation Study
Any improvements or modifications of your base model, should be summarized in this table. Feel free to adjust the columns in the table below.

| model | layer_A | layer_B | layer_C | ... | top1_acc | top5_acc |
| --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | Conv(3x3, 64) x2 | Conv(3x3, 512) x3 | Conv(1x1, 2048) x3 | ... | 77.43% | 80.08% |
| vit_b_16 | Conv(3x3, 32) x3 | Conv(3x3, 128) x3 | Conv(1x1, 1028) x2 | ... | 72.11% | 76.84% |
| ... | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
Insert an image regarding your training and evaluation performances (especially their losses). The aim is to assess whether your model is fit, overfit, or underfit.
 
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
