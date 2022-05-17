To launch Gazebo

```
roslaunch jackal_helper copy_gazebo_launch.launch
```

To launch AMCL node
```
roslaunch jackal_navigation amcl_demo.launch map_file:=/home/ril/jackal_ws/src/nav-competition-icra2022/BARN_dataset/map_files/yaml_0.yaml
```

To view navigation in RViz
```
roslaunch jackal_viz view_robot.launch config:=gmapping
```
