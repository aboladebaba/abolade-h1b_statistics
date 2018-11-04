# Table of Contents
1. [Solution](README.md#solution)
2. [Input Dataset](README.md#input-dataset)
3. [Output](README.md#output)
4. [Repo directory structure](README.md#repo-directory-structure)
5. [Questions?](README.md#questions?)

# Solution

I created two functions for my entry for this challenge.
1. getidx(columnList) is a function I created to extract the indexes of respective columns of index. I found the common strings factor that can uniquely identify each columns we are intersted in using the file structure document for each year's data. Calling this function returns a three element list with the exact column position for each new file to be processed.
2. process_file(filename, file1, file2) is the main workhorse that does the actual file processing and write the results into the required output files - file1 for top_10_occupations.txt and file2 for top_10_states.txt.

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code. I envisaged that there may be case sensitivity in parssing the STATUS column of each file, I took care of this fact in my approach.

# Input Dataset

I used the input file h1b_input.csv that originally came with the clone and  created a sampled h1b_input.csv file containing about 8000 rows from one of the given test files in the shared google drive.

**Note:** Each year of data can have different columns. Check **File Structure** docs before development. 

# Output 

My program created 2 output files:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

Each line holds one record and each field on each line is separated by a semicolon (;).

1. Each line of the `top_10_occupations.txt` file contains the required fields sorted in the specified order.
2. Each line of the `top_10_states.txt` file contains the required fields sorted in the specified order.


# Repo directory structure

The directory structure for my repo looks like this:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_counting.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── abolade-test_1
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```

## Testing your directory structure and output format

I simply reuse the `run_tests.sh` file in the `insight_testsuite` folder while adding abolade-test_1 folder with all the required data file in the input folder. Also I `chmod +x run_tests.sh` to turn it to an executable file.

My tests file was stored in `.csv` format under the `insight_testsuite/tests/abolade-test_1/input` folder. Each test have a separate folder with an `input` folder and `h1b_input.csv` file and an `output` folder with the two requested output files.

You can run the test with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh 

On success:

    [PASS]: abolade-test_1 
    [PASS]: abolade-test_1 top_10_states.txt
    [PASS]: test_1 
    [PASS]: test_1 top_10_states.txt
    [Sun Nov  4 16:07:03 CST 2018] 2 of 2 tests passed


Here is a <a href="https://github.com/aboladebaba/abolade-h1b_statistics">link</a> to my repo.

# Questions?
I could be reached for answers to your question(s) at abolade.babawale@gmail.com
