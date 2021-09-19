git add . && git commit -m "update readme"

if error comes then 
git remote add origin-push https://github.com/sharad28/ML_CICD_ENDTOEND.git

git fetch origin-push

git push --force-with-lease origin-push
