# YCDaU
Youtube Channel Downloader and Updater
This is a script to download a whole channels set of videos and checks for updates and downloads new videos.

## Install

To install run this command (for Linux and macOS)

```shell
bash install.sh
```

## Usage
### downloading
To download based on the data in the channel file
``` shell
ycdau -c channel file
```

### adding channels or playlist
To use this program you must add the channels using -a E.G
```shell
ycdau -a "[channel file, directory to download to, video url, any options for youtube-dl (quality, name, Etc)]"
```
you can add as many channels at once if you make each channel a different arrays.
