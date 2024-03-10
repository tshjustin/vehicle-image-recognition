## Traffic Images Vehicle Detection 

### Training of Model 
![image](https://github.com/tshjustin/vehicle-image-recognition/assets/122602657/4abbeac3-b411-440e-b571-b0de2bf15f7c)

<ul>
<li>Traffic Images downloaded from API and annotated using Roboflow, which is then exported for training of model</li>
<li>Import pre-trained model forom YoloV8 and fined-tuned (train) with exported data, then exported in ONNX Format</li>
<li>Prepare ONNX model for inference </li>
</ul>

| Tools      | Description |
| ----------- | ----------- |
| Roboflow      | Computer vision framework for data collection, annotation, preprocessing and augementation. Supports custom datasets and smart labeling with pre-trained model on COCO (Common Objects in Context).       |
| YoloV8   | Pre-trained model that comes with different weights and sparcity of model. Model can be imported and fined-tuned with custom dataset for specific use cases.        |
| ONNX   | Intermediary Machine Learning framework to convert between different ML frameworks to deploy accross differnet platforms. ONNX was used for easy deployment to Render cloud hosting & for comparison of model in different frameworks for a common platform.  |

### Outcomes

Endpoint enacted that accepts a image URL. An example of the annoted image is shown below: 

![image](https://github.com/tshjustin/vehicle-image-recognition/assets/122602657/0a09ebd3-a256-47bf-9eaf-654a347de46b)


Confidence values for identified objects are also logged: 
```
Class 0 : Score 0.906679630279541
Class 0 : Score 0.8510133028030396
Class 0 : Score 0.8255020380020142
Class 0 : Score 0.7501163482666016
Class 0 : Score 0.7322111129760742
Class 0 : Score 0.7169588804244995
Class 0 : Score 0.7063149213790894
Class 0 : Score 0.6881899833679199
Class 0 : Score 0.6813197135925293
Class 0 : Score 0.6607131361961365
Class 0 : Score 0.6455743312835693
Class 0 : Score 0.6336331367492676
Class 0 : Score 0.3735249638557434
```

Testing the ONNX model on test data yields an accuracy score of 0.706. 

Images are hand annotated to ensure correct classfication of objects and control over classes.
