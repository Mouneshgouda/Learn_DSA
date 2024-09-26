- Truth time: learning about theoretical things every week can get a bit monotonous. As much as it’s important to learn the method behind the madness, it’s equally crucial to understand why we’re embarking upon the path of madness to 
 begin with it. In other words — what’s the point of the theory that we’re learning here together?

- Sometimes, this can be a little tricky to illustrate. It’s hard to understand breadth first search if you don’t already know Big O notation. And Big O notation doesn’t mean anything to you unless you’ve seen it in action, in the 
 context of an algorithm.

- But every so often, we get lucky in that we stumble across the most perfect metaphor. Metaphors can be a great way of learning through analogy, and they’re useful in illustrating otherwise complicated concepts. I spent a few days 
 trying to understand a data structure I was only recently introduced to, and it was only in the context of this metaphor that I really began to grasp it.

- So, let’s see if we can unpack together.

- Books on books on books
- If you’ve moved across the country recently like I have, you probably have vivid memories of the horrors of trying to unpack everything. Or, maybe you’ve blocked it all out, in which case: well done! I was unpacking all of my books 
 last week, and found myself sticking them all on the shelves rather haphazardly, without any order or logic behind which book went where.

![image](https://github.com/user-attachments/assets/5ce5853c-4828-4b1c-8029-7ebbdada3483)

- We can think of our book collection as a dataset.

- I own a lot of books, sure, but I don’t have that many that it becomes difficult for me to find one. This got me thinking about libraries and their giant book collections, and how organized they actually have to be.

- Imagine, for a moment, if all the libraries in the world didn’t organize or sort their books? Or, imagine if they were sorted by something super complicated…like by ISBN number?

- We’re all better off because libraries are so methodically organized. But how did they come up with that? In fact, how does anyone come up with a good way of sorting through and finding an item within a large number of things?

- Hopefully, a lightbulb just lit up in your head, and you’re thinking the same thing that I am: this is a computer science problem!

- If we abstract this problem into programmatic terms, we can think of our book collection as our dataset. You can imagine that if we didn’t organize our books at all, there’s a good chance that we’d have to search through every single 
 book on the shelf before we find the book that we’re looking for. And if we organized our books by ISBN number, or by the year that they were published, we’d still have to look through a subset of them, since it would still be a little 
 difficult to find one item from amongst all the items on the shelf.

- We’re already familiar with so many different data structures at this point — perhaps we can use one of them to handle our dataset? Let’s try them out for size.
![image](https://github.com/user-attachments/assets/bd115fea-23e7-4df8-9b7a-51f64ff8ba33)

- Imagine a library as a data structure

- How about using an array or a linked list?

- Well, that would probably work fine in terms of holding all of our data. However, does this really solve our problem of searching through our dataset? Let’s think about it. In order to find a book using a linked list or an array, we’d 
 still have to search through every single node in the worst case that the data that we were looking for was in the last node. This basically means that the time it takes for us to search through all of our books is directly related to 
 how many books we have, which is linear time or O(n).

-And what if we sorted our linked list, instead of adding in data randomly? Well, this would be a bit more helpful, since we could implement binary search on our linked list. Remember that we can apply binary search to any collection of 
 sorted data, which is what we’d have in this case. We could split our large, sorted linked list or array into smaller sub-arrays, and narrow down for the book that we’re looking for. Even in the best case scenario, however, binary 
 search would only ever let us reach logarithmic time, or O(log n). This would be nicer than linear time, of course, but still…none of these really seem like the most efficient way to search for a book.

- It would be awesome if there was a way to just look up a book instantly — without having to search through everything. Surely, there must be a better way of doing this.

- Mappings to make our lives easier
 Okay, okay, we’re just learning about a cool data structure today — not inventing a new one! I guess I should finally let you in on the secret: there is a better way of searching through our dataset. And, as you might have guessed, it’s 
 called a hash table.

- Hash tables are made up of two distinct parts: an array, which you’re already familiar with, and a hash function, which is probably a new concept! So, why these two parts? Well, the array is what actually holds our data, and the hash 
 function is more or less the way that we decide where our data will live — and how we’ll get it out of the array, when the time comes!

![image](https://github.com/user-attachments/assets/66e1d5b0-0179-4b54-a6ba-7d6b5c78885a)

# What exactly is a hash table?

- In the example above, we’re restructuring our bookshelf to be a hash map! Our shelves start off empty, and in order to add books (our data) to them, we pass the book into a hash function, which tells us which shelf to put it on.

- Hash tables are interesting for a lot of reasons, but what makes them so efficient for our purposes is that they create a mapping, which is a relationship between two sets of data. Hash tables are made up of sets of pairs: a key and a 
 value, often referred to as (k, v). The idea here is that if you have the key in one set of data, you can find the value that corresponds to it in another set of data.

- In the case of a hash table, it is the hash function that creates the mapping. Since we’re working with arrays, the key is the index of the array, and the value is the data that lives at that index. The hash function’s job is to take 
 an item in as input, and calculate and return the key for where that item should live in the hash table.

- Alright: if we’re really going to sink our teeth into this topic, we’ll need an example. Let’s abstract out our bookshelf from earlier and simplify it further. In the example below, we’re looking at a hash table for book titles. The 
 hash tables has its two predictable parts: an array, and a hash function.

![image](https://github.com/user-attachments/assets/ce36d309-7788-4ddd-ad22-9593f60351b0)

- A hash table with a size of 12

- Our hash table has a size of 12, which ultimately means that every single book needs to be stored somewhere within these twelve slots, which are also referred to as hash buckets.

- Wait a second: how is that hash function deciding where to put those books!? If you take a closer look, you’ll notice that we’re using the modulo operator %, which you might have already seen before. The modulo operator returns the 
 remainder when one number is divided by another (or it returns 0, if the number can be divided evenly). So what is our hashing algorithm doing? Maybe you’ve already figured out the pattern here!

- Our hash function takes the number of characters in the title, adds them up, and divides that summed total by the size of the table. For example, "The Great Gatsby" has 14 characters in it (ignoring spaces), which, when divided by the 
 12, the size of the table, gives us a remainder of 2. So, our hash function will determine that "The Great Gatsby" should live in the hash bucket with an index of 2.

- We can write out what our hash function would actually look like in code:

- Alright, that’s simple enough! In fact, it’s almost…too simple. I feel like something’s going to go wrong now. Let’s keep going and see how far we can get with our hash function. We’ll try another book title: "The Old Man and the Sea":
![image](https://github.com/user-attachments/assets/7b12cfcc-5f23-40e6-8e06-4395f6a9cce9)

- A collision occurs when two elements are supposed to be inserted at the same place in an array.

- Oh no. I had a feeling this was going to happen!

- When we input "The Old Man and the Sea" into our hash function, it returns 6. This is bad because we already have a "The Sound and the Fury” at hash bucket 6! That is bad, right?

- Well, as it turns out, this isn’t bad at all. It’s actually quite normal. In fact, it’s so normal that this phenomenon even has a name: a collision, which occurs when two elements are supposed to be inserted at the exact same place in 
 an array — in other words, at the same hash bucket.

# What does this tell us about our hash function?

- For starters, we can be sure that no hash function will always return a unique hash bucket value for every item that give it. In fact, a hash function will always input multiple elements to the same output (hash bucket), because the 
 size of our dataset will usually be larger than the size of our hash table.

- But why is this the case?

- Super cool constant time
 If we think more about hash tables in a practical context, it becomes pretty clear that we will pretty much always have multiple elements per hash bucket.

- A good example of a hash table being applied to a real-world problem is a phonebook. A phonebook is massive, and contains all the data and contact information of every person that lives in a certain area.

- How is it organized? By last name, of course. Each letter of the alphabet will have many people with that last name, which means that we’ll have many pieces of data at each letter’s hash bucket.

- ![image](https://github.com/user-attachments/assets/5944526f-0e0c-44f8-aae0-fdf6ce2cdeb3)

- Hash functions that lean on alphabetization always result in 26 hash buckets.

- The hash function for a phonebook or a dictionary will always group any inputted data into one of 26 buckets — one bucket for each letter of the alphabet. This ends up being rather interesting, because what this effectively means is 
 that we’ll never have a hash bucket (or in this case, a letter of the alphabet) that is empty. In fact, we’ll have close to an even distribution of last names that start with each letter of the alphabet.

- In fact, that’s an important part of what makes a good hash algorithm: an equal distribution of data amongst all the possible hash buckets. But hold that thought for now — we’ll get more into that next week!

- For now, let’s look at the other cool part about hash tables: their efficiency! Whether we’re dealing with a phonebook, a dictionary, or a library, the approach remains the same: our hash function will be what tells us where to put 
 our data, and also where to get it out from!

![image](https://github.com/user-attachments/assets/6c25cc32-382d-4ee4-982c-38c5cf6cd7e1)

- Hash tables leverage constant time search, which is what makes them so powerful.

- Without using hash tables, we have to search through an entire dataset, probably starting with the first element in an array or linked list. If our items is at the very end of the list — well, good luck! We could be searching for a 
 long time. In fact, as much time as there are elements! Herein lies the major problem with using linked lists, stacks, queues, arrays: searching through them for something always ends up being linear in time, or O(n).

- Comparing this to hash tables, the choice between the two seems pretty easy, now that we understand how hash functions work! If we’re looking for an element, we need only to pass that element into the hash function, which will tell us 
 exactly what index in the array — that is to say, which hash bucket — to look in. This means that even if the item we’re looking for is at the very end of the hash table array, it’ll take us the exact same amount of time to find it as 
 it would for us to find the first element in the array!

- No need to iterate through a massive list, or look through all the shelves in the library: we can look up our data quickly and easily, in constant time, or O(1). It also only takes constant time to insert or delete an item into a hash 
 table, because we’re always going to lean on our hash function to determine where to add or remove something!

- Algorithms and data structures that have a constant search time are super powerful. And, what’s more, they’re all around us. In fact, you might not even notice them. To bring it all back to where we started: think about how libraries 
 organize things! Libraries around the world use the Dewey Decimal Classification System, which is really just a hash table with 10 buckets (and of course, a complex hash function that still I don’t quite understand yet).

- Next week, we’ll dive deeper into hash functions and their collisions and discover how to resolve these conflicts, which are so common that there are entire algorithms for handling them. Try to resist the urge to reorganize your 
 bookshelves until then!

- Over the course of the past few months, I’ve noticed one trait about each new concept that I learn in computer science: everything has its drawbacks.

- In fact, I’d guess that this is actually a trait of software in general and, to be honest, any creative and technical craft. Whether we’re writing just a little bit of code, or architecting a large, complex system, we always have many 
 tools to choose from. The trick, of course, is knowing which tool is the right one for the job. And in order to really get good at the decision-making process of choosing the right tool, we have know what its benefits and drawbacks are 
 in order to make a fair assessment.

- Hash tables, we recently discovered, are really great options for storing and retrieving specific data, quickly. They’re not always the best tool for the job — for example, they’re not great for finding ordered data — but sometimes, 
 they can make our lives a lot easier. We already know that a hash table is made up of two parts: an array that stores all of the data that we’re hashing, and the hash function that decides where all of that data will go. However, hash 
 tables do intrinsically have some issues of their own, and the usefulness of a hash table is tied directly to its hash function. Hash functions can be somewhat complicated, particularly if you don’t know the different types of 
 functions that are out there.

- So, let’s find out more about hash functions, how they work, and their strengths and weakness. Hopefully, this will help us understand when exactly they can help us out!

![image](https://github.com/user-attachments/assets/46b2549a-ac8f-4064-8829-33d2b0065929)

- What makes a good hash table?

- Ultimately, the usability of a hash table to solve a store-and-later-search-through-all-this-data problem hinges on how good of a hash function the hash table has.

- Let’s break that statement down even further. A good hash table must always:

- have a hash function that is easy to compute
 have a hash function that avoids collisions
 have a hash function that returns the same key, every single time, when given a value, and be able to use up all of the input data
 So, we can take these at face value…but I think that it’s better to ask why.

- Well, a hash table should have an easy-to-compute function because anything that’s too hard to compute will take up too much time an space! An expensive function defeats the purpose of finding an efficient data structure, so this 
 actually makes sense. A hash function should be able to handle all the data and store all of it when it’s inputted, because if it doesn’t…well, that would also defeat the purpose of the data structure being able to store mass 
 quantities of data very quickly! And if the hash function didn’t return the same key every time? Well, that would be very bad, because we’d never be able to retrieve the data after we stored it, because we could never be sure where 
 things are!

- Okay, so that just leaves collisions. You might remember from last week that a collision occurs when two elements are supposed to be inserted at the same place in an array.

- In the example below, the hash function is fairly simple: it takes the number of characters in the word, sums them, and then divides that character total by the size of the hash table (which is 10). Using the modulo operator, it uses 
 the remainder from that division to find the correct hash bucket for the item we’re trying to store. Notice that we run into a collision with the last two items, since we can’t store two of them in the same place!

![image](https://github.com/user-attachments/assets/85c84e5a-e9c2-41a6-a93c-dee7894b879e)

- Collisions occur whenever a hash function generates the same key for two elements

- Almost all hash functions will encounter a collision at some point or another. The only situation where this is not the case is for a perfect hash function, where every single input value maps to a unique hash bucket, and no two 
 values end up at the same key in the hash. But perfect hash functions are rare, because we usually don’t know how big our dataset will be before we write a hash function!

- The tl;dr here is that we have to understand how to handle collisions, because they are almost certainly going to happen. This is probably the most important thing to understand about hash functions, because they each need to account 
 for collisions.

- Collision resolution tactics
 There are a handful of ways to handle collisions in a hash function, and the important thing to remember that none of them is necessarily the “right tactic” to use. It all depends on your dataset, the size of your hash table, and what 
 operations you know you’ll want to perform on the table later on.

- Let’s take a look at two of the most common collisions resolution tactics used in hashing functions.

# Linear Probing
- One way of handling a collisions in a hash function is by just looking for the next empty hash bucket nearby! If this sounds simple…well, that’s because it is! Don’t worry, I’m going to complicate it a little more in a minute.

- The idea here is that if a collision occurs, and two elements are determined to live at the same spot in a hash table, a hash function can simply go to the next empty bucket over, and add the element there. This is a kind of 
 rehashing, and this technique is known as linear probing.

- The interesting thing about linear probing is that if the next hash bucket is also filled by an element, the hash function will just continue to probe through the hash table until it finds an empty bucket, cycling back if necessary.

- This means that if we’re at the end of the hash table and no buckets are empty, the function will just loop back around to the beginning of the table, effectively probing through the table until it finds an available bucket for the 
 element!
![image](https://github.com/user-attachments/assets/813ad023-c214-4de2-ab1e-87d71a02dc70)

- Linear probing

- However, there’s a downside that comes with linear probing. (I said I was going to complicate things, didn’t I?!). The issue with this specific technique is that the act of simply moving over to the next available hash bucket and 
 inserting an element at the “next free space” leads to something called clustering.

- We haven’t talked yet about what clustering is, so let’s figure that out first!

- The easiest way of thinking about clustering is by assessing where all of the data lives in the hash table.

- ![image](https://github.com/user-attachments/assets/27a1eb06-c2a0-4458-8680-b0163283f928)

# Chaining
- The second form of implementing collision resolution within a hash function involves changing the structure of the hash function itself! But don’t stress — we’re already familiar with the stuff we’re about to talk about, so we’ll be 
 total pro’s.

- Rather than having to deal with the downsides of linear probing and having to solve the problem of clustering, it would be great if we could just store multiple things in one hash bucket. And with the process of chaining, that’s 
 exactly what we can do!

- In order to implement chaining, the hash table has to be restructured so that multiple elements can be stored at one key. Hopefully, you’ve already got an idea in your head about what we could use here: a handy dandy linked list!

- Instead of storing a single item at each hash bucket, we can chain multiple elements together so that each key of the table has a pointer that references a linked list.

- This makes adding a single element easy — even if there is a collision (which won’t even be an issue anymore)! We just have to add it to the front of the linked list at the appropriate hash bucket.
![image](https://github.com/user-attachments/assets/65ed3589-ec24-41b8-9a1e-635032cdb110)

# Chaining

- Are you ready for a slight complication? It turns out that there’s a downside to chaining, too. And you might already see it coming: searching through a linked list takes a long time. In fact, it takes exactly as much time as there 
 are elements — or, in other words, it takes O(n) time.

- Again, whether or not chaining is a good approach to collision resolution all boils down to our hash function.If our hash function takes in words but puts all 50% of the words in one single hash bucket, we haven’t really solved our 
 problem, because now have a long linked list we’ll have to search through, and we don’t have our quick hash-access time anymore!

![image](https://github.com/user-attachments/assets/17cb6cc5-e2a5-4abf-b72f-1bba5ce2e950)



