from pyniryo import *
import time
from camera_code import take_photos

from button_detection import ocr_on_bounding_boxes



ned = NiryoRobot("10.10.10.10")
# ned = NiryoRobot("169.254.114.65")
# ned = NiryoRobot("169.254.200.200")
initial_pos=ned.get_pose()
print(initial_pos)
print(ned.need_calibration())
ned.calibrate_auto()
ned.move_to_home_pose()
time.sleep(3)
# ned.tool_reboot()
# ned.reset_tcp()

#*******************Starting position*************************
initial_pos=(0.1353,-0.0089, 0.2372,-0.056,0.080, -0.063)
# initial_pos=(0.2851,-0.0012, 0.05,0.019,0.073,-0.003)
ned.move_pose(initial_pos)

# ned.move_joints(-2.9, -0.3, 0.1, 0.0, 0.5, -0.8)
time.sleep(2)
# ned.go_to_sleep()


# ned.move_joints(-2.9, -0.3, 0.1, 0.0, 0.5, -0.8)#Joints are expressed in radians
# ned.move_joints(1.0, -0.6, -1.0, 0.0, 0.5, -0.8)
# ned.move_joints([1.3071506023406982, 0.16242043673992157, -0.652149498462677, -1.6970915794372559, -1.3387484550476074, 2.0752642154693604])

# ned.move_pose(x=200, y=200, z=200, roll=0, pitch=0, yaw=0)

#*******************take the picture*************************


take_photos()



#*******************receive position*************************


image_path = '/media/asmany/Drive_D/Intelligent_Robotics/cameraphoto.jpg'  # Replace with the path to your image


print('Which floor do you want to go?')
floor_number = input()
time.sleep(1)
1# Perform OCR on the bounding boxes in the image
coordinates = ocr_on_bounding_boxes(image_path, floor_number)

# print(coordinates)

if coordinates == None:
    print('Button is already pressed')
    ned.go_to_sleep()

else:
    desired_x = ((coordinates[0]+coordinates[2])/2)/3779.53

    desired_x = float(round(desired_x,3))

    desired_y = ((coordinates[1]+coordinates[3])/2)/3779.53

    desired_y = float(round(desired_y,3))
    print(desired_x, desired_y)



    #*******************Inverse kinematics*************************
    #x = back-front
    #y=left to right 
    #z=up-down
    x = 0.3067
    y = 0.1711 
    z = 0.4469
    roll = -0.225
    pitch = -0.232
    yaw = 0.499

    desired_pose = (0.3, y -desired_x*2.6, z-desired_y*2, 0, 0, 0)  # X, Y, Z, roll, pitch, yaw

    # desired_pose = (x+desired_x, y-desired_y, 0.1, roll, pitch, yaw)  # X, Y, Z, roll, pitch, yaw

    # desired_pose = (x, y, z, roll, pitch, yaw)  # X, Y, Z, roll, pitch, yaw
    joint_angles = ned.inverse_kinematics(desired_pose)
    # print(joint_angles)
    ned.move_joints(joint_angles)


    #*******************press the button*************************

    # x2,y2,z2,roll2,pitch2,yaw2 = desired_pose
    # press=(x2+0.01, y2, z2, roll, pitch, yaw)
    press=(0.3+0.02, y -desired_x*2.6, z-desired_y*2, 0, 0, 0)
    joint_angles=ned.inverse_kinematics(press)
    # print(joint_angles)
    ned.move_joints(joint_angles)

    time.sleep(1)

    press=(0.3-0.02, y -desired_x*2.6, z-desired_y*2, 0, 0, 0)
    joint_angles=ned.inverse_kinematics(desired_pose)
    ned.move_joints(joint_angles)
    time.sleep(5)


    ned.go_to_sleep()



# def inverse_kinematics(x, y, z):
    
    




#     return theta1, theta2, theta3, theta4, theta5, theta6


# button_x = 0.2  
# button_y = 0.2
# button_z = 0.2

# theta1, theta2, theta3, theta4, theta5, theta6 = inverse_kinematics(button_x, button_y, button_z)
