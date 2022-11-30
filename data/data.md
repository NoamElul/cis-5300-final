## Twitter Hatespeech
* Source: https://github.com/t-davidson/hate-speech-and-offensive-language/tree/master/data
  * Anything whose majority class was "hate speech" (0) was marked as "problematic"

* Format:
  * `text`: Input. String. The text of the tweet/comment/post
  * `problematic`: Target. Boolean, as 1 or 0. Whether the text is problematic (that is, whether it is hate speech)

* Dataset size
  * Train: 12391 examples
  * Dev: 6196 examples
  * Test: 6196 examples

## Abusive Reddit Comments

`Entries from Reddit post titles, bodies, and comments are annotated and are assigned with at least 1 category by two human annotators.`

* Source: [Reddit Datasets](https://zenodo.org/record/4881008#.Y4S1XexBy3K )

* Format 


| id      | text |labels |
| ----------- | ----------- |----------- |
| atub0y-post      |In 1971, it gave birth to Bangladesh; now Balochistan is on its way!      |Neutral       |
| efmzos7   | Ol' Mikey was gay as all fuck. Leo too I think?        |IdentityDirectedAbuse       |
| eft34gc   | Lol you think that poor people don't rape kids? There's a reason why 'addict parents sold me to their friends' is a trope.        |AffiliationDirectedAbuse       |


* Dataset size
  * Train: 13585
  * Dev: 4527
  * Test: 5308
  * <img width="350" alt="Screen Shot 2022-11-30 at 10 31 45 AM" src="https://user-images.githubusercontent.com/104866320/204693384-43d52be0-a557-4be8-80da-5bab6e3068fe.png">

## Political Twitter Hatespeech
* Source: (#link)

* Format:

* Dataset size
  * Train: ## examples
  * Dev: ## examples
  * Test: ## examples

## Toxic Wikipedia Comments
* Source: https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data

* Format: csv
   * `id`: comment id 
   * `comment_text`: The text of the comment.
   * `hate_speech`: Boolean. 1 if the comment is hate speech and 0 if it's not hate speech.

* Dataset size
  * Train: 127656 examples
  * Dev: 31915 examples
  * Test: 63978 examples

* Sample Comments
  * Hate Speech: You people are posting the WRONG results so its MY problem jackass
  * Not Hate Speech: Fine. (Are we going to change all the others, too? No? Just asking.) Schmuckola could have saved a lot of grief by simply citing the policy, rather than strutting around like some self-important little peacock. (But that's Wikipedia; it has a tendency to attract such people. Whatever.)
