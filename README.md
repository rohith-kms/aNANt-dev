# aNANt-dev

## 1 Introduction

Developer repository for aNANt materials database. Owned by ThSim group from MRC, IISc.


## 2 Contributing to aNANt:

Project management for aNANt is done almost entirely through GitHub. We will review some useful git concepts in the following subsection, followed by step-by-step instructions on making changes to the code.

### 2.1 Useful GitHub concepts:

- __Cloning:__ Cloning is the process of copying a GitHub repository into your local machine. For cloning the entire aNANt repo, the command is:
`git clone https://github.com/rohith-kms/aNANt-dev` This will clone the main branch. If you want to clone another branch (only), the command is: `git clone --single-branch --branch <branch-name> https://github.com/rohith-kms/aNANt-dev`


- __Branching:__ A branch is a parallel verion of the repository. Any changes made in a separate branch will not affect the `main` branch. When developing a new feature, create a new branch and make all changes there. Merge with the `main` branch only after all development is completed and bugs are fixed. To check what branch you are working on currently (in your local machine), use `git branch`. To switch to another branch, use `git checkout <branch-name>`. You can create a branch from the GitHub webpage.

- __Commiting:__ Once you have made changes to the project, you have to commit those changes. The command for this is `git commit -m "Your message"` make sure to include relevant and informative commit messages, so that everyone can clearly understand what changes were made to the project. Before commiting, make sure you have added all the new file paths using `git add .` Use `git status` to check what all you are changing. To push the changes from your local computer to the remote branch, use `git push`

- __Pull requests and merging:__ Once you have developed your branch to a sufficient point, it is time to `merge` it with the `main` branch. To do this, you will have to submit what is called a pull request. Go to the GitHub webpage and click on "compare and pull request". As with the commits, you will need to include a message along with your pull request. Make sure these messages are informative and to the point. If you are sure of your changes and you have permission, you can merge with the `main` branch. If you're not sure, get someone to review your changes and merge.

### 2.2 Step-by-step instructions:

1. Create a branch through the GitHub website. If you're not sure how, click [here](https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/managing-branches)

2. Clone the new branch onto your local computer. `git clone --single-branch --branch <branch-name> https://github.com/rohith-kms/aNANt-dev`

3. Make changes to the project.

4. Run `git add .`

5. Commit your changes: `git commit -m "Informative commit message"

6. When you reach a milestone, push your changes into the remote repo. `git push`

7. Once you are done with the development of your feature, push your changes and create a pull request through the GitHub webpage. If youre not sure how, click [here](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi-gcDau_fsAhUOeisKHRiiCAEQ0gIoADAbegQIHBAJ&url=https%3A%2F%2Fdocs.github.com%2Fen%2Ffree-pro-team%40latest%2Fgithub%2Fcollaborating-with-issues-and-pull-requests%2Fcreating-a-pull-request&usg=AOvVaw3-FQu7PRhMBsDZ_4zbVTtw)

8. If you are really sure of your changes, you can go ahead and [merge](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/merging-a-pull-request) if you have permission. However, this is not recommended. Ideally before merging, we should all look at the pull request and [comment](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request) on it. Click on the links for detailed instructions on how to do each of these.

