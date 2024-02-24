import java.util.ArrayList;
import java.util.LinkedList;

public class Graph {
    ArrayList<LinkedList<Node>> list_of_nodes;

    public Graph() {
        //
    }

    public void add_node(Node node) {
        LinkedList<Node> current_list = new LinkedList<>();
        current_list.add(node); // new node is head of this new linked list
        list_of_nodes.add(current_list);
    }

    public void add_edge() {

    }
}
