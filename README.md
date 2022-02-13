# Disk-Analyzer-Tool

In this project, I designed and developed a disk analyzer for Linux. Its purpose is to scan your file system structure and graphically represent the directory entries with emphasis on size occupied by each entry. It has the capability to zoom in/out on selected entries (i.e., moving in or out from partitions to subdirectories to files).

## Backend

The backend of our tool which is written in c++ consists of main function, a tree class, a function that cab access and store the sizes of files(dirSize) and a listing function which writes all the extracted
information to a text file(writeFile).

1. tree class: The tree class consists of a struct Node which represents the file of directory. Each node has the attributes size, level, path, name and vector type pointer node to children. Since the files under every directory is unknow, a vector was the best option to use because its size increases when only an item is pushed into it, thus better than a fixed size array which will consume more unneeded memory and might be insufficient in some cases. The tree will be constructed incrementally by pushing back new nodes to the vector child.

2. Main Function: it starts by initializing node called disk among other several variables. in form of character, the path of the directory “/” is passed to a function called opendir()which opens the directory or return null. Then the function readdir() reads what is inside the directory. The program loops over the file inside the directory, construct their path and check if it’s a file or directory. if it’s a file, a function stat fills the struct statbuf with the file information and a new node contains file path, name, size and level is pushed back to the vector child. if it’s a directory, the program pushes back a node with its name and calles function dirsize() which takes the file path, child node that was last created, the level and returns the size of this directory. the main then opens a text file and pass it to the function WriteFile which fill it with data pushed in the tree.

3. Dirsize: This function has the same functions as the main. when it finds a directory in calls itself. it also calculates the total size of the directory while filling in the nodes inside.

4. WriteFile: This function takes the node constructed in the main and the opened file. It visits every node depth first, converts the information of the node to a string and write it to the file. In terms of performance and efficacy, this tool visits every node once which is the least possible number to get the needed data. it stores all this information in a tree then in text file all at once.

## Frontend

Our GUI was developed using python programming language. In particular, we used pyqt5 library because of the multiple features, shapes, and data structures it offers. For example, using pyqt5 we could easily specify the layout of our GUI, show buttons, write labels, etc. The communication between the backend and frontend layers of our program happens through a .txt file that is produced by the backend and that contains the level, path, name, and size of every single file or directory on the computer. This text file is then read and parsed by the frontend layer to display all the needed info. Our Disk Analyzer GUI is split into two windows: first, the Main Disks Window then, the Disks Info Window. As the name implies, the Main Disks Window simply shows the names of the four main disks on the computer so that the user can choose one of them and display its detailed info. The Disk Info Window, on the other hand, shows two graphical ways of displaying the contents of the chosen disk: A Tree structure and a Pie Chart. Below is a detailed explanation of what each window does separately:

### Main Disks Window:

- Reading and parsing the .txt file: the first job of the Main Disks Window py script is to read and parse the text file to extract the names of the four main directories on the computer. This happens by searching the text file for the specific path of each directory and cutting out its name from the file to display it on the screen. For example, we know that the home directory file path is /home/username so we used a python function the returns the username of the user (getpass.getuser()) and appended that username to /home/ then searched the text file for it to get the name of the home directory. The other three main directories follow the same way.

- Displaying names of main disks: We created four instances of the button data structure from pyqt5 library on which we displayed the names of the four main directories. The reason we chose buttons is simply because buttons are interactive, and the user can simply click on them to choose the directory they are interested in. Below is a screenshot of the Main Disks window that shows those four buttons:

<p align="center">
<img src="First Window.png">
</p>

- Passing variables between the two scripts: in order to show the graphical representation of the contents of each of those main disks in the Disk Info Window, we need to pass the path of the selected disk from the Main Disks window script to the other one. We do so again by utilizing one of the pyqt5 functions which is called button.clicked. This function calls another specific function whenever the button is clicked. In other words, each of those four buttons calls a different function whenever it is clicked. When any of them is clicked, it calls the function that starts the Disk Info Window from the Disk Info Window script setupUi() and it passes to this function the path of the selected disk so that it can be passed to the other py script to display its info.

### Disk info Window
The two ways in which we display data on the screen are Trees and Pie Charts. The overall disk info is displayed in this way:


<p align="center">
<img src="Second Window.png">
</p>

- Treewidget: the best, most organized way to show the contents and different branches of each disk is using a tree structure. Below is a screenshot that shows the output of one of the main directories. The algorithm that organizes the data in this way goes as follows:

1- After receiving the path of the directory that was selected by the user, we search the text file for every file or directory in the following tree level (or whose level = directory level +1) that starts with the same path.

2- In each of those children, we cut out the name and size from its respective line in the text file and display it as one of the main items as shown in the picture below. Then, we call a recursive function get_subitems() that gets the names and sizes of each of its children, grandchildren, etc from the text file.

<p align="center">
<img src="Items Tree.png">
</p>


3- The recursive get_subitems() function starts off by searching the text file for any children of the received item. It does so be searching for any line in the text file whose path starts off with the same path of the received item but whose level is higher by one. If any is found, it adds it as a child to the received item and the functions calls itself again with the child path to search for its children in turn. If none is found, the function returns empty.

- Pie Chart: The pie chart is also one of the most useful pyqt5 data structures with a wide range of functions to tune the chart as preferred by the user. The Main Target behind using the pie chart was to display the largest 3 directories and the remaining ones in a graphical way as shown in the screenshot below. We used a list data structure to store the names and the sizes of the largest three items as we iterated over all items in the tree part. Then, using pyqt5 series.append() function, we appended four slices to the pie chart, three for the largest 3 directories and one for others.

<p align="center">
<img src="Pie Chart.png">
</p>


## How to use
Assuming you have python3, gcc, and pyqt5 installed on your linux:

1- 
```
git clone https://github.com/Moo-osama/Disk-Analyzer-Tool.git
```
2- From the terminal, cd to the OS directory
```
cd OS
```
3- compile the c++ backend script: 
```
g++ test.cpp -o test
```
4- run the c++ file: 
```
./test
```
5- run the GUI: 
```
python3 FirstWindow.py
```
