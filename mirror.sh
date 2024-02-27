#!/usr/bin/env bash
#
# Script to set up mirroring from GitLab to GitHub. Requires ssh access to both.
# Clone gitlab git file as a mirror, add a github remote, push to github as mirror.
# Can be run from inside main repo.

repo="git-for-science"
gituser="jatkinson1000"

rm -rf ${repo}.git
git clone --mirror git@gitlab.com:${gituser}/${repo}.git
cd ${repo}.git
git remote add github git@github.com:${gituser}/${repo}.git
git push --mirror github
