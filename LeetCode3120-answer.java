class Solution {
    public int numberOfSpecialChars(String word) {
        int[] arr = new int[256];
        int ans = 0;

        for(char ch : word.toCharArray()){
            arr[ch]++;
        }

        for(int i = 65; i <= 90; i++){
            if(arr[i] != 0 && arr[i + 32] != 0){
                ans++;
            }
        }

        return ans;
    }
}