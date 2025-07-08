# Day 2 am: Regression and formula-based models

## Regression

Recall from the previous session that one of the advantages of Bayesian statistical inference---aka using a sample to answer questions about a population in the form of probability statements---is that probability functions decompose into the following convenient form:

$$
p(y, \theta) \propto p(\theta)p(y\mid\theta)
$$

In particular, we mentioned that the form $p(y\mid\theta)$ is convenient for representing data generating processes.

Regression is the main way to flesh out this idea: it provides specific ways to say, for data $y$ and parameters $\theta$, what is the likelihood $p(y\mid\theta)$.

The key idea of regression is to separate out some components of $y$ called "covariates", or "independent" variables, and typically denoted $x$. Here we will use the term $y_{\text{dep}}$ to refer to the other members of $y$, typically called "variates" or "dependent variables" and used to represent things that are measured in an experiment.

::: {.note}

The rest of this course, an most statistics notation, typically omits the subscript $_{\text{dep}}$ in $y_{\text{dep}}$ and $\hat{y}_{\text{dep}}$, as there is usually no need to refer to the full data $y=\{x, y_{dep}\}$. 

:::

With this split made, the next step in regression modelling is to define a way to turn the covariates into a summary statistic, then connect this statistic probabilistically with $y_{\text{dep}}$. In mathematical notation, this means that a regression model has this form:

$$
p(y\mid\theta) = p(y_{\text{dep}}\mid T(x, \theta), \theta)
$$

where $T$ is a deterministic function that maps any $x$ and $\theta$ to a summary statistic.

A popular approach, which we will concentrate on in this course, is for the summary statistic $T(x, \theta)=\hat{y}_{\text{dep}}(x, \theta)$ to be an estimate of the most likely, or "expected", value of $y_{dep}$. Alternatively, in [quantile regression](https://en.wikipedia.org/wiki/Quantile_regression) the summary statistic estimates an extreme value of $y_{dep}$.

Formulating $p(y\mid\theta)$ up in this way allows a regression modeller to separately create a deterministic model of the underlying process and a probabilistic model of the measurement process. This separation is very convenient!

Being able to choose any deterministic function $T$ to represent the relationship between $x$, $\theta$ and $y_{dep}$ allows the modeller a lot of freedom to represent domain knowledge. For example, $T$ might encode a kinetic model connecting experimental conditions with things we can measure in a bioreactor.

On the other hand, writing down a function $p(y_{\text{dep}}\mid T(x, \theta), \theta)$ is often easier than directly specifying a likelihood function $p(y\mid\theta)$. The former, regression-based formulation is natural for representing how noisy measurements work. For example, regression models often represent measurements using the normal distribution:

$$
\begin{align*}
\theta &= \theta_1, ..., \theta_k, \sigma \\
T(x, \theta) &= T(x, \theta_1, ..., \theta_k) = \hat{y}_{\text{dep}}\\
p(y_{\text{dep}}\mid T(x, \theta), \theta) &= N(y_{\text{dep}}\mid \hat{y}_{\text{dep}}, \sigma)
\end{align*}
$$

In this equation $N$ indicates the normal probability density function:

$$
N(y_{\text{dep}}\mid\hat{y}_{\text{dep}},\sigma) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp{-\frac{(y_{\text{dep}}-\hat{y}_{\text{dep}})^2}{2\sigma^2}}
$$

To get an intuition for why this makes sense as a way to represent a measurement, consider the following plot of this function:

![](img/norm.png)

Note that, as we usually expect for a measurement, the density is highest when the measured and expected values are the same, and smoothly and symmetrically decreases with this distance. The accuracy of the measurement can be captured by the parameter $\sigma$, as shown by comparing the blue and orange lines.

### Representing measurements using probability distributions

Here are some rules of thumb for representing measurements using probability distributions.

The most important thing is to consider are natural constraints: where does the measurement *have* to live?

#### Unconstrained measurements

If both measureable and measurement can in principle live on any the real line, the Normal regression model presented above is usually a good starting point. Many standard statistical methods explicitly or implicitly assume such a model.

If your unconstrained measurements come in batches, consider whether they are likely to be correlated, so that the value of one batch component could be informative about the value of another. If so, you may want to use a [multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution) to model your measurements.

If, as happens quite often, your unconstrained measurements potentially include outliers, they may be better described using a measurement distribution with heavier tails than the normal distribution, such as the [student-T distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution).

If your unconstrained measurements are skewed, so that errors in one direction are more likely than the other, consider modelling them with a [skew-normal distribution](https://en.wikipedia.org/wiki/Skew_normal_distribution).

#### Non-negative measurements

We often want to measure things that cannot possibly be negative, like concentrations or temperatures. This kind of measurement is often **not** well described by the normal distribution.

First, note that the normal distribution has support across the whole real number line, half of which is inaccessible to a non-negative measurement. Modelling non-negative measurements using the normal distribution therefore necessarily involves allocating probability mass to something structurally impossible. How big of a problem this is in practice depends on the amount of probability mass misallocated: this in turn depends on the distance in measurement standard deviations from $\hat{y}_{\text{dep}}$ to zero. As a general rule of thumb, if this distance is less than 3 standard deviations for any measurement, there is a potential problem. 

Second, note that the normal probability density function is symmetrical: the density decreases at the same rate both up and down from $y_{\text{dep}}-\hat{y}_{\text{dep}}=0$. This behaviour is desirable when an error gets less likely proportionally to its absolute size. However non-negative measurement errors are often naturally expressed relatively, not absolutely. If you usually talk about your errors in terms like "+/- 10%" or similar, an unconstrained probability distribution is probably a bad fit.

For these reasons, when modelling non-negative measurements, it is often a good idea to use a probability distribution whose support lies only on the non-negative real line. This can often easily be done by log-transforming the measurements and then using an unconstrained measurement distribution centred at the logarithm of $\hat{y}_{\text{dep}}$.

#### Measurements that live in the interval [-1, 1]

Try transforming the measurements to unconstrained space using the inverse hyperbolic tangent function.

#### Counts

Use the poisson distribution.

#### Ranks

Try the rank-ordered logit distribution. Good luck!

#### Compositions

This is a whole area of statistics, but you can get a long way by transforming compositional measurements to unconstrained space using a [log-ratio function](https://en.wikipedia.org/wiki/Compositional_data#Linear_transformations).

### Representing domain knowledge using linear models

In a regression model the function $T(x, \theta)$ encodes the modeller's knowledge about how the measurement targets depend on the covariates and parameters. The simplest, and by far most common, way to do this is with a linear model.

A linear model assumes that the expected value of the measurable, i.e. $\hat{y}_{\text{dep}}$, depends on a weighted sum of the covariates $x$. For example, we might have

$$
\hat{y}_{\text{dep}} = x\beta
$$

Where $\beta$ is a vector of weights.

::: {.note}

Note that this formulation allows for an intercept, i.e. a weight that applies to all measurements, via inclusion of a dummy variable in $x$ whose value is 1 for all measurements.

:::

To accommodate constrained measurement models without changing the approach too much, linear models often add a "link" function that transforms the unconstrained term $x\beta$ to match the constrained term $\hat{y}_{\text{dep}}$. Models with this form are called "generalised linear models" or "GLM"s. For example, here is a poisson GLM for describing count data, where the link function is the natural logarithm:

$$
\begin{align*}
\hat{y}_{\text{dep}} = \ln(x\beta)
y_{\text{dep}} \sim Poisson(\hat{y}_{\text{dep}})
\end{align*}
$$

#### Don't forget to transform the covariates!

Linear models have a lot of hidden flexibility, as the modeller is free to transform the covariates however they like. You can and should make the most of this freedom. In particular, consider log-transforming any positive-constrained covariates.

## Formula-based models

## Why formula-based models aren't enough

