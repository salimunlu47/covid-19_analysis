#Copy the related information from CSV file and paste it to here and create a list
turkey_case = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,5,5,6,18,47,98,192,359,670,1236,1529,1872,2433,3629,5698,7402,9217,10827,13531,15679,18135,20921,23934,27069,30217,34109,38226,42282,47029,52167,56956,61049,65111]
#sliced the list beginning from March 1st
turkey_case_sliced = turkey_case[39:]
#multiplying by 2 each element in the list
turkey_case_sliced_expected = [i * 2 for i in turkey_case_sliced]
