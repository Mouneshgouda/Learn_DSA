

![image](https://github.com/user-attachments/assets/39ea1835-80da-4ae1-9e9d-a5c677556891)

## Trying to understand how mergesort works will seem overwhelming at first, but let's take it easy by walking through an example. In our example, we have nine numbers that we'd like to sort:

 ![image](https://github.com/user-attachments/assets/03fbbef6-1aff-4214-ba7e-ea97967fdc57)


 

## One quick aside. I should mention that mergesort is a divide and conquer algorithm...and it is quite shameless about that. All that it means is that mergesort performs its magic on numbers by dividing them into smaller and smaller sections first. Right now, we have nine numbers that we threw at mergesort. The first thing mergesort does is break that up into two halves:

 
<img src="https://github.com/user-attachments/assets/40940c0c-0f2e-49c8-bb7d-87ba4c58b4f9" alt="Description of the image" >



 

## Your original input is now divided into two sections. Next, we continue the dividing by breaking our two sections into four sections:

 
<img src="https://github.com/user-attachments/assets/ba861938-dda1-4344-90db-f2357854ee1c" alt="Description of the image"  height="">



 

## We are going to keep dividing these sections until you get to the point where you are left with just one number in each section and can't divide any further:

<img src="https://github.com/user-attachments/assets/36163c5f-cf27-4134-9470-0b4b791a20b6" alt="Description of the image"  height="">




## At this point, we have a bunch of individual values that look identical to what we started off with. That's not the goal of what we started out to do, but this is an important part of how mergesort functions. At this stage, we are done dividing. What we are going to see next is a whole lot of merging and sorting...aka the conquering part.

## Let's start with the first two sections:


 <img src="https://github.com/user-attachments/assets/b3e474e8-c748-4973-8073-b67ac1ba019a" alt="Description of the image"  height="">




 

## What we are going to do is merge these numbers together. As part of the merging, we'll also do a sort to ensure the the numbers in the combined section are arranged from smalles to largest. Because we are only dealing with two numbers, this is pretty easy for the 5 and 12:

 

 <img src="https://github.com/user-attachments/assets/368822e1-e77c-4542-91d9-73bdc2c43279" alt="Description of the image"  height="">



 

## We now repeat this for the next two sections made up of the numbers 4 and 1:


 <img src="https://github.com/user-attachments/assets/4fb25ee8-f613-4091-ab38-8f44af46106e" alt="Description of the image"  height="">



 

## Just like before, we combine the two sections into one section. The sorting part is more clear this time around because the original arrangement wasn't already sorted. We start with a 4 and 1, and the merged arrangement is 1 and 4. Pretty simple so far, right?

## Now, we will keep repeating this merge and sort operation on each pair of sections until we run out of sections:

 

 <img src="https://github.com/user-attachments/assets/417fb0ba-5c4b-4d0d-a1ae-e42fc0d94737" alt="Description of the image"  height="">


 

## If you have a number that is the odd one and can't be a part of a merge and sort...like our number 10 here, that's OK. Stop making fun of it. We will just carry it along for the next round of merging and sorting and hope its luck improves!

## Earlier, we were merging pairs of sections that were made up of one number. That was easy. This time around, we are going to continue merging pairs of sections, but each section will contain two numbers. Take a look:

 


 <img src="https://github.com/user-attachments/assets/2a682ccf-6387-483c-a480-80b3503fc3a9" alt="Description of the image"  height="">

 

## Instead of the merged section containing two numbers, it now contains four numbers...all in perfectly sorted bliss. We repeat this process for the remaining sections as well:


 <img src="https://github.com/user-attachments/assets/31529ee2-5b08-4099-8fe8-084b6fa9b7f1" alt="Description of the image"  height="">


## The number 10 is still not quite in the right position to be sorted and merged, so we'll drag it along for the next round:


 <img src="https://github.com/user-attachments/assets/b226a249-f699-477c-8408-1e9867036da2" alt="Description of the image"  height="">



 

## By now, you should start to see a pattern emerge. We are nearing the home stretch here, so let's continue merging and sorting with the next row:

 

 <img src="https://github.com/user-attachments/assets/c1d7e7bb-1ea6-48f9-b691-c175f3789069" alt="Description of the image"  height="">


## This almost looks fully sorted! We just have one one more round to go, and to those of you deeply worried about the number 10...it makes the cut this time around:



![image](https://github.com/user-attachments/assets/b65462cf-2a09-41c2-a205-8af94062eb51)


## Wohooo! You now have a sorted list of numbers. There are no more sections to merge and sort, so you are done. As a quick recap (and to reminisce about all the good times we had), take a look at the full list of steps we performed to sort our initial collection of numbers:


 <img src="https://github.com/user-attachments/assets/cf37a1ad-fb92-4a95-999f-18d43992bd3d" alt="Description of the image"  height="">



 

This giant list of steps is a visual representation of mergesort - with all of its dividing and conquering goodness!


