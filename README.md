# SigfoxPlugin

It's a Python v3.7 program wich facilitates the communicacion between Sigfox and Ubidots by providing an API endpoint for Sigfox and a user code space for decoding the Sigfox hexadecimal message, then it provisions a Ubidots device with the decoded data.

# Instalation 

In your Ubidots account go to Devices --> Plugins, click the plus sign, select the Sigfox plugin and click on the > button

# Usage

Once installed, go to 'Decoder' and then to 'Decoding Function' to write your code.
there's a test payload you may use to test your decoding function and once you are ready click on 'save&make live'

# return

The decoding function must return a json payload in order to provision the Ubidots device for instance: 

{"temperature": {"value":10, "timestamp": 1534881387000, "context": {"machine": "1st floor"}}}

# License
[MIT]
