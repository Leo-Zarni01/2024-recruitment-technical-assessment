To help with marking, I have drafted a brief breakdown of my workings for the tasks.

Since we will be working on a file system with a **parent-child** relationship, there exists a certain **hierarchical** structure for the system. Since the number of children per file is uncertain, I cannot simply assume this structure to be a binary tree, so I thought it was best to treat the file system as a **Graph**. Therefore, I have created a Graph class, where each node (vertex) is a `File`. In this question, I have represented the graph in a form of adjacency list, so the Graph has a list of adjacency lists as its field.

There are also helper functions which I have defined; most of them are obvious in what they do, but I think it is worth mentioning what `dfs()` does --- I will talk about it in my explanation for Task 3.

Task 1 was pretty straighforward. First, I converted the `Files` array into a directed graph. Since my graph representation is in a form of adjacency list, to determine whether a `File` is a _leaf_ file (node) or not, I just have to see the length of the adjacency list for each file. If the length of the adjacency list for file `X` is $\large 1$, then `X` is a _leaf_ file.

For Task 2, I relied on the two helper functions, `find_categories` and `sort_categories`. The former iterates through the `Files` array and keeps track of the number of files that matches the category. The latter, albeit fancy, is simply a sorting function that uses a lambda function. For reference, I got the solution from Stackoverflow:
`https://stackoverflow.com/questions/73181017/how-to-sort-a-list-by-number-first-in-descending-order-and-then-by-alphabet-in-a`

Here was how I approached Task 3. Since the prompt wants me to also account for the sizes of every file's children and grandchildren, I will be required to exhaustively go through all the relations between each and every file and update the file size accordingly. We will stop updating the size of the file once we reach the _leaf_ file, which implies that we will have to search the graph prioritizing on depth over breadth. Some things to note are, we do not have to care about the size of the file that are in-between, and at the end. Consider this,

File 1 --> File 2 --> File 3
File 2 --> File 4

We are not required to check for the total size of File 2, 3, nor 4. The reason why that is the case is because the total size of File 1 will be larger than all three of them. Thus, it calls to reason that it is best to apply the depth-first-search on only the ancestor nodes, i.e., the nodes with no parents. This is where the helper function `dfs` comes to fruition. The `files_visited` is a dictionary where its keys are files, and the values are an array consisting of a flag that marks whether the file has been visited or not, and the index of that file in the Graph's list of adjacency list. The reason why we need the index of each file is because we are required to go through the neighbours of each file.
