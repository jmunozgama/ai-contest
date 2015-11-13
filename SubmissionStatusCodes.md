# Submission Status Codes #

  * 10: entry record created in database.
  * 15: entry archive file placed in temporary directory. Still has to be transferred to where the compile script expects to find it.
  * 20: Ready to be unzipped and compiled.
  * 24: entry currently in the process of being compiled. The compiler script should not try to compile this entry now.
  * 27: entry has compiled successfully, and is awaiting test cases.
  * 30: error receiving submission zip file.
  * 40: compiled successfully and passed test cases.  Ready to be run.
  * 50: error while unzipping submission file.
  * 60: problem with submission file.
  * 70: error while compiling submission.
  * 80: compiled successfully but failed test cases.
  * 90 through 99: suspended for various reasons
  * 100: retired. The entry was once active and may have played games. However, the submitting user has since submitted another submission, which may or may not have compiled successfully.