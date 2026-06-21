class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int c=0;
        int max=coins+1;;
        int res=0;
        int n=0;
        Arrays.sort(costs);
        for(int i=0;i<=costs.length-1;i++){
           if(costs[i]<coins && c<coins){
            c+=costs[i];
            if(  c!=0 && c<=coins){
            n++;
           }
           }
           
           
        }
        return n;
        
    }
}