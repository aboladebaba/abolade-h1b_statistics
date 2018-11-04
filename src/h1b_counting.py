import csv, sys

def getidx(columnList):
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
    Function process a given file to extract information of interest.
    PARAMETERS
    ----------
    filename: STRING (required) - name of the file to process.
    sep: STRING (required) - delimiter for the columns in each row.
    '''
    sep = ';'
    occupation = {}
    states = {}
    counts = 0
    # Read in the file
    fh = open(filename, 'r', encoding="utf8")
    raw = csv.reader(fh, delimiter=sep)
    header = next(raw, None)
    idx = getidx(header)
    #print(idx)
    
    #"""
    # Start Extracting the data elements
    for row in raw:
        if len(row) == len(header) and row[idx[0]].lower() == 'certified':
            occupation[row[idx[1]]] = occupation.get(row[idx[1]], 0) + 1
            states[row[idx[2]]] = states.get(row[idx[2]], 0) + 1
            counts += 1

    #print(occupation)
    #print(states)

    # Building the output file
    ##Top 10 occupation
    occp_file = []
    for k,v in occupation.items():
        temp = k, v, (v/counts)*100
        occp_file.append(temp)

    sorted_occp_file = sorted(sorted(occp_file, key= lambda x: (x[0])), key=lambda k: k[1], reverse=True)
    top10Occupation = sorted_occp_file[:10]
    #print(top10Occupation)   
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
    #print(top10States)
    state_file = open(file2, 'w')
    state_file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n') # writes header
    for elem in top10States:
        state_file.write('{};{};{:0.1f}%\n'.format(elem[0], elem[1], elem[2]))

    state_file.close()
    
    #"""    



if __name__ == "__main__":

    process_file(sys.argv[1], sys.argv[2], sys.argv[3])
