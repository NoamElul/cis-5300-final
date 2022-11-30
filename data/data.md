## Twitter Hatespeech
* Source: https://github.com/t-davidson/hate-speech-and-offensive-language/tree/master/data
  * Dataset of tweets labeled by several labelers for hate speech, offensive language, or both. We preprocessed and only kept the text input, and a target indicating whether the text is problematic. Anything whose majority class was "hate speech" (0) was marked as "problematic" in our processed dataset.

* Format:
  * `text`: Input. String. The text of the tweet.
  * `problematic`: Target. Boolean, as 1 or 0. Whether the text is hate speech.

* Dataset size
  * Train: 12391 examples
  * Dev: 6196 examples
  * Test: 6196 examples

* Examples (`text`, `problematic`)
  * *"RT @Annnna_dav69: I hate trailer trash &#128567;"*, 1
  * *"The irony is so deep you can use a shovel."*, 0


## Abusive Reddit Comments
* Source: [Reddit Datasets](https://zenodo.org/record/4881008#.Y4S1XexBy3K )

* Format: tsv

* Dataset size
  * Train: 13585
  * Dev: 4527
  * Test: 5308

<img width="350" alt="Screen Shot 2022-11-30 at 10 31 45 AM" src="https://user-images.githubusercontent.com/104866320/204693384-43d52be0-a557-4be8-80da-5bab6e3068fe.png">

## Political Twitter Hatespeech
* Source: (#link)

* Format:

* Dataset size
  * Train: ## examples
  * Dev: ## examples
  * Test: ## examples

## Toxic Wikipedia Comments
* Source: (#link)

* Format:

* Dataset size
  * Train: ## examples
  * Dev: ## examples
  * Test: ## examples
