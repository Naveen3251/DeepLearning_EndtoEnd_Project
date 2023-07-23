# DeepLearning_EndtoEnd_Project

## Workflows
1.Update config.yaml <br>
2.Update secrets.yaml [Optional] <br>
3.Update params.yaml <br>
4.Update the entity <br>
5.Update the configuration manager in src config <br>
6.Update the components <br>
7.Update the pipeline <br>
8.Update the main.py <br>
9.Update the dvc.yaml <br>

## General Steps to follow for End to end project
Step 1: Create new Repository in github <br>
Step 2: Create Folder in Your local machine <br>
Step 3: Right click in the created folder and click "Open Terminal" then cmd will open <br>
Step 4: Copy the Repository url which you have created in step 1 <br>
Step 5: Now in cmd type [git clone <url>] <br>
Step 6: Now open Your Local cloned file in VS code <br>
Step 7: Start to work in your desired project

## Create vitrual environment
'''python
python -m venv env <br>
## To activate the virtual environment
'''python
.\environmentname\Scripts\Activate

## To push your changes to your source repo of github 
### Use following command
'''python
git add . <br>
git commit -m "message" <br>
git push origin main <br>

#### Sometimes if you try to connect with  github if will ask for Authentication
Open cmd use these two commands,<br>
git config --global user.gmail "Yourmail@gmail.com" <br>
git config --global user.name "GithubUserName" <br>

Then you can connect and push your updates to your repository

#### You may sometimes face security issue
Open Windows powerShell Admin <br>
Set -ExecutionPolicy -Scope Process -ExecutionPolicy Bypass <br>
##### After completion of your work To avoid security implication
Set -ExecutionPolicy -Scope Process -ExecutionPolicy Restricted <br>


## DVC-Data version control
DVC is used to track the changes in the pipeline.This is very helpfull in avoiding the repeated execution of the file which is already executed in the pipeline.<br>

1.Initialize dvc by running<br>
dvc init <br>
2.To run dvc pipeline <br>
dvc repro<br>
3.If you have to see relationship between each stage of pipeline <br>
dvc dag

## Result

![Web capture_23-7-2023_155622_127 0 0 1](https://github.com/Naveen3251/DeepLearning_EndtoEnd_Project/assets/114800360/69282157-f296-4512-a556-1a9d45c8ef2f)
