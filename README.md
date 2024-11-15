# The metamorphosis of Movie Archetypes: A timeless tale of film personas

## Abstract
A given historical context has a high influence on the topics approached in its contemporary movies. Typically, the Japanese animes were a catharsis of the traumas caused by the Second World War to the Japanese population. In this research, we aim to investigate whether this influence extends to the characters portrayed in the movies. Has each era a stereotypical character derived from time corresponding historical events (i.e. : are more soldiers characters presented after war events or more astronauts during the space exploration period) ? 
This project will begin by exploring various methods of character related information extraction from movie summaries. Then, we will use this information in order to get meaningful insights on the impact of historical event in character portrayal in films. Finally, we aim to create a time journey in which we will meet some time stereotypes and, maybe, given our own historical context, be able to predict what is the incoming character movie star that will be seen played for perhaps the future ten years or more.

## Research Questions : 
Does important historical events induce the creation of corresponding stereotypical characters in their contemporary movies ? For example, did the World War II induce a higher occurrence of soldiers characters in the ten years following it ? 

Does a time-lapse exist between the event and its character representation in the movie database ? From previous examples, when is the peak of soldiers representation in the movies, during the war, five years after or more ?

What types of events were the most influential of the stereotypical character representation over the twentieth century (ex : wars, social revolutions,
natural catastrophes) ? 

Are eras having a similar historical context presenting the same stereotypical characters ?

Can we predict the stereotypical characters of an era given its historical context ? Is it possible to train a model to perform such a task ?

## Additional dataset : 
In order to match historical moments with the results obtained in the other sections, we need a rather comprehensive timeline of the most relevant events of the years included in the film dataset. 
To do this, we implemented several methods to objectively obtain significant events, such as extracting content from wikipedia pages or downloading more precise datasets using Wikidata queries. 
In doing so, we realised that using datasets that are too long does not allow us, with the time and means at our disposal, to be able to analyse these events in depth. For example, dividing wars by nation is very difficult, as it involves a part of manual data addition, which can never be objective (e.g. are economic supporters of the war included or not, how are political parties belonging to several nations treated?, ...). For this reason, for project milestone 3 we have chosen to focus on fewer events, but which can be clearly and objectively treated, e.g. world wars, the cold war, the economic crisis of ‘29 and events of this magnitude.

## Methods : 

### Character related information extraction : 

We tested two main techniques to extracte characters description from the text (see in results.ipynb for more details) : 
1. NLTK combined with LDA
2. BERT (Named Entity Recognition) combined with Spacy

We also intend to try a more performant LLM than BERT like GPT-4 to perform the extraction.

### Information analysis : 

We intend to perform our analysis in this way : 
For the most part of our analysis we decided to split our dataset by decade with each decade having its own historical context given by the timeline. In each century we will split the timeline in different cathegories (ex : wars, social revolutions, natural catastrophes) to be able to test the influence of the type of event. We will also select some partiuclar events in order to study their influence on the stereotypical characters appearing in the movies that follow them.   
1. Using the previously cited tools we will obtain the most recurrent names and adjectives qualifying the characters for each decade or period of interest (see examples in results.ipynb).
2. This will allow us to perform bar and cloud plots illustrating the most common characters name and adjectives that they are described with for each decade or period of interest (see examples in results.ipynb). We will also complete this analysis by plotting the distribution of some specific terms (or set of terms) highly associated with some historical events (ex : war could be associated with soldiers, captain etc.). 
3. We intend execute some hypothesis testing and calculate correlations to compare the occurrence of adjectives or names between the different decades (and some specific historical contexts). This will also be helpful to compare the influence of different types of historical events. 
4. We will also push our analysis further by performing some clustering of the decades or movies within a decade or a historical context by the words related to the characters in them.

### Eventual predictive model : 

If we have some time left, we might try to fit a machine learning model (regression or neural network) on encoded subsections of the timeline and corresponding character describing adjectives.  

### Website concept : 

Our vision for the website is to create an interactive, historical timeline featuring Ada, a timeless traveler. Starting in 1910, Ada journeys through each decade, encountering significant historical events and iconic film characters that embody the spirit of their eras. When we uncover connections between historical events and film characters, these characters reveal how each decade's society is reflected in cinema. Ada could either adapt her appearance to align with each era’s customs, mirroring these characters, or remain ‘neutral’ to highlight the transformations she experiences across time. At each stop, the characters she meets explain the events of their time and how they personify those changes. If possible, we aim to add a machine learning model to predict how film characters may evolve over the next 10–15 years, drawing on current events.

From a technical perspective, Ada’s journey begins with an introduction at the start of the timeline, followed by her journey through each decade as the user scrolls. Each stop on the timeline features 1–2 film characters representing typical figures of the era, who engage in dialogue with Ada against a backdrop of period-specific photos and plots illustrating our analysis. The “dialogues” could be structured vertically, with characters accompanying Ada as she travels downward, or horizontally, with images and narratives displayed sequentially across the screen.


## Proposed timeline :

22.10.24 : Team zoom call to discuss first results after dataset discovery

28.10.24 : Explore how the timeline can be extracted from Wikipedia ; Further analyze the dataset

08.11.24 : Analyze movie genre distribution analysis ; Implement LDA and LLM methods in order to analyze plot.summaries dataset ; Extract timeline

15.11.24 : README; Prepare results notebook ; push the LDA + LLM analysis further

06.12.24 : Collecting necessary data for each decade ; Try GPT-4 for information extraction; Begin the inter decade statistical analysis ; Create website

13.12.24 : Clustering analysis ; Maybe some ML ; Pursue website

20.12.24 : Project wrap up

## Organization within the team : 

Léa : LDA + statistical analysis + clustering analysis

Camille : BERT + statistical analysis + ML 

Samara : Timeline extraction + data story + website 

Sara : Dataset exploration + data visualization + website

Annabelle : LDA + GPT-4 + ML

## Questions : 
- What kind of techniques can we implement to accelerate some very long-running parts in our code ?
- How can we quantify the bias of our models (especially the pretrained LLMs) ? 
