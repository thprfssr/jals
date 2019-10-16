# jals

**SUMMARY**

This project is intended to be a collection of scripts written in Python, Perl,
and Bash, to help me organize and manage the lexicon for my constructed
language, Danetian. With this project, we should be able to:
* Add, edit, and remove entries in a lexicon database,
* Alphabetize a given lexicon database,
* Generate a dictionary in PDF format using LaTeX, and
* Apply orthographic or phonetic changes to the lexicon.

We should be able to access all of these features through a single command line
interface.



**JUSTIFICATION FOR THE CHOICE OF SCRIPTING LANGUAGES**

Python is a very powerful and beautiful scripting language, which has native
support for Unicode. Thus, it's best suited for writing all our Unicode stuff,
and even all of our sorting algorithms.

However, Python pales in comparison to Perl when it comes to regexes; Perl has
regexes built into the language. Thus, all the regex requirements are basically
*begging* to be written in Perl.

But having our code written in two different languages presents a problem: How
are we going to make these two pieces communicate? This is where Bash comes in.
With the help of heredocs, we're able to call different parts of our code,
whether they're written in Perl or in Python. Thus, Bash serves as a "glue"
language, to put it like that.

In conclusion, the Python-Perl-Bash trio is the perfect combination for this
project. We should write in each language what is best suited for that language.
*Render therefore unto Caesar the things which are Caesar's; and unto God the
things which are God's.*
