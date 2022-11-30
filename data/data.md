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

* Format 
  * <img width="1193" alt="image" src="https://user-images.githubusercontent.com/104866320/204695187-0d35fd55-7be2-4ff8-a7d2-785041ecc53b.png">
  * <img width="1193" alt="image" src="https://user-images.githubusercontent.com/104866320/204695005-1018b913-d632-48ee-8d62-da8d718c1097.png">
  * <img width="1193" alt="image" src="https://user-images.githubusercontent.com/104866320/204694259-844353a4-bdee-4cc5-ac91-5fa249cd5357.png">
  * <img width="1193" alt="image" src="https://user-images.githubusercontent.com/104866320/204695122-1d829352-44b3-4cc0-b378-cecb70d4f818.png">
  * <img width="1193" alt="image" src="https://user-images.githubusercontent.com/104866320/204694858-f849f5bb-8c46-428a-be28-aee5c3f1d206.png">

* Dataset size
  * Train: 13585
  * Dev: 4527
  * Test: 5308
  * <img width="350" alt="Screen Shot 2022-11-30 at 10 31 45 AM" src="https://user-images.githubusercontent.com/104866320/204693384-43d52be0-a557-4be8-80da-5bab6e3068fe.png">

## Political Twitter Hatespeech

* Source: https://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/stance-hof/

  * Tweets were fetched for 6 weeks leading to the presidential election, on election data, and 1 week after. They describe their filtering process as using “the mention of the presidential and vice presidential candidates and the outsider West; the mention of hashtags that show a voter’s alignment such as the campaign slogans of the candidate websites, and further nicknames of the candidates.”
  * The exact terms used to filter tweets were: “#Trump2020, #TrumpPence2020, #Biden2020, #BidenHarris2020, #Kanye2020, #MAGA2020, #BattleForTheSoulOfTheNation, #2020Vision, #VoteRed2020, #VoteBlue2020, Trump, Pence, Biden, Harris, Kanye, President, Sleepy Joe, Slow Joe, Phony Kamala, Monster Kamala”
  * Hatefulness annotations were done by 3 annotators with a Cohen’s k of .62, representing a fair amount of agreement between annotators. Particular guidelines mentioned were that name-calling was classified as hateful/offensive, as well as abbreviations like POS and BS.

* Format: 
  * `text`: Input. String. The text of the tweet/comment/post
  * `HOF`: Target. Boolean, as 1 or 0. Whether the text is classified as hateful/offensive (1) or not (0).

* Dataset size
  * Train: 2040 examples
  * Dev: 360 examples
  * Test: 600 examples
* Randomly selected example of speech deemed hateful/offensive:
  * “@greenfield64 No Way!   @realDonaldTrump   F** K Trump  Wish him the best but you know what, he knew the risks and should have worn a mask.  #BidenHarris2020 #screwtrump…”
* Randomly selected example of speech deemed non-hateful/offensive:
  * “@SukiRavan @ProgressPotato @MarkZuckerb0rg @JSiffordson @KyleKulinski If Joe Biden is .00000000000000001 % better I will vote for him.”

## Toxic Wikipedia Comments
* Source: https://drive.google.com/drive/folders/1-lqUa8oPOMF6EsFEQyOgjBkPe2Apf5th?usp=sharing

* Format: csv
  * `id`: comment id 
  * `comment_text`: The text of the comment.
  * `hate_speech`: Boolean. 1 if the comment is hate speech and 0 if it's not hate speech.

* Dataset size
  * Train: 127656 examples
  * Dev: 31915 examples
  * Test: 63978 examples
