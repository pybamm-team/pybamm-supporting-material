---
title:  'Python Battery Mathematical Modelling (PyBAMM)'
author: Martin Robinson
date: 15th July, 2019
urlcolor: blue
link-citations: true
header-includes:
    - \usepackage{multimedia}
---


# What is PyBaMM

- *Python Battery Mathematical Modelling* (PyBAMM) solves continuum models for batteries,
  using both numerical methods and asymptotic analysis.

- Designed as a Common Modelling Framework for the Multiscale Modelling Faraday project.
  Facilitates sharing and distribution of **model** and **numerical methodologies** .

- Use it for:
    1. Running a battery simulation using one of the pre-built models, either as a
       single simulation or within parameter estimation
    2. Inserting your own model, discretisation or solver. Compare with the pre-built pybamm
       components, or to share with other PyBaMM users.
    3. Develop within the PyBaMM framework, or use any of PyBaMM's components within
       your own code

# Organisation

- developers:

\includegraphics[width=0.8\textwidth]{images/developers.pdf}

# Organisation

- developed as an open source (BSD licensed) Python library on GitHub: 
    - <https://github.com/pybamm-team/PyBaMM>

- software engineering best practices:
    - Full suite of unit and integration tests
    - Automated testing on Linux, Mac and Windows using Python 3.5+
    - Generated API documentation and example notebooks/scripts demonstrating
      features
    - Project management, issue tracking and code review via GitHub

# Current features

- Lithium-ion battery models:
    1. Single Particle Model (SPM) 
    2. Single Particle Model with Electrolyte (SPMe)
    3. Doyle-Fuller-Newman (DFN)
- Lead-acid battery models:
    1. LOQS Model 
    2. Composite Model 
    3. Newman-Tiedemann Model
- Discretisations:
    1. 1D Finite Volumes
    2. Control Volumes (electrode particle domains)*
- Solvers:
    1. Scipy ODE solvers
    2. Scikits ODE & DAE solvers (SUNDIALS)
    3. Dae-Cpp DAE solver (Ivan Korotkin - Southampton)*

# PyBaMM Pipeline

\begin{columns}
\begin{column}{0.4\textwidth}
\begin{itemize}
\item PyBaMM's design separates the different stages solving a model, can develop or
  customise each stage separately
\item Construction of a pipeline is a python script, reuse the stages as you see fit (e.g. comparing different models, re-solving with different parameters, custom plotting, ...)
\end{itemize}
\end{column}
\begin{column}{0.6\textwidth}  %%<--- here
    \begin{center}
\centering \includegraphics[width=1.0\textwidth]{images/pipeline.pdf} 
     \end{center}
\end{column}
\end{columns}


# PyBaMM's Expression Tree

\begin{columns}
\begin{column}{0.4\textwidth}
\begin{itemize}
\item Communication between the stages is done via expression trees representing equations
\item Different stages operate on these. E.g. Parameter Values walks though tree replacing symbolic parameters with scalars.
\end{itemize}
\end{column}
\begin{column}{0.6\textwidth}  %%<--- here
    \begin{center}
\centering \includegraphics[width=1.0\textwidth]{images/expression_tree.pdf} 
     \end{center}
\end{column}
\end{columns}

# Use Case 1 - Adding your own model

1. Create a Python class representing your model\footnote{see repository documentation for more details}
2. Define `rhs`, `algebraic`, `boundary_conditions`, `initial_conditions`, `variables`
   as **expression trees**
3. An expression tree is built from building blocks such as
   `pybamm.Variable` or `pybamm.Parameter`, and normal Python operators such as `+`. For
   example, the expression $$\nabla \cdot D(c) \nabla c + a c$$
   
   is written in Python as

```python
c = pybamm.Variable('c')
a = pybamm.Parameter('a')
D = lambda x: pybamm.FunctionParameter('D', x)

expr = pybamm.div( D(c) * pybamm.grad(c) ) + a * c 
```

# Use Case 2 - Using your own parameters

- Each model has a set of default parameters that you can use

```python
model = pybamm.lithium_ion.SPM()
param = model.default_parameter_values
```

- You can change individual parameters in a python script using:

```python
param['Typical current [A]'] = 1.4
```

- Alternatively, the default parameter sets are defined as `csv` files, so can supply
  your own to specify an entire parameter set.

# Other potential use cases

1. **Custom discretisation**: discretisation is set on a per-domain basis (
   electrolyte, positive electrode particle, etc.). Can supply your own discretisation
   for one or more domains. Can be as general purpose or as model-specific as you
   require. 
2. **Parameter estimation**: Those parameters that do not affect the discretisation can
   be altered and a new solutions obtained just be re-running the solver (i.e. no need
   to re-generate and discretise your model)
3. **Others..?**: We are keen to hear your ideas! PyBaMM is in a formative stage so keen
   to receive and incorporate feedback into the library.

# Summary



