import java.util.*;

class Solution {
    // Segment Tree to maintain the maximum gap in the range [0, M]
    int[] tree;
    int M = 50005;

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = Math.max(tree[2 * node], tree[2 * node + 1]);
    }

    private int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return 0;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = start + (end - start) / 2;
        int p1 = query(2 * node, start, mid, l, r);
        int p2 = query(2 * node + 1, mid + 1, end, l, r);
        return Math.max(p1, p2);
    }

    public List<Boolean> getResults(int[][] queries) {
        tree = new int[4 * M];
        TreeSet<Integer> obstacles = new TreeSet<>();
        
        // Initialize with boundaries
        obstacles.add(0);
        obstacles.add(M);
        update(1, 0, M, M, M); 

        List<Boolean> ans = new ArrayList<>();

        for (int[] q : queries) {
            int type = q[0];
            if (type == 1) {
                int x = q[1];
                
                // Find adjacent obstacles
                Integer L = obstacles.floor(x);
                Integer R = obstacles.ceiling(x);
                
                // Update the gaps in the Segment Tree
                update(1, 0, M, x, x - L);
                update(1, 0, M, R, R - x);
                
                // Add the obstacle to our tracker
                obstacles.add(x);
            } else {
                int x = q[1];
                int sz = q[2];
                
                // Find the obstacle immediately to the left of x
                int L = obstacles.floor(x);
                
                // Check the trailing space between L and x
                int trailingGap = x - L;
                
                // Check the largest available gap completely within [0, L]
                int maxLeftGap = query(1, 0, M, 0, L);
                
                if (trailingGap >= sz || maxLeftGap >= sz) {
                    ans.add(true);
                } else {
                    ans.add(false);
                }
            }
        }

        return ans;
    }
}