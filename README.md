# TELEOP_KEYBOARD

This is a script that publishes messages to a topic called /cmd_vel of type Twist

script_name: teleop_keyb.py
package: lab1-teleop/

Teclas importantes:
	a -> linear_x += 2
	d -> linear_x += -2
	w -> linear_y += 2
	s -> linear_y += -2
	m -> angular_z += 2
	q -> Stop
	
class KeyboardTeleop(Node):

- This class is a subclass of RCLPy Node, the node that controls keyboard teleoperation. The __init__ constructor is called when a KeyboardTeleop object is created.
	
def inicia:

- Starts linear and angular velocity values ​​as 0.
	
def on_key_press:

- Reads the keyboard, checks if any key has been pressed and changes the linear or angular velocity value
	
def main(args=None):

- Create the node and call the on_key_press function in a loop

## Requirements
- ROS2

## Run
- Clone the repository as it contains the ROS2 package
- Do: ```colcon build # in your workspace```
- Do: ```source install/setup.bash # in your workspace```
- Do: ```ros2 run teleop teleop```