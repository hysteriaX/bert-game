import pandas as pd
import numpy as np
test_tsv=pd.read_csv('test_results.tsv', header=0,sep='\n')
test_arr = np.array(test_tsv)
answer = []
for i in range(test_arr.shape[0]):
    a = test_arr[i][0].split("\t")[0]
    b = test_arr[i][0].split("\t")[1]
    if(a>b):
        answer.append("0")  # 将字符串写入文件中
    else:
        answer.append("1") # 将字符串写入文件中
f = open('predict.txt', 'w')
f.write("\n".join(answer))
f.close()
print("Done!")