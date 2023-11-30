 
from bardapi import Bard

import os
os.environ['_BARD_API_KEY']="dQhnUsOnWpl6lL6q5-FOw1rf_-hddblWryrc7LMBYFF3XNKFySzQiMI8Wes-Ck2X2sg9wg."
h1=input("enter somethings ;")

print(Bard().get_answer(h1)['content'])

