class Solution:
    def find_longest_increasing_subsequence(self, arr):
            count = 0
            prev = arr[0]-1
            greatest = 0
            print(arr)
            #type arr: list of int
            #return type: int
            # arr = arr.sort()
            for i in arr:
                if i > prev:
                    count = count+1
                prev = i
            # for i in range(len(arr)):
            #     if arr[i] > prev:
            #         count = count + 1
            #         if count > greatest:
            #             greatest = count
            #     else:
            #          count = 0
            #     prev = arr[i]
            # # #if greatest == 0:
            # #    # greatest = 1
            # print(greatest)
            return count
                 
            
            #TODO: Write code below to return an int with the solution to the prompt.
            pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.find_longest_increasing_subsequence(array)
    print(ans)

if __name__ == "__main__":
    main()
