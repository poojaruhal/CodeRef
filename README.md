# CodeRef

## Setup
Run on Virtual Machine with the following flavors: CUDA latest on Ubuntu 20.04 (2022-02-03), 8cpu-32ram-hpcv3-gpuT4

### Install Python and virtual env
```
sudo apt install software-properties-common && \ 
sudo add-apt-repository ppa:deadsnakes/ppa && \
sudo apt install python3.7 && \
sudo apt-get install python3.7-venv && \
sudo apt-get install python3.7-dev
python3.7 -m venv venv
```
### Activate virtual env
```
. venv/bin/activate
```
### Install python packages
```
pip install -r requirements.txt
```
### Login for WandB logging
```
wandb login <your-auth-key>
```

### Change pre-training script and run in deattached mode
[CHANGE sh/pre-train.sh]
```
chmod +x ./pre-train.sh
nohup ./sh/pre-train.sh > /dev/null 2>&1&
```
