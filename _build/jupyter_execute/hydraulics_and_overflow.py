#!/usr/bin/env python
# coding: utf-8

# # Overflow and Hydraulics

# ## Overflow - they are everywhere!

# Not only a toilet can overflow! A *memory overflow* error can ruin a programmer's morning; 21st century homosapiens deal with *information overflow* every single day; a river can overflow its banks and/or dams and cause flooding; etc. When we talk about overflow, the hidden subject we actually talk about is a constraint, which regulates the flow (**hydraulic control**). When the overflow goes beyond the capacity of the constraint, influences on the upstream reservoir (**upstream influence**) and chaos downstream (**hydraulic jump**) arise.
# 
# Think about a perfect semester: you learn something at school, you discuss it with your professor and classmates, you spend the right amount of time working on your assignments, and most importantly, you digest the knowledge along the way, and do not feel overwhelmed or burnout. You feel comfortable and feel that you've learned something. That's how a constraint can regulate a flow without causing chaos (weakly nonlinear). 
# > hydraulic control
# 
# As you feel the course load becomes too heavy on you, you talk to the professor and your classmates. The professor receives feedback from the class and adjusts the courses accordingly and offer help. That's how a constraint can influence the upstream condition. 
# > upstream influence
# 
# In another scenario, you bite off more than you can chew and refuse to talk to anyone. You may feel overwhelmed, meltdown, or burnout. It's not healthy nor safe cause that really stirred up chaos downstream (strongly nonlinear). Fortunately, by sending information upstream and changing the upstream condition, you can restore your status and regain the regularity of life.
# > hydraulic jump
# 
# 
# <div style="text-align: right"> *Disclaimer: Above are my not-that-great analogies and may not reflect the actual physics. </div>

# ## Hydraulics - a zoo of nonlinear topographic effects

# <!-- From Wikipedia, the word "[hydraulics](https://en.wikipedia.org/wiki/Hydraulics)" originates from the Greek word: ὑδραυλικός (hydraulikos), with its first part ὕδωρ (hydor) meaning water and the second part αὐλός (aulos) meaning pipe. It somewhat speaks the essence of hydraulics, which requires a moving fluid (through a pipe, over a dam, etc.) and thus is different from hydrostatics. When a fluid moves, especailly over topography, transformation may occur between kinetic energy and potential energy (may also between interal energy/heat when friction/viscosity is involved), which renders rich and exciting physical phenomena. In this lecture, we will discuss two classic hydraulic phenomena: **hydraulic control** and **hydraulic jump**.
# 
# <figure>
#     <a title="See page for author, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Table_of_Hydraulics_and_Hydrostatics,_Cyclopaedia,_Volume_1.jpg"><img width="280" alt="Hydraulic and Hydrostatic" src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Table_of_Hydraulics_and_Hydrostatics%2C_Cyclopaedia%2C_Volume_1.jpg"></a>
#     <figcaption>Hydraulic and Hydrostatic, See page for author, Public domain, via Wikimedia Commons.</figcaption>
# </figure>
#  -->
#  
# Watch the below video and notice how the water moves:
# 
# [![hydraulics in a tank](https://img.youtube.com/vi/nX6aemsdFIo/0.jpg)](https://www.youtube.com/watch?v=nX6aemsdFIo "hydraulics in a tank")
# 
# I hope you noticed the water level shows asymmetry: high on the left of the obstacle and low on the right of the obstacle. Or maybe you even noticed the ping pong ball moves very slowly on the left of the obstacle and cascades down as it crosses the obstacle. You may also notice the "boiling" waters further downstream where the Pingpang ball gets trapped and rolls. Then congratulations, you have identified some of the most important hydraulic phenomena:
# - the flow is **hydraulically controlled** by topography
# - the flow transfer from **subcritical** to **critical** to **supercritical** as it crosses the obstacle crest
# - at the base of the spillway is a **hydraulic jump**, an abrupt increase in the fluid depth accompanied by intense turbulence
# 

# But 
# > what do geophysicists mean when they talk about hydraulics and why should one listen? - Pratt and Whithead (2008)
# 
# - the ocean moves and the seabed is not flat: passages, channels, straits, ...
# - topography blocks the densest water from entering the next basin, draws down the interface level, causes "mixing hotspot" downstream, ..., an important chain in the Meridional Overturning Circulation.
# <!-- "controls" the volume flow rate and the reservoir level -->
# 
# ```{figure} hydraulics/vertical-movement-of-water-along-a-north-south-cross-section.png
# ---
# width: 600
# name: directive-fig
# ---
# Fig. 18.4.8 in [Earle and Panchuk (2019)](https://opentextbc.ca/physicalgeology2ed/): Schematics of major ocean masses, the ocean bottom in the schematics is flat, which is not true.
# ```
# 
# ```{figure} hydraulics/Fig1_Bryden_Nurser2003.png
# ---
# width: 600
# name: directive-fig
# ---
# Fig. 1 in [Bryden and Nurser (2003)](https://journals.ametsoc.org/view/journals/phoc/33/8/1520-0485_2003_033_1870_eosmoo_2.0.co_2.xml): Schematic model for the effects of strait mixing on the properties of bottom water, notice that basins are divided by ridges and connected by passages.  
# ```
# 
# <!-- <figure>
#     <a title="Fig. 18.4.8 in Earle and Panchuk (2019)" href="https://opentextbc.ca/physicalgeology2ed/"><img width="480" alt="Flat bottom ocean not true" src="https://opentextbc.ca/physicalgeology2ed/wp-content/uploads/sites/298/2019/08/vertical-movement-of-water-along-a-north-south-cross-section.png"></a>
#     <figcaption>Fig. 18.4.8 in Earle and Panchuk (2019): Schematics of major ocean masses, the ocean bottom in the schematics is flat, which is not true.  </figcaption>
# </figure> -->
# 
# <!-- <figure>
#     <a title="Fig. 1 in Bryden and Nurser (2003)" href="https://journals.ametsoc.org/view/journals/phoc/33/8/1520-0485_2003_033_1870_eosmoo_2.0.co_2.xml"><img width="480" alt="Ocean basins divided by straits" src="hydraulics/Fig1_Bryden_Nurser2003.png"></a>
#     <figcaption>Fig. 1 in Bryden and Nurser (2003): Schematic model for the effects of strait mixing on the properties of bottom water. </figcaption>
# </figure> -->
# 

# <!-- ![fishy](hydraulics/Fr1.gif) -->

# <!-- ![Fr=1 illustration by Dr. Mirjam S. Glessmer](hydraulics/Fr1.gif)
# 
# <figure>
#     <a title="Fr=1 illustration by Dr. Mirjam S. Glessmer" href="https://mirjamglessmer.com/tag/hydraulic-jump/"><img width="480" alt="Fr = 1" src=hydraulics/Fr1.gif></a>
#     <figcaption>Fr=1 illustration by Dr. Mirjam S. Glessmer. </figcaption>
# </figure> -->

# ### 1. Hydraulic Control
# 
# #### 1) Theory
# 
# ##### i) Shallow water waves
# 
# ```{figure} hydraulics/sand_wave_Guam_vertical.jpg
# ---
# width: 300
# name: directive-fig
# ---
# Sand Ripples by S.Tan, Alupang Beach Tower, Guam. As the bottom water particals contain much momentum for shallow water waves, they can move the sands back and forth and leave the "footprint" of waves.
# 
# ```
# 
# ```{figure} hydraulics/Shallow_water_wave.gif
# ---
# width: 600
# name: directive-fig
# ---
# Shallow Water Wave, Animations by Kraaiennest, [Wikimedia Commons, Creative Commons A S-A 3.0](http://commons.wikimedia.org/wiki/File:Shallow_water_wave.gif).
# 
# ```
# 
# ```{figure} hydraulics/Deep_water_wave.gif
# ---
# width: 600
# name: directive-fig
# ---
# Deep Water Wave, Animations by Kraaiennest, [Wikimedia Commons, Creative Commons A S-A 3.0](http://commons.wikimedia.org/wiki/File:Deep_water_wave.gif).
# 
# ```
# 
# <!-- <figure>
#     <img src="hydraulics/sand_wave_Guam_vertical.jpg" 
#          width="400" 
#          alt="">
#     <figcaption>Sand Ripples by S.Tan, Alupang Beach Tower, Guam.</figcaption>
# </figure>
#  -->
# 
# <!-- <figure>
#     <img src="hydraulics/Shallow_water_wave.gif" 
#          width="400" 
#          alt="">
#     <figcaption>Shallow Water Wave, Animations by Kraaiennest, Wikimedia Commons, Creative Commons A S-A 3.0, http://commons.wikimedia.org/wiki/File:Deep_water_wave.gif and http://commons.wikimedia.org/wiki/File:Shallow_water_wave.gif.</figcaption>
# </figure>
# 
# <figure>
#     <img src="hydraulics/Deep_water_wave.gif" 
#          width="400" 
#          alt="">
#     <figcaption>Deep Water Wave, Animations by Kraaiennest, Wikimedia Commons, Creative Commons A S-A 3.0, http://commons.wikimedia.org/wiki/File:Deep_water_wave.gif and http://commons.wikimedia.org/wiki/File:Shallow_water_wave.gif.</figcaption>
# </figure> -->
# 
# Shallow water wave speed
# 
# $$
# c=\sqrt{gH}
# $$
# 
# ##### ii) Who is faster, the currents or the waves? 
# 
# 
# <!-- <figure>
#     <video width="480" controls src="hydraulics/Froude_dude.mov">animation</video>
#     <figcaption>From Australian Water School “Webinar: Froude, Dude!” https://awschool.com.au/training/webinar-froude-dude/</figcaption>
# </figure> -->
# 
# <!-- <a title="See page for author, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Williams_Froude.jpeg"><img width="128" alt="Williams Froude" src="https://upload.wikimedia.org/wikipedia/commons/6/64/Williams_Froude.jpeg"></a> -->
# 
# $$
# \text{Froude Number}: F_r = \frac{\text{wave speed}}{\text{flow speed}}
# $$
# 
# ```{figure} hydraulics/Fr1.gif
# ---
# width: 600
# name: directive-fig
# ---
# Fr=1 illustration by [Dr. Mirjam S. Glessmer](https://mirjamglessmer.com/tag/hydraulic-jump/).
# ```
# 
# <!-- <figure>
#     <a title="Fr=1 illustration by Dr. Mirjam S. Glessmer" href="https://mirjamglessmer.com/tag/hydraulic-jump/"><img width="480" alt="Fr = 1" src=hydraulics/Fr1.gif></a>
#     <figcaption>Fr=1 illustration by Dr. Mirjam S. Glessmer. </figcaption>
# </figure> -->
# 
# ##### iii) Subcritical, critical, supercritical
# 
# ```{figure} hydraulics/hydraulic_transition.png
# ---
# width: 900
# name: directive-fig
# ---
# Hydraulic transition from subcritical to critical to supercritical at the sill, from supercritical to subcritical crossing the dissipative hydraulic jump. At the critical section, $F_r$=1, the wave is stationary. 
# ```
# 
# <!-- <figure>
#     <img width="960" alt="hydraulic transition from subcritical to critical to supercritical" src="hydraulics/hydraulic_transition.png">
#     <figcaption>Hydraulic transition from subcritical to critical to supercritical at the sill, from supercritical to subcritical crossing the dissipative hydraulic jump. </figcaption>
# </figure> -->
# 
# [![hydraulics in a tank](hydraulics/Weir_Pinnau_2016_Slide4.jpeg)](https://vimeo.com/152074901 "Hydraulic control illustration by Dr. Mirjam S. Glessmer")
# 
# <!-- <figure>
#     <a title="Hydraulic control illustration by Dr. Mirjam S. Glessmer" href="https://mirjamglessmer.com/tag/hydraulic-jump/">
#     <video width="480" controls src="hydraulics/weir_pinnau_2016.mp4">animation</video></a>
#     <figcaption>Wave illustrations by Mirjam S. Glessmer, https://mirjamglessmer.com/2016/02/11/observing-hydrodynamic-phenomena-on-a-creek/</figcaption>
# </figure> -->
# 
# ##### iv) Weir Formula
# <!-- $$
# Q=(\frac{2}{3})^{\frac{3}{2}}wg^{\frac{1}{2}}\Delta z^{\frac{3}{2}}
# $$ -->
# 
# ```{figure} hydraulics/weir_formula.png
# ---
# width: 600
# name: directive-fig
# ---
# Weir formula: transport of a hydraulically controlled flow being a function of channel width $w$, reduced gravity $g'=\frac{\Delta \rho}{\rho_0}g$, and the height difference between the interface of the overflow and the sill top. 
# ```
# 
# <!-- <figure>
#     <img width="480" alt="weir formula" src="hydraulics/weir_formula.png"></a>
#     <figcaption>Weir formula: transport of a hydraulically controlled flow being a function of channel width $w$, reduced gravity $g'=\frac{\Delta \rho}{\rho_0}g$, and the height difference between the interface of the overflow and the sill top. </figcaption>
# </figure> -->
# 
# This allows oceanographers to estimate the transport of overflows without expensive and technically difficult velocity measurements. 
# 
# <!-- print('Samoan Passage parameters for example: ')
# w = float(input("What's the channel width w [km]? "))
# g = float(input("What's the reduced gravity g' [ms^-2]? "))
# hu = float(input("What's the height difference between the upstream interface and the sill top h_u [m]? "))
# Q = (2/3)**(3/2)*w*1000*g**(1/2)*hu**(3/2)*1e-6 
# print(f"Estimated transport for hydraulically controlled flow = {Q} Sv") -->
# 

# #### 2) Overflow applications
# 
# 
# ##### i) Application 1: transport estimate
# ```{figure} hydraulics/passage_Atlantic_Morozov2021.png
# ---
# width: 600
# name: directive-fig
# ---
# Fig. 2.1 in [Morozov et al. (2021)](https://link.springer.com/book/10.1007/978-3-030-83074-8) Bottom topography and main deep cataracts of the Atlantic Ocean. Red and magenta ellipses show the cataracts related and not related to the propagation of Antarctic waters in the abyss of the World Ocean. The arrows show the general direction of the flow in the cataracts. Deep blue numerals in circles indicate: (1) Drake Passage, (2) Falkland Trough (3) Georgia Basin, (4) Guinea Basin, (5) Sierra Leone Basin, (6) Cape Verde Basin, (7) Guiana Basin, (8) Madeira Basin, (9) Iberian Basin, (10) West European Basin. Brown letters in circles indicate: (a) North Weddell Ridge, (b) Southwest Indian Ridge, (c) Islas Orcadas Rise, (d) Falkland Plateau, (e) Zapiola Ridge, (f) Shona Ridge, (g) Meteor Rise, (h) Agulhas Ridge (i) Newfoundland Bank.
# ```
# 
# <!-- <figure>
#     <a title="Fig. 2.1 in Morozov et al. (2021)" href="https://link.springer.com/book/10.1007/978-3-030-83074-8">
#     <img width="480" alt="passages in the Atlantic Ocean" src="hydraulics/passage_Atlantic_Morozov2021.png"></a>
#     <figcaption>Fig. 2.1 in Morozov et al. (2021) Bottom topography and main deep cataracts of the Atlantic Ocean. Red and magenta ellipses show the cataracts related and not related to the propagation of Antarctic waters in the abyss of the World Ocean. The arrows show the general direction of the flow in the cataracts. Deep blue numerals in circles indicate: (1) Drake Passage, (2) Falkland Trough (3) Georgia Basin, (4) Guinea Basin, (5) Sierra Leone Basin, (6) Cape Verde Basin, (7) Guiana Basin, (8) Madeira Basin, (9) Iberian Basin, (10) West European Basin. Brown letters in circles indicate: (a) North Weddell Ridge, (b) Southwest Indian Ridge, (c) Islas Orcadas Rise, (d) Falkland Plateau, (e) Zapiola Ridge, (f) Shona Ridge, (g) Meteor Rise, (h) Agulhas Ridge (i) Newfoundland Bank. </figcaption>
# </figure> -->
# 
# ##### ii) Application 2: long-term transport
# 
# ```{figure} hydraulics/passage_Atlantic_Morozov2021.png
# ---
# width: 600
# name: directive-fig
# ---
# Adapted from Fig. 1 in [K$\ddot{o}$sters et al. (2003)](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2003pa000972). The Denmark Strait is deeper submerged under water in morden era compared to the last glacial era, and thus allows more overflow flux.
# ```
# 
# <!-- <figure>
#     <a title="Denmark Strait topography changes" href="https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2003pa000972">
#     <img width="960" alt="Denmark Strait changes" src="hydraulics/weir_formula_history.png"></a>
#     <figcaption>Adapted from Fig. 1 in K$\ddot{o}$sters et al. (2003). Morden era allows more overflow flux. </figcaption>
# </figure>
#  -->

# ### 2. Hydraulic Jump
# #### 1) Shock waves
# 
# #### 2) "Mixing hotspot" in the ocean

# <!-- <figure>
#     <a title="Canal Surfing in Munich" href="https://www.youtube.com/watch?v=zjZUqmHe838&t=2s">
#     <video width="480" controls src="hydraulics/river_surfing.mp4">animation</video></a>
#     <figcaption>Canal Surfing in Munich, notice the hydraulic jump.</figcaption>
# </figure>
#  -->

# ### 3. Upstream Influence (optional)
# #### 1) Upstream-propagating waves
# 
# #### 2) Ocean basin adjustment

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
# [**Descriptive Physical Oceanography, An Introduction** by Talley et al.](https://www.sciencedirect.com/book/9780750645522/descriptive-physical-oceanography) <br /> - for a comprehensive introduction of oceanography, good for this course in general
# <br />
# [**Linear and Nonlinear Waves** by Whitham](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118032954) <br /> - for those who wants to look into the math behind waves and hydraulics
# <br /> 
# [**Topographic Effects in Stratified Flows** by Baines](https://assets.cambridge.org/97811084/81526/frontmatter/9781108481526_frontmatter.pdf) <br /> - a challenging book to read, no pdf, but I have a hard copy you can borrow from
# 
# <!-- 
# ## Papers
# [**Turbulent mixing and hydraulic control of abyssal water in the Samoan Passage** by Alford et al.](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/grl.50684) <br /> - hydraulic control and jump found in Samoan Passage <br /> 
# [**Modelling the Föhn in the MIM Laboratory** by Josef Schröttle](https://minigcm.org/ba.pdf) <br /> - undergrad thesis, great review on hydraulics
# <br />
# [**Hydraulic Jump: A Brief History and Research Challenges** by De Padova and Mossa](https://www.mdpi.com/2073-4441/13/13/1733) <br /> - for a brief history of hydraulic jump, from engineering perspectives
#  -->
#  
# ### Videos!
# [National Committee for Fluid Mechanics Films (NCFMF)](http://web.mit.edu/hml/ncfmf.html) (strongly recommended for anyone who are interested in fluid mechanics, art \& masterpiece) <br /> - for waves \& hydraulics [Stratified Flow](https://www.youtube.com/watch?v=9hmjcIfy8wE&list=PL0EC6527BE871ABA3&index=19), you will see the famous **[Robert Long](https://onlinebooks.library.upenn.edu/webbin/book/lookupname?key=Daugherty%2C%20Robert%20L%2E%20%28Robert%20Long%29%2C%201885%2D)'s towing experiment**!

# In[ ]:




