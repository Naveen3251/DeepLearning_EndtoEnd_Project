# DeepLearning_EndtoEnd_Project

## Workflows
1.Update config.yaml <br>
2.Update params.yaml <br>
3.Update the entity <br>
4.Update the configuration manager in src config <br>
5.Update the components <br>
6.Update the pipeline <br>
7.Update the main.py <br>
8.Update the dvc.yaml <br>

## General Steps to follow for End to end project
Step 1: Create new Repository in github <br>
Step 2: Create Folder in Your local machine <br>
Step 3: Right click in the created folder and click "Open Terminal" then cmd will open <br>
Step 4: Copy the Repository url which you have created in step 1 <br>
Step 5: Now in cmd type [git clone <url>] <br>
Step 6: Now open Your Local cloned file in VS code <br>
Step 7: Start to work in your desired project

## Create vitrual environment
```
python -m venv env
```
## To activate the virtual environment
```
.\<environmentname>\Scripts\Activate
```
## To push your changes to your source repo of github 
### Use following command
```
git add . 
git commit -m "message"
git push origin main
```

### Sometimes if you try to connect with  github if will ask for Authentication
Open cmd use these two commands,<br>
```
git config --global user.gmail "Yourmail@gmail.com"
git config --global user.name "GithubUserName"
```

Then you can connect and push your updates to your repository

### You may sometimes face security issue
Open Windows powerShell Admin <br>
```
Set -ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### After completion of your work To avoid security implication
```
Set -ExecutionPolicy -Scope Process -ExecutionPolicy Restricted
```


## DVC-Data version control
DVC is used to track the changes in the pipeline.This is very helpfull in avoiding the repeated execution of the file which is already executed in the pipeline.<br>

#### 1.Initialize dvc by running<br>
```
dvc init
```
#### 2.To run dvc pipeline <br>
```
dvc repro
```
#### 3.If you have to see relationship between each stage of pipeline <br>
```
dvc dag
```
## Result

![Web capture_23-7-2023_155622_127 0 0 1](https://github.com/Naveen3251/DeepLearning_EndtoEnd_Project/assets/114800360/69282157-f296-4512-a556-1a9d45c8ef2f)

## Other basics
### how to write .gitignore file
Inside the .gitignore file, you can add patterns to ignore specific files or directories. Each pattern is written on a separate line. Here are some examples of patterns:<br>

#### Ignore a specific file: myfile.txt<br>
#### Ignore files with a specific extension: *.log, *.tmp, *.dll<br>
#### Ignore a directory: myfolder/<br>
#### Ignore all files in a directory: myfolder/*<br>
#### Ignore all .csv files: *.csv<br>
#### Ignore all files in the root folder: /*<br>
#### Ignore all files in subdirectories of a specific folder: myfolder/*/*<br>

## git and dvc for data tracking
dvc-->mainly used for tracking data
#### To initialize git : 
```
git init
```
Upload your data in env <br>
#### Now initialize dvc :
```
dvc init
```
Note: Before [dvc init] ensure you downloaded in env and when you run the dvc init command you will get .dvc and .dvcignore file<br>

#### Adding the data to dvc:<br>
```
dvc add path/filename
```
Note: After the above step we will get .gitignore and .dvc data file inside the data directory<br>

Now you have to add these ,gitignore and .dvc file in git (because .dvc file conatins hash key of the original data through that hash key we can access the original data and remoteky track without upload in github<br>
```
git add path/.gitignore
git add path/filename.dvc
```

#### switch to particular commit of data run:<br>
```
git log
```
### You will get all logs along with commit key copy your desired key and then run<br>
```
git checkout <key>
dvc checkout
```

#### Again back to original state by
```
git checkout master
dvc checkout
```

