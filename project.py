from pyniryo import *
import time

ned = NiryoRobot("10.10.10.10")
# ned = NiryoRobot("169.254.114.65")
# ned = NiryoRobot("169.254.200.200")
initial_pos=ned.get_pose()
print(initial_pos)
print(ned.need_calibration())

ned.move_to_home_pose()
time.sleep(3)

#*******************Starting position*************************
initial_pos=(0.2851,-0.0012, 0.05,0.019,0.073,-0.003)
ned.move_joints(initial_pos)

# ned.move_joints(-2.9, -0.3, 0.1, 0.0, 0.5, -0.8)
time.sleep(2)
# ned.go_to_sleep()


# ned.move_joints(-2.9, -0.3, 0.1, 0.0, 0.5, -0.8)#Joints are expressed in radians
# ned.move_joints(1.0, -0.6, -1.0, 0.0, 0.5, -0.8)
# ned.move_joints([1.3071506023406982, 0.16242043673992157, -0.652149498462677, -1.6970915794372559, -1.3387484550476074, 2.0752642154693604])

# ned.move_pose(x=200, y=200, z=200, roll=0, pitch=0, yaw=0)

#*******************take the picture*************************






#*******************receive position*************************





#*******************Inverse kinematics*************************
#(left-right(x), front-back(y), up-down(z))
x=0.3
y=0.1
z=0.5
roll=0
pitch=0
yaw=0


desired_pose = (x, y, z, roll, pitch, yaw)  # X, Y, Z, roll, pitch, yaw
joint_angles = ned.inverse_kinematics(desired_pose)
# print(joint_angles)
ned.move_joints(joint_angles)


#*******************press the button*************************

x2,y2,z2,roll2,pitch2,yaw2 = desired_pose
press=(x2+0.01, y2, z2, roll2, pitch2, yaw2)
joint_angles=ned.inverse_kinematics(press)
# print(joint_angles)
ned.move_joints(joint_angles)

time.sleep(1)

desired_pose=(x2-0.01, y2, z2, roll2, pitch2, yaw2)
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
