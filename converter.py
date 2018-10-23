percentlist = [0.00,1.60,2.70,3.80,5.10,6.30,
8.60,
11.00,
11.50,
12.00,
12.60,13.20,
14.90,
16.50,
17.00,
17.40,
18.40,
19.40,
20.10,
20.80,
22.60,
24.50,
25.00,
25.40,
26.20,
27.00,
29.70,
32.30,
33.60,
34.90,
35.90,
36.90,
38.10,
39.40,
42.60,
45.80,
46.60,
47.50,
48.80,
50.00,
51.20,
52.50,
53.40,
54.30,
57.40,
60.60,
61.90,
63.10,
64.10,
65.10,
66.40,
67.70,
70.30,
73.00,
73.80,
74.60,
75.10,
75.50,
77.40,
79.30,
79.90,
80.60,
81.60,
82.60,
83.00,
83.50,
85.10,
86.80,
87.40,
88.10,
88.60,
89.10,
91.40,
93.70,
95.00,
96.20,
97.30,
98.40,
100.00]
 
linelist = [20,
19.5,
19,
18.5,
18,
17.5,
17,
16.5,
16,
15.5,
15,
14.5,
14,
13.5,
13,
12.5,
12,
11.5,
11,
10.5,
10,
9.5,
9,
8.5,
8,
7.5,
7,
6.5,
6,
5.5,
5,
4.5,
4,
3.5,
3,
2.5,
2,
1.5,
1,0,-1,-1.5,
-2,
-2.5,
-3,
-3.5,
-4,
-4.5,
-5,
-5.5,
-6,
-6.5,
-7,
-7.5,
-8,
-8.5,
-9,
-9.5,
-10,
-10.5,
-11,
-11.5,
-12,
-12.5,
-13,
-13.5,
-14,
-14.5,
-15,
-15.5,
-16,
-16.5,
-17,
-17.5,
-18,
-18.5,
-19,
-19.5,
-20]
 
games_info = []
 
def convert_percent_to_line(percent):
  assert(isinstance(percent, float))
  mindiff = 200
  index = None
  for i in range(len(percentlist)):
    entry = percentlist[i]
    diff = abs(percent - entry)
    if diff < mindiff:
      mindiff = diff
      index = i
 
 
  return linelist[index]
 
 
 
 
while True:
  #percent = float(input("What is the percent chance to win?"))
  csv_filename = (input("Enter CSV filename with Column 1 = team name, Column 2 = FPI chance."))
  with open(csv_filename, 'r') as csv_file:
    for line in csv_file:
      game = line.split(',')
      games_info.append(game[0]+","+str(convert_percent_to_line(float(game[1]))))
 
  print()
  with open('result.csv', 'w') as result_file:
    for line in games_info:
      result_file.write(line+"\n")

  games_info = []
