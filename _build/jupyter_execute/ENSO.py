#!/usr/bin/env python
# coding: utf-8

# # ENSO, where ocean plays a leading role

# <!-- > When you can measure what you are speaking about and express it in numbers,
# then you know something about it. <div style="text-align: right"> — Lord Kelvin, 1883 </div>
#  -->
# > No single thing abides; \
# but all things flow.
# Fragment to fragment clings--the things thus grow \
# Until we know and name them. By degrees \
# They melt, and are no more the things we know. <div style="text-align: right"> — Lucretius (c. 99-55 B.C.) </div> <div style="text-align: right"> translated by W. H. Mallock </div>
# 

# ## What is ENSO?
# ```{figure} ENSO/MEI-schematic.png
# ---
# width: 600
# name: directive-fig
# ---
# Schematic diagram showing the SST (shaded) and sea level pressure (represented by "H" and "L" which indicate the high and low pressure center, respectively). Credit: [NOAA](https://psl.noaa.gov/enso/mei/)
# ```

# ### El Niño (EN in ENSO)
# 
# Peruvian fishermen found every couple of years around Christmas time, the ocean along the westernmost shores of South America became unusually warm, and they had bad anchovy harvest. They named this phenomenon El Niño, "the Christ child". For a long time, El Niños were thought to be an ocean phenomenon.
# 
# 
# ### Southern Oscillation (SO in ENSO)
# 
# [Gilbert Walker](https://mathshistory.st-andrews.ac.uk/Biographies/Walker_Gilbert/) found a connection between barometer readings at stations on the eastern and western sides of the Pacific (Tahiti Island and city Darwin). He coined the term Southern Oscillation to dramatize the ups and downs in this east-west seesaw effect. 

# ## ENSO Neutral

# [Jacob Bjerknes](https://en.wikipedia.org/wiki/Jacob_Bjerknes) was the first one to recognizes that El Niño is not just an oceanic phenomenon. In stead, he hypothesized that the warm waters of El Niño and the pressure seasaw of Walker’s Southern Oscillation are part and parcel of the same phenomenon: the ENSO. Nowadats, we use El Niños and La Niñas represent the warm and cold phases of ENSO. The condition shifts back and forth between the two phases, around the [ENSO neutral](https://iridl.ldeo.columbia.edu/maproom/ENSO/New/phase_neutral.html), which is the condition when there is zero fluctuation. Before we dive into the exciting El Niños and La Niñas, let's first understand how the tropical atmosphere and ocean are like during ENSO neutral.

# ### Hadley Circulation

# ```{figure} ENSO/hadley-cell-trade-winds.png
# ---
# width: 600
# name: directive-fig
# ---
# Warm, moist air from the equator rises in the atmosphere and eventually cools and sinks a bit further north in the tropics. This phenomenon is called the Hadley circulation/cell. Credit: NASA/JPL-Caltech
# ```

# ### Trade Wind

# Earth's rotation causes the winds to curve toward rigtht in the Northern Hemisphere and left in the Southern Hemisphere. The lower branches of the Hadley Cell thus form easterly winds (note: an easterly wind is a wind that blows from the east), also called the [trade winds](https://scijinks.gov/trade-winds/). The winds help ships travel west, and they can also steer storms such as hurricanes, too. A narrow band centered at the equator has almost no wind, and is called the doldrums. Europeans have known the trade winds before they found Alaska. $\Downarrow$
# ```{figure} ENSO/Moll_-_A_new_map_of_the_whole_world_with_the_trade_winds.png
# ---
# width: 600
# name: directive-fig
# ---
# Herman Moll's 1736 world map with the trade winds. [source: Wikipedia](https://de.wikipedia.org/wiki/Datei:Moll_-_A_new_map_of_the_whole_world_with_the_trade_winds.png).
# ```

# ### Walker Circulation
# Different from the Hadley Circulation, which is a meridional circulation, the Walker circulation is a zonal circulation located at the equator. A more important difference is that the Hadley Circulation which would exist no matter whether there is a watery ocean underneath, the walker circulation, however, is a result of air-sea interactions. 

# ```{figure} ENSO/WalkerNeutral_large.jpg
# ---
# width: 600
# name: directive-fig
# ---
# The east to west movement of the trade wind along the equatorial Pacific Ocean works on the water below it, resulting in an east to west current near the surface. The accumulation of warm surface waters in the equatorial Western Pacific pushes the thermocline down and causes the western Pacific warm pool. As the surface water existing from the equatorial eastern Pacific, the cold and nutrient rich subsurface waters upwell to compensate the advective surface water loss. This form a narrow equatorial strip of relatively low SSTs in the eastern Pacific, often referred to as the cold tongue. The thermocline is slanted down hundreds of meters from east to west across the equatorial Pacific Ocean, and the sea levels in the western Pacific, for example, in Indonesia, can be up to 50 cm higher than those in the eastern Pacific, for example, in Peru.  The low level winds converge over the western Pacific warm pool and rise. The very moist air rises creates heavy rainfall in the region. The air releases its moisure at high altitude and diverges out of the top of the convective region, moving out over the eastern Pacific to sink over the cooler waters. [NOAA Climate.gov drawing by Fiona Martin.](https://www.climate.gov/media/13542)
# ```

# ```{admonition} Given that the coastal city Darwin is in the Northern Australia and the Tahiti island is in the south central Pacific, can you tell where to measure a higher sea level pressure (SLP)? 
# :class: dropdown
# 
# As the low level air rises in the equatorial western Pacific and sinks in the equatorial eastern Pacific, the SLP is relatively high near Tahiti and relatively low near Darwin. 
# 

# ### ENSO Phases
# 
# ```{figure} ENSO/Stressors_ENSO3.png
# ---
# width: 600
# name: directive-fig
# ---
# This diagram shows a model of surface temperatures, winds, areas of rising air, and the thermocline (blue surface) in the tropical Pacific during El Niño, normal, and La Niña conditions. During El Niño, the warm pool of water moves eastward and the slope of the thermocline flattens. The equatorial eastern Pacific become abnormally warm, so El Niño is called the warm phase of ENSO. During La Niña, the cold phase of ENSO, the warm pool moves westward, and the slope of the thermocline steepens. [source: PMEL](https://www.pmel.noaa.gov/elnino/schematic-diagrams)
# ```

# ```{figure} ENSO/ensoanim.gif
# ---
# width: 600
# name: directive-fig
# ---
# Moving diagrams shows ENSO changing phase. [source: John Baez's blog](https://johncarlosbaez.wordpress.com/2014/08/01/exploring-climate-data-part-1/)
# ```

# ```{admonition} Given that the Nino3 index is the sea surface temperature anomaly averaged over a specified area of equatorial eastern Pacific and the Southern Oscillation Index (SOI) is given by the SLP at Tahiti minus SLP at Darwin, can you tell how Nino3 and SOI are correlated (positively or negatively)?
# :class: dropdown
# 
# ![](ENSO/alexey_sst_slp.gif)
# 

# ## ENSO Impacts
# 
# ```{figure} ENSO/lanina_impact.png
# ---
# width: 600
# name: directive-fig
# ---
# Figure 1.2 in [McPhaden et al.'s book](https://agupubs.onlinelibrary.wiley.com/doi/book/10.1002/9781119548164) Typical impacts of La Niña on global weather patterns during the peak season of development in December–February (after Ropelewski & Halpert, 1987; Courtesy of NOAA/Climate Prediction Center).
# ```
# 
# ```{figure} ENSO/DJF23_World_pcp.gif
# ---
# width: 600
# name: directive-fig
# ---
# [The IRI seasonal forecasts of precipitation](https://iri.columbia.edu/our-expertise/climate/forecasts/seasonal-climate-forecasts/) for the next three months. Note we are currently experiencing a "triple-dip" La Niña.
# ```

# Broader impacts:
# - [__The Record-Breaking Winter of 1976–77__](https://www.tandfonline.com/doi/abs/10.1080/00431672.1977.9931797) 
# <!-- (El Niño and cold extreme winter weather across the eastern half of the United States) -->
# - [__1982-1983 El Niño: The worst there ever was__](https://www.whoi.edu/science/B/people/kamaral/1982-1983ElNino.html) 
# - [__2015-2016 El Niño Triggered Disease Outbreaks Across Globe__](https://www.nasa.gov/feature/goddard/2019/2015-2016-el-nino-triggered-disease-outbreaks-across-globe)
# - [__IRI ENSO impact page__](https://iridl.ldeo.columbia.edu/maproom/ENSO/Impacts.html)

# ## Growth Mechanism - Bjerknes feedback
# The growth mechanism is the mechanism that is responsible for amplifying SST anomalies during both the warm and cold phases of the ENSO cycle. El Niño arises through reinforcing feedbacks between changes in surface winds and SSTs
# ([Bjerknes, 1966](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.2153-3490.1966.tb00303.x), [Bjerknes, 1969](https://doi.org/10.1175/1520-0493(1969)097<0163:ATFTEP>2.3.CO;2)).
# 
# ```{figure} ENSO/WalkerElNino_2colorSSTA_large.jpeg
# ---
# width: 600
# name: directive-fig
# ---
# During El Niño, the trade winds systematically weaken, which allows warm water piled up in the west to migrate eastward. Upwelling is also reduced, causing SSTs in the eastern Pacific to rise. Warming east of the dateline causes the ascending air masses, deep convection, and heavy rainfall to shift eastward as well. This in turn leads to a further relaxation of the trade winds to the west of the convective center, causing additional surface warming along the equator. This __self‐amplifying__ sequence of events involving weakening zonal winds, warming sea surface temperatures, and reduction in equatorial upwelling has been widely referred to as the “Bjerknes feedback.” -- [M. McPhaden](https://books.google.com/books/about/Physical_Oceanography.html?id=h6OR1Wv2jJsC&source=kp_book_description) Picture credit: [NOAA Climate.gov drawing by Fiona Martin.](https://www.climate.gov/media/13546)
# ```

# ## Phase transition Mechanism
# Any successful theory for the phase-transition mechanism has to be able to 
# 
# (1) provide a negative feedback to reverse the phase of the ENSO cycle, and \
# (2) account for the long period associated with the cycle. 
# 
# <div style="text-align: right"> - by J. Yu from UCI </div>
# 
# - __Delayed Oscillator__ (we will only discuss this mechanism in class) - [Suarez and Schopf (1988)](https://journals.ametsoc.org/view/journals/atsc/45/21/1520-0469_1988_045_3283_adaofe_2_0_co_2.xml), [Battisti & Hirst (1989)](https://journals.ametsoc.org/view/journals/atsc/46/12/1520-0469_1989_046_1687_iviata_2_0_co_2.xml?tab_body=pdf)
# - Recharge Oscillator - [Wyrtki (1975)](https://journals.ametsoc.org/view/journals/phoc/5/4/1520-0485_1975_005_0572_entdro_2_0_co_2.xml), [Wyrtki (1985)](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/JC090iC04p07129), [Cane (1986)](https://www.nature.com/articles/321827a0), [Jin (1997)](https://journals.ametsoc.org/view/journals/atsc/54/7/1520-0469_1997_054_0811_aeorpf_2.0.co_2.xml)
# - Western Pacific Oscillator - [Weisberg and Wang (1997)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97GL00689)
# - Advective-Reflective Oscillator - [Picaut et al. (1997)](https://www.science.org/doi/10.1126/science.277.5326.663?cookieSet=1)

# ### Delayed Oscillator

# #### Kelvin wave
# The dispersion relationship of the equatorial Kelvin wave is: 
# 
# $$
# \omega=kc_n
# $$
# 
# `````{admonition} Note
# :class: tip
# Equatorial Kelvin waves propagate eastward and are non-dispersive.
# `````

# ```{admonition} Do you know why?
# :class: dropdown
# 
# From the dispersion relation we know the phase speed $c=\frac{\omega}{k}$ quals group speed $c_p=\frac{\partial \omega}{\partial k}$. Also, the direction of group speed represents the direction of energy propagation, energy of Equatorial Kelvin waves also propagates eastward. 
# ```
# The dispersion relationship of mode-1 (n=1) equatorial Kelvin wave looks like this $\Downarrow$.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

k = np.arange(0,10,.1)
c = 1
omega_kelvin = k*c

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
ax.plot(k, omega_kelvin, label='Kelvin wave', lw=4)
ax.set_aspect('equal')
ax.set_xlim([-4,2])
ax.set_ylim([0,4])
ax.set_xlabel('$kL_{eq}$', fontsize=30)
ax.set_ylabel('$\omega/(\\beta L_{eq}$)', fontsize=30)
ax.plot([-10, 10], [0, 0], 'k')
ax.plot([0, 0], [-10, 10], 'k')
ax.legend(fontsize=15)


# Recall that the dispersion relationship is a relation between the wave vector $\vec{K}$ and the frequency $\omega$, $c_n$ is the phase speed of the $n_\text{th}$ baroclinic mode Kelvin wave. 
# 
# $c_0=\sqrt{gH}$ is the phase speed of the barotropic mode. With the average depth of the ocean $H$ is about 4000 m and $g\sim$10 ms$^{-2}$, $c_0$ is about 200 ms$^{-1}$. For the first baroclinic mode in the ocean, a typical value of $c_1$ is 2-3 ms$^{-1}$ [(Wunsch and Gill, 1976)](https://doi.org/10.1016/0011-7471(76)90835-4). So a mode-1 Kelvin wave would take about 2-3 months to cross the Pacific Ocean.

# Can you identify Equatorial Kelvin waves and their propagation direction from the animation of Satellite-observed sea surface height anomalies?
# 
# 
# [![Sea Surface Height Anomalies 1993 - 2011, from NASA](ENSO/geo234-toc-0001-m.jpeg)](https://sealevel.jpl.nasa.gov/resources/1146/sea-surface-height-1993-2011/)
# 

#  Hovmöller diagram equtorial Kelvin waves:
# ```{figure} ENSO/fig02.jpeg
# ---
# width: 600
# name: directive-fig
# ---
# Fig. 2 in [McPhaden 1997](https://www.pmel.noaa.gov/pubs/outstand/mcph2029/text.shtml) Time versus longitude sections of anomalies in surface zonal wind (left), SST (middle), and 20°C isotherm depth (right) from September 1996 to August 1998. Analysis is based on 5-day averages between 2°N and 2°S of moored time-series data from the TAO array. Positive winds are westerly, and positive 20°C isotherm depths indicate a deeper thermocline. 
# ```
# 

# #### Rossby wave

# The dispersion relationship of the equatorial Rossby wave is: 
# 
# $$
# \omega=-\frac{\beta k}{k^2+\frac{\beta}{c_n}(2j+1)}
# $$
# Here j=1,2,3,... is the number of "meridional modes". Similar to the combinition of continuous stratification and boundary condition giving rise to "baroclinic modes" for gravity waves, the combinition of continuously varying coriolis parameter and boundary condition gives rise to "meridional modes" for Rossby waves (interested students may read Lecture 18 of [Pelosky's text book](https://link.springer.com/book/10.1007/978-3-662-05131-3)). 
# 
# `````{admonition} Note
# :class: tip
# Long Rossby waves and energy propagate westward and are non-dispersive.
# 
# Short Rossby waves propagate westward, but energy propagates eastward, and are dispersive.
# `````

# ```{admonition} Can you prove this?
# :class: dropdown
# Hints:
# 
# The dispersion relationship for long Rossby wave is:
# $\omega=-\frac{c_n k}{2j+1}$
# 
# The dispersion relationship for short Rossby wave is:
# $\omega=-\frac{\beta}{k}$
# ```

# The dispersion relationship of mode-1 (j=1) Rossby wave looks like this $\Downarrow$.

# In[2]:


# non-dimensional dispersion relation omega = -k/(k^2+(2j+1)), 
# where omega scaler is beta*Leq, Leq=sqrt(cn/beta) is equatorial Rossby radius,
# k scaler is 1/Leq

j = 1
omega_rossby = -k/(k**2+2*j+1)

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
ax.plot(k, omega_kelvin, label='Kelvin wave', lw=4)
ax.plot(-k, -omega_rossby, label='Rossby wave', lw=4)
ax.set_aspect('equal')
ax.set_xlim([-4,2])
ax.set_ylim([0,2])
ax.set_xlabel('$kL_{eq}$', fontsize=30)
ax.set_ylabel('$\omega/(\\beta L_{eq}$)', fontsize=30)
ax.plot([-10, 10], [0, 0], 'k')
ax.plot([0, 0], [-10, 10], 'k')
ax.legend(fontsize=15)


# For the first meridional mode (j=1), the speed of long Rossby wave is $-\frac{c_n}{3}$, which is 1/3 of Kelvin wave speed. Thus Rossby wave takes 6-9 months cross the Pacific Ocean.

# #### Delayed Oscillator
# 
# If the trade winds weaken, an initial westerly wind stress anomaly in the central Pacific causes the generation of an eastward propagating and downwelling oceanic Kelvin wave. These Kelvin waves carry signals of anomalous warming and after a couple of months arrive at the western coast of the Americas. 
# 
# Coincident with the eastward-moving Kelvin wave are westward-moving Rossby waves. 

# ```{figure} ENSO/delayed_oscillator_xsects.jpeg
# ---
# width: 600
# name: directive-fig
# ---
# Fig. 4.29 in [Laing and Evans's 2021 textbook](https://ftp.comet.ucar.edu/memory-stick/tropical/textbook_2nd_edition/navmenu.php_tab_5_page_2.1.3.htm) Idealized model of a single equatorial eastward-moving Kelvin wave generated by wind stress anomaly (red and orange) and corresponding Rossby waves propagating westward.
# ```
# 
# ```{admonition} Given the typical time for Equatorial Kelvin waves and Rossby waves to cross the Pacific Ocean, can you predict where the upwelling and downwelling anomalies are after 3 months, 9 months, and one year? 
# :class: dropdown
# Fig. 4.30 in [Laing and Evans's 2021 textbook](https://ftp.comet.ucar.edu/memory-stick/tropical/textbook_2nd_edition/navmenu.php_tab_5_page_2.1.3.htm) Time evolution for the idealized experimental waves generated in the picture above. Picture credit: IRI
# 
# ![](ENSO/delayed_oscillator2.jpeg)
# ```
# 

# ## A tale of the 1982/83 El Ni$\tilde{n}o$

# The 1982–83 El Ni$\tilde{n}o$, which was neither predicted nor even detected until nearly at its peak, caught the scientific community completely by surprise. 
# 
# At the time, most in situ oceanographic data collected were available only many months or, in some cases, years after collection. Some data on oceanic and atmospheric conditions from islands and volunteer observing ships were available in real time (within a day) or near real time (within a month for climate purposes), but they were far too few and scattered to be of much value in providing a coherent picture of evolving conditions. NOAA satellites capable of high-precision measurements of SST from space had been launched for the first time in 1981. However, unbeknownst to NOAA, SST retrievals after March 1982 were contaminated by stratospheric aerosols from the eruption of El Chichon. The aerosols produced a cold bias in the satellite SSTs that was mistakenly interpreted as clouds. These biased retrievals were flagged as bad and replaced with climatology in gridded analyses of the data. Thus, throughout much of 1982, SST analyses based on satellite data indicated near normal conditions in tropical Pacific. Moreover, those few in situ data that showed extraordinarily warm SSTs several degrees Celsius above normal were rejected as erroneous because they did not agree with the satellite analyses. -- [M. McPhaden](https://books.google.com/books/about/Physical_Oceanography.html?id=h6OR1Wv2jJsC&source=kp_book_description)
# 

# ```{figure} ENSO/oceanObs2021-morris-f3.jpeg
# ---
# width: 600
# name: directive-fig
# ---
# Fig. 3 in [Morris et al., 2022](https://doi.org/10.5670/oceanog.2021.supplement.02-07) Morden technologies and instruments that measure the ocean. However, they either were not born or failed to capture the 1982–83 El Ni$\tilde{n}o$.
# ```
# 
# ```{figure} ENSO/elchichon.png
# ---
# width: 600
# name: directive-fig
# ---
# Fig. 7 in [Cruz-Reyna and Del Pozzo (2008)](https://www.scielo.org.mx/scielo.php?pid=S0016-71692009000100003&script=sci_arttext&tlng=en) Initial explosion of the plinian eruption of April 3, 1982 (photo by S. De la Cruz-Reyna taken from Ostuacán. 
# ```

# ## The 1982/83 El Ni$\tilde{n}o$ stimulates observation
# 
# The 1982-1983 El Niño was one of the strongest and most devastating El Niño events in recorded history, which caused [between 1,300 and 2,000 deaths and more than \$13 billion](https://www.whoi.edu/science/B/people/kamaral/1982-1983ElNino.html) in damage to property and livelihoods. The climatic and societal impacts of the stunning 1982–1983 El Niño helped motivate the Tropical Ocean Global Atmosphere (TOGA) program
# [(McPhaden et al., 2010)](https://www.jstor.org/stable/24860888).
# 
# ```{figure} ENSO/taga.png
# ---
# width: 600
# name: directive-fig
# ---
# Fig. 2 in [McPhaden et al., 2010](https://www.jstor.org/stable/24860888) The Tropical Ocean Global Atmosphere (TOGA) program was carried out between 1985 and 1994. The data greatly benefited the study of ENSO dynamics as well as ENSO prediction. TOGA's successors are Tropical Atmosphere Ocean (TAO) led by the US and TRIangle Trans-Ocean buoy Network (TRITON) led by Japan, and [observations are updated online daily](https://www.pmel.noaa.gov/tao/drupal/disdel/). 
# ```

# ## Brain Storm

# `````{admonition} Why Only Pacific Has ENSO?
# :class: dropdown
# - Based on the delayed oscillator theory of ENSO, the ocean basin has to be big enough to produce the “delayed” from ocean wave propagation and reflection.
# - It can be shown that only the Pacific Ocean is “big” (wide) enough to produce such delayed for the ENSO cycle.
# - It is generally believed that the Atlantic Ocean may produce [ENSO-like oscillation](https://www.aoml.noaa.gov/news/the-atlantic-nino-el-ninos-little-brother/) if external forcing are applied to the Atlantic Ocean.
# - The Indian Ocean is considered too small to produce ENSO.
# `````
# `````{admonition} Why ENSO has a preferred period of 2 to 7 years?
# :class: dropdown
# Hints:
# 
# - Western Pacific moonsoon has a 1-year period
# - The quasi-biennial oscillation (QBO) is a quasiperiodic oscillation of the equatorial zonal wind, has a 2-year period
# - Equatorial waves connect the western and eastern Pacific Ocean, the time scale for Rossby waves to propagate across Pacific is at order of one year. Waves of higher modes propagate slower. Recall the dispersion relationship for long Rossby wave,
# $\omega=-\frac{c_n k}{2j+1}$.
# `````
# 

# ## Resources
# 
# General Reading:
# - [IRI ENSO theme page](https://iridl.ldeo.columbia.edu/maproom/ENSO/index.html)
# - [IRI ENSO Forecast](https://iri.columbia.edu/our-expertise/climate/forecasts/enso/current/)
# - [PMEL ENSO theme page](https://www.pmel.noaa.gov/elnino/what-is-el-nino)
# - [Other Earths Climate Oscillations by Connie Ing](https://storymaps.arcgis.com/stories/d62f89509b504633a2c7516ab12d7767)
# 
# Books:
# - [Introduction to Tropical Meteorology by Laing and Evans](https://ftp.comet.ucar.edu/memory-stick/tropical/textbook_2nd_edition/index.htm), [Chap. 4.2.1](https://ftp.comet.ucar.edu/memory-stick/tropical/textbook_2nd_edition/navmenu.php_tab_5_page_2.1.0.htm)
# - [Waves in the Ocean and Atmosphere by Joe Pedlosky](https://link.springer.com/book/10.1007/978-3-662-05131-3), [Chap. Equatorial Beta-Plane and Equatorial Waves](https://link.springer.com/chapter/10.1007/978-3-662-05131-3_18)
# - [El Niño Southern Oscillation in a Changing Climate by McPhaden et al.](https://agupubs.onlinelibrary.wiley.com/doi/book/10.1002/9781119548164)
# 
# Visualizations & data:
# - Visulize Equatorial waves: [Data in Action: New NASA Sea Surface Height Grids to Study the Climate](https://podaac.jpl.nasa.gov/DataAction-2022-06-15-New-NASA-Sea-Surface-Height-grids-to-study-the-Climate)
# - [TAO/TRITON data page](https://www.pmel.noaa.gov/tao/drupal/disdel/)
# 

# In[ ]:




