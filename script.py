import sys
from functions import get_indeed_internships

if len(sys.argv) == 1:
  get_indeed_internships()
else:
  get_indeed_internships(sys.argv[1])