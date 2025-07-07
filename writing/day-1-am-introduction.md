# Day 1 am: Bayesian Inference

The aim of today's morning session is to understand Bayesian inference from a theoretical point of view, and to introduce a data analysis problem that motivates the course.

## Bayesian statistical inference

Bayesian statistical inference can be understood pretty well by looking separately at the two concepts "Bayesian" and "statistical inference".

### "Bayesian"

The word "Bayesian" comes from the statistician [Thomas Bayes](https://en.wikipedia.org/wiki/Thomas_Bayes), who proved some theorems about conditional probability functions in the 18th century. However, in modern usage of the term "Bayesian" doesn't really have much to do with the original Bayes; rather it means something like "to do with probability functions".

Mathematically, a probability function is a function  $p: \mathcal{S} \rightarrow [0,1]$ where:

- $\mathcal{S}$ is an [event space](https://en.wikipedia.org/wiki/Event_(probability_theory)#Events_in_probability_spaces) 
- If $A, B \in \mathcal{S}$ are disjoint (i.e. they have no members in common), then $p(A\cup B) = p(A) + p(B)$

Intuitively, probability functions describe more or less anything that can be measured. For example, a jug containing 1 unit of water

:::{#fig-jug}
![](img/jug.jpg)

A jug of water
:::

To draw out the analogy a little and connect the mathematical definition with the intuition, consider:

- In this case the set $mathcal{S}$ corresponds to all possible ways of dividing the water in the jug into subsets. For example, pouring it into two disjoint cups $A$ and $B$.
- If cup $A$ contains 0.4 units of water and cup $B$ contains $0.2$ units, then the total amount of water in both cups is 0.4 + 0.2 = 0.6 units.

#### Bayesian epistemology

Bayesian epistemology is the idea that probability functions can describe belief or information. In other words, sometimes it is convenient to think about information as a thing that can be measured and shared around, like water. For example, we might use the cups $A$ and $B$ to represent some mutually exclusive propositions. Then we could represent the information "definitely B" by dividing the belief up like this:

![](img/definitely_b.jpg)

We could also use this method to represent some other beliefs:

"Not sure if A or B":

![](img/not_sure.jpg){width=35%}

"B a bit more plausible than A":

![](img/probably_b.jpg){width=35%}

Interesting philosophical discussions can be had about whether this kind of analogy can describe *any* information. My personal favourite is the book "Patterns of Plausible Inference" [@polyaMathematicsPlausibleReasoning1990]. However, for Bayesian statistics to be useful we only need the weaker proposition that the analogy sort of works sometimes. I think this is pretty hard to dispute, as shown by how often people say things like "probably" or "100%" to describe information.

### Statistical inference

The problem of finding things out about a population by examining a sample from the population encompasses statistical inference. This is something we all do all the time, which shows that you really know how to do statistical inference already: doing this course may not teach you something new so much as make your existing knowledge easier to articulate! An example of sample to population inference that you may have experience with is tasting a spoonful from a pot of soup:

::: {#fig-soup}
![](img/soup.jpg)

A nice soup: [here is the recipe](https://www.theguardian.com/lifeandstyle/2017/jan/24/20-best-one-pot-recipes-part-2-tom-kerridge-nigella-lawson-broths-hangover-food)

:::

Typically, salt mixes pretty well into the soup, so it is pretty safe to say that the salt concentration of the whole pot of soup will be about the same as the concentration in the spoon. On the other hand, if your goal was to establish the total number of carrots in the pot per unit volume, counting the number in a spoonful might not be so reliable!

The aim of theoretical statistical inference is to construct systematic rules for sample-to-population reasoning of this type. For example, we might use the following rule:

> It is safe to say that the concentration of a thing in the spoon is about the same as the concentration in the pot, provided there are at least 1000 particles of the thing in the spoon.

::: {.callout-tip}
#### Exercise
Can you think of any problems with this rule?
:::

### What is Bayesian statistical inference?

Equipped with the concepts "Bayesian" and "statistical inference", we can now make a definition of "Bayesian statistical inference":

Bayesian inference is sample-to-population inference that results in statements about a probability function, i.e. an assignment of numbers to elements of an event space.

For example, faced with the tasting problem, these statistical inferences are "Bayesian"

- spoon $\rightarrow$ $p(\text{soup not salty})$ = 99.9%
- spoon $\rightarrow$ $p(\text{no carrots in soup})$ = 95.1% 

To illustrate that other forms of statistical inference are possible, consider these non-Bayesian inferences:

- spoon $\rightarrow$ Best estimate of salt concentration is 0.1mol/l
- $p_{\text{carrot hypothesis}}(\text{spoon with fewer carrots than this}) = 4.9\%$ $\rightarrow$ There are no carrots in the pot!

The first inference is non-Bayesian because the result---a best estimate of the population salt concentration---is not a probability.

::: {.callout-tip}
#### Something to think about
How might we *get* an estimate of the population concentration from a Bayesian inference, if that was what we wanted?
:::

The second inference has the same form as a null-hypothesis significance test, a statistical inference method you may be familiar with. The inference kind of looks probability-like, so you might wonder if it is Bayesian according to our definition. The answer is no! There *is* a probability statement on the left hand side of the inference, i.e. the statement that, according to a probability function representing the hypothesis that there are carrots in the pot, it would be unlikely to see this few carrots. However, according to our definition Bayesian inference requires a probability statement on the right hand side. 

### Why probability?

Since the special thing about Bayesian inference, compared with other ways of doing statistical inference is that it outputs a statement about a probability function, the reasons for choosing Bayesian inference also have to do with the features of probabilities.

#### Probabilities are interpretable

It is straightforward to interpret statements about probabilities in terms of information and plausible reasoning. For example, after doing a Bayesian inference, one can say things like "According to my model, proposition x..."

- "...is highly plausible."
- "...is more plausible than y."
- "...is neither ruled in or out by the available data. There just isn't enough information for firm conclusions about x."

In contrast, non-Bayesian statistical inferences can be trickier to interpret.

For a lot more about this and other connections between Bayesian inference, information and plausible reasoning, check out [@jaynesProbabilityTheoryLogic2003].

#### Probability theory is old

Probability theory is a mature and well-developed branch of mathematics. This makes probability functions a good choice for the output of a statistical inference for several reasons. First, since so much work has already been done, it is rare that Bayesian inference is blocked by the need to develop new mathematical theory. In fact, the theoretical apparatus of Bayesian inference was already available to Pierre-Simon Laplace: the Bayesian inference that he practised before the French revolution is essentially the same as you will learn in this course.

::: {#fig-laplace width="40%"}

[![(https://en.wikipedia.org/wiki/Pierre-Simon_Laplace)](img/laplace.jpg)](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace){height=80%}

Laplace, who did Bayesian inference in the 1780s
:::

Second, the maturity of probability theory means that Bayesian statistical inference is compatible with a wide range of related tools, and in particular Bayesian decision theory. Whereas users of newer statistical frameworks must do some original work to justify what they want to do with their inferences, Bayesian inference practitioners can simply specify a utility function and then plug in to the existing theory.

#### Probabilities decompose conveniently, aka Bayes's theorem

Probabilities decompose nicely, as shown by the following slight alteration of Bayes's theorem:

$$
p(\theta, y) \propto p(\theta)p(y\mid\hat{y}(\theta))
$$

- $p(\theta)$: nice form for *background* information, e.g. anything non-experimental
- $\hat{y}(\theta)$: nice form for *structural* information, e.g. physical laws
- $p(y\mid\hat{y}(\theta))$: nice form for *measurement* information, e.g. instrument accuracy
- $p(\theta, y)$ a single function that encapsulates the whole model

### Why (or why not) use Bayesian statistical in *my* project?

Perhaps you are convinced by the arguments above but are still not sure about whether Bayesian inference is a good fit for your practical data analysis problem. This may well be because the arguments above are quite general, and have to do with choosing Bayesian statistical inference compared with non-Bayesian statistical inference.

## Motivating example


## Things to read

@boxBayesianInferenceStatistical1992 [Ch. 1.1] (available from dtu findit) gives a
nice explanation of statistical inference in general and why Bayes.

Historical interest:

- @laplaceMemoirProbabilityCauses1986 and @stiglerLaplace1774Memoir1986 
- @jaynesProbabilityTheoryLogic2003 Preface
