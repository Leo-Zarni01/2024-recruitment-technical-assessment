package src;

import java.util.ArrayList;
import java.util.List;

public class Task {
    public record File(int id, String name, List<String> categories, int parent, int size) {
        this.id = id;
        this.name = name;
        this.categories = categories;
        this.parent = parent;
        this.size = size;
    }

    /**
     * Task 1
     */
    public static List<String> leafFiles(List<File> files) {
        return new ArrayList<>();
    }

    /**
     * Task 2
     */
    public static List<String> kLargestCategories(List<File> files, int k) {
        return new ArrayList<>();
    }

    /**
     * Task 3
     */
    public static int largestFileSize(List<File> files) {
        return 0;
    }

    public static void main(String[] args) {
        List<File> testFiles = List.of(
                new File(1, "Document.txt", List.of("Documents"), 3, 1024),
                new File(2, "Image.jpg", List.of("Media", "Photos"), 34, 2048),
                new File(3, "Folder", List.of("Folder"), -1, 0),
                new File(5, "Spreadsheet.xlsx", List.of("Documents", "Excel"), 3, 4096),
                new File(8, "Backup.zip", List.of("Backup"), 233, 8192),
                new File(13, "Presentation.pptx", List.of("Documents", "Presentation"), 3, 3072),
                new File(21, "Video.mp4", List.of("Media", "Videos"), 34, 6144),
                new File(34, "Folder2", List.of("Folder"), 3, 0),
                new File(55, "Code.py", List.of("Programming"), -1, 1536),
                new File(89, "Audio.mp3", List.of("Media", "Audio"), 34, 2560),
                new File(144, "Spreadsheet2.xlsx", List.of("Documents", "Excel"), 3, 2048),
                new File(233, "Folder3", List.of("Folder"), -1, 4096));

        List<String> leafFiles = leafFiles(testFiles);
        leafFiles.sort(null);
        assert leafFiles.equals(List.of(
                "Audio.mp3",
                "Backup.zip",
                "Code.py",
                "Document.txt",
                "Image.jpg",
                "Presentation.pptx",
                "Spreadsheet.xlsx",
                "Spreadsheet2.xlsx",
                "Video.mp4"));

        assert kLargestCategories(testFiles, 3).equals(List.of(
                "Documents", "Folder", "Media"));

        assert largestFileSize(testFiles) == 20992;
    }
}