I tested my solution using the input rules in the PDF document and also by using the tests that were mentioned in the document.

I noticed that the central component to the problem was figuring out the best data structure to use when storing the input rules to make accept_packet as optimal as possible without sacrificing too much space. I did this by using a dictionary (hashmap) where the directions would map to the protocol and then map to the ports. I stored individual ports in the dictionary (as opposed to intervals of ports) to help search time as well, but this would sacrifice some space as many ranges would have the same IP addresses. However, I stored all IP addresses as intervals defined by the IP_Interval class, as the ranges of IP Addresses could be incredibly large.

If I had more time, I would implement a system to merge the IP intervals and assess the tradeoffs of creating an interval system with the ports as opposed to my current solution of making every port a key to its own dictionary. The merging of intervals would reduce search time and is an easy optimization, but I did not have enough time to implement it. I am not entirely sure how much of a help creating a port interval system would make to runtime complexity, but I would definitely consider it in length if I had more time.

I am interested in all of the teams that Illumio has, as I'm still discovering which discipline of software engineering I enjoy the most. However, if I had to rank them, I'd choose:

  1) Platform
  2) Data
  3) Policy
  
  
Thank you :)
