# UTokyo_RL_School
Repository for Jupyter notebooks accompanying lecture series on RL in University of Tokyo.

# How to run this on your computer 

The recommended way to run notebooks is installing Docker on your local computer, please refer to [Local Set Up](#local-set-up). After successful installation, please consult [Running the notebook](#running-the-notebook) on how to run the notebooks.

Running on the cloud will also be possible, however, due to reliability issue, run it at your own risk, if the cloud method refuses to boot up during the lecture, there is nothing I can do!

# Local Set Up

For Windows and Mac User, the easiest way is to install [Docker Desktop](https://www.docker.com/products/docker-desktop/) on your computer. For Linux user, just install `docker` and `docker-compose` according to your distro.  The following sections will try to summarize the installation process on Windows and Mac.

## 1a. Installing Docker Desktop on Windows

### Installing WSL2
As a prerequisite, you have to WSL2 installed, if you are not sure you already installed it, please follow [this guide](https://docs.microsoft.com/en-us/windows/wsl/install-manual) Up to Step 5.  If you encounter any problem, please consult their [troubleshooting website](https://docs.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues), especially the part about enabling virtualization in your BIOS.

[This](https://youtu.be/cgXZ8Ecrdg0) is a video of my attempt.

### Installing Docker Desktop
If you already have WSL2 installed, consult this [webpage](https://docs.docker.com/desktop/install/windows-install/) for installation. It should be very straightforward, download the `.exe` file and install. 

[This](https://youtu.be/HbMPZl0Hd90) is a video of my attempt

## 1b. Installing Docker Desktop on MacOS
Download and install [Docker Desktop from here https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/).

NB: Chose the correct chip architecture for your notebook - with newer Macs having the Apple Silicon (~575MB download)

Follow the instructions there to install Docker or use the command line:

`sudo hdiutil attach Docker.dmg`

`sudo /Volumes/Docker/Docker.app/Contents/MacOS/install`

`sudo hdiutil detach /Volumes/Docker`


## 2. Running the notebook 

- Open terminal (or CMD/Powershell on Windows), navigate the the repo folder
- Type `docker compose up --build --force-recreate`
- Copy link to web browser
- Start Using

Note, if you have problem with "name already exists", you can run:
- In Linux: `docker stop tokyo-rl && docker rm tokyo-rl`
- In Windows Powershell: `docker stop tokyo-rl; docker rm tokyo-rl`

If you have nvidia driver and NVIDIA container toolkit, and you want to run the docker with GPU, you can run

```
docker compose -f docker-compose-gpu.yml up --build --force-recreate
```

## Other Methods

Note that this repo is just a collection of jupyter notebooks, so if you already have a Python environment setup on your computer, feel free to use it. The repo includes `dependencies.txt` that lists all the dependencies (I didn't use `requirements.txt` because Deepnote will actually try to install stuff inside `requirements.txt` when it boots up which is redundant).

Sometimes the `ipywidgets` will not work properly out of the box, you have to look online yourself on how to enable that in your `jupyter notebook` or `jupyter lab` (It is pretty straightforward).

If you choose this, you have to figure it out yourself if you experience any problems. If the notebook simply refuse to run, and I cannot replicate the error you are experiencing, I will advise you to install Docker Desktop.

