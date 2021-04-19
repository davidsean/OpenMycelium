# OpenMycelium
Yet another Raspberry Pi project: an IoT environmental controller for mycelium growth and fruiting.
This is a open-hardware and open-source DIY project.
It can be used to control the conditions for spawn incubation, mycelium growth and for fruiting.

# Project status
This is still in its infancy. Nothing works yet, so please join the OpenIoT discord server (https://discord.com/invite/Ft229PDrxF) to contribute.

# Hardware
It comprises of a control board with temperature and humidity sensors, that can actual a heater, fan (and ultrasonic mister), light.
All the sensors and actuators are optional, so you jsut need to buy/assemble what you need.

## GOAL (not done yet)
The KiCAD PCB is provided that takes the form of a Raspberry-pi hat.
It needs be populate with some through-hole components (so find someone with a soldering iron if you aren't sure of being able to do this).
The PCB is more or less modular so you dpn't need to fully assemble it with all the features if you don't need them.

# Sofware
The software runs on a Raspberry-Pi.

## Goal (not done yet)
Uses cloud-link to host a Firebase webserver as an interface.
Logs telemetry over MQTT, can choose control "growth recipes".


# dev
```bash
conda create -n openmycelium python=3.8
conda activate openmycelium
python3 -m pip install -r requirements.txt
```
