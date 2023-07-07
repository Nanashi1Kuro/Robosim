# Robosim
Turtlebot3
Данная сборка была реализована на ros galactic
Для сборки проекта надо загрузить данный репозиторий, потом выполнить команды

source /opt/ros/galactic/setup.bash

В главной папке выполнить 

colcon build

После сборки пакета 

source install/setup.bash

И для того, чтобы запустить проект

ros2 launch like_a_rumba_robot runpy.launch.py


Для загрузки snap проекта надо выполнить следующие команды

cd ~/snap

sudo snap install

И для запуска пакета

ros2-move
