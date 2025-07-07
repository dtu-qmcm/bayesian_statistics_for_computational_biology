# Bayesian Statistics for Computational Biology

[![CC BY 4.0][cc-by-shield]][cc-by]

This repository has materials for the course "Bayesian Statistics for Computational Biology".

## About the course

The course currently takes place physically over three weeks in the summer at DTU Biosustain. If you are taking or want to take that course, congratulations you are in the right place! If not, you may still find something interesting here!

The aim of the course is to teach students with a background in computational biology how to:

- Describe Bayesian inference in the abstract
- Assess whether Bayesian inference is a good fit for a problem
- Formulate custom measurement models to describe biological problems
- Solve statistical modelling problems by iteratively fitting and evaluating a series of models
- Choose appropriate software for a Bayesian statistical modelling project
- Understand gradient-based MCMC techniques and their failure modes
- Fit biological models with embedded ODE systems, root-finding problems and Gaussian processes.
- Perform Bayesian optimisation
- Understand recent trends in Bayesian statistical inference 

The learning material consists of 20 sessions, each intended to take up half a day over two weeks. The third week of the course is set aside for the students to complete a project. For the first two weeks, the first half-day will generally cover theoretical topics, with the second consisting of practical, computer-based tasks. Here is the rough plan:

- Day 1. am: Bayesian statistical inference, motivating example
- Day 1. pm: Set up computers (Python, uv, git, editor)
- Day 2. am: Regression, formula-based models and why they aren't enough
- Day 2. pm: Some regression examples, bambi
- Day 3. am: Markov Chain Monte Carlo, why you still probably want to use it.
- Day 3. pm: A Bayesian statistics stack for computational biology
- Day 4. am: What to do with MCMC output?
- Day 4. pm: Worked examples:
             - convergence
             - divergent transitions
             - model comparison
             - change of variables causing bad model
- Day 5. am: Bayesian workflow
- Day 5. pm: Workflow example with automation
- Day 6. am: Ordinary differential equations
- Day 6. pm: Diffrax, fermentation examples
- Day 7. am: Algebraic equation systems, implicit differentiation
- Day 7. pm: Optimistix, steady state example, grapevine
- Day 8. am: Gaussian processes, HSGPs
- Day 8. pm: GP example
- Day 9. am: Bayesian optimisation
- Day 9. pm: BO example
- Day 10. am: Fun new Bayesian trends
              - Probabilistic numerics
              - Amortised Bayesian inference
              - New MCMC algorithms
              - Control
              - Normalising flows
- Day 10. pm: examples 

## What is in this repository?

This repository contains:

- Source material for the course's website (folder `writing`)
- The html files that comprise the website (folder `docs`)
- Code that might be useful during the course (folder `src`)
- Datasets that come up in the course (folder `data`)

Why is the html folder called `docs`? Well, that just makes it easier to avoid effort using GitHub pages.

## Licence

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg


