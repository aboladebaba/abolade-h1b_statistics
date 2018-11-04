import csv, sys

def getidx(columnList):
    """
    Gets the indexes of the data columns of interest for this challenge.
    The if statements can be updated as needed to reflect 
    common-string-factor that generally identify the changed columns.

    Parameter:
    ---------
    columnList: list (required)
        List of column name in the header row.

    Returns a 3-element list of indexes of required columns in the 
    following order: 
        idx[0]: index of column corresponding to the STATUS of the application
        idx[1]: index of column corresponding to the SOC_NAME for the application
        idx[2]: index of column corresponding to the Work location site for the application
    """
    colPos = [(c,p) for p, c in enumerate(columnList)]
    n = 0
    while n < len(colPos):
        x = colPos[n]
        if 'STATUS' in x[0]:
            statusPos = x[1]
        elif 'WORKLOC1_STATE' in x[0] or 'WORKSITE_STATE' in x[0]:
            statePos = x[1]
        elif 'SOC_NAME' in x[0]:
            occupationPos = x[1]
        n += 1
    idx = [statusPos, occupationPos, statePos]
    return idx

def process_file(filename, file1, file2):
    '''
    Function process a given file to extract information required for completing this challenge.

    Parameters
    ----------
    filename: STRING (required) 
        The name of the file to be processed
    file1: string (required)
        The name and location of the first output file
    file1: string (required)
        The name and location of the second output file 

    Output:
        Generated top_10_occupations.txt
        Generated top_10_states.txt
    '''
    sep = ';' #String - delimiter for the columns in each row.
    occupation = {} # data structure for counting number of each occupation as they are encountered
    states = {} # data structure for counting number of each state as they are encountered during processing
    counts = 0 # number of application with "Certified" status. 

    # Read in the file
    fh = open(filename, 'r')
     
    raw = csv.reader(fh, delimiter=sep)
    header = next(raw, None)
    idx = getidx(header)

    # Start Extracting the data elements
    for row in raw:
        if len(row) == len(header) and row[idx[0]].lower() == 'certified':
            occupation[row[idx[1]]] = occupation.get(row[idx[1]], 0) + 1
            states[row[idx[2]]] = states.get(row[idx[2]], 0) + 1
            counts += 1

    # Building the output file
    ##Top 10 occupation
    occp_file = []
    for k,v in occupation.items():
        temp = k, v, (v/counts)*100
        occp_file.append(temp)

    sorted_occp_file = sorted(sorted(occp_file, key= lambda x: (x[0])), key=lambda k: k[1], reverse=True)
    top10Occupation = sorted_occp_file[:10]
   
    occp_file = open(file1, 'w')
    occp_file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n') # writes header
    for elem in top10Occupation:
        occp_file.write('{};{};{:0.1f}%\n'.format(elem[0], elem[1], elem[2]))
    
    occp_file.close()

    ##top 10 states output
    state_file = []
    for k,v in states.items():
        temp = k, v, (v/counts)*100
        state_file.append(temp)

    sorted_state_file = sorted(sorted(state_file, key= lambda x: (x[0])), key=lambda k: k[1], reverse=True)
    top10States = sorted_state_file[:10]
    
    state_file = open(file2, 'w')
    state_file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n') # writes header
    for elem in top10States:
        state_file.write('{};{};{:0.1f}%\n'.format(elem[0], elem[1], elem[2]))

    state_file.close()


if __name__ == "__main__":

    process_file(sys.argv[1], sys.argv[2], sys.argv[3])
