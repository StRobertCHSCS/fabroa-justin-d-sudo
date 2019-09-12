# ICS2O
 
## Set Up (One time only)

### 1) Create your ICS2O-fabroa Repository
* create a github account using your k12.ca
* check your email for a new assignment in github called ICS2O-Fabroa and accept the assignment.  This will generate a new repository for you

### 2) Clone your repository
* From *your* repository StRobertCHSCS/ICS2O-fabroa-[your name], click on the **Clone or Download** button (the green one on the right) and copy the URL
* In vs code, load a new terminal, verify it is positioned in the default directory
* In terminal, clone your repository to your device `git clone [your repositoryurl]`
* In vs code, got to `File -> open folder` and choose the new director created from the previous clone 
* repeat this for any computer you will be working on

### 3) Set the upstream remote
* in the terminal `git remote add upstream https://github.com/StRobertCHSCS/ICS2O-Fabroa.git`

### 4) Set the user name and email for the project
IN the terminal, type:
```
git config user.name [yourgithub user name]
git config user.email [your user.email]
```


## Day-To-Day Steps
For each class you want to:
1. pull any of my updates from the upstream
2. pull any of your updates (if you made any changes from the another device i.e home)
3. copy any example files from the master to your working directory
4. edit files in your Working directory
5. Stage and Commit your changes
6. Push your changes to github

### 1. Pull changes from the upstream
`git pull upstream master`

### 2. Pull any of your updates down from github
`git pull origin master`

### 3. copy any example files from the master to your working directory
You can use the Explorer in vs code or use the cp command in terminal when directed to copy files to the working directory

### 4. Edit files in your Working directory
When working with class examples, make sure you are editing files in your Working directory

### 5. Stage and Commit Your Changes
#### In VS Code
* click on the Source Control icon on the left in VS Code (the forked path under the search icon )
* any modified files should appear in the CHANGES section
* Stage your changes by clicking the + in the CHANGES section header
* commit your changes by typing in a message (short and descriptive) in the message box and then CTRL + ENTER.

#### In terminal
* make the changes to your code or other files
* In the terminal (make sure you are in the directory of your project (type `pwd` on the terminal to verify your current directory):

* `git add yourfilename` to stage single file or `git add -A` to stage all changes in the project
then

```
git commit -m "type a short meaningful message in present tense about your changes"
```

### 6. Push Changes to Github
#### In VS Code
* With the Source Control pane, click on ... (more actions ), choose `Push`

#### In Terminal
* ensure that all changes have been committed
* in the terminal type `git push origin master`

