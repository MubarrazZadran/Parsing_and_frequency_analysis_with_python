Email Hour Distribution:

This Python script reads a mailbox file (e.g., `mbox-short.txt`), extracts the hours from timestamps in lines that begin with `"From "`, and calculates how many emails were sent during each hour of the day.

 What It Does

- Reads a file name from user input (default: `mbox-short.txt`)
- Scans through the file line by line
- Looks for lines starting with `"From "` (not `"From:"`)
- Extracts the hour from the timestamp (e.g., `09` from `09:14:16`)
- Counts how many times each hour appears
- Sorts and prints the hour and corresponding count
