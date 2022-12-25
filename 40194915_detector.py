import os,sys, re

def levenshtein_dist(string1, string2):
    x = len(string1)
    y = len(string2)
    matrix = [[i] for i in range(1, x + 1)]   #  matrix rows
    matrix.insert(0, list(range(0, y + 1)))   # matrix columns
    for j in range(1, y + 1):
        for i in range(1, x + 1):
            if string1[i - 1] == string2[j - 1]:   
                substitutionCost = 0
            else:
                substitutionCost = 1
            matrix[i].insert(j, min(matrix[i - 1][j] + 1,matrix[i][j - 1] + 1,
                               matrix[i - 1][j - 1] + substitutionCost))
    return matrix[-1][-1]



def bool_plagiarism(d, root, threshold):
    if d <= root * threshold:
        result = 1
    else:
        result = 0
    return result   


def text_preprocessing(text):
    text =  re.sub(r'[^\w\s]', '', text)
    # text = text.translate(text.maketrans("",""), string.punctuation)
    text = text.lower()
    text = text.strip()
    return text


def is_plagiarism(file1: str, file2: str, threshold) -> str:
    text1, text2  = [], []
    with open(file1, 'r', encoding="utf8") as f:
        text1 = f.readlines()
    text1 = ''.join(text1)
    with open(file2, 'r', encoding="utf8") as f:
        text2 = f.readlines()
    text2 = ''.join(text2)
    text1 = text_preprocessing(text1).split()
    text2 = text_preprocessing(text2).split()
    distance = (levenshtein_dist(text1,text2))
    result = bool_plagiarism(distance, max(distance, len(text1), len(text2)), threshold)
    return result, distance


if __name__ == '__main__':
        threshold = 0.7555
        if len(sys.argv) > 3:
            print("Invalid arguments")
        file1, file2 = sys.argv[1], sys.argv[-1]
        file1 = os.path.join(os.getcwd(),sys.argv[1])
        file2 = os.path.join(os.getcwd(),sys.argv[-1])
        result, distance  = is_plagiarism(file1, file2, threshold)
        print(f"{result}")
        # data_folder = "data"
        # folders = [os.path.join(data_folder,x) for  x in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder,x))]
        # for folder in folders:
        #     file1 = os.path.join(folder, "1.txt")
        #     file2 = os.path.join(folder, "2.txt")
        #     result, distance  = is_plagiarism(file1, file2, threshold)
        #     print(f"{result}")
   