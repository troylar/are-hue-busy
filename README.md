arehuebusy
========================
Do you wish you could politely let people know you would not like to be disturbed? This is a simple command-line script that lets you define busy statuses and use your Hue bulb to signal that status to others.

## Installation
Clone the repo and run:
`$ python setup.py install`
## Configuration
* Copy the `config.yml.sample` to `<home directory>/.arehuebusy.yml`
* Open the file in your text editor and make two changes: replace `bridge_ip` with your IP and `light` with the full name of the light you want to manage

## Usage
*If you are **very** busy:*

`$ arehuebusy very`

*If you are **kinda** busy:*

`$ arehuebusy kinda`

*If you're **not** so busy:*

`$ arehuebusy not`

## Customization
All of the statuses, color and brightness is read from the config file, so you can customize any of the settings to your liking.