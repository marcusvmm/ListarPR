# Pull Request Listing

Project that performs the pull request query in a given project/repository.

## Context
Code review is important to ensure the security and availability of the service or product. For this, a pull request visualization automation script in 'open' status is created.
In this way, it is possible to have greater control over codes that are not yet accessible.

- The script uses a GitHub API to return all Pull Requests that are open.


Example of generate script output: 
```
#Report(With Pull Requests 'OPEN')
#microsoft/mu_basecore
Bugfix: Special Separation Region Logic Can Cause Duplicate Memory Map Entries - https://api.github.com/repos/microsoft/mu_basecore/pulls/153     
Activate Improved Memory Protection Init Functionality - https://api.github.com/repos/microsoft/mu_basecore/pulls/152
Handle Special Region Overlap - https://api.github.com/repos/microsoft/mu_basecore/pulls/151
Fixing local build for PolicyDxe - https://api.github.com/repos/microsoft/mu_basecore/pulls/150
Check Page Table on Protection Policy Application - https://api.github.com/repos/microsoft/mu_basecore/pulls/149
Generalize List Functions in MemoryProtectionSupport - https://api.github.com/repos/microsoft/mu_basecore/pulls/148
Fixing bug in GuidCheck plugin + cleanup - https://api.github.com/repos/microsoft/mu_basecore/pulls/147
Update Special Region Logic to Handle Broken Cases - https://api.github.com/repos/microsoft/mu_basecore/pulls/146
Add the Interrupt Entry Code to the Special Region List - https://api.github.com/repos/microsoft/mu_basecore/pulls/145
Add Logic to Merge the Memory Map by Attributes - https://api.github.com/repos/microsoft/mu_basecore/pulls/144
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
- Put project name
- Put repo name
---