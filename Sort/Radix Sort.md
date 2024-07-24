# How Radix Sort Works


### To understand how radix sort works, we'll start with an unsorted collection of numbers and walk through how we can sort them. Note that the collection has to be numbers (no strings, objects, emojis, etc.) that are in integer form. With that constraint in mind, our starting numbers are as follows:

![image](https://github.com/user-attachments/assets/3d2380e8-b5e3-495c-9f16-934aed2d5932)


### The first thing we are doing to do is find the largest number that we need to sort. For our example, that would be 2310:

![image](https://github.com/user-attachments/assets/128d477a-4359-485d-a169-18f796e85e04)


### What we are doing with this value is trying to find out how many digits it has. For 2310, the number of digits would be four:

![image](https://github.com/user-attachments/assets/481f5239-8221-43bd-a777-9b5c21f7a089)



### This is an important detail, for the way radix sort works heavily revolves around the number of digits present in the largest number. If we had to describe radix sort's behavior, it would be:

- 1.Find the maximum number of digits in the largest number that needs to be sorted.
- 2.Start with the least significant digit (the rightmost digit) and sort the numbers based on that digit.
- 3.Move to the next digit place (tens, hundreds, etc.) and sort the array based on that digit while maintaining the order from the previous step.
- 4.Repeat the process until you have sorted based on the most significant digit (the leftmost digit). This digit would correspond to the highest digit found in step 1.
- 5.If these three steps aren't totally clear, don't worry. We are going to walk through them and look at how this all ties together. Our starting point is right after we determined that our largest number (2310) has four digits.


## Sorting by the Ones (Units) Digit
#### We start our sort with the least significant (aka rightmost) digit, and that is going to be our ones or units digit. Let's go ahead and mark those numbers:

![image](https://github.com/user-attachments/assets/7cf47b8b-d41e-45f5-95cb-afdf227b8fbf)


#### What we do next is sort all of our items based on the value from the ones digit. This would cause the items in our array to be rearranged as follows:

![image](https://github.com/user-attachments/assets/f47e1fab-fd24-4a3d-8d12-290839a5fdf5)


#### The detail to keep in mind is that all of our items in our array aren't sorted in their final positions. They are only sorted with respect to the ones digit, and that is the sorting order we see currently.

## Sorting by the Tens Digit
#### With our values sorted by their ones (units) digit, we keep moving left to sort the values. We are now about to sort by the tens digit:

![image](https://github.com/user-attachments/assets/4a6f5838-01fc-4e44-89dc-1084f48eca6e)


#### Just like earlier, we shift all of our items around until they are sorted using their tens digit value as the primary value:

![image](https://github.com/user-attachments/assets/d1214c73-2a8d-45bf-894c-f9386dda32a9)


#### The end result is another round of sorting. Can you guess what we are going to be doing next?

## Sorting by the Hundreds Digit
#### Yes, we will keep going left until we run out of digits to sort. Earlier, we calculated the maximum number of digits by looking at our largest value (2310), and we know that it has four digits all the way up to the thousands position. We are not there yet, for we are now going to sort by the hundreds (aka third least significant digit) next:

![image](https://github.com/user-attachments/assets/402c7aed-c8dd-49fd-90eb-f6741f9a1dee)



#### Notice that some of the numbers we wish to sort do not have a value for the hundreds position. That is OK. We'll just treat those empty values as having a 0 present there instead. It's time to get sortin':

![image](https://github.com/user-attachments/assets/e1bb692d-aaf6-4349-9c8b-5f5bbd6eec15)


#### One thing to observe is that all of the values that don't have a hundreds place jump to the beginning while still maintaining their relative order. This is done to ensure stability. After all of this, we just wrapped up sorting all of our values by their hundreds position. All that is left is to...


## Sorting by the Thousands Digit
#### Our last step is to sort by the thousands digit, which is the final digit as determined by our max value calculation earlier:

![image](https://github.com/user-attachments/assets/504d6ad5-2077-4bd7-8d6f-8292f7285a8a)


#### We only have one number with a thousands digit, and that is the 2 in 2310. All of the rest of the numbers have a thousands digit value of 0, for they don't actually have a thousands value. Let's go ahead and perform one last sorting operation:

![image](https://github.com/user-attachments/assets/ebfdbdac-becd-4bca-9c25-2e2f1394c244)


#### And with this step, we are done. Notice the final ordering of our numbers. They are all properly sorted from smallest to largest. There is an important detail with the sorting here that we glossed over. We'll revisit that next.

## It's Counting Sort Time...Again!
#### In our quest to explain how radix sort works and how it sorts each digit from the least significant digit to the most significant digit, we skipped over the important question of How does the actual sorting of each digit work?

#### It works by using, now...wait for it, counting sort:

![image](https://github.com/user-attachments/assets/4f91a180-3151-4f38-b42e-34e04d17fde9)


## What Influences Radix Sort Performance?
#### Radix sort's performance is influenced by three things. First, it is influenced by the size of our input which we'll identify as n:

![image](https://github.com/user-attachments/assets/e19a200d-5ceb-40af-9ff6-7300458dee5a)


#### Second, it is influenced by the number of digits in our largest number, and this is identified by d:

![image](https://github.com/user-attachments/assets/5d8384bc-a413-4023-9313-57ed2a3aa06e)


#### Third and lastly, it is influenced by the range of digits that are possible. For decimal (base-10) numbers, the range of numbers goes from 0 to 9 for a total of 10 possible digits:

![image](https://github.com/user-attachments/assets/29ee521c-8acc-4bc1-9429-96036017e665)


## We can represent this range of digits as k.

## It's Big-O Notation Time
- 1.If we take n, d, and k together, the running time for radix sort can be represented as O(d ⋅ (n + k)). When we look at how radix sort operates, we can see why this is the running time representation:

- 2.The number of items we have to sort (n) sets the bar for how long our other operations will take
- 3.The sorting subroutine is counting sort (which runs in linear time as well), with its range being the digits (k) that exist in our base-10 world
 We call counting sort on all (n) items once for each digit in the largest value (d) we are trying to sort
- Putting it all together, radix sort runs in linear time provided the values for n, d, and k are in the same very large ballpark. The following table provides the best, worst, and average case results:
