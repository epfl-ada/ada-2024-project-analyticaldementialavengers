# The metamorphosis of Movie Archetypes: A timeless tale of film personas

## Abstract
A given historical context has a high influence on the topics approached in its contemporary movies. Typically, the Japanese animes were a catharsis of the traumas caused by the Second World War to the Japanese population. In this research, we want to test if it is true for the characters portrayed in the movies as well. Has each era a stereotypical character derived from time corresponding historical events (i.e. : are more soldiers characters presented after war events or more astronauts during the space exploration period) ? 
This project will begin by exploring various ways of extracting character related information from movie summaries. Then, we will use this information in order to get meaningful insights on the impact of historical event in character portrayal in films. Finally, we aim to create a time journey in which we will meet some time stereotypes and, maybe, given our own historical context, be able to predict what is the incoming character movie star that will be seen played for perhaps the future ten years or more.

## Research Questions : 
Does important historical events induce the creation of corresponding stereotypical characters in their contemporary movies ? For example, did the World War II induce a higher occurrence of soldiers characters in the ten years following it ? 

Does a time-lapse exist between the event and its representation in the movie database ? From previous examples, when is the peak of soldiers representation in the movies, during the war, five years after or more ?

Can we predict the stereotypical characters of an era given its historical context ? Is it possible to train a model to perform such a task ?

What types of events were the most influential of the stereotypical character representation over the twentieth century (ex : wars, social revolutions,
natural catastrophes) ? 

Are eras having a similar historical context presenting the same stereotypical characters ?

## Additional dataset : 
In order to match historical moments with the results obtained in the other sections, we need a rather comprehensive timeline of the most relevant events of the years included in the film dataset. 
To do this, we implemented several methods to objectively obtain significant events, such as extracting content from wikipedia pages or downloading more precise datasets using Wikidata queries. 
In doing so, we realised that using datasets that are too long does not allow us, with the time and means at our disposal, to be able to analyse these events in depth. For example, dividing wars by nation is very difficult, as it involves a part of manual data addition, which can never be objective (e.g. are economic supporters of the war included or not, how are political parties belonging to several nations treated?, ...). For this reason, for project milestone 3 we have chosen to focus on fewer events, but which can be clearly and objectively treated, e.g. world wars, the cold war, the economic crisis of ‘29 and events of this magnitude.

## Methods : 

### Character related information extraction : 

We tested two main techniques to extracte characters description from the text (see in results.ipynb for more details) : 
1. NLTK combined with LDA
2. BERT combined with Spacy

We also intend to try a more performant LLM than BERT like GPT-4 to perform the extraction.

### Information analysis : 

We intend to perform our analysis in this way : 
We decided to split our dataset by decade. 
1. Using the previously cited tool we will obtain the most recurrent names and adjectives qualifying the characters for each decade (see examples in results.ipynb).
2. This will allow us to performed bar and cloud plots illustrating the most common characters name and adjectives that they are described with for each decade (see examples in results.ipynb).
3. We intend execute some hypothesis testing to compare the occurrence of adjectives or names between the different decades (and maybe some specific historical contexts).
4. We will also push our analysis further by performing some clustering of the decades or movies within a decade or a historical context by the words related to the characters in them. 


## Proposed timeline :

