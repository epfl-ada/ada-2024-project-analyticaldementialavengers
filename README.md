# The metamorphosis of Movie Archetypes: A timeless tale of film personas

## Abstract
<p style="text-align: justify;">
This research investigates how historical events influence the creation and evolution of character archetypes in films. While it's well-known that films reflect societal changes through themes, we explore whether this also extends to the characters portrayed. Our hypothesis posits that major historical events, such as wars and revolutions, give rise to stereotypical character archetypes, like soldiers or activists. We aim to develop methods for extracting character data from film datasets and analyze how these archetypes change over time. This study will deepen our understanding of how cinema mirrors societal transformations.
</p>

## Research Questions : 
<p style="text-align: justify;">
1.How do major historical events influence the creation of stereotypical characters in films with an evenutal temporal gap between both? Specifically, how do major historical events (e.g., wars, social revolutions, economic crises) lead to the emergence of recurring character traits or archetypes? For instance, do global conflicts like World War II result in an increase in soldier archetypes? Stereotypical characters will be defined based on recurring descriptors (e.g., soldier, activist, hero) present in plot summaries.
</p>

<p style="text-align: justify;">
2. Which types of historical events have the most significant influence on the emergence of stereotypical character archetypes? Do wars, social revolutions, economic crises, or natural disasters produce the most pronounced shifts in character representation? What types of characters (e.g., soldiers, rebels, entrepreneurs) are most strongly associated with different types of events? We will categorize events into types (e.g., wars, revolutions, economic downturns) and measure the association between each type and the emergence of specific character traits.
</p>

<p style="text-align: justify;">
3. How do historical contexts with similar characteristics result in the emergence of comparable character archetypes across different eras? Do similar social or political climates (e.g., periods of war or economic hardship) lead to the creation of similar character types across different decades? For example, do both the World Wars and the Cold War produce characters like soldiers, spies, or heroes? We will use clustering or semantic similarity techniques to identify common character traits across different eras and compare how similar historical contexts influence character creation. 
</p>

## Additional datasets
<p style="text-align: justify;">
To link historical events with their cinematic representations, we used wikipedia pages in .txt format of decades from 1900s to 2000s. 

  
To see if correlations between the historical wikipedia pages and the movies summaries from plot_summaries were biased by their different structures we also tried some correlations with the wikipedia summaries of some movies in .txt format (see in src/data/movie_selection.ipynd to have a list of the movies).
</p>

## Methods : 

### Character related information extraction : 

We tested different techniques to extracte characters description from the text: 
1. NLTK combined with LDA
2. BERT (Named Entity Recognition) combined with Spacy
3. SBERT (Sentence-BERT) 
4. LLAMA (extraction of stereotypical characters of each decade from the clustered movies summaries)

### Information analysis

Our analysis proceeds by splitting the dataset into decades to match the historical context of each period. We focus on identifying recurring names and adjectives associated with characters, which will allow us to:
1. Plot character trends: Visualizing the most common words for each decade using bar plots and word clouds.
2. Conduct statistical tests: Comparing the frequency of character names and traits across different decades to identify correlations (Pearson) between historical events and character types.
4. Clustering analysis: Grouping films by decade or historical context based on terms in their summaries to explore patterns and similarities between eras with similar events.
5. S-BERT (sentence-BERT) : creation of embeddings from the sentences of movie summaries and wikipedia timeline based on lexical fields.
6. PCA and clustering : 2D representation of clusters of movies embeddings clustered with k-means.

### Installation requirements

The use of Llama requires installation of Ollama (more information about download on https://ollama.com).

## Contribution of all group members
- **Léa**: LDA application to each decade and clustering
- **Camille**: LLM application (LLAMA and BERT)
- **Annabelle**: LDA correlation and wikipedia summaries dataset extraction
- **Samara**: History dataset extraction and LLM application (SBERT)
- **Sara**: Statsitical analysis during data analysis, writing up the data story and website

**Link to the data story (website)**: https://s-vannay.github.io/
