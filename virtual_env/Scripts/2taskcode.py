import os 
import csv

data_path = "C:/Users/user/Desktop/intern/quantium-starter-repo/data/"
output_path = "C:/Users/user/Desktop/out/final_output.csv"

with open(output_path, "w", newline = "") as file:
      a = csv.writer(file)
      title = ["sales", "date", "region"]
      a.writerow(title)
      for i in os.listdir(data_path):
            with open(f"{data_path}{i}", "r") as file:
                 b = csv.reader(file)
                 for j in b:
                       if j[0] == "pink morsel":
                             sale = float(j[1][1:]) * int(j[2])
                             d = [sale, j[3], j[4]]
                             a.writerow(d)
                            
                            