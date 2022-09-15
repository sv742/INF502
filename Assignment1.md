**On your local machine:** Using the command line, find and access the "handson/" directory (if you didn't download and unzip the file, go back to the beginning of Part 1's instructions). Then, answer the following questions (on your *Assigment1.md* file):

1. List all the branches in this repository and, for each branch, list the commits.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.

```

D:\handson>git branch
* master
  math

D:\handson>git checkout

D:\handson>git log --decorate
commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:15:28 2019 -0700

    Making a small change here

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)

```

2. Try `git log --graph --all` to see the commit tree. Paste the result here and write a paragraph to provide an interpretation of what you found.
```
* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
|
|     Making a small change here
|
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|
|       Adding some more knowledge to the function
|
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
|
|     Added a draft of A.py
|
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

       Creating all files (all empty)

I found some commits along with branch name, merge from and to, author's name, and the date of the commits. I also found the messages attached to the commits.

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.

```
diff --git a/A.py b/A.py
index 0afa98c..dc1e9bd 100644
--- a/A.py
+++ b/A.py
@@ -1,11 +1,3 @@
 #this is just an example, do not freak out
 def calculate_this(operator, num1, num2):
-   if operator == 'sum':
-      print num1 + num2
-      print 'That was easy buddy'
-   else:
-      if operator == 'subtraction':
-         print num1 - num2
-         print 'I could handle that...'
-      else:
-         print 'my knowledge is limited'
+   print 'my knowledge is limited'
diff --git a/B.py b/B.py
index e69de29..c63f94c 100644
--- a/B.py
+++ b/B.py
@@ -0,0 +1 @@
+# Another file that will receive a line of code... at least.

The lines that do not have any starting special character are the lines that exist in the Master branch as well. The lines starting with a '-' sign means that these lines are excluded in the other branch. The files starting with a '+' sign are the lines that are added to the new file.

```

4. Write a command sequence to merge the non-master branch into `master`.

```
D:\handson>git branch
* master
  math

D:\handson>git checkout math
Switched to branch 'math'

D:\handson>git commit -m "Part 4"
On branch math
nothing to commit, working tree clean

D:\handson>git checkout master
Switched to branch 'master'

D:\handson>git merge math
Merge made by the 'recursive' strategy.
 A.py | 10 +++++++++-
 1 file changed, 9 insertions(+), 1 deletion(-)

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) and (ii) change to this branch.

```
git branch math
git checkout math

```
   
6. Edit B.py adding the following source code below the content you have there.
```
print 'I know math, look:'
print 2+2
```

7. Write a command (or sequence) to commit your changes.
```
git add .
git commit -m "Updated B.py"

```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened.
```
When trying to merge 'math' branch into the 'master' branch, an error message is given. The message warns that the contents of B.py will be overwritten because of the merge.
Moreover, the warning asks to commit the changes in the 'master' branch so that they are not overwritten. This error message appears since hte contents of the B.py in both branches are different.

```
   
10. Write a set of commands to abort the merge.
```
git merge --abort

```
   
11. Now repeat item 9, but proceed with the manual merge (editing B.py). All implemented methods are needed. Explain your procedure.
```
First, I went to the math branch, and opened the B.py file in a text editor. I copied the content of the file. Then, I went back to the main branch and opened B.py in text editor.
I pasted the copied code carefully where it should have been positioned, and saved the file.

```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date.
```
git rebase master

```

13. Complete Part 2. Then, come back here and answer the following:
Report your experience of submitting the Part 2. Please, include the steps you followed, the commands you used, and the hurdles you faced (within the file you created for the **Part 1**).
```
The experience was overall good. I created a file named my name with the .md extension. I opened the cheatsheet for md file commands, and added the tile, venue, number of pages, and three main outcomes of the research paper I had read. I also added the link to the research paper. Then, I committed the md file and created a pull request to check the conflicts. The commands included pulling the repo, simple file creation, file edit, and commit changes. There were no hurdles faced in particular to which I couldn't find help.

```
