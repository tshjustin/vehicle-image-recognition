## Traffic Images Vehicle Detection 

# Workflow 
![image](https://github.com/tshjustin/vehicle-image-recognition/assets/122602657/4abbeac3-b411-440e-b571-b0de2bf15f7c)

<ul>
<li>Traffic Images downloaded from API and annotated using Roboflow, which is then exported for training of model/li>
<li>Import pre-trained model forom YoloV8 and fined-tuned (train) with exported data, then exported in ONNX Format</li>
<li>Prepare ONNX model for inference </li>
</ul>

| Tools      | Description |
| ----------- | ----------- |
| Roboflow      | Computer vision framework for data collection, annotation, preprocessing and augementation. Supports custom datasets and smart labeling with pre-trained model on COCO (Common Objects in Context).       |
| YoloV8   | Pre-trained model that comes with different weights and sparcity of model. Model can be imported and fined-tuned with custom dataset for specific use cases.        |
| ONNX   | Intermediary Machine Learning framework to convert between different ML frameworks to deploy accross differnet platforms.        |
