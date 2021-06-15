[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# Genie
Playing around with Genie and pyATS

## TODO: few things to fix/update
  - Add more comments
  - Add a function to the CDP neighbor class that will update my testbed file. (Maybe, but need to figure out a wait to dynamically update my testbed file)
  - Add more parsers

What is the difference between pyATS and Genie? 
- pyATS
    - define topologies and device/interconnects
    - programmatically interact with various devices
    - write, execute and report on test scripts

- Genie
    - parsers: converting/formatting command output into Pythonic data structures
    - models: OS/platform agnostic Python classes that represents feature/protocol configuration state and operational status
    - triggers & verifications: reusable pool of data-driven testcases

Which one do I use, Genie or pyATS?
BOTH

Which one should I use Ansible or Python in combnation with pyATS|Genie?
This is up to you. What do you want to use and what are you trying to accomplish?

    - CLI - If you are just learning Genie|pyATS, I reccommend playing around with the Genie CLI. The CLI is not as expandable or as powerfull by itself. However, it's a great way to get started in tool.
    - Python - This is the most customizable. NEED TO ADD MORE INFO HERE
    - Ansible - NEED TO ADD MORE INFO HERE

What are the modes of Genie?

What makes up a pyATS Network test project?
    - Testbed
      - YAML Files
      - Describes network topology
    - AEtest Testscripts
      - 1 or more Python Files
      - Define setup, execution and cleanup of tests
    - Easypy jobfiles
      - Python files
      - Combines testscripts and defines runtime, logging and archives

    |--- Testbed.yaml
    |---Network_test_projects
    |   |---testbed_connections.py
    |   |---interface_errors.py
    |   |---network_test_job.py
    | 

  ## Convenience Commands
    pyats create testbed
    pyats create project

AEtest Testscript Basics
- Phases
  1. CommonSetup
     - Everything that must be done before your can actually run your test
  2. Testcase(s)
     - This is the actual test you want to run
     - Cleanup might not always need to happen so you may decide to ommit the setup or clean up steps
  3. CommonCleanup
     - This is to cleanup anything you need to clean
- View the example folder

Easypy Jobfiles
- A "job" is a combination of test scripts together for excution
- Each testscript to be run is a "task"
  - Note: taskid is optional and defaults to Task-#
- Each job executions generates single log and archive
- View the example folder

How you would run the job

<code> pyats run job sample2/sample2_job.py --testbed testbedFile.yaml </code>

### Protip
Use the following command to view your logs locally:

<code>pyats logs view</code>

^^^
This will give you a HTML file in an easy to read format

## Other Notes
- if you do not want to enter config mode enter the following in your testbed connect 

  <code> testbed.connect(init_exec_commands=[], init_config_commands=[])</code>


- if you do not want to see all the connection status enter the following into your testbed connect

  <code> testbed.connect(log_stdout=False)</code>

Other Gotcha...
DO NOT NAME YOU PYTHON FILE genie.py(bad things will happen)


I found most of the infomation in different video or websites. Below is a list of the locations I gathered data from.
- Siming Yuan - "pyATS & Genie – Beneath the Surface" - https://blogs.cisco.com/developer/pyATS-genie-beneath-the-surface
- Cisco - "Getting Started with pyATS" - https://developer.cisco.com/docs/pyats-getting-started/