#!/usr/bin/env python
# coding: utf-8

# # Hydraulics and Overflow
# 
# In Wikipedia, the definition of [hydraulics](https://en.wikipedia.org/wiki/Hydraulics) (from Greek: Υδραυλική) is a technology and applied science using engineering, chemistry, and other sciences involving the mechanical properties and use of liquids. But 
# > what do geophysicists mean when they talk about hydraulics and why should one listen? - Pratt and Whithead (2008)
# 
# For me, I speak the ability of topography (ocean passages and straits) that renders waves to be significant enough to interact with flow, eventually regulate the flow structure as well as volume flux. 
# 
# Watch the below video: 
# 
# [![hydraulics in a tank](https://img.youtube.com/vi/nX6aemsdFIo/0.jpg)](https://www.youtube.com/watch?v=nX6aemsdFIo "hydraulics in a tank")

# ## Hydraulic Control
# 
# As it is markdown, you can embed images, HTML, etc into your posts!
# 
# ### Theory
# 
# ![Animations by Kraaiennest, Wikimedia Commons, Creative Commons A S-A 3.0, http://commons.wikimedia.org/wiki/File:Deep_water_wave.gif and http://commons.wikimedia.org/wiki/File:Shallow_water_wave.gif](Shallow_water_wave.gif "Shallow Water Wave")
# 
# ![Animations by Kraaiennest, Wikimedia Commons, Creative Commons A S-A 3.0, http://commons.wikimedia.org/wiki/File:Deep_water_wave.gif and http://commons.wikimedia.org/wiki/File:Shallow_water_wave.gif](Deep_water_wave.gif "Deep Water Wave")
# 
# ### Overflow applications
# 
# 
# 
# 
# You can also $add_{math}$ and
# 
# $$
# math^{blocks}
# $$
# 
# or
# 
# $$
# \begin{aligned}
# \mbox{mean} la_{tex} \\ \\
# math blocks
# \end{aligned}
# $$
# 
# But make sure you \$Escape \$your \$dollar signs \$you want to keep!
# 
# 

# ## Hydraulic Jump
# 
# MyST markdown works in Jupyter Notebooks as well. For more information about MyST markdown, check
# out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html),
# or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# 

# In[1]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


# In[2]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)

# In[ ]:





# ## To ease your burning curiosity
# contact me! shuwent@ldeo.columbia.edu
# - for the pdf of materials
# - to join my annual to decadal time scale book reading group
# 
# ### Books
# [**Rotating Hydraulics \- Nonlinear Topographic Effects in the Ocean and Atmosphere** by Pratt and Whithead](https://www2.whoi.edu/staff/lpratt/textbook-on-rotating-hydraulics/) <br /> - for hydraulics overview and ocean application: *[Introduction](https://www2.whoi.edu/staff/lpratt/wp-content/uploads/sites/120/2019/06/PrattIntroFigsI1-I2_78844.pdf)*, *[section 2.14](https://www2.whoi.edu/staff/lpratt/wp-content/uploads/sites/120/2019/07/PrattSec2.14_11964.pdf)* <br /> - for the essence of hydraulics (wave \& flow): *section 1.1-1.4*
# <br />
# [**Bottom Gravity Currents and Overflows in Deep Channels of the Atlantic Ocean** by Morozov et al.](https://link.springer.com/book/10.1007/978-3-030-83074-8) <br /> - for a comprehensive review of ocean passages/straits and overflow
# <br />
# [**Linear and Nonlinear Waves** by Whitham](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118032954) <br /> - for those who wants to look into the math behind waves and hydraulics
# <br /> 
# [**Topographic Effects in Stratified Flows** by Baines](https://assets.cambridge.org/97811084/81526/frontmatter/9781108481526_frontmatter.pdf) <br /> - a challenging book to read, no pdf, but I have a hard copy you can borrow from
# 
# ### Papers
# [**Turbulent mixing and hydraulic control of abyssal water in the Samoan Passage** by Alford et al.](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/grl.50684) <br /> - hydraulic control and jump found in Samoan Passage <br /> 
# [**Modelling the Föhn in the MIM Laboratory** by Josef Schröttle](https://minigcm.org/ba.pdf) <br /> - undergrad thesis, great review on hydraulics
# <br />
# [**Hydraulic Jump: A Brief History and Research Challenges** by De Padova and Mossa](https://www.mdpi.com/2073-4441/13/13/1733) <br /> - for a brief history of hydraulic jump, from engineering perspectives
# 
# ### Videos!
# [National Committee for Fluid Mechanics Films (NCFMF)](http://web.mit.edu/hml/ncfmf.html) (strongly recommended for anyone who are interested in fluid mechanics, art \& masterpiece) <br /> - for waves \& hydraulics [Stratified Flow](https://www.youtube.com/watch?v=9hmjcIfy8wE&list=PL0EC6527BE871ABA3&index=19), you will see the famous **[Robert Long](https://onlinebooks.library.upenn.edu/webbin/book/lookupname?key=Daugherty%2C%20Robert%20L%2E%20%28Robert%20Long%29%2C%201885%2D)'s towing experiment**!

# In[ ]:




