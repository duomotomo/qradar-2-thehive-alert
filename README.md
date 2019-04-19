# What is it?
the script is getting offenses from QRadar, creating Alerts for TheHive and importing them.

# How to run script
update config file (conf/smartclonner.conf) by your values<br/>
launch smart_clonner.py. You could run script inside crontab also.

# Parameters

TheHive - related:<br/>
<br/>
url - URL to TheHive instance (for ex. http://172.20.1.5:9000)<br/>
user - TheHive user used to connect to the TheHive(for ex. quser)<br/>
api_key = API key used to connect to the TheHive(for ex. = g1p5xYJiT/rAqsdf98fTdfsBa620Zypu)<br/>

QRadar - related:

server = IP address of the QRAdar server( for ex. 172.16.0.1)<br/>
auth_token = API key configured on QRAdar used to gather information about Offences (for ex. f598c71e-a7b8-44fc-9116-51a5dsdf2e1)<br/>

//TODO add more information about parameters

# How this script differs from Pierre BARLET (https://github.com/pierrebarlet/qradar2thehive) work?
qradar2thehive script creates Cases with static task list while our script creates Alerts that you could turn to Cases with any templates you want.