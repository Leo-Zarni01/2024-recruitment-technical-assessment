from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int

class Node:
    def __init__(self, val: File):
        self.vertex = val

class Graph:
    def __init__(self):
        self.list_of_adj_lists = []

    def add_node(self, node: Node):
        current_list = []
        current_list.append(node)
        self.list_of_adj_lists.append(current_list)

    def add_edge(self, source: int, target: int):
        # print("Source is: ", source, " and target is: ", target)
        current_list = self.list_of_adj_lists[source] 
        target_node = self.list_of_adj_lists[target][0]
        current_list.append(target_node)

    def check_edge(self, source: int, target: int) -> bool:
        current_list = self.list_of_adj_lists[source]
        target_node = self.list_of_adj_lists[target][0]
        for node in current_list:
            if node == target_node:
                return True
        return False
    
    def print_graph(self):
        for adj_list in self.list_of_adj_lists:
            print("Current node is: ", adj_list[0].vertex.id)
            print(f"It has {len(adj_list) - 1} neighbors")
            for each_node in adj_list:
                if each_node.vertex.id != adj_list[0].vertex.id:
                    print("Neighbors are: ", each_node.vertex.id)
            print()

def convert_files_to_graph(files: list[File]) -> Graph:
    file_graph = Graph()

    ## add nodes first
    for i in range(len(files)):
        file_node = Node(files[i])
        file_graph.add_node(file_node)

    ## then check for edges
    for i in range(len(files)):
        for j in range(len(files)):
            if files[i].parent == files[j].id:
                if not file_graph.check_edge(j, i):
                    file_graph.add_edge(j, i)
            elif files[j].parent == files[i].id:
                if not file_graph.check_edge(i, j):
                    file_graph.add_edge(i, j)
    return file_graph

def find_categories(files: list[File]) -> dict:
    categories = {}
    for each_file in files:
        for each_category in each_file.categories:
            if each_category not in categories:
                categories[each_category] = 1
            else:
                categories[each_category] += 1
    return categories

def sort_categories(categories_dict: dict) -> dict:
    return sorted(categories_dict.items(), key=lambda x: (-x[1], x[0]))


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    res = []
    file_graph = convert_files_to_graph(files)
    for each_list in file_graph.list_of_adj_lists:
        if len(each_list) == 1:
            res.append(each_list[0].vertex.name)
    return res
    
"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    if k > len(files):
        return [[i] for i in files]
    categories = find_categories(files)
    sorted_categories = sort_categories(categories)
    res = []
    for i in range(len(sorted_categories)):
        if i <= k - 1: ## cuz index is 0!!!
            res.append(sorted_categories[i])
    return res

"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    sizes = []
    visited = {}
    file_graph = convert_files_to_graph(files)
    for each_list in file_graph.list_of_adj_lists:
        visited[each_list[0].vertex.id] = False

    for each_list_2 in file_graph.list_of_adj_lists:
        current_head = each_list_2[0].vertex.id
        if not visited[current_head]:
            print(f"current head {current_head} has not yet been visited!")
            sum = 0
            for i in range(len(each_list_2)):
                neighbour_file = each_list_2[i].vertex.id
                visited[neighbour_file] = True
                sum += each_list_2[i].vertex.size
            print(f"The sum of all the files starting from {each_list_2[0].vertex.id} is {sum}")
            sizes.append(sum)            
        else:
            print(f"The current file {current_head} has been visited.")
        print()
    return 0


testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
        ]

largestFileSize(testFiles)
# testFiles2 = [
#     File(3, "Folder", ["Folder"], -1, 0),
#     File(1, "Document.txt", ["Documents"], 3, 1024),
# ]

# graph_2 = convert_files_to_graph(testFiles2)
# graph_2.print_graph()

# if __name__ == '__main__':
#     testFiles = [
#         File(1, "Document.txt", ["Documents"], 3, 1024),
#         File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
#         File(3, "Folder", ["Folder"], -1, 0),
#         File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
#         File(8, "Backup.zip", ["Backup"], 233, 8192),
#         File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
#         File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
#         File(34, "Folder2", ["Folder"], 3, 0),
#         File(55, "Code.py", ["Programming"], -1, 1536),
#         File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
#         File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
#         File(233, "Folder3", ["Folder"], -1, 4096),
#     ]

#     assert sorted(leafFiles(testFiles)) == [
#         "Audio.mp3",
#         "Backup.zip",
#         "Code.py",
#         "Document.txt",
#         "Image.jpg",
#         "Presentation.pptx",
#         "Spreadsheet.xlsx",
#         "Spreadsheet2.xlsx",
#         "Video.mp4"
#     ]

#     # assert kLargestCategories(testFiles, 3) == [
#     #     "Documents", "Folder", "Media"
#     # ]

#     # assert largestFileSize(testFiles) == 20992
