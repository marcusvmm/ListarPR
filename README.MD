# Pull Request Listing

Project that performs the pull request query in a given project/repository.

## Context
Code review is important to ensure the security and availability of the service or product. In order to have a better management, some processes are automated by script that can help in everyday life. Among them is a simple script that shows open PRs.

- The script uses a GitHub API to return all Pull Requests that are open.


Example of generate script output: 
```
#Report(With Pull Requests 'OPEN')
#microsoft/mu_basecore
[REBASE && FF] Cherry-pick Memory Protection Init Updates - https://api.github.com/repos/microsoft/mu_basecore/pulls/155
Add CodeQL build plugin - https://api.github.com/repos/microsoft/mu_basecore/pulls/154
Fix buffer overflow when merging guard pages in MergeMemoryMap - https://api.github.com/repos/microsoft/mu_basecore/pulls/126
CodeQL Fixes - Second Pass - https://api.github.com/repos/microsoft/mu_basecore/pulls/125
Improve log messages for DependencyCheck, UncrustifyCheck, and SpellCheck - https://api.github.com/repos/microsoft/mu_basecore/pulls/115
Adding Microsoft SECURITY.MD - https://api.github.com/repos/microsoft/mu_basecore/pulls/109
Convert GCC azure pipeline to use docker image - https://api.github.com/repos/microsoft/mu_basecore/pulls/108
```



### Business assumptions
- If there is no Pull Request open, the script does not perform no action;
- If there are open Pull Requests, the script will print the title and the Pull Request link concatenated into a paginated string, respecting the limit of 10 PR's.
---

## Getting Started

### Dependencies

- [Python >= 3.11.0](https://www.python.org/downloads/ "python")
- [PIP >= 22.3](https://pypi.org/project/pip/ "pip")

---
## Setup
- In your favorite console, clone this repo then go to the created folder.. following these next steps:
  - `git clone https://github.com/marcusvmm/ListarPR.git`

  - `cd ListarPR`


### Run
- Build project(install dependencies)
- Set command `py main.py`
- Enter the name of the chosen project
- Enter the name of the chosen repository
---