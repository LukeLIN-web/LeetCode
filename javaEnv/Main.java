
import java.util.*;

class Node {
    int ORDER = 3;
    int cnt_data = 0;
    int cnt_child = 0;
    int[] data = new int[ORDER + 1];
    Node[] child = new Node[ORDER + 2];
    Node parent = null;
    Node next;

    Node() {
    }

    public Node(Node pra, int[] data_src, int[] data_interval, Node[] child_src, int[] child_interval) {
        this.parent = pra;
        this.cnt_data = data_interval[1] - data_interval[0];
        this.data = Arrays.copyOf(data_src, data_interval[1] - data_interval[0]);
        this.cnt_child = child_interval[1] - child_interval[0];
        this.child = Arrays.copyOf(child_src, child_interval[1] - child_interval[0]);
        for (int i = 0; i < cnt_child; i++) {
            child[i].parent = this;
        }
    }

    void print() {
        System.out.print("[");
        for (int i = 0; i < cnt_data; i++) {
            if (i > 0)
                System.out.print(",");
            System.out.print(data[i]);
        }
        System.out.print("]");
    }
}

class BplusTree {
    public Node Root = new Node();
    private final int ORDER = 3;

    void insert(Node node, int n) {
        if (node == null)
            node = new Node();
        node.data[node.cnt_data++] = n;
        Arrays.sort(node.data,0,node.cnt_data);// sort node.data[0,node.cnt_data-1]
        split(node);
    }

    void split(Node node) {
        int cntData = node.cnt_data;
        int cntChild = node.cnt_child;
        boolean is_leaf = cntChild == 0;
        Node[] child = node.child;
        int[] data = node.data;

        if ((is_leaf && cntData <= ORDER) || (!is_leaf && cntData < ORDER))
            return;
        
        if (node.parent == null)
            Root = node.parent = new Node();
        Node pra = node.parent;
        int mid;
        Node l;
        Node r;
        if (is_leaf) {
            mid = (int) Math.ceil(1.0 * ORDER / 2);
            l = new Node(pra, data, new int[]{0, mid}, child, new int[]{0, 0});
            r = new Node(pra, data, new int[]{mid, cntData}, child, new int[]{0, 0});
        } else {
            mid = (int) Math.ceil(1.0 * (ORDER - 1) / 2);
            l = new Node(pra, data, new int[]{0, mid}, child, new int[]{0, mid + 1});
            r = new Node(pra, data, new int[]{mid + 1, cntData}, child, new int[]{mid + 1, cntChild});
        }
        // update 
        pra.data[pra.cnt_data++]  = data[mid];

        if (pra.cnt_child > 0 ){
            for (int i = 0; i < pra.cnt_child; i++) {
                if (pra.child[i] == node){
                    pra.child[i] = l ;
                    break;
                }
            }
        }else{
            pra.child[pra.cnt_child++] = l;
        }
        pra.child[pra.cnt_child++] = r;
        Arrays.sort(pra.data);
        Arrays.sort(pra.child,new Comparator<Node>()
        {
            @Override
            public int compare(Node o1, Node  o2) {
                return o2.data[0] - o1.data[0];
            }
        });

        split(pra);

    }

    Node find(Node root, int n) {
        if (root == null) {
            return null;
        }
        if (root.cnt_child == 0) {
            return root;
        }
        int i = Arrays.binarySearch(root.data, n);
        return find(root.child[i], n);
    }

    int exist(Node node, int n) {
        if (node == null)
            return -1;
        if (node.data == null) {
            return -1;
        }else{
            return Arrays.binarySearch(node.data, n);
        }
    }

    void print_tree() {
        Node BlankLine = null;
        Queue<Node> que = new LinkedList<Node>();
        que.offer(Root);
        que.offer(BlankLine);
        while (!que.isEmpty()) {
            Node t = que.element();
            que.poll();
            if (t == BlankLine) {
                System.out.println();
                if (!que.isEmpty())
                    que.offer(BlankLine);
                continue;
            }
            t.print();
            for (int i = 0; i < t.cnt_child; i++) {
                que.offer(t.child[i]);
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        BplusTree BT = new BplusTree();

        Scanner sc = new Scanner(System.in);
        // int N = sc.nextInt();
        int N =6 ;
        int[] a = {7, 8, 9 ,10, 7, 4};

        for (int i = 0; i < N; i++) {
            // int num = sc.nextInt();
            int num = a[i];
            Node leaf = BT.find(BT.Root, num);
            if (BT.exist(leaf, num) < 0) {
                BT.insert(leaf, num);
            } else {
                System.out.println("Key " + num + " is duplicated");
            }
        }
        BT.print_tree();
    }
}

