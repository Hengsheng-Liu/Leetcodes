/*
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
 */

/*
Time:42mins 18s
Solve: Yes
Difficulty: Easy
Comments:
Had this question during for CodePath's OA, I come up O(n^2) solution but it went kaboom for hidden test cases, I come up with this solution
while on the train, is could solve in O(n) time but I need to use a lot of extra space I don't think is a good solution. 
*/

public int[] answerQueries(int[] nums, int[] queries) {
    Arrays.sort(nums);
    int[] size = new int[queries.length];
    Arrays.fill(size,0);
    int[] sorted_queries = Arrays.copyOf(queries, queries.length);
    Arrays.sort(sorted_queries);
    int[] answer = new int[queries.length];
    HashMap<Integer,Integer> hashmap = new HashMap<>();
    int sum = 0;
    int i = 0; 
    int j = 0;
    while(i < queries.length){
        while(j < nums.length && sum+nums[j] <= sorted_queries[i]){
            sum+= nums[j];
            size[i]+=1;
            j++;
        }
        i++;
        if(i < queries.length){
            size[i] = size[i-1];
        }
    }
    for(int k = 0; k < sorted_queries.length; k++){
        hashmap.put(sorted_queries[k], size[k]);
    }
    for(int l = 0; l < queries.length; l++){
        answer[l] = hashmap.get(queries[l]);
    }
    return answer;
}