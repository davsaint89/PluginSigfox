# SigfoxPlugin

Recieve and decode data from Sigfox devices. 

This plugin facilitates the communicacion between Sigfox and Ubidots by providing an API endpoint for Sigfox and a user code space for decoding the Sigfox hexadecimal message, then it provisions a Ubidots device with the decoded data.

# Instalation 

In your Ubidots account go to Devices --> Plugins, click the plus sign, select the Sigfox plugin and click on the > button

# Inputs

Ubidots device Type: An Ubidots device type will be created and linked to this plugin. This allows you to make batch changes to all of the devices that receive data through this plugin.



# Usage

Once installed, go to 'Decoder' and then to 'Decoding Function' to write your script for decoding hex data. There's a test payload you may use to test your decoding function and once you are ready click on 'save&make live'

# return

The decoding function must return a python dictionary with a valid data structure in order to provision the Ubidots device for instance: 

{"variable1": {'value': "12.5", 'context':{'lat':-23.6, 'ln':45.2}}}

# License
[MIT]
