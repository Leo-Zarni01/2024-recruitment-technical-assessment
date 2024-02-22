from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    res = []
    for i in files:
        current_id = i.id
        print("Current file id is: ", current_id)
        found = False
        for j in files:
            if j.id == current_id:
                print("Same file being analyzed")
                continue

            if j.parent == current_id:
                print("Not a leaf node")
                found = True ## so not a leaf -> stop iterating
                break

        if found:
            print("Current file has children")
            continue
        else:
            print("Current file is a leaf node")
            res.append(i.name)
        print()

    print(sorted(res))
    return res


"""
Task 2
"""
# def kLargestCategories(files: list[File], k: int) -> list[str]:
#     return []


"""
Task 3
"""
# def largestFileSize(files: list[File]) -> int:
#     return 0


if __name__ == '__main__':
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

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    # assert kLargestCategories(testFiles, 3) == [
    #     "Documents", "Folder", "Media"
    # ]

    # assert largestFileSize(testFiles) == 20992
