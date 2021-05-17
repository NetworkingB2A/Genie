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


Other Gotcha...
DO NOT NAME YOU PYTHON FILE genie.py(bad things will happen)


I found most of the infomation in different video or websites. Below is a list of the locations I gathered data from.
- Siming Yuan - "pyATS & Genie – Beneath the Surface" - https://blogs.cisco.com/developer/pyATS-genie-beneath-the-surface
- Cisco - "Getting Started with pyATS" - https://developer.cisco.com/docs/pyats-getting-started/