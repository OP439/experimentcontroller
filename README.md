This repo was created to make development of the autorun script easier. 

The autorun script is run on a Chromebook that has a Linux virtual machine from which it runs the script. The use of another linux install other than the pi creates a bit of logical safety between the different processes and frees up processing power on the pi.

The requests library is used as it mimics what a human operator would do. It is also much easier to use than the paho-mqtt library. Having the auto run script mimic the user also means there is no additional development cost.

A lot of sleep statements are added to the code to ensure that commands are spaced out enough and do not clash - it is unknown what happens when the system is spammed. 
