# Elevator-Botton-Arm-Control

## "yolov5" folder contains all codes and datasets for button detection and "Pressed_NonPressed_model" folder contains all codes and datasets for pressed unpressed button detection

### To run this code successfully with Niryo Arm:

1. Activate virtual environment:
```
source robotics/bin/activate
```
or create a new virtual environment and install "requirements.txt" using the following command and activate that environment:
```
pip install -r /path/to/requirements.txt
```
2. Intreget Niryo Arm2 with a laptop using the following password:
```
niryorobot
```
3.  Run the following command from the activated virtual environment

```
python project.py 
```

### To run this code successfully without Niryo Arm:


1. Activate virtual environment:
```
source robotics/bin/activate
```
or create a new virtual environment and install "requirements.txt" using the following command and activate that environment:
```
pip install -r /path/to/requirements.txt
```
2. Change image_path from main.py. There are some test images in the "test_image" folder.
   
3.  Run the following command from the activated virtual environment

```
python main.py 
```
