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
- Extraction of the most frequent words in the summary database using NLTK and LDA
- Extraction of the adjectives associated with the characters in the summaries using BERT and Spacy
- Extraction of the characters description and characteristics in the summaries using LLM (GPT-4)
- Implementing student T-tests to assess different occurrences of words, adjectives or characteristics associated with characters depending on the time era
- Maybe try some ML (simple regression or neural network) to see if given some historical context, it is possible to predict the words, adjectives or characteristics that appears the most in the movies summaries


## Proposed timeline :

