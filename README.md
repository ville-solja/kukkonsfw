# KukkoHelper

## General
This is a lite version of the Kukkohelper discord bot which currently only has the NSFW filter feature

## NSFW -filter
* User posts an image attachment
.gif is not currently supported and link previews are not checked either
* Attachment url is sent to Azure cognitive services
If it's NSFW process continues
* Channel is checked for nsfw status
If it safe for work (As in the status NSFW is not enabled) process continues
* Image is removed from the channel and it's NSFW rating is posted instead

## Installation
### Env variables for docker image
#### Azure Key
If you want to make use of the Azure cognitive services, you need to provide the access key for that as an environment variable

Example: "KEY=key with length of 32 characters"

Also make sure your cognitive services is using north europe URL:
"https://northeurope.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=adult"

#### Discord bot token
In order to provide access for the bot you need to provide it with the appropriate access token 

Example: "TOKEN=token with length of 59 characters"