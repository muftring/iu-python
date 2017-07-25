Michael Uftring
I590 - Python
Summer 2017
--------------------------------------------------------------------------------

Final Project, Phase 3

Instructions for running the main.py program which will perform some basic
statistical analysis of the input data: Wisconsin Breast Cancer, and run a
classification algorithm on the data.

The program will prompt the user to provide the name of the CSV file which
contains the data; a default value for the file name is also provided.
The program will alsp promot the user to specify the number of iterations
for the k-means classification.

The program will generate histograms of each data attribute and save them in a
PNG file named after the attribute number (i.e., A2.png, A3.png and so on). 
The statistical analysis table is output to the console.

Next the program will use the k-means method to classify the data into each of 
the two classes: 2-Benign, 4-Malignant. The algorithm will run 1500 iterations
which can take several minutes to run. Upon completion, the final means will be
displayed along with a sampling of the first twenty rows in each class.

Finally, the program will compute and display some performance metrics on the
classification. A Confusion Matrix will be presented, which shows the true and
false positives and negatives. Also the error rate for each classification
prediction will also be computed and displayed.

Usage:

  ./main.py

