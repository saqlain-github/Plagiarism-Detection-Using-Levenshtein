Question : 
    Create a plagiarism detection tool that can detect plagiarism between any two given text files

Solution :
        The detector tool accepts two command line arguments: both being the path to the text files.
        In case of plagiarism the program prints 1 as output else 0. The detector is built using Levenshtein Distance Distance(Edit Distance Algorithm).
        

    -> How to run the plagiarism detection tool:
        The tool accepts two command line arguments: both being the path to the text files.
        
        COMMAND :
                 python <filename.py> <FILEPATH1> <FILEPATH2>

        MAKEFILE :
                make FILE1=<pathofFILE1> FILE1=<pathofFILE2> run

        NOTE :  Please make sure tha paths include the extension of the text files i.e. ".txt"

        EXAMPLE :  following is a example of the command to run the tool
                make FILE1=E:/Detector/1.txt FILE2=E:/Detector/2.txt run
                python 40194915_detector.py E:/Detector/1.txt E:/Detector/2.txt

    Steps Invloved :
        1. Import necessarily inbuilt Libraries
        2. Read Required text files from the path provided
        3. Text Preprocessing
        4. Apply Levenshtein Distance Algorithm
        5. Classify if plagiarism is detected.

    Steps 1 : Import necessarily inbuilt Libraries
            - The only Libraries that are required is os, sys and re
            -  sys is used to read command line arguments
            -  OS is helps us to deal with the problem of backslash and forwardslash in differernt operation system
            -  Regex is used in text Preprocessing

    Steps 2 : Read Required text files

            -  The required files path is taken from the command line arguments.
            -  Both files are read using readlines() which returns a list of all the lines present in a file.
            -  The list of all the lines are converted into a single string using join() 

    Step 3 : Text preprocessing
            Text preprocessing is one the most important step as it help to clean the data that inturn helps to generate/Create
            models/tools or applications with better performance

            - We have create a function text_preprocessing() which takes string as a input andd also returns a string with all the following 
            operations performed.
                 -> Convert all the text to lower using .lower()
                 -> Remove all punctuation using regulat expression
                 -> Remove all the extra spaces using .strip()

    Step 4 : Levenshtein Distance Algorithm
            Create a function levenshtein_dist() that accepts two strings as input and returns a integer
            It is a dynamic programming approach that can be used to calculate the minium distance between two strings.

            - The distance is the number of operations/ required to convert first string to second string.
            
            HOW DISTANCE IS CALCULATED : 
                Distance is calculated by counting number of operations used to find minimum number of edits (operations) required.
                    Operations: 
                            -> Insert 
                            -> Remove
                            -> Replace
                    EXAMPLE : 
                            str1 = voldemort
                            str2 = dumbledore
                            distance between string 1 and 2 = 7
                    
                    Time Complexity: O(m x n) 
                    Auxiliary Space: O(m *n)+O(m+n)
                            where m = length of str1 and
                                  n =  length of str2
            
            MAIN IDEA : 
                -> Main idea is to calculate the distance between two strings so that we can Classify if both the files are similar or not.
                -> If the distance is high with respect the maxium len between the files we can conclude that the files are copy of each other.
                -> If the distance is high with respect the maxium len between the files we can conclude that the files are not copy of each other
    
    Step 5 : Classify if plagiarism. (Threshold)
            We have created a function bool_plagiarism() that returns 1 and 0 if plagiarism is detected or not.
            
            - Threshold is most important parameter that is used set if plagiarism is present or not.
            - The current Threshold is set to 75% (0.755), which is opted by trail and error

