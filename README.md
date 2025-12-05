# advent_of_the_code2025
This will be our join code, each one will have a folder to put their code, and we will do PRs to gain exp.
If you have any questions ask Yufan.

## Spells
cantrip
Minor Illusion
- Virtual Environment: 
    `python3 -m venv name_of_ur_virt_env` creates a virtual environment in your current directory
    `source name_of_ur_virt_env/bin/activate` activate you virtual environment
    Each with their own independent set of Python packages installed in their site directories
    Known as the virtual environment’s “base” Python
    By default is isolated from the packages in the base environment
    So that only those explicitly installed in the virtual environment are available
- Simulation: `sudo apt-get install -s package_name1_v1`
    never run apt-get install blind; simulate first.
    The `-s` (or `--simulate`) flag:
        shows all packages that would be installed/upgraded/removed
        **makes no actual changes
- Inspect: `apt-cache policy package_name1_v1 package_name2_v1`
    See what version apt thinks is available
    This will show:
        Installed version (if any)
        Candidate version
        Which repository it comes from, if it does
