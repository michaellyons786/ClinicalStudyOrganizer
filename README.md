# Clinical Study Organizer
[![Build Status](https://travis-ci.com/michaellyons786/ClinicalStudyOrganizer.svg?branch=master)](https://travis-ci.com/michaellyons786/ClinicalStudyOrganizer)

## Goal
To abstract away the more difficult aspects of designing studies (especially randomization) away from researchers to improve science. Instead of hard to comprehend strings of random numbers and letters, my program combines two random words from a noun list to create memorable (and sometimes amusing) aliases that can be used to identify patients anyomyously.

For instance:

![identity](https://github.com/michaellyons786/ClinicalStudyOrganizer/blob/master/research/identity_table.png?raw=true)
![alias](https://github.com/michaellyons786/ClinicalStudyOrganizer/blob/master/research/alias_table.png?raw=true)

As you can see, the alias is the foreign key that could be used to join the two tables. Identifying information, such as the unique id assigned to each new patient and last and first names are hidden behind this alias, and information that might be useful to a researcher such as age, height, and eye color can safely be accessed without the danger of introducing bias and keeping the study potentially double-blind. 

*Note: All example patients were randomly generated and are not meant to resemble any real person*
