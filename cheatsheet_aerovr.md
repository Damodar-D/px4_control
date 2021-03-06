## run simulator

    cd ~/PX4/Firmware
    make px4_sitl_default jmavsim

    cd ~/aerovr_ws/src/px4_control/scripts
    
    # connect to the simulated drone:
    roslaunch px4_control px4_sim.launch
    
    # EITHER execute test-flight command:
    rosrun px4_control drone_test.py
    
    # OR try with controller:
    rosrun px4_control position_interactive_control_vr.py

## rqt_plot

    rosrun rqt_plot rqt_plot
    # choose topic and press enter
    
## Crazyflie

    # ON OMEGA
    # roslaunch vicon_bridge vicon.launch
    # crazyflie drone is:
    # /vicon/cf4/cf4

    # ON OMEGA
    # connect to crazyflie
    roslaunch crazyflie_demo connect_crazyflie4.launch
    
    # ON OMEGA
    # launch rviz and controller
    roslaunch px4_control pos_control_viz.launch

## setup HTC Vive
    
    1) turn headset to the X-direction (facing window)

## Tests

    # vicon  (using ethernet connection!)
    ping 192.168.10.1
    roslaunch vicon_bridge vicon.launch
    rostopic hz /vicon/markers


    # controller
    python controller_test.py 10


## Technical params

        nick: 192.168.88.224
        odroid: 192.168.88.253
        vicon: 192.168.88.223
    
        есть еще fcu_url. 
        Там телеметрию указываем, что-то вроде /dev/ttyUSB0:921600 
        (баудрейт в конце)

## Connect to VICON through ethernet

on Omega (nick's pc) add IP in vicon's network

    sudo su
    vim /etc/network/interfaces

    auto eth0         
    allow-hotplug eth0                                      
    iface eth0 inet static       
        address 192.168.10.249      
        netmask 255.255.255.0 

In vicon.launch change IP to ethernet:

    <param name="datastream_hostport" value="192.168.10.1:801" type="str" />

Go to internet - edit connections - IPv4 Settings

add address:
192.168.10.125  (can be anything)
netmask 24

DNS servers: 192.168.10.254


## Connect to the big drone

ON DRONE
запустить этот лаунч для локализации по мокапу и получения данных с дрона
проверить, идут ли данные локализации на пиксхок
    
    roslaunch px4_control drone.launch gcs_url:=udp://@192.168.88.224
    
ON OMEGA (Nick's computer)
EITHER полетный скрипт (без пропеллеров, естественно сначала):
    
    roslaunch px4_control main.launch

OR drone_test ON OMEGA
    
    # uncomment five strings in main.launch
    # and comment out position_interactive_control_vr

## Configure pixhawk

    актуальная инструкция:
    https://dev.px4.io/v1.9.0/en/companion_computer/pixhawk_companion.html

    Sys_companion - баудрейт указывать 921600
    

## Add ip to interfaces

TODO: CHANGE THIS!

Check network config:

    sudo su
    vim /etc/network/interfaces

    # here wlan, adress, netmask, bssid, pas 
    auto wlan0 


## Configure network to get visualization remotely
Your working computer and NUC need to now about each other.

here is complete instruction (first link)

    https://roboticsknowledgebase.com/wiki/networking/ros-distributed/
    http://www.iri.upc.edu/files/scidoc/1607-Multi-master-ROS-systems.pdf


<!-- http://wiki.ros.org/multimaster_fkie
Install multimaster_fkie to create multimaster network:
    sudo apt-get install ros-kinetic-multimaster-fkie -->

On your working computer:

Inside /etc/hosts add IP of device you want to connect to and it's hostname (nuc@skcr):

    sudo vim /etc/hosts
    192.168.88.253 odroid
    
On robot:

    sudo vim /etc/hosts
    192.168.88.224 alex-System-Product-Name
    

## Graphics in QGroundControl

    qgroundcontrol. Widgets -> Analyse
    
    
## Mocap to Pixhawk

    скрипт mocap2pixhwak делает преобразование координат с вайкона в маврос 
    и в нужный топик локализации отправляет данные 
    (/mavros/vision_position/pose, из визуальной позиции потом уже EKF в local_pose публикует)