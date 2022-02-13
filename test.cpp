#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <limits.h>
#include <langinfo.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <inttypes.h>
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
using namespace std;

struct Node
{
    int  size;
    int level;
    string name;
    string path;
    vector< Node *>child;
};

Node *newNode(int size,int level, string name, string path)
{
    Node *temp = new Node;
    temp->size = size;
    temp->name = name;
    temp->level= level;
    temp->path = path;
    return temp;
}

void LevelOrderTraversal(Node * root)
{
    if (root==NULL)
        return;

    // Standard level order traversal code
    // using queue
    queue<Node *> q;  // Create a queue
    q.push(root); // Enqueue root
    while (!q.empty())
    {
        int n = q.size();

        // If this node has children
        while (n > 0)
        {
            // Dequeue an item from queue and print it
            Node * p = q.front();
            q.pop();
            cout << p->size << " ";
            cout << p->name << " ";
            cout << endl;
            // Enqueue all children of the dequeued item
            for (int i=0; i<p->child.size(); i++)
                q.push(p->child[i]);
            n--;
        }

        cout << endl; // Print new line between two levels
    }
}
void writeFile(struct Node* disk, ofstream &myfile)
{
        if(disk->level>5)
            return;
        string s= "!" + to_string(disk->level)+ "@" +disk->path + "#" + disk->name + "$" + to_string(disk->size) + "^" +"\n";
        cout << s;
        myfile << s;
        for (int i = 0; i <disk->child.size(); i++)
            {
               // if(disk->child[i]!=NULL)
                    writeFile(disk->child[i], myfile);

            }


}
int  dirSize( char * root, struct Node* node, int level)
{
        int  total= 0;
        int  currentDir=0;
        DIR *dr;
        int z=0;
        level ++;

        struct dirent  *dp;
        struct stat  statbuf;
        if((dr = opendir(root))== NULL)
        {
           // printf(" %s \n","Could not open current directory \n");
            return 0;
        }

        while ((dp = readdir(dr)) != NULL)
        {
            char filepath[PATH_MAX + 1];
            strcpy(filepath, root);
            strcat(filepath, "/");
            strcat(filepath, dp->d_name);
            if(strcmp(dp->d_name, "." )!=0 && strcmp(dp->d_name, ".." )!=0)
            {   if(dp->d_type != DT_DIR)
                {
                    if (stat(filepath, &statbuf) == 0)
                    {
                        (node->child).push_back(newNode((intmax_t)statbuf.st_size,level,dp->d_name ,filepath));
                        z++;

                        total += (intmax_t)statbuf.st_size;
                    }
                }else if(dp->d_type == DT_DIR)
                {



                    (node->child).push_back(newNode((intmax_t)currentDir,level,dp->d_name,filepath ));
                    currentDir = (intmax_t)dirSize(filepath, node->child[z], level);
                    node-> child[z]->size = currentDir;
                    total += currentDir;
                    z++;

                }
            }
        }
        closedir(dr);
        return total;
}


int main()
{
    struct Node *disk = newNode( 50,0,"whole disk","/");

    int  totalSize=0;
    int  currentDirSize=0;
    int z=0;
    int level=1;
    char *root = "/";
    struct dirent  *dp;
    struct stat  statbuf;

    DIR* dr = opendir(root);
    if (dr == NULL)  // opendir returns NULL if couldn't open directory
    {
        printf(" %s \n","Could not open current directory 1 \n");
        return 0;
    }
    while ((dp = readdir(dr)) != NULL) {

        char filepath[PATH_MAX + 1];
        strcpy(filepath, root);
        strcat(filepath, "/");
        strcat(filepath, dp->d_name);

        if(strcmp(dp->d_name, "." )!=0 && strcmp(dp->d_name, ".." )!=0)
        {   if(dp->d_type != DT_DIR)
            {

                if (stat(filepath, &statbuf) == 0)
                {
                    (disk->child).push_back(newNode((intmax_t)statbuf.st_size,level, dp->d_name ,filepath));
                    totalSize+= (intmax_t)statbuf.st_size;
                    z++;

                }
                else
                    printf(" %s \n","error, go fuck yourself");

            }else if(dp->d_type == DT_DIR)   // directory
            {
                (disk->child).push_back(newNode((intmax_t)currentDirSize,level, dp->d_name ,filepath));
                currentDirSize = (intmax_t)dirSize(filepath, disk->child[z],level);
                disk-> child[z]->size = currentDirSize;
                totalSize+= currentDirSize;
                z++;
            }
        }
    }
    disk->size =totalSize;
    //cout << disk->child[2]->size;
    //cout << disk->child[2]->name;
    //LevelOrderTraversal(disk);
    closedir(dr);
    ofstream myfile ("dir.txt");
    if (myfile.is_open())
    {
        writeFile(disk, myfile);
        myfile.close();
    }
    else cout << "Unable to open file";


    return 0;
}
