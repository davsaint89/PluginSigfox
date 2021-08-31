# SigfoxPlugin

Recieve and decode data from Sigfox devices. 

This plugin facilitates the communicacion between Sigfox and Ubidots by providing an API endpoint for Sigfox and a user code space for decoding the Sigfox hexadecimal message then it provisions a Ubidots device with the decoded data.

# Instalation 

In your [Ubidots account](https://industrial.ubidots.com/accounts/signin/)
[Instalation](https://res.cloudinary.com/di2vaxvhl/image/upload/v1630362242/Customer%20Success/DocsAssets/plugin-sigfox/plugin_instalation.gif)


# Usage

Once installed, go to 'Decoder' and then to 'Decoding Function' to write your script for decoding hex data. There's a test payload you may use to test your decoding function and once you are ready click on 'save&make live'.

[Decoding example](https://res.cloudinary.com/di2vaxvhl/image/upload/v1630360340/Customer%20Success/DocsAssets/plugin-sigfox/pruebaDecoding.gif)

# return

The decoding function must return a python dictionary with a valid data structure in order to provision the Ubidots device for instance: 

{"variable1": {'value': "12.5", 'context':{'lat':-23.6, 'ln':45.2}}}

# License
[MIT]
