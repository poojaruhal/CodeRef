# CodeRef

## Login
- Login into ScienceCluster

```
ssh shortusername@cluster.s3it.uzh.ch
```

- Enter your Active directory password 

- To setup the password less authentication, please refer to [ScienceCluster documentation](https://docs.s3it.uzh.ch/cluster/connecting/)

- Once you login successfully to the server, you should see details about your directory usage. 


## Load the project data 

### Change to the data directory 
You can know more about the [directory structure](https://docs.s3it.uzh.ch/cluster/data/) 
```
cd data
``` 

- Create a folder for your project and change to the folder
```
mkdir <folder-name>
cd <folder-name>
```

### Clone the GitHub repository
```
git clone https://github.com/poojaruhal/CodeRef.git
```

### Load the dataset
You can download the dataset from the SeaDrive folder "CodeRef-dataset"


## For the first time, load required libraries and create a virtual environment

### Load the required modules:
```
module load mamba
module load multigpu
module load cuda/11.6.2
module load libxml2/2.9.13-ndomtw6
module load libxml2/2.9.12-koohqap
```
### Load the required packages
```
wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh
sh Miniconda3-py310_23.1.0-1-Linux-x86_64.sh
source ~/.bashrc
```

### Create a virtual environment
```
conda info --envs
conda create -n "shirin-codet5" python=3.7 cudatoolkit
```

### Activate virtual env
```
conda activate shirin-codet5
```
### Install python packages
```
pip install -r requirements.txt
```
### Login for WandB logging
```
wandb login <your-auth-key>
```

### Change pre-training script
[CHANGE sh/pre-train.sh]
```
chmod +x ./pre-train.sh
```

## for the consecutive runs
```
module load mamba
```

- Change to the project directory 
```
cd data/<folder-name>/CodeRef
```

- Activate the virtual environment
```
conda activate shirin-codet5
```

- Submit sbatch job to slurm and it should return the <job_id> and create files with <job-id>.out and <job-id>.err names
```
sbtach scluster-codet5-sbatch.sh
```

- Check the job status 
```
squeue -u <shortname>
```

- Check the status of the job_id
```
scontrol show --detail jobid <390248>
```

- Monitor the resources
```
nvidia-smi
```

- Cancel the job
```
scancel <job-id>
```

Find further [documentation](https://docs.s3it.uzh.ch/) about science cluster 
