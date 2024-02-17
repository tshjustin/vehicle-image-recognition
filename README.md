# Singapore Traffic Images Vehicle Detection 

# Workflow 

1. Using Roboflow - Images that are queired from LTA API are downloaded and formatted to fit into the format accepted by Roboflow 

2. Images are labelled and annotated individually for the model to learn from. 

3. Using a pre-trained model from YoloV8, Images are fed and used to train it. Model is then tested using test data. 

4. Model is then exported in ONNX format that is viable across differnet platforms and prepared for inference. 

[![Tech Stack](https://skillicons.dev/icons?i=opencv,py)](https://skillicons.dev)