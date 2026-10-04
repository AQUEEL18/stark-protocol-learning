# Week 1: ROS 2 Nodes and Communication

**Environment:** ROS 2 Jazzy, Ubuntu 24.04

## What I built

Two ROS 2 nodes written in Python, in the package `my_first_pkg`:

- `my_node.py` is a publisher. Every 1 second it sends the message "Hello from Aqueel - count: N" on the topic `/my_topic`.
- `subscriber_node.py` is a subscriber. It listens to `/my_topic` and prints every message it receives.

## In my own words
+so node means a file and its a basic unit in a program this file communicate each other while working so as these guys need a channel to communicate so we  have three ways for that 
1.publisher and subscriber this is similar like a youtube channel bcs when u subscribe to a channel we get the info they post so now here to samre the subcriber subscribes to a publisher to get the data from him and then this will be like a workers working like a team a system  probably 
2.we the next one as service so this time  service provider i sthe one to takes request and does the work and send the our pur backt ot he client 
3.actions is the other one  i will give u  a simple example like u r i n the earth and need to send the rover in the mars to a certain location u will say a coordinate the rover sends u the exact location it is preset then while working on u r request also it will send rthe live coordinates until  it reaches the coordinates u sent
that it for now 


## How to run

```bash
cd ~/ros2_ws
colcon build --packages-select my_first_pkg
source install/setup.bash
ros2 run my_first_pkg my_node          # terminal 1
ros2 run my_first_pkg subscriber_node  # terminal 2
```

## Commands I used to inspect it

```bash
ros2 node list
ros2 topic list
ros2 topic echo /my_topic
ros2 topic hz /my_topic
```
