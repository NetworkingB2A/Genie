from pyats.easypy import run

def main (runtime):
    #run scripts
    run (testscript='testscript1.py',
         taskid="Script 1",  #used for logging and notification 
         runtime=runtime)
    run (testscript='testscript2.py',
         taskid="Script 2",
         runtime=runtime)
    run (testscript='testscript3.py',
         taskid="Script 3",
         runtime=runtime)
    run (testscript='testscript4.py',
         taskid="Script 4",
         runtime=runtime)
