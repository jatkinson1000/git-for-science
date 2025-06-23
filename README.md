# git-for-science

Materials for a workshop for educating academic researchers in how to use the
features of git and GitLab/GitHub effectively to enhance scientific software development.


### A note on mirrors

This repository exists mainly as a
[GitLab repository](https://gitlab.com/jatkinson1000/git-for-science)
with a [mirror on GitHub](https://github.com/jatkinson1000/git-for-science).\
Please open issues and contributions on GitLab.

## Usage

This material is designed to be delivered as either a live demonstration or as
a code-along with participants.

There is an accompanying set of slides which can be viewed at
[jatkinson1000.github.io/git-for-science](https://jatkinson1000.github.io/git-for-science).
The code for generating these is available in the [`slides/`](slides/) directory.

A complete walkthrough for delivering the workshop, with references to the slides,
can be found in [the walkthrough](#walkthrough) at the end of this README.

## License

Copyright &copy; Jack Atkinson

Unless otherwise noted the programs and other software provided in this repository are
made available under an [OSI](https://opensource.org/)-approved
[GPL-3.0-only](https://opensource.org/license/gpl-3-0/) license.

Unless otherwise noted the teaching materials provided in this repository are
made available under a Creative Commons [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
license for which the full legal text is [available online](https://creativecommons.org/licenses/by/4.0/legalcode).

## Acknowledgments

Anyone is welcome to make use of these materials in education, build upon them, or
use them as inspiration.
If you do this please provide visible acknowledgment.

## Contributions

Contributions and collaborations are welcome from anyone with an
interest in RSE education.

For bugs, feature requests, and clear suggestions for improvement please
[open an issue](https://gitlab.com/jatkinson1000/power-up-python/-/issues).

If you built something upon this that would be useful to others, or can
address an [open issue](https://gitlab.com/jatkinson1000/git-for-science/-/issues),
please [fork the repository](https://gitlab.com/jatkinson1000/git-for-science/-/forks/new)
and open a merge request.

### Code of Conduct

Everyone participating in this project, including as a participant at a workshop,
is expected to treat other people with respect and more generally to follow
the guidelines articulated in the
[Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/).

## Walkthrough

### Setup

The completed workshop is in this branch: `main-real`.
The starting point for a workshop has the git tag `start-workshop` and should be made
available to participants on the `main` branch.

Before a workshop:

- Fork this repository.
- Clone this repository.
- Run:
  ```
  git checkout -b main
  git reset --hard start-workshop
  git push origin main
  ```
- Change the default branch from `main-real` to `main` on GitLab/GitHub.

This will leave the online repo in the "starting state" for the workshop
whilst leaving the "improved" files in an adjacent `main-real` branch.

It is advised to make your terminal prompt relatively simple so as not to distract or
confuse participants.
Similarly disable any unusual aspects of your git config such as commit signing.

### Delivery

#### Introduction

The first part of the workshop is delivered from the slides and is an introduction
to git.

It presents:

- the idea of git as being version control
- where to get git
- the different areas of git (workspace, index/staging, local repo, remote/upstream repo).
- the key git commands (as a refresher -- some prior knowledge is assumed)
- a conceptual model for understanding git based on diffs and how to read them
- how git _actually_ works (optional)

#### Exercise 1
The first exercise comes after recapping the basic commands:

- Introduce participants to finding repositories on GitHub/GitLab
- Clone the repository with main as the default branch.
- Encourage them to Fork and clone their local copy if they have an account.\
  Participants without an account can clone this repository via https.
- For newer users of git demonstrate use of the basic commands by creating a new text
  file, adding it to the index, committing, and pushing, showing that it appears online.
- Take a look at the code and try to use it:
  - Create a virtual environment locally (this will be useful to demonstrate .gitignore)
  - Try and use the code in the python repl.\
    Demonstrate being unable to use the code because we don't know how to install it or
    what the dependencies are!

#### README

The first topic is the introduction of the README file and why it is useful.
Examples of good and bad READMEs are given, with a summary of what should be in them.

#### Exercise 2

- Show that we can install the code with:
  ```
  pip install -e .
  ```
  and add an installation section to the README.
- Show basic usage of the code in the repl
  ```python
  from pyndulum import equations as peq
  peq.get_period(2)
  2.837006706885775
  peq.check_small_angle(0.0002)
  True
  ```
  and add getting started/demo to the README.
- Improve the description
- Add contribution and issue information
- Add acknowledgments
- Add anything else you see fit as suggested by participants.

An example of this task can be seen in commit
[d3d78e30 (GitLab)](https://gitlab.com/jatkinson1000/git-for-science/-/commit/d3d78e3005f2a057af1e403d704dfa52ef31a406)
or
[d3d78e30 (GitHub)](https://github.com/jatkinson1000/git-for-science/commit/d3d78e3005f2a057af1e403d704dfa52ef31a406)
on `main-real`.

#### License

Discuss the importance of open source software having a license and the different types
(permissive, copyleft etc.)

#### Exercise 3

- Demonstrate adding a license using the GitHub/GitLab interface.
- Show how we are offered templates and select one.
- Show that this is an online edit, and we now need to `git pull` back to our locak repo.

An example of this task can be seen in commit
[2340f072](https://gitlab.com/jatkinson1000/git-for-science/-/commit/2340f07267291bfb1acd65e491cad5e1a7870925)
on `main-real`.

#### .gitignore

Discuss the importance of the .gitignore file and why it is useful.

#### Exercise 4

- Use the GitLab/GitHub interface again to add a .gitignore file.
- Show that we are offered templates for languages.
- Demonstrate editing the template before commit to add a `data/` directory.
- Mention [gitignore.io](https://www.gitignore.io) for multi-language templates.
- Remember to do a local pull again

An example of this task can be seen in commit
[2340f072 (GitLab)](https://gitlab.com/jatkinson1000/git-for-science/-/commit/2340f07267291bfb1acd65e491cad5e1a7870925)
or
[5dbe33ec (GitHub)](https://github.com/jatkinson1000/git-for-science/commit/2340f07267291bfb1acd65e491cad5e1a7870925)
on `main-real`.

#### Issues

Introduce the idea of GitHub/GitLab issues and how they help in project management.

#### Exercise 5

- Using the relevant issue tracker open issues for adding energy equation and adding
  an inverse length equation.
- If there are participants encourage them to open the second (or more).

Examples of the issue to open can be seen at
[#1 on GitLab for Energy](https://gitlab.com/jatkinson1000/git-for-science/-/issues/1)
and
[#2 on GitLab for Length](https://gitlab.com/jatkinson1000/git-for-science/-/issues/2)

#### Branches

Introduce branches and how we create them.

Discuss how branches are useful in collaborative projects, but also solo projects for
improving workflow, allowing multitasking, and keeping things organised.

#### Exercise 6

- Create a branch and add the energy equation with good quality.\
  See commit [42b73e15 (GitLab)](https://gitlab.com/jatkinson1000/git-for-science/-/commit/42b73e154ed7ccc83aa696da0e4503351f153c83)
  ```python
  def energy(m: float, len: float, theta: float) -> float:
      """
      Calculate the energy of a pendulum.

      Parameters
      ----------
      m : float
          mass of the pendulum bob [kg]
      len : float
          length of the pendulum [m]
      theta : float
          maximum angle of displacment of the pendulum [radians]

      Returns
      -------
      float
          energy [kg . m2 /s2] of the pendulum
      """
      return m * 9.81 * max_height(len, theta)
  ```
- Create a branch and add the length equation with bad quality and an error.\
  See commit [650c7d9a (GitLab)](https://gitlab.com/jatkinson1000/git-for-science/-/commit/650c7d9a7172355bdb9c9ce351eedc5fc8c6ff86)
  note the bad commit message "Add equation" as well!
  ```python
  def inv(p):
      return ((p / 2.0 * np.pi) ** 2) / 9.81
  ```
- Don't merge these branches on the command line, instead push them up to the remote.

#### Merge/Pull Requests

Discuss how GitHub/GitLab have Pull/Merge requests, and how this makes the process
of merging branches friendlier.
Also discuss their use in development as a way of documenting discussions and tracking
progress/tasks.

As an optional extra here discuss kanban boards on GitLab/GitHub, and other project
management tools. E.g. labels, linking issues and requests etc.

#### Exercise 7

- Open a Merge/Pull request for the energy equation branch.
- Show how to write a nice statement with linking to close issues, task boxes, etc.
  See for example
  [Merge #2 on GitLab](https://gitlab.com/jatkinson1000/git-for-science/-/merge_requests/2).
- Show how to merge the code online.
- Remember to pull your changes back locally.
- Open a Merge/Pull request (or better, ask a colleague to open) for the length equation
  with a bad statement e.g. "Added equation".
  See for example [Merge #5 on GitLab](https://gitlab.com/jatkinson1000/git-for-science/-/merge_requests/5)\
  Note: if a colleague is opening a PR they should ensure their fork is up to date
  (or branch from the workshop starting point) to avoid other detritus entering their PR.
- Do not merge yet.

#### Code Review

Introduce the idea of code review and how it is useful.
Discuss how to conduct a code review with colleagues or peers.

#### Exercise 8

- Return to the poor length equation request.
- Conduct a code review with participants.
    - Note a lack of docstrings showing how to write a general review
    - Note a poor choice of function name showing how to write an inline comment
    - Note the error in the code requiring `* 9.81` instead of `/ 9.81` showing how to
      make a suggestion
    - Note that the commit message and PR isn't helpful and needs more detail.
    - See for example [Merge #5 on GitLab](https://gitlab.com/jatkinson1000/git-for-science/-/merge_requests/5)
- Afterwards make the changes requested and push back up.\
  These can be seen in commits
  - [43a89364](https://gitlab.com/jatkinson1000/git-for-science/-/commit/43a89364e5a4efd8e9321c7a00c0bd7b375e3e0e)
  accepting the suggestion for mathematical error (show this)
  - [81482ce8](https://gitlab.com/jatkinson1000/git-for-science/-/commit/81482ce8271380bdb7101b89c9e693e865b4e485)
  for function name and docstrings:
  ```python
  def get_length(p: float) -> float:
      """
      Calculate the length of a pendulum based on period.

      Parameters
      ----------
      p : float
          period [s] for a swing of the pendulum

      Returns
      -------
      float
          length of the pendulum [m]
      """
  ```

Bonus Content:

- Merging the length equation branch may well lead to merge conflicts.
- If the audience seems at a suitable level demonstrate resolving this and the typical
  notation.
- This can be useful as users are likely to see conflicts as they use git in
  better ways and they can be quite daunting!
- Note that it is better to do this manually where possible, rather than with an
  automated system, as sometimes it is not easy.

#### Summary

Summarise what has been learnt and finish off.

### Cleanup

After the workshop is complete:

- Change the default branch from `main` back to `main-real` on GitLab/GitHub.
- Delete the `main` branch on GitLab/GitHub ready for the next workshop.

