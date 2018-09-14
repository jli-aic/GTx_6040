#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 21:17:26 2018

@author: zacholivier
Re-introduction to Linear Algebra

One of the prerequisites for this course is linear algebra. This notebook is 
designed to "re-introduce" you to the topic. It guides you through some 
fundamental concepts using (Python) code and code-generated pictures. 
So, beyond reviewing math we hope it gives you yet-another opportunity to 
improve your Python code-reading skills.
This notebook contains a mix of pencil-and-paper exercises as well as coding 
"exercises." But for the coding exercises, we have provided solutions. You 
should read them to see that they make sense, and you might even try erasing 
them and seeing if you can generate the same (or similar) 
solutions on your own.
Aside. You may be wondering why you need a linear algebra refresher at all. 
The answer is that linear algebra is, arguably, the mathematical and 
computational foundation for much of modern data analysis and machine learning.
 Modern computers are also very good at executing linear algebra operations 
 quickly. Therefore, the more of a computation you can cast into a linear 
 algebraic form, the easier it will be to speed up and scale up later on.
In fact, there are many computations that do not even look like linear algebra
 at first, but can, in fact, be cast into "patterns" that do resemble it. 
 These include database queries and searches in graphs and networks. 
 Some of these ideas appear in Topic 2. Therefore, knowing linear algebra and 
 knowing how it maps to code gives you a framework for doing fast 
 computations more generally. So, even if the topic seems a bit dry at first 
 glance, try to stick with it and you'll earn dividends in the long-run, 
 well beyond this topic and course.
 """
 
 # Just for reference, this prints the currently version of Python
import sys
print(sys.version)

# Code for pretty-printing math notation
from IPython.display import display, Math, Latex, Markdown

def display_math(str_latex):
    display(Markdown('${}$'.format(str_latex)))
    
# Demo:
display_math(r'x \in \mathcal{S} \implies y \in \mathcal{T}')


# Code for drawing diagrams involving vectors
import matplotlib.pyplot as plt
%matplotlib inline

DEF_FIGLEN = 4
DEF_FIGSIZE = (DEF_FIGLEN, DEF_FIGLEN)

def figure(figsize=DEF_FIGSIZE):
    return plt.figure(figsize=figsize)

def multiplot_figsize(plot_dims, base_figsize=DEF_FIGSIZE):
    return tuple([p*x for p, x in zip(plot_dims, base_figsize)])

def subplots(plot_dims, base_figsize=DEF_FIGSIZE, sharex='col', sharey='row', **kw_args):
    assert len(plot_dims) == 2, "Must define a 2-D plot grid."
    multiplot_size = multiplot_figsize(plot_dims, base_figsize)
    _, axes = plt.subplots(plot_dims[0], plot_dims[1],
                           figsize=multiplot_size[::-1],
                           sharex=sharex, sharey=sharey,
                           **kw_args)
    return axes

def new_blank_plot(ax=None, xlim=(-5, 5), ylim=(-5, 5), axis_color='gray', title=''):
    if ax is None:
        ax = plt.gca()
    else:
        plt.sca(ax)
    ax.axis('equal')
    if xlim is not None: ax.set_xlim(xlim[0], xlim[1])
    if ylim is not None: ax.set_ylim(ylim[0], ylim[1])
    if axis_color is not None:
        ax.axhline(color=axis_color)
        ax.axvline(color=axis_color)
    if title is not None:
        ax.set_title(title)
    return ax

def draw_point2d(p, ax=None, marker='o', markersize=5, **kw_args):
    assert len(p) == 2, "Point must be 2-D."
    if ax is None: ax = plt.gca()
    ax.plot(p[0], p[1], marker=marker, markersize=markersize,
            **kw_args);

def draw_label2d(p, label, coords=False, ax=None, fontsize=14,
                 dp=(0.0, 0.1), horizontalalignment='center', verticalalignment='bottom',
                 **kw_args):
    assert len(p) == 2, "Position must be 2-D."
    if ax is None: ax = plt.gca()
    text = '{}'.format(label)
    if coords:
        text += ' = ({}, {})'.format(p[0], p[1])
    ax.text(p[0]+dp[0], p[1]+dp[1], text,
            fontsize=fontsize,
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment,
            **kw_args)

def draw_line2d(start, end, ax=None, width=1.0, color='black', alpha=1.0, **kw_args):
    assert len(start) == 2, "`start` must be a 2-D point."
    assert len(end) == 2, "`end` must be a 2-D point."
    if ax is None:
        ax = plt.gca()
    x = [start[0], end[0]]
    y = [start[1], end[1]]
    ax.plot(x, y, linewidth=width, color=color, alpha=alpha, **kw_args);

def draw_vector2d(v, ax=None, origin=(0, 0), width=0.15, color='black', alpha=1.0,
                  **kw_args):
    assert len(v) == 2, "Input vector must be two-dimensional."
    if ax is None:
        ax = plt.gca()
    ax.arrow(origin[0], origin[1], v[0], v[1],
             width=width,
             facecolor=color,
             edgecolor='white',
             alpha=alpha,
             length_includes_head=True,
             **kw_args);
    
def draw_vector2d_components(v, y_offset_sign=1, vis_offset=0.05, comp_width=1.5, **kw_args):
    assert len(v) == 2, "Vector `v` must be 2-D."
    y_offset = y_offset_sign * vis_offset
    draw_line2d((0, y_offset), (v[0], y_offset), width=comp_width, **kw_args)
    draw_line2d((v[0], y_offset), v, width=comp_width, **kw_args)
    
def draw_angle(theta_start, theta_end, radius=1, center=(0, 0), ax=None, **kw_args):
    from matplotlib.patches import Arc
    if ax is None: ax = plt.gca()
    arc = Arc(center, center[0]+2*radius, center[1]+2*radius,
              theta1=theta_start, theta2=theta_end,
              **kw_args)
    ax.add_patch(arc)
            
def draw_angle_label(theta_start, theta_end, label=None, radius=1, center=(0, 0), ax=None, **kw_args):
    from math import cos, sin, pi
    if ax is None: ax = plt.gca()
    if label is not None:
        theta_label = (theta_start + theta_end) / 2 / 360 * 2.0 * pi
        p = (center[0] + radius*cos(theta_label),
             center[1] + radius*sin(theta_label))
        ax.text(p[0], p[1], label, **kw_args)

print("Ready!")



"""
Points in Euclidean geometry
First, recall the notion of  d-dimensional space that obeys Euclidean geometry.
 The space is an infinite set of points whose positions may be described in 
 terms of  d-coordinate axes, which are perpendicular to one another. 
 Each axis is associated with real-values that range from  −∞ to  ∞. 
 Here is a snapshot of a  d=2-dimensional space with the usual x- and y-axes 
 intersecting at the origin,  x=0,y=0.
 
"""
figure()
new_blank_plot();



"""
We will refer to these "standard" perpendicular axes as the canonical axes of 
a  d-dimensional space.
The position of each point p
 in this space is a tuple of d
 real-valued coordinates, p=(p0,p1,…,pd−1)
. Each coordinate pi
 is a real number, which in math terms we write by saying pi∈
, where 
 is the set of real numbers. Each pi
 measures the extent of p
 along the i
-th axis. In 2-D, the x-coordinate of p
 is p0
 and the y-coordinate is p1
.
Note. We are using a convention in which the axes and coordinates are numbered starting at 0, in part for consistency with how Python numbers the elements of its tuples, lists, and other collections.
Here is an example of three points, a, b, and c, in a 2-D Euclidean space. 
The code uses the natural data type for representing the points, namely, 
Python's built-in 2-tuple (i.e., pair) data type.
"""


# Define three points
a = (-2, 2)
b = (3.5, 1)
c = (0.5, -3)

# Draw a figure containing these points
figure()
new_blank_plot()
draw_point2d(a, color='blue'); draw_label2d(a, 'a', color='blue', coords=True)
draw_point2d(b, color='red'); draw_label2d(b, 'b', color='red', coords=True)
draw_point2d(c, color='green'); draw_label2d(c, 'c', color='green', coords=True)

"""
Exercise. We will assume you are familiar with the basic geometry of Euclidean 
spaces. For example, suppose you connect the points into a triangle whose 
sides are  ab⎯⎯⎯⎯⎯,  bc⎯⎯⎯⎯⎯, and  ac⎯⎯⎯⎯⎯. 
What are the lengths of the triangle's sides? What are its angles?
"""


"""
Vectors (vs. points)
In linear algebra, the first concept you need is that of a vector. 
A vector will look like a point but is, technically, a little bit different.

Definition: vectors. A  d-dimensional vector is an "arrow" in  d-dimensional 
space. It has a length and a direction. It does not have a position! 
Having said that, we will represent a vector by its length along each of the
canonical axes, albeit using the following slightly different notation.


In particular, we will write a  d-dimensional vector  v as a column vector,
v≡v0v1⋮vd−1,
v
≡
[
v
0
v
1
⋮	
v
d
−
1
 
]
,
 
where each entry  vi is the length of the vector with respect to the  i-th 
axis. 
We will also refer to the entries as elements or components of  v


In our class, we are always interested in spaces in which the possible values
 of  vi are real numbers. Therefore, when we want to say a mathematical object
 v is a  d-dimensional vector, we will sometimes write that using the 
 shorthand,  v∈ℝd, meaning  v is an element of the set of all possible 
 d-dimensional vectors with real-valued components.
 
Aside 1. We usually use the term "coordinates" when referring to the 
components of a point. And while a vector does not have a position, 
making it not a point, we will nevertheless "abuse" terminology sometimes 
and refer to the "coordinates" of a vector when we mean "components" or 
"elements."

Aside 1. The term "column" suggests there is a notion of a "row" vector. 
We'll discuss that later.
"""


"""
A code representation. As we did with points, let's again use tuples to 
represent the elements of a vector. Below, we define a Python function, 
vector(), whose arguments are, say,  d coordinates; it returns a tuple that 
holds these elements. 

In this  d=2 example, suppose a vector  vhas a length of  v0=1.0 along the
0-th coordinate (e.g., x-axis) and  v1=2.0 in the  1st coordinate 
(e.g., y-axis):
"""

def vector(*elems, dim=None):
    """
    if dimension defined ensure it equals the number of elements
    else return a 0 vector duplicated to match elements
    if dimension is not defined return a tuple of the elements provided
    """
    if dim is not None:
        if len(elems) > 0:
            assert dim == len(elems), "Number of supplied elements differs from the requested dimension."
        else: # No supplied elements
            elems = [0.0] * dim
    return tuple(elems)


def dim(v):
    """Returns the dimensionality of the vector `v`"""
    return len(v)

v = vector(5.0, 9.0)
d = dim(v)
print('v = {}    <==  {}-dimensional'.format(v, d))

# Another example: Creates a zero-vector of dimension 3
z3 = vector(dim=3)
print('z3 = {}    <== {}-dimensional'.format(z3, dim(z3)))





"""
Aside: Pretty-printing using LaTeX. Recall the abstract mathematical notation 
of a vector's elements as a vertical stack. Using the standard Python print()
 renders a vector as a row-oriented tuple. However, Jupyter notebooks also 
 support LaTeX notation for rendering mathematical formulas in a "pretty" way. 
 This feature means we can write Python code that generates LaTeX and renders 
 it in the notebook!
You don't need to understand too much about how this process works. 
However, we mention it because you will see us define helper functions to 
help pretty-print math throughout this notebook.
"""

# pretty printing in LaTex
def latex_vector(v, transpose=False):
    """Returns a LaTeX string representation of a vector"""
    s = r'''\left[ \begin{matrix} '''
    sep = r'''\\''' if not transpose else r''', &'''
    s += (r' {} ').format(sep).join([str(vi) for vi in v])
    s += r''' \end{matrix}\right]'''
    return s

# Demo: Pretty-print `v` from before
print("Standard Python output:", v)
print("\n'Mathy' output:")
v_latex = latex_vector(v)
display_math('v \equiv ' + v_latex)

"""
Okay, back to math...

Definition: direction of the vector. 

To determine a vector's direction, start 
at the origin, and then take a step of size  vi along each axis i. 
We say the vector points from the origin toward the ending point. 
That's its direction. We'll draw a picture momentarily to make this clearer.


Definition: length of a vector. 

The length of the vector is the straight-line
 (Euclidean) distance between the origin and the endpoint, if the vector is
 placed at the origin. With respect to the coordinates, this distance is given 
 by the familiar formula,
v20+v21+⋯+v2d−1⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√,
 
that is, the square-root of the sum of squared lengths along each axis.

"""

# python function to determine a vector length
def length(v):
    from math import sqrt
    return sqrt(sum([vi*vi for vi in v])) # euclidean distance formula
# square-root of the sum of squared lengths

print("The length of v = {} is about {}.".format(v, length(v)))


# take a look at a vector
figure()
new_blank_plot(title='Vector v = {}'.format(str(v)))
draw_vector2d(v, color='blue')


# vectors only have length and direction - they DO NOT have a position!

"""
Remember: Vectors do not have a position! In the picture above, we drew the
 vector beginning at the origin. However, remember that a vector technically 
 does not have a position. That is, if we do "move" it to some other point of 
 the space, it is the same vector. So in the following picture, the blue 
 vectors have the same representation, that is, identical components.
"""

def random_vector(dim=2, v_min=-1, v_max=1):
    """Returns a random vector whose components lie in (`v_min`, `v_max`)."""
    from random import uniform
    v = vector(*[uniform(v_min, v_max) for _ in range(dim)])
    return v

def flip_signs_randomly(v):
    from random import choice
    return [choice([-1, 1])*vi for vi in v]

# Draw `v` at the origin
subfigs = subplots((1, 2))
new_blank_plot(subfigs[0], title='v, placed at the origin')
draw_vector2d(v, color='blue')

# Draw `v` somewhere else
dv = flip_signs_randomly(random_vector(dim=dim(v), v_min=1, v_max=3))
new_blank_plot(subfigs[1], title='v, placed at ({:.1f}, {:.1f})'.format(dv[0], dv[1]))
draw_vector2d(v, color='blue', origin=dv)

"""
Definition:  p-norms. 
We defined the length using the familiar Euclidean notion of distance.
 However, there are actually many other kinds of distance. The  p-norm of a
 vector  v is one such generalized idea of a distance:
∥v∥p≡(∑i=0d−1|vi|p)1p.
 
The usual Euclidean distance is the same as  p=2, i.e., the "two-norm." 
There are some other commonly used norms.
p=1: The one-norm, which is the same as the "Manhattan distance." 
In machine learning applications, judicious use of this norm often leads to
 "sparse" models, that is, models where less important parameters are 
 automatically driven to zero.
p=∞: The infinity-norm, also known as the "max norm." 
It is the largest absolute entry, that is,  ∥v∥∞=maxi∥vi∥.
"""


# calculate a p-norm in python
def norm(v, p=2):
    assert p > 0
    from math import sqrt, inf, pow
    if p == 1: return sum([abs(vi) for vi in v]) # manhattan distance
    if p == 2: return sqrt(sum([vi*vi for vi in v])) # euclidean distance
    if p == inf: return max([abs(vi) for vi in v]) # max distance infinity norm
    return pow(sum([pow(abs(vi), p) for vi in v]), 1.0/p)

def latex_norm(x, p=2):
    from math import inf
    if p == inf: p = r'\infty'
    s = r'\left\| '
    s += x
    s += r' \right\|_{}'.format(p)
    return s

import math
for p in [1, 2, math.inf]:
    v_pnorm_latex = latex_norm(v_latex, p)
    display_math(r'{} \approx {}'.format(v_pnorm_latex, norm(v, p)))

"""
Exercise. Convince yourself that the 1-norm, 2-norm, and  ∞
 -norm satisfy the following properties.
Triangle inequality.  ∥v+w∥≤∥v∥+∥w∥
 .
Absolute homogeneity. Let  σ
  be a scalar value. Then  ∥σv∥=|σ|⋅∥v∥.
  
"""
 


"""
Comparing norms. In the previous example, the one-norm is the largest value 
and the infinity-norm is the smallest. 
In fact, this holds in general and it is possible to show the following:
∥v∥∞≤∥v∥2≤∥v∥1≤d⎯⎯√∥v∥2≤d∥v∥∞.
 
Feel free either to prove it, or check it experimentally by running the 
following code.
"""

from math import inf, sqrt

def normalize_vector(v, p=2):
    """Returns a rescaled version of the input vector `v`."""
    v_norm = norm(v, p=p)
    return vector(*[vi/v_norm for vi in v])

# Generate random points whose 2-norm equals 1. Then
# compute the 1-norm and inf-norm of these points.
norms_1 = [None] * 250
norms_inf = [None] * 250
for k in range(len(norms_1)):
    v = normalize_vector(random_vector())
    norms_1[k] = norm(v, p=1)
    norms_inf[k] = norm(v, p=inf)

# shows that inf-norm < 2-norm < 1-norm    
figure(figsize=(6, 6))
new_blank_plot(xlim=None, ylim=None, axis_color=None, title='$\|v\|_2 = 1$')
plt.plot(norms_1, norms_inf, marker='o', markersize=2, linestyle='none')
plt.xlabel('$\|v\|_1$', fontsize=18);
plt.ylabel('$\|v\|_\infty$', fontsize=18);
plt.hlines(y=1/sqrt(2), xmin=1, xmax=sqrt(2), linestyle=':')
plt.vlines(x=sqrt(2), ymin=1/sqrt(2), ymax=1, linestyle=':')
plt.axis('square');



"""
Exercise. Consider all the 2-D vectors whose p-norm equals 1. Place all the
 vectors at the origin, and imagine their endpoints. 
 What shapes do the endpoints sketch out, for  p=1,  p=2, and  p=∞?
 
Hint.
 Start by considering all the 2-D points whose two-norm, or Euclidean distance,
 equals 1. Convince yourself that their endpoints from the origin would all lie
 on a circle of radius 1. What shapes will  p=1 and  p=∞ sketch out?
 
When you have an answer, check it by running the code below. It performs an 
experiment where, for each value of  p∈{1,2,∞}
 , it generates a random point  v
 , normalizes the coordinates of the point by  ∥v∥p
  so that  v/∥v∥p=1
 , and then plots the result.

"""

# the norms are identical for (+-1, 0) and (0, +-1)
# the norms 1-norm < 2-norm < inf-norm...what does this mean?
from math import inf

figure(figsize=(6, 6))
new_blank_plot(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25))

for p, color in zip([1, 2, inf], ['blue', 'green', 'red']):
    print("Points whose {}-norm equals 1 are shown in {}.".format(p, color))
    for _ in range(250):
        v = normalize_vector(random_vector(), p=p)
        # The `p`-norm of `v` is now equal to 1; plot `v`.
        draw_point2d(v, color=color)



"""
Basic operations: scaling, addition, and subtraction
The most elementary operations on vectors involve changing their lengths 
("scaling" them), adding them, and subtracting them.
Let's start with scaling.
Operation: Scaling a vector. Given a vector v
, scaling it by a scalar value σ
 simply multiplies every element of the vector by α
Here is a picture of the scaling operation.

"""

def scale(v, sigma):
    return tuple([sigma*vi for vi in v])

va = vector(3.0, 2.0)
sigma = 0.75
va_scaled = scale(va, sigma)

va_latex = latex_vector(va)
va_scaled_latex = latex_vector(va_scaled)
display_math(r'''(\sigma={}) {} = {}'''.format(sigma, va_latex, va_scaled_latex))

axes = subplots((1, 2))
new_blank_plot(axes[0], xlim=(-1, 3.25), ylim=(-1, 3.25), title='blue')
draw_vector2d(va, color='blue')

new_blank_plot(axes[1], xlim=(-1, 3.25), ylim=(-1, 3.25), title='alpha * blue')
draw_vector2d(va_scaled, color='blue')



"""
Operation: Vector addition. 

Adding two vectors  v and  w
consists of matching and summing component-by-component, also referred to 
as elementwise addition:
    
Geometrically, the act of adding  v and  w is the same as connecting the end 
of v to the start of  w, as illustrated by the following code and picture.

"""

def add(v, w):
    assert len(v) == len(w), "Vectors must have the same length."
    return tuple([vi+wi for vi, wi in zip(v, w)])

vb = vector(-1.5, 1.0)
vc = add(va, vb)

vb_latex = latex_vector(vb)
vc_latex = latex_vector(vc)
display_math('{} + {} = {}'.format(va_latex, vb_latex, vc_latex))

# adding - move the end of one vector to the start of the other!
axes = subplots((1, 3))
new_blank_plot(ax=axes[0], title='blue, red');
draw_vector2d(va, color='blue')
draw_vector2d(vb, color='red')

new_blank_plot(ax=axes[1], title='black = blue + red');
draw_vector2d(va, color='blue')
draw_vector2d(vb, origin=va, color='red', alpha=0.5)
draw_vector2d(vc)

new_blank_plot(ax=axes[2], title='black = red + blue');
draw_vector2d(vb, color='red', alpha=0.5)
draw_vector2d(va, origin=vb, color='blue', alpha=0.5)
draw_vector2d(vc)

"""
In the picture above, there are two vectors, "blue" and "red" (left subplot).
 Adding the red vector to the blue vector ("blue + red") is geometrically 
 equivalent to attaching the start of the red vector to the end of the blue 
 vector (middle subplot). Moreover, since scalar addition is symmetric 
 ( a+b=b+a), so, too, is vector addition (right subplot).

Aside. Observe that our visualizations "exploit" the fact that vectors only .
have lengths and directions, not positions, so that vector addition becomes a 
symmetric operation.
"""

"""
Negation and subtraction. Subtracting two vectors is also done elementwise. 
Alternatively, one may view  v−w as  v+(−w), that is, first scaling  w by -1 
and then adding it to  v, which is what the code below implements.
"""

def neg(v):
    return tuple([-vi for vi in v])

def sub(v, w):
    return add(v, neg(w))

vd = sub(va, vb)

vd_latex = latex_vector(vd)
display_math('{} + {} = {}'.format(va_latex, vb_latex, vd_latex))

axes = subplots((1, 2))
new_blank_plot(ax=axes[0], title='blue, green');
draw_vector2d(va, color='blue')
draw_vector2d(vb, color='green')

new_blank_plot(ax=axes[1], title='black = blue - green');
draw_vector2d(va, color='blue')
draw_vector2d(neg(vb), origin=va, color='green', alpha=0.5)
draw_vector2d(vd)

"""
As the visualization indicates, scaling by -1 makes the vector point in the
 opposite direction.
Lastly, observe that scaling and addition––e.g., σv+w
––combine as expected.
"""

ve = add(va_scaled, vb)

ve_latex = latex_vector(ve)
display_math(r'''{} {} + {} = {}'''.format(sigma, va_latex, vb_latex, ve_latex))

axes = subplots((1, 3))
new_blank_plot(axes[0], title='blue, red')
draw_vector2d(va, color='blue')
draw_vector2d(vb, color='red')

new_blank_plot(axes[1], title='sigma * blue')
draw_vector2d(va_scaled, color='blue', alpha=0.5)

new_blank_plot(axes[2], title='black = sigma*blue + red')
draw_vector2d(va_scaled, color='blue', alpha=0.5)
draw_vector2d(vb, origin=va_scaled, color='red', alpha=0.5)
draw_vector2d(ve)



"""
Dot (or "inner") products
Another critically important operation on vectors is the dot product.

Definition. The dot product (or inner product) between two  d-dimensional 
vectors,  u and  w, will be denoted by  ⟨u,w⟩
  and defined as follows:
⟨u,w⟩ ≡ u0w0+⋯+ud−1wd−1 = ∑i=0d−1uiwi .
 
That is, take  u and  w, compute their elementwise products, and then sum 
these products.

Observation. The result of a dot product is a single number, i.e., a scalar.
Here is a Python implementation, followed by an example.

"""
# dot product is the sum of the element wise products between two vectors
def dot(u, w):
    return sum([ui*wi for ui, wi in zip(u, w)])

u = (1, 2.5)
w = (3.25, 1.75)

display_math('u = ' + latex_vector(u))
display_math('w = ' + latex_vector(w))
u_dot_w_sum_long_latex = '+'.join([r'({}\cdot{})'.format(ui, wi) for ui, wi in zip(u, w)])
display_math(r'\langle u, w \rangle = ' + u_dot_w_sum_long_latex + ' = ' + str(dot(u, w)))


"""
There is another commonly used notation for the dot product, which we will use
 extensively when working with matrices. It requires the concept of a row 
 vector.
 
Definition: row vectors and (vector) transposes. 

Recall that we used the term column with vectors and drew a vector as a 
vertical stack. As the very term "column" suggests, there is also a concept of 
a row vector. It will become important to distinguish between row and column 
vectors when we discuss matrices.

In this class, the convention we will try to use is that a vector is a column
 vector unless otherwise specified; and when we need a "row" version of  v
 , we will use the operation called the transpose to get it from the (column)
 version, denoted as vT≡[v0,v1,…,vd−1].
 
 """
 
 # row vector is a transpose of a column vector
 display_math('v^T = ' + latex_vector(v, transpose=True))



""" 
Notation: vector transpose form of the dot product. Armed with the notions of 
both row and column vectors, here is an alternative way we will define a dot 
product:
⟨u,v⟩≡uTw ≡ [u0,…,ud−1]⋅w0⋮wd−1.
 
That is, given two (column) vectors  u and  w, the dot product is the sum of 
the elementwise products between the transpose of  u and  v. We read  uTw as 
u -transpose times  v.
"""
 
u_dot_w_vec_latex = latex_vector(u, transpose=True) + r' \cdot ' + latex_vector(w)
display_math(r'\langle u, w \rangle = u^T w = ' + u_dot_w_vec_latex + ' = ' + u_dot_w_sum_long_latex + ' = ' + str(dot(u, w)))

"""

Exercise. Write some code to verify, using some examples, that 
 ⟨u,u⟩=uTu=∥u∥22. In other words, the dot product of a vector with itself is 
 the two-norm of that vector, squared.
 
"""

u = (1.0, 2.5)

dot_u = dot(u, u)
norm2_u = norm(u, p = 2)
dot_u == norm2_u * norm2_u
(dot_u, norm2_u*norm2_u)



"""
A geometric interpretation of the dot product
Here is another important fact about the dot product that, later on, will help
 us interpret it.
 
Fact.  uTw=∥u∥2∥w∥2cosθ
 , where  θ
  is the angle between  u
  and  w
 .
To see this fact, consider the following diagram.


"""

def radians_to_degrees(radians):
    from math import pi
    return radians * (180.0 / pi)

def get_angle_degrees(point):
    assert len(point) == 2, "Point must be 2-D."
    from math import pi, atan2
    return radians_to_degrees(atan2(point[1], point[0]))

figure((6, 6))
new_blank_plot(xlim=(-0.5, 4), ylim=(-0.5, 4));

draw_vector2d(u, color='blue', width=0.05)
plt.text(u[0], u[1], '$(u_x, u_y) = ({}, {})$'.format(u[0], u[1]), color='blue',
         horizontalalignment='center', verticalalignment='bottom', fontsize=14)
draw_vector2d(w, color='green', width=0.05)
plt.text(w[0], w[1], '$(w_x, w_y) = ({}, {})$'.format(w[0], w[1]), color='green',
         horizontalalignment='center', verticalalignment='bottom', fontsize=14)

draw_vector2d_components(u, y_offset_sign=1, color='blue', linestyle='dashed')
draw_vector2d_components(w, y_offset_sign=-1, color='green', linestyle='dashed')

phi_degrees = get_angle_degrees(w)
theta_degrees = get_angle_degrees(u) - phi_degrees
draw_angle(0, phi_degrees, radius=1.5, color='green')
draw_angle_label(0, phi_degrees, r'$\phi$', radius=1.6, color='green', fontsize=18)
draw_angle(phi_degrees, phi_degrees+theta_degrees, radius=2, color='blue')
draw_angle_label(phi_degrees, phi_degrees+theta_degrees, r'$\theta$', radius=2.1, color='blue', fontsize=18)


"""
Exercise. 

Let  u=[uxuy]and  w=[wxwy]. The vector  u is shown as the blue line and  w
  as the green line in the figure above. 
  Let  ϕ be the angle that  w makes with the x-axis, and let  θ be the angle
  between  u and  w. 
  
  Using trigonometric identities from elementary geometry, prove that 
 uTw=∥u∥2∥w∥2cosθ

Hint. Here is one way to start: observe that, for instance,  wy=∥w∥2sinϕ and
ux=∥u∥2cos(θ+ϕ), and then apply one or more trigonometric identities as needed.
 
 """


"""
Interpretation. So what does the dot product mean? One can interpret it as a 
"strength of association" between the two vectors, similar to statistical 
correlation. 

To see why, observe that the dot product accounts for both the lengths of the
 vectors and their relative orientation.

The vector lengths are captured by the product of their lengths (∥u∥2∥w∥2). 
The longer the vectors are, the larger the product of their lengths, ∥u∥2∥w∥2.

 If you know only the lengths of the vectors, their dot product can never be
 larger than this product.

The relative orientation is captured by  cosθ. That factor moderates the 
maximum possible value. In particular, if the two vectors point in exactly 
the same direction, meaning  θ=0, then  cosθ=1 and the dot product is exactly
 the maximum,  ∥u∥2∥w∥2. 
 
 If instead the vectors point in opposite directions, meaning  θ=π radians=180∘,
 then  cosθ=−1 and the dot product is  −∥u∥2∥w∥2. For any other values of  θ 
 between  0 and  2π radians (or  360∘),  |cosθ|<1 so that  |uTw|<∥u∥2∥w∥2.
 
In the context of data analysis, the analogous measurement to  cosθ
is the Pearson correlation coefficient. Each vector would represent a 
regression line that goes through some sample of points, with  cosθ
  measuing the angle between the two regression lines. The diagram above 
  gives you a geometric way to think about such correlations.

"""






"""
Linear transformations
The basic operations we considered above take one or more vectors as input and transform them in some way. In this part of the notebook, we examine what is arguably the most important general class of transformations, which are known as linear transformations. Before doign so, let's start with some auxiliary concepts.
Definition: vector-valued functions (also, vector functions). Let f(v)
 be a function that takes as input any vector v
 and returns another vector. Because f
 returns a vector, we will sometimes refer to it as a vector-valued function or just vector function for short.
Note that the input and output vectors of f
 need not have the same lengths!
Example: scaleα(v)
. Scaling is a simple example of a vector function. If we name this function scale
 and parameterize it by the scaling coefficient α
, then we might write it down mathematically as
scaleα(v)≡αv.
So,
scale1.25(v)=1.25v0⋮vd−1=1.25v0⋮1.25vd−1.

The code implementation would look identical to the Python scale() we defined previously.


Example: avgpairs(v) Let v be a vector whose length, d, is even. Here is a vector function that returns a new vector of half the 
length, where elements of the new vector are the averages of adjacent pairs of v:
avgpairs(v)≡12(v0+v1)12(v2+v3)⋮12(vd−2+vd−1).


Exercise. Write a Python function that implements avgpairs(v).

"""


# Sample solution; how would you have done it?
def avgpairs(v):
    assert dim(v) % 2 == 0, "Input vector `v` must be of even dimension."
    v_pairs = zip(v[:-1:2], v[1::2])
    v_avg = [0.5*(ve + vo) for ve, vo in v_pairs]
    return vector(*v_avg)

v_pairs = vector(1, 2, 3, 4, 5, 6, 7, 8)
print(v_pairs, "=>", avgpairs(v_pairs))



"""
Definition: linear functions (or linear transformations). A function  f(v)
  is a linear transformation if it satisfies the following two properties:
f(σv)=σf(v)
 , where  σ
  is a scalar value.
f(v+w)=f(v)+f(w).

The first property says that  f
  applied to a scaled vector is the same as first applying  f
  to the vector and scaling the result. The second property says that  f
  applied to the sum of two vectors is the same as first applying  f
  to the individual vectors and then adding the result.
When combined, these properties are equivalent to the more concise statement that  f(σv+w)=σf(v)+f(w)
 .
Exercise.

 The function scaleα(v)
 is a linear transformation––true or false?
Answer. This statement is true:
Property 1: scaleα(σv)=α(σv)=σ(αv)=σscaleα(v).
Property 2: scaleα(v+w)=α(v+w)=αv+αw=scaleα(v)+scaleα(w).
To see this fact in action, run the following experiment.

"""

DEFAULT_ALPHA = 1.25
def scale_alpha(v, alpha=DEFAULT_ALPHA):
    return scale(v, alpha)

def latex_scale_alpha(x, alpha=DEFAULT_ALPHA):
    return r'\mathrm{{scale}}_{{{}}}\left( {} \right)'.format(alpha, x)

display_math(r'''{} \equiv {} \cdot {}'''.format(latex_scale_alpha('x'), DEFAULT_ALPHA, 'x'))


# f(ve) where ve = sigma*va + vb
u0 = scale_alpha(ve)

u0_latex = latex_vector(u0)
arg_str = r'{} {} + {}'.format(sigma, va_latex, vb_latex)
lhs_str = latex_scale_alpha(arg_str)
arg2_str = ve_latex
mid_str = latex_scale_alpha(arg2_str)
rhs_str = u0_latex
display_math(r'u_0 \equiv {} = {} = {}'.format(lhs_str, mid_str, rhs_str))

axes = subplots((1, 2))
new_blank_plot(axes[0], title='black = sigma*blue + red')
draw_vector2d(va_scaled, color='blue', alpha=0.5)
draw_vector2d(vb, origin=va_scaled, color='red', alpha=0.5)
draw_vector2d(ve)

new_blank_plot(axes[1], title='f(black)')
draw_vector2d(scale_alpha(ve))


display_math(r'''\frac{{{}}}{{{}}} = {}'''.format(latex_norm(rhs_str),
                                                  latex_norm(arg_str),
                                                  norm(u0) / norm(ve)))

# sigma*f(va) + f(vb)
u1_a = scale_alpha(va)
u1_aa = scale(u1_a, sigma)
u1_b = scale_alpha(vb)
u1 = add(u1_aa, u1_b)

display_math(r'''u_1 \equiv {} \cdot {} + {} = {}'''.format(sigma,
                                                            latex_scale_alpha(va_latex),
                                                            latex_scale_alpha(vb_latex),
                                                            latex_vector(u1)))

_, axes = plt.subplots(1, 4, figsize=(19, 4), sharey='row')

new_blank_plot(axes[0], title='blue, red')
draw_vector2d(va, color='blue')
draw_vector2d(vb, color='red')

new_blank_plot(axes[1], title='f(blue), f(red)')
draw_vector2d(u1_a, color='blue')
draw_vector2d(u1_b, color='red')

new_blank_plot(axes[2], title='sigma * f(blue)')
draw_vector2d(u1_aa, color='blue')

new_blank_plot(axes[3], title='black = sigma*f(blue) + f(red)')
draw_vector2d(u1_aa, color='blue', alpha=0.5)
draw_vector2d(u1_b, origin=u1_aa, color='red', alpha=0.5)
draw_vector2d(u1)


# is norm(v) a linear transformation - looks like YES!
scalar_a = 5.0
v = (1.0, 3.0)
norm(v, 2)
scalar_a*norm(v, 2)
norm((y*scalar_a for y in v), 2)


# is offsetg(v) a linear transformation? - looks like...NO!
def offset(v, g):
    offset = list(y+g for y in v)
    return offset

scalar_b = 10.0
v = (1.0, 3.0)
g = 5.0
offset = offset(v, g = 5.0)
list(scalar_b * x for x in offset)


"""
Exercise. Suppose we are operating in a two-dimensional space. Let
rotateθ(v)≡[v0cosθ−v1sinθv0sinθ+v1cosθ].
 
Is  rotateθ(v)
  a linear transformation?
While, after, or instead of pondering the answer for  rotateθ, here is some 
code to visualize its effects. (This code selects a rotation angle at random, 
so you run it repeatedly to see the effects under different angles.)

"""


def random_angle(min_angle=0, max_angle=None):
    """
    Returns a random angle in the specified interval
    or (0, pi) if no interval is given.
    """
    from math import pi
    from random import uniform
    if max_angle is None: max_angle = pi
    return uniform(0, max_angle)

def rotate(v, theta=0):
    from math import cos, sin
    assert dim(v) == 2, "Input vector must be 2-D."
    return vector(v[0]*cos(theta) - v[1]*sin(theta),
                  v[0]*sin(theta) + v[1]*cos(theta))

v_rand = normalize_vector(random_vector())
theta_rand = random_angle()
w_rand = rotate(v_rand, theta_rand)

figure()
new_blank_plot(xlim=(-1, 1), ylim=(-1, 1),
               title=r'black = rotate blue by $\approx${:.0f}$^\circ$ counterclockwise'.format(radians_to_degrees(theta_rand)))
draw_vector2d(v_rand, color='blue', width=0.05)
draw_vector2d(w_rand, color='black', width=0.05)





"""
Linear transformations using matrices
If  f
  is a linear transformation, then  f(αv+βw)=αf(v)+βf(w)
 . In fact, the reverse is also true: if  f(αv+βw)=αf(v)+βf(w)
 , then  f
  must be a linear transformation. Refer to the LAFF notes for a formal proof of this fact.
Here is one immediate consequence of this fact. Suppose you have n
 vectors, named v0
, v1
, \ldots, vn−1
. Here, vi
 is the name of a vector, rather than an element of a vector; the components of vi
 would be v0,i,v1,i,…
. Let's also suppose you have n
scalars, named α0,α1,…,αn−1
. Then,
f(α0v0+α1v1+⋯+αn−1vn−1)=α0f(v0)+α1f(v1)+⋯+αn−1f(vn−1).
This fact makes f
 very special because it allows you to figure out the effect of f
 if you are allowed to "sample" it on particular values of vi
. For example, suppose f(v)
 operates on two-dimensional vectors and returns two-dimensional vectors as a result.
Exercise. Let f(v)
 be a linear transformation on two-dimensional vectors v
. Suppose you are told that
f([10])f([01])==[35][−12].
Determine f([2−4])
Answer. Start by observing that
[2−4]=2[10]−4[01].
Since f
f
 is a linear transformation,
f([2−4])=f(2[10]−4[01])=2f([10])−4f([01])=2[35]−4[−12]=[2⋅3−4⋅(−1)2⋅5−4⋅2]=[102].
Canonical axis vectors. In the preceding example, you were given samples of f
f
 on two very special vectors, namely, a distinct set of perpendicular unit vectors having a "1" in just one component of the vector. Let's denote these special vectors by ej
e
j
 where, in a d
d
-dimensional space,
ej≡0⋮010⋮0←0-th component←j-th component←(d−1)-th component
We'll refer to these as the canonical axis vectors.
In the LAFF notes, these are called the unit basis vectors, which is more standard terminology in the linear algebra literature.

"""

"""
Matrix representations. Any vector may be written in terms of these canonical axis vectors.
v=v0⋮vd−1=v01⋮0+⋯+vd−10⋮1=v0e0+⋯+vd−1ed−1=∑j=0d−1vjej.

Therefore, consider any linear transformation, f
f
. If you are given samples of f
f
 along all axes, {xj≡f(ej)}
, then that is enough to calculate f
 for any vector v
f(v)=f∑j=0d−1vjej=∑j=0d−1vjf(ej)=∑j=0d−1vjxj.

Let's suppose v
v
 is n-dimensional. Therefore, there are n canonical axis vectors. If the 
 result of f(v) is m-dimensional, then each of the xj vectors is also m dimensional. Therefore, we can write each xj asxj=x0,j⋮xm−1,j.
A convenient way to represent the full collection of all n of the xj
 vectors is in the form of a matrix, where each column corresponds to one of these xj
 vectors:
X=[x0⋯xn−1]=x0,0⋮xm−1,0⋯⋱⋯x0,n−1⋮xm−1,n−1.
Aside: Specifying the dimensions of a matrix. Similar to the way we "declare" a vector v
 to have dimension d by writing v∈ℝd
, we have a similar notation to specify that a matrix has dimensions of, say, m-by-n
: we write X∈ℝm×n
Example. Recall the previous example where
f([10])=[35]andf([01])=[−12].
What is the matrix X that represents f?
Answer. We were given fat the canonical axis vectors, which then become the columns of the corresponding matrix.
X=[35−12].

"""


"""
A code representation. In this course, you will see many ways of representing
 matrices and vectors. For the purpose of this notebook, let's store a 
 matrix as a tuple of (column) vectors. Here is a Python function, 
 matrix(x0, x1, ...), where each argument is a column vector, that stores the
 columns in a tuple.
"""

def matrix(*cols):
    if len(cols) > 2:
        a_cols = cols[:-1]
        b_cols = cols[1:]
        for k, (a, b) in enumerate(zip(a_cols, b_cols)):
            assert dim(a) == dim(b), \
                   "Columns {} and {} have different lengths ({} vs. {})".format(k, k+1, dim(a), dim(b))
    return tuple(cols)

def num_cols(X):
    return len(X)

def num_rows(X):
    return dim(X[0]) if num_cols(X) >= 1 else 0

# Demo
X = matrix(vector(3, 5), vector(-1, 2))
print("X =", X)


def matelem(X, row, col):
    assert col < dim(X), "Column {} is invalid (matrix only has {} columns).".format(col, dim(X))
    x_j = X[col]
    assert row < dim(x_j), "Row {} is invalid (matrix only has {} rows).".format(row, dim(x_j))
    return x_j[row]

def latex_matrix(X):
    m, n = num_rows(X), num_cols(X)
    s = r'\left[\begin{matrix}'
    for i in range(m):
        if i > 0: s += r' \\' # New row
        for j in range(n):
            if j > 0: s += ' & '
            s += str(matelem(X, i, j))
    s += r' \end{matrix}\right]'
    return s

X_latex = latex_matrix(X)
display_math('X = ' + X_latex)





"""

Definition: matrix-vector product (matrix-vector multiply). Let's define the matrix-vector product (or matrix-vector multiply) as follows.
Given an  m
 -by- n
  matrix  X
  and a vector  v
  of length  n
 , the matrix-vector product is given by
Xv=[x0⋯xn−1]v0⋮vn−1=x0v0+⋯+xn−1vn−1.
 
With this notation, a linear transformation f
 represented by X
 may be written as f(v)=Xv
We will sometimes write the matrix vector product with an explicit "dot" operator, X⋅v
his usage is arbitrary and we will use it for aesthetic reasons only.
Linear combination. The action of a matrix-vector product is to use the entries of v to scale the corresponding columns of X
followed by a sum of the resulting scaled vectors. We say that Xv is a linear combination of the columns of X. The "coefficients" or "weights" of this linear combination are the elements of v
Example. Continuing the example above, calculate f([2,−4]T)
 using X.
Answer. We can apply the matrix-vector product:
[35−12][2−4]=2[35]−4[−12],
[3	−1	5	2 ],
which is the same result as before.


Here is a Python code implementation of the matrix-vector product. 
Take a moment to verify that you understand how it works.

"""

def matvec(X, v):
    assert dim(X) == dim(v), "Matrix and vector have mismatching shapes."
    w = [0] * num_rows(X)
    for x_j, v_j in zip(X, v):
        w = add(w, scale(x_j, v_j))
    return w

v = vector(2, -4)
w = matvec(X, v)
X
w

v_latex = latex_vector(v)
w_latex = latex_vector(w)
display_math('X v = ' + X_latex + v_latex + ' = ' + w_latex)

s = '10a.c'

if '.' not in  s and s.isalpha() == False:
    print(s)




for i in str('af'):
    print(i)


vals = []

for i, j in list(enumerate(reversed(s))):
    if j.isalpha() == True:
        name = str(digit_dict[j])
        vals.append(int(name * (base**i)))
    else:
        val = vals.append(int(j) * (base**i))































