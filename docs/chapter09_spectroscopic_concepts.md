(chapter09_spectroscopic_concepts)=

# Spectroscopic Concepts

:::{danger}
This page still needs substantial revision to match the content presented during the lectures
:::

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

A stellar spectrum records how the light received from a star is distributed in wavelength. Superposed on its continuum are lines whose wavelengths identify atoms and ions and whose strengths depend on conditions in the atmosphere. To interpret those features, we first consider how they form and how a spectrograph records them. We then use spectra to estimate stellar parameters and to understand the classification of stars.

## Working definitions

In astronomy, **metals** are all elements heavier than helium in atomic number, including carbon, oxygen, neon, sodium, and iron. The term describes composition in the astronomical sense and includes elements that chemists classify as non-metals.

A Roman numeral after a chemical symbol gives the **ionization stage**. The numeral I denotes a neutral atom, II a singly ionized atom, and III a doubly ionized atom. Thus O III is $\mathrm{O}^{2+}$ and Fe II is $\mathrm{Fe}^{+}$. Square brackets, as in [O III], identify lines from transitions with very low radiative probabilities. Such lines can be prominent in low-density gas, where an excited ion can radiate before a collision de-excites it.[^ch09_lines]

## Spectroscopy

**Spectroscopy** is the study of the interaction of matter with electromagnetic radiation as a function of wavelength or frequency. In experiments begun in 1666, Isaac Newton used a prism to disperse sunlight. A second prism showed that a component selected from the first spectrum retained its colour and its characteristic refrangibility. The spectrum therefore revealed a property of the incident light. A rainbow provides a natural example of dispersion. Refraction on entering and leaving raindrops and internal reflection send different wavelengths in different directions.

The laboratory experiment and the natural example are shown in [Figure 1](fig01_spectroscopy_newton) and [Figure 2](fig02_spectroscopy_rainbow).

```{figure} _static/_chapter09/fig01_newton.png
:width: 72%
:align: center
:name: fig01_spectroscopy_newton

**Figure 1** An illustration of Newton’s prism experiment. Sunlight entering the darkened room spreads into a band of colours after passing through the prism.
```

```{figure} _static/_chapter09/fig02_rainbow.png
:width: 38%
:align: center
:name: fig02_spectroscopy_rainbow

**Figure 2** A rainbow produced by refraction and internal reflection in water droplets. The angle at which the light returns towards the observer depends on wavelength.
```


In 1814 Joseph von Fraunhofer began his systematic study of the dark lines in the solar spectrum. He mapped 574 lines and assigned letters such as D, G, and H to conspicuous features ([Figure 3](fig03_spectroscopy_fraunhofer)). Around 1859–1860 Gustav Kirchhoff and Robert Bunsen compared laboratory spectra with the solar spectrum. The sodium D doublet offers a direct comparison. A hot, rarefied sodium vapour produces bright lines at the same wavelengths at which cooler sodium vapour absorbs radiation from a brighter continuum source. A solar spectrum recorded from the ground can also contain absorption lines from the Earth's atmosphere.[^ch09_history]

```{figure} _static/_chapter09/fig03_fraunhofer.png
:width: 78%
:align: center
:name: fig03_spectroscopy_fraunhofer

**Figure 3** Fraunhofer’s drawing of the solar spectrum. Labels such as D, G, and H mark prominent absorption features. [Fraunhofer-Gesellschaft, historical record](https://www.fraunhofer.de/en/about-fraunhofer/profile-structure/chronicles/joseph-von-fraunhofer.html).
```


### Origin of spectral lines

The **photosphere** is the deepest layer of a stellar atmosphere from which visible radiation can readily escape. Its apparent depth depends on wavelength and viewing angle. Most of the visible continuum of a Sun-like star emerges where the continuum optical depth along the line of sight is of order unity. At an absorption line the opacity is higher, so the layer from which radiation escapes is generally higher and cooler. The emergent flux at the line wavelength is then lower than the adjacent continuum. Different parts of the same line can sample different heights ([Figure 4](fig04_spectroscopy_photosphere)).[^ch09_photosphere]

```{figure} _static/_chapter09/fig04_photosphere.png
:width: 53%
:align: center
:name: fig04_spectroscopy_photosphere

**Figure 4** Schematic view of radiation escaping through the photosphere. At a given wavelength we see layers from which photons can escape along the line of sight.
```


Sunspots are cooler magnetic structures seen in the photosphere. The active regions in which they occur can also extend into the higher atmosphere. The effective temperature $T_{\rm eff}$ is defined by the emergent bolometric flux per unit stellar surface area, $F=\sigma T_{\rm eff}^4$. The local gas temperature varies with depth, and the solar atmosphere reaches a temperature minimum near the transition from the photosphere to the chromosphere.[^ch09_photosphere]

Hot, tenuous gas can produce **emission** lines. In a planetary nebula, ultraviolet radiation from the hot central star photoionizes the gas. Electron collisions can then excite $\mathrm{O}^{2+}$ and radiative decay produces the visible [O III] lines near $496$ and $501\ \mathrm{nm}$. Collisionally excited [O III] can also arise in shocked gas in a supernova remnant, as in the Veil Nebula. The two examples of planetary nebulae below illustrate a distinction between imaging and spectroscopy. The NGC 2392 composite uses observations in several emission lines, while the assigned colours of the Helix image represent infrared bands.[^ch09_nebulae] See [Figure 5](fig05_spectroscopy_ngc2392) and [Figure 6](fig06_spectroscopy_helix).

```{figure} _static/_chapter09/fig05_ngc2392.png
:width: 55%
:align: center
:name: fig05_spectroscopy_ngc2392

**Figure 5** Planetary nebula NGC 2392 imaged with Hubble in four emission bands, including [O III]. Credit NASA, Andrew Fruchter, and the ERO Team. [NASA image record](https://science.nasa.gov/image-detail/c39-1/).
```

```{figure} _static/_chapter09/fig06_helix.png
:width: 71%
:align: center
:name: fig06_spectroscopy_helix

**Figure 6** The Helix Nebula (NGC 7293), a planetary nebula, in a Spitzer infrared composite. The image represents infrared emission from gas and dust. Credit NASA/JPL-Caltech. [NASA image record](https://science.nasa.gov/image-article/apod-2007-february-23-dust-and-the-helix-nebula/).
```


## Instruments

### Measuring spectra

A spectrograph maps wavelength onto position at the detector. A wavelength calibration establishes that mapping, and the **spectral range** specifies the interval covered by a given setup. The **resolving power** describes the scale on which the instrument can distinguish nearby spectral features,

$$
\boxed{R=\frac{\lambda}{\Delta\lambda_{\rm res}}}.
$$

Here $\Delta\lambda_{\rm res}$ is the width in wavelength of one resolution element at $\lambda$. In practice it is often quoted as the full width at half maximum (**FWHM**) of the instrument's response to a monochromatic input, the **line-spread function**. For example, $R=50\,000$ at $500\ \mathrm{nm}$ gives $\Delta\lambda_{\rm res}=0.010\ \mathrm{nm}$. The criterion for resolving two lines also depends on the line-spread function, their relative strengths, and the signal-to-noise ratio. In [Figure 7](fig07_spectroscopy_resolution), the separation of the two input lines is fixed while instrumental broadening increases. When the FWHM becomes large compared with their separation, the recorded spectrum has a single broad maximum.[^ch09_resolution]

```{figure} _static/_chapter09/fig07_resolution.png
:width: 52%
:align: center
:name: fig07_spectroscopy_resolution

**Figure 7** Two spectral features at fixed separation observed with increasing instrumental broadening. The blue curve has the narrowest instrumental profile and the red curve the broadest.
```


The detector also samples each resolution element over a finite number of pixels. If the local wavelength increment is $\delta\lambda_{\rm pix}$ per pixel, a line-spread function of width $\Delta\lambda_{\rm res}$ covers approximately $\Delta\lambda_{\rm res}/\delta\lambda_{\rm pix}$ pixels at half maximum. The uncertainty in the fitted line position increases at coarse sampling and can depend on where the line falls relative to the pixel centres ([Figure 8](fig08_spectroscopy_sampling)).

:::{note}
About three pixels per FWHM is a useful design guideline. The sampling needed for a specified precision depends on the shape of the instrumental profile and on the quantity being measured.[^ch09_sampling]
:::

```{figure} _static/_chapter09/fig08_sampling.png
:width: 89%
:align: center
:name: fig08_spectroscopy_sampling

**Figure 8** Relative uncertainty in a fitted wavelength versus the number of pixels per FWHM. The panels illustrate the effects of sampling different instrumental profiles. Robertson (2017).
```


### Prisms

The **refractive index** is $n=c/v_{\rm ph}$, where $c$ is the speed of light in vacuum and $v_{\rm ph}$ is the phase velocity in the medium. For a ray crossing the interface between two media, **Snell's law** gives

$$
n_1\sin\theta_1=n_2\sin\theta_2,
$$

with both angles measured from the interface normal ([Figure 9](fig09_spectroscopy_snell)). The refractive index generally varies with wavelength. A beam that crosses the two inclined faces of a prism therefore emerges in different directions at different wavelengths. In the visible range of ordinary optical glass, violet light usually deviates more than red light ([Figure 10](fig10_spectroscopy_prism)).

```{figure} _static/_chapter09/fig09_snell.png
:width: 42%
:align: center
:name: fig09_spectroscopy_snell

**Figure 9** Refraction at the boundary of two media. The incident and refracted angles $\theta_1$ and $\theta_2$ are measured from the normal.
```

```{figure} _static/_chapter09/fig10_prism.png
:width: 67%
:align: center
:name: fig10_spectroscopy_prism

**Figure 10** A prism spreads visible light into different directions. For ordinary dispersion the violet rays deviate more than the red rays.
```


A prism can transmit visible light efficiently and produces a single dispersed spectrum. Its angular dispersion varies with wavelength. The material, apex angle, usable aperture, and optical quality influence the achievable resolving power, and the slit and imaging optics can further limit the delivered resolution. These constraints help explain the widespread use of diffraction gratings for high-resolution spectroscopy.[^ch09_optics]

### Diffraction gratings

Waves from two coherent sources interfere constructively when the path difference is an integer multiple of the wavelength. Intermediate path differences give partial or complete cancellation, depending on the phase difference and amplitudes ([Figure 11](fig11_spectroscopy_interference)). A **diffraction grating** extends this principle to a periodic array of many grooves or rulings. The grooves can transmit or reflect light, depending on the design. For normal incidence and groove spacing $d$ the maxima satisfy

$$
d\sin\theta_m=m\lambda,\qquad m=0,\pm1,\pm2,\ldots,
$$

where $\theta_m$ is measured from the grating normal. The integer $m$ is the diffraction **order**. At normal incidence the zeroth order is undeviated and undispersed. On either side of it, different wavelengths in each nonzero order emerge at different angles ([Figure 12](fig12_spectroscopy_gratingorders) and [Figure 13](fig13_spectroscopy_gratingphoto)). An ideal grating with $N$ illuminated grooves has resolving power $R=|m|N$. The resolving power delivered by the complete instrument also depends on how it is illuminated and on the slit, optics, and detector.[^ch09_optics]

```{figure} _static/_chapter09/fig11_interference.png
:width: 65%
:align: center
:name: fig11_spectroscopy_interference

**Figure 11** Interference of waves from two coherent sources. Crests that arrive in phase reinforce one another, while equal-amplitude waves arriving in opposite phase cancel.
```

```{figure} _static/_chapter09/fig12_gratingorders.png
:width: 75%
:align: center
:name: fig12_spectroscopy_gratingorders

**Figure 12** Dispersion by a grating at normal incidence. The central beam is the undispersed zeroth order. Nonzero orders spread the input wavelengths over a range of angles.
```

```{figure} _static/_chapter09/fig13_gratingphoto.png
:width: 73%
:align: center
:name: fig13_spectroscopy_gratingphoto

**Figure 13** A demonstration of diffraction with white light. The central, undispersed beam is flanked by dispersed orders.
```


The light in a chosen order depends on the efficiency of the grating. A **blazed grating** has groove facets shaped to direct a large fraction of the light into a chosen order over a wavelength interval. The efficiency has a maximum near that order's **blaze wavelength**. Its shape and the relative efficiency of different orders depend on the groove profile, angles, wavelength, and polarization.

Two wavelengths can leave the grating at the same angle whenever $m\lambda=m'\lambda'$. For example, $600\ \mathrm{nm}$ in first order overlaps $300\ \mathrm{nm}$ in second order. The spacing in wavelength between overlapping orders near $\lambda$ shrinks as $|m|$ increases. A filter can suppress unwanted wavelengths in an instrument that records one order. To record several orders at once, a second dispersive element can spread them in a different direction.[^ch09_optics]

```{figure} _static/_chapter09/fig14_overlap.png
:width: 61%
:align: center
:name: fig14_spectroscopy_overlap

**Figure 14** Overlap of grating orders. At a given angle a shorter wavelength in a higher order can coincide with a longer wavelength in a lower order.
```


### Grisms

A **grism** combines a transmission grating and a prism ([Figure 15](fig15_spectroscopy_grism)). The two elements can be arranged so that the diffraction and refraction angles cancel for a chosen wavelength in a chosen nonzero order. A grism placed in the beam of an imaging camera makes **slitless spectroscopy** over a field possible. Each source produces one or more dispersed images, with its position in a direct exposure providing the reference for the wavelength calibration. The apparent size of an extended source along the dispersion direction can broaden a spectral feature. Spectra from different sources can overlap in a crowded field.

Hubble Space Telescope imaging of SN 1987A in the Large Magellanic Cloud shows the rings of glowing gas around the explosion site ([Figure 16](fig16_spectroscopy_sndirect)). In the ACS grism field ([Figure 17](fig17_spectroscopy_sngrism)), stars produce elongated traces, and strong emission lines from the bright inner ring produce displaced images of the same ring. The separation of orders and the displacement along a trace encode wavelength. The direct image in the two-colour grism display marks positions on the sky, while the dispersed signal includes contributions from more than one order.[^ch09_sn1987a]

```{figure} _static/_chapter09/fig15_grism.png
:width: 59%
:align: center
:name: fig15_spectroscopy_grism

**Figure 15** A transmission grating coupled to a prism. The illustrated reference wavelength travels through the grism without net deviation.
```

```{figure} _static/_chapter09/fig16_sndirect.png
:width: 43%
:align: center
:name: fig16_spectroscopy_sndirect

**Figure 16** A direct Hubble image of the glowing rings around SN 1987A. Credit Christopher Burrows, ESA/STScI and NASA. [Hubble image and observing context](https://science.nasa.gov/missions/hubble/hubble-finds-mysterious-ring-structure-around-supernova-1987a/).
```

```{figure} _static/_chapter09/fig17_sngrism.png
:width: 77%
:align: center
:name: fig17_spectroscopy_sngrism

**Figure 17** SN 1987A in a composite of Hubble ACS/HRC direct and G800L grism observations. The ring is blue in the direct image and reappears in the dispersed signal in orange. [Hubble Legacy Archive example](https://archive.stsci.edu/mug/mug_2008/hla_mug2008.pdf).
```


### Slit spectroscopy

In a **long-slit spectrograph**, a slit in the telescope focal plane selects a narrow strip of sky. The detector retains position along the strip in one direction and records wavelength in the perpendicular direction. Each wavelength produces an image of the illuminated slit. A wider slit generally lowers the resolving power in the slit-limited regime while admitting more light. For a point source narrower than the slit, the seeing and the optical response also affect the width of the recorded image. Long-slit observing modes are used from the ground and in space.[^ch09_slit]

A slit across a galaxy can record a stellar continuum and emission from regions of ionized gas. In [Figure 19](fig19_spectroscopy_slit), the diffuse horizontal trace is the galaxy continuum. At particular wavelengths, compact emitting regions stand out in $\mathrm{H}\alpha$, [N II], and [S II]. Sky emission extends along the slit at fixed wavelengths. Isolated bright spots from cosmic rays are detector events. This two-dimensional view helps distinguish the different signals before extracting a spectrum. The direct galaxy image in [Figure 18](fig18_spectroscopy_galaxy) illustrates the kind of extended field sampled by a slit.

```{figure} _static/_chapter09/fig18_galaxy.png
:width: 58%
:align: center
:name: fig18_spectroscopy_galaxy

**Figure 18** A spiral galaxy and its surrounding field. A long slit placed across an extended galaxy can sample multiple emitting regions in one exposure.
```

```{figure} _static/_chapter09/fig19_slit.png
:width: 93%
:align: center
:name: fig19_spectroscopy_slit

**Figure 19** Two-dimensional long-slit spectrum. Wavelength runs horizontally and position along the slit vertically. The stellar continuum, nebular lines, sky emission, and cosmic-ray events have distinct appearances.
```


### Echelle spectroscopy

An **echelle grating** has widely spaced grooves and a large blaze angle. It concentrates light into high diffraction orders, giving high dispersion and high resolving power ([Figure 20](fig20_spectroscopy_echellegrooves)). The wavelength interval free of adjacent-order overlap is small, so an echelle spectrograph uses a **cross-disperser**. A prism or a second grating disperses the light approximately perpendicular to the first dispersion direction. The detector then records a stack of separated spectral orders ([Figure 21](fig21_spectroscopy_crossdispersion) and [Figure 22](fig22_spectroscopy_ordermap)). These traces are often tilted or curved, and their spacing and wavelength coverage depend on the optical design. Each recorded order has a blaze response across its wavelength span. The detector size and optical layout determine how much of that span is recorded.[^ch09_echelle]

```{figure} _static/_chapter09/fig20_echellegrooves.png
:width: 64%
:align: center
:name: fig20_spectroscopy_echellegrooves

**Figure 20** An echelle grating in cross-section. The steep groove facets direct light efficiently into high diffraction orders.
```

```{figure} _static/_chapter09/fig21_crossdispersion.png
:width: 42%
:align: center
:name: fig21_spectroscopy_crossdispersion

**Figure 21** Cross-dispersion separates the orders produced by an echelle grating on a two-dimensional detector.
```

```{figure} _static/_chapter09/fig22_ordermap.png
:width: 67%
:align: center
:name: fig22_spectroscopy_ordermap

**Figure 22** Example of an echelle order map from a GMT near-infrared spectrograph design study. The rectangle represents the detector area and the points mark the blaze wavelengths of the orders.
```


High-resolution echelle instruments can be fed by a slit or by an optical fibre. ESPRESSO at the VLT has a very-high-resolution mode with median $R\simeq190\,000$. The E140H echelle mode of STIS on Hubble reaches $R\simeq114\,000$ in the far ultraviolet. The cross-dispersed design therefore has both ground-based and space-based implementations.[^ch09_echelle]

### Integral-field spectroscopy

An **integral field unit** (IFU) samples an image in both spatial directions and produces a spectrum at each spatial element, or **spaxel**. A lenslet array can form a regular set of inputs ([Figure 23](fig23_spectroscopy_ifu)). Lenslets can also feed fibres, which can be rearranged at the spectrograph entrance. An image slicer divides the field into strips and reformats them into one or more pseudo-slits. After calibration and reconstruction the data form a cube $I(x,y,\lambda)$. A slice at a given wavelength gives a narrow-band image. A cut through the cube at fixed sky position gives a spectrum.

```{figure} _static/_chapter09/fig23_ifu.png
:width: 90%
:align: center
:name: fig23_spectroscopy_ifu

**Figure 23** Three approaches to integral-field spectroscopy. Lenslets, lenslets coupled to fibres, or an image slicer preserve information from two spatial directions for reconstruction into a data cube.
```


The NIRSpec IFU on the James Webb Space Telescope uses a mirror image slicer. It provides an example of spatially resolved spectroscopy from space.[^ch09_ifu]

### Multi-object spectroscopy

In **multi-object spectroscopy** we choose discrete targets across the field. Fibres, masks with slits, or configurable apertures select light from those targets and route it to one or more spectrographs. The spectra are separated on the detector. A multiplexed exposure can also allocate some inputs to blank sky for background measurements.

FLAMES at ESO's Very Large Telescope positions fibres in the focal plane and can feed the GIRAFFE spectrograph ([Figure 24](fig24_spectroscopy_fibrepositioner) and [Figure 25](fig25_spectroscopy_giraffe)). 4MOST uses the VISTA 4-m-class telescope at Paranal and has 2,436 science fibres. The number of distinct targets in an exposure depends on how the fibres are allocated.[^ch09_mos]

```{figure} _static/_chapter09/fig24_fibrepositioner.png
:width: 67%
:align: center
:name: fig24_spectroscopy_fibrepositioner

**Figure 24** Fibre positioner at the Very Large Telescope. The fibres collect light from selected locations in the telescope focal plane.
```

```{figure} _static/_chapter09/fig25_giraffe.png
:width: 36%
:align: center
:name: fig25_spectroscopy_giraffe

**Figure 25** Multiple spectra on the GIRAFFE detector. Separate traces record the light delivered by individual fibres.
```


## Analysis of spectra

### Spectrophotometry

In **spectrophotometry** we measure the flux density as a function of wavelength. The spectrum must first be wavelength-calibrated. Observations of a flux standard help determine the wavelength-dependent instrument response. Ground-based measurements also require attention to atmospheric extinction and to telluric absorption bands, which may carry little useful stellar signal where the transmission is low. Interstellar reddening is a separate effect along the path from the star to the observer.

Once calibrated, the shape of the continuum and broad discontinuities can be compared with model atmospheres to estimate $T_{\rm eff}$. The comparison must account for the scaling between surface flux and observed flux, and for the effects of gravity, composition, and reddening where relevant. In [Figure 26](fig26_spectroscopy_spectrophotometry), models at $6250$ and $6500\ \mathrm K$ have the same $\log g=4.0$ but predict different spectral shapes for BD $+3^\circ\,740$. The comparison illustrates the information in the slope and in the Balmer discontinuity near $365\ \mathrm{nm}$.[^ch09_analysis]

```{figure} _static/_chapter09/fig26_spectrophotometry.png
:width: 76%
:align: center
:name: fig26_spectroscopy_spectrophotometry

**Figure 26** Flux distribution of BD $+3^\circ\,740$ compared with models at $6250$ and $6500\ \mathrm K$. The horizontal axis is wavelength in ångströms and the vertical scale is relative flux density.
```


### Temperature and surface gravity

The number of absorbers in the lower level of a transition depends on the excitation and ionization balance. A line may strengthen as temperature rises and more ions or atoms reach that level, then weaken when further ionization depletes that stage. For instance, the Balmer absorption lines are strongest near the early A types. At lower temperatures few neutral hydrogen atoms occupy $n=2$, the lower level of the Balmer transitions. At higher temperatures an increasing fraction of the hydrogen is ionized ([Figure 27](fig27_spectroscopy_diagnostics)).

**Surface gravity** is $g=GM_\star/R_\star^2$, where $M_\star$ and $R_\star$ are the mass and radius of the star. The notation $\log g$ conventionally gives the base-ten logarithm of the numerical value of $g$ in $\mathrm{cm\,s^{-2}}$. At comparable $T_{\rm eff}$ and composition, changes in $g$ affect the density and electron pressure in the line-forming layers. Ratios of lines from different ionization stages and the pressure-broadened wings of suitable lines help constrain $g$. In practice we fit several diagnostics together, using their different sensitivities to separate the effects of temperature and gravity.[^ch09_analysis]

```{figure} _static/_chapter09/fig27_diagnostics.png
:width: 70%
:align: center
:name: fig27_spectroscopy_diagnostics

**Figure 27** Relative line strengths as a function of spectral type. Different ionization stages, atoms, and molecules reach their strongest absorption at different temperatures.
```


### Chemical composition

We express the **abundance** of an element $X$ by the ratio of the number of its nuclei to the number of hydrogen nuclei. Two common logarithmic measures are

$$
\log\epsilon(X)=12+\log_{10}(N_X/N_{\mathrm H}),\qquad
[X/{\rm H}]=\log_{10}(N_X/N_{\mathrm H})_\star
-\log_{10}(N_X/N_{\mathrm H})_\odot.
$$

We also use $[X/{\rm Fe}]=[X/{\rm H}]-[{\rm Fe}/{\rm H}]$. A difference of one dex is a factor of ten in the corresponding ratio. For a given atmosphere, increasing the abundance generally strengthens weak absorption lines of the element. Saturation limits the response of strong lines. The inferred abundance also depends on the adopted $T_{\rm eff}$, $\log g$, background composition, and other parameters that affect the line profile. Molecular bands depend on molecular equilibrium and can be blended. Fitting a synthetic spectrum over an entire region helps account for the contributions of several transitions.

The metal-poor star SMSS J023139.43−523957.4 provides an example. Its observed CH bands are compared with synthetic spectra in two intervals around $430\ \mathrm{nm}$. The central model has $\log\epsilon(\mathrm C)=5.89$ and gives the best fit of the three curves. The models offset by $\pm0.20$ dex show how changing the carbon abundance affects the predicted absorption ([Figure 28](fig28_spectroscopy_carbonabundance)).[^ch09_carbon]

```{figure} _static/_chapter09/fig28_carbonabundance.png
:width: 90%
:align: center
:name: fig28_spectroscopy_carbonabundance

**Figure 28** CH absorption in SMSS J023139.43−523957.4. Crosses are measured fluxes and the black curve is the best-fitting synthetic spectrum. The red curves change the carbon abundance by $\pm0.20$ dex. Jacobson et al. (2015), Fig. 3.
```


### Equivalent-width analysis

For an absorption line on a continuum $F_{\lambda,c}$, the **equivalent width** is

$$
\boxed{W_\lambda=\int_{\lambda_1}^{\lambda_2}
\left(1-\frac{F_\lambda}{F_{\lambda,c}}\right)\mathrm{d}\lambda}.
$$

The integral has units of wavelength. It is the width of a rectangle extending from the continuum to zero flux that removes the same amount of continuum-normalized flux as the line ([Figure 29](fig29_spectroscopy_equivalentwidth)). The FWHM describes the profile at half its depth, while $W_\lambda$ measures its integrated strength. A broader line can have a larger equivalent width even when its core is shallower. The estimate depends on the continuum placement and on how well the line can be separated from neighbouring features.[^ch09_ew]

```{figure} _static/_chapter09/fig29_equivalentwidth.png
:width: 68%
:align: center
:name: fig29_spectroscopy_equivalentwidth

**Figure 29** Equivalent width $W$ and FWHM of an absorption line centred at $\lambda_0$. The shaded equivalent rectangle extends over the full continuum height. Barbieri and Bertini (2021), Fig. 17.6.
```


In the iron example, we measure equivalent widths of many Fe I and Fe II lines. A model atmosphere converts each measurement to an iron abundance. The lower-level excitation energy $\chi_{\rm exc}$ is known for each transition. In [Figure 30](fig30_spectroscopy_ironbalance) the near-horizontal fit illustrates excitation balance. In a conventional local-thermodynamic-equilibrium analysis we adjust the model iteratively as follows.

1. Adjust $T_{\rm eff}$ so that the abundances from Fe I have no systematic trend with $\chi_{\rm exc}$ in the **excitation balance**.
2. Adjust $\log g$ so that the mean abundances from Fe I and Fe II agree in the **ionization balance**.
3. If the analysis includes partially saturated lines, adjust the microturbulent velocity so that the inferred abundance has no systematic trend with the reduced equivalent width $\log_{10}(W_\lambda/\lambda)$. Update the model metallicity to match the measured abundance.

```{figure} _static/_chapter09/fig30_ironbalance.png
:width: 71%
:align: center
:name: fig30_spectroscopy_ironbalance

**Figure 30** Iron abundance versus lower-level excitation energy. The red fit has a negative slope and the blue fit is nearly flat. In excitation balance the fitted slope is consistent with zero.
```


The diagnostics are coupled. Changing temperature also changes ionization, so excitation and ionization balance must be checked again after updating the model. Departures from local thermodynamic equilibrium or errors in the atmospheric model can bias the inferred parameters.[^ch09_ew]

### Doppler shift

A spectrum also records the motion along the line of sight. If a line has rest wavelength $\lambda_0$ and observed wavelength $\lambda_{\rm obs}$, the non-relativistic **Doppler shift** is

$$
\boxed{\frac{\lambda_{\rm obs}-\lambda_0}{\lambda_0}\simeq\frac{v_r}{c}},
\qquad |v_r|\ll c .
$$

We take radial velocity $v_r$ to be positive for recession. A receding source gives a redshift, and an approaching source gives a blueshift. Motion across the line of sight produces no first-order radial Doppler shift. For example, a line at $500\ \mathrm{nm}$ shifts by about $+0.050\ \mathrm{nm}$ for $v_r=+30\ \mathrm{km\,s^{-1}}$. The motion of the observer must be accounted for when the velocity is to be quoted in a specified reference frame. In [Figure 31](fig31_spectroscopy_doppler), the rainbow bands give the wavelength scale and the dark marks show line positions. The bands carry no information about the shape of the flux distribution.[^ch09_doppler]

```{figure} _static/_chapter09/fig31_doppler.png
:width: 89%
:align: center
:name: fig31_spectroscopy_doppler

**Figure 31** Radial Doppler shift. Relative to the middle reference, the lines move to shorter wavelengths for an approaching source and to longer wavelengths for a receding source.
```


## Stellar classification

Stars of similar colour can have very different radii and luminosities. In [Figure 32](fig32_spectroscopy_stellar_sizes), Pollux and Arcturus are much larger than the Sun even though all three have spectra characteristic of relatively cool photospheres. Betelgeuse and Antares extend the comparison to red supergiants ([Figure 33](fig33_spectroscopy_supergiant_sizes)). We will first classify spectra by the features that change mainly with temperature, then introduce the additional features that distinguish luminosity classes.

```{figure} _static/_chapter09/fig32_stellar_sizes.png
:width: 70%
:align: center
:name: fig32_spectroscopy_stellar_sizes

**Figure 32** An illustrative size comparison including the Sun, Sirius, Pollux, and Arcturus. Pollux and Arcturus are cool giants with larger radii than the Sun.
```

```{figure} _static/_chapter09/fig33_supergiant_sizes.png
:width: 69%
:align: center
:name: fig33_spectroscopy_supergiant_sizes

**Figure 33** Betelgeuse and Antares illustrate the large sizes of red supergiants. The drawing compares approximate sizes and colours.
```


### Secchi classification

In the 1860s Angelo Secchi grouped stellar spectra according to their most conspicuous features. The strength of the hydrogen lines, the presence of metallic lines, and the appearance of molecular bands provided criteria that could be applied systematically. Secchi extended the scheme as more spectra became available, adding a separate group for emission-line spectra in 1877.[^ch09_class_history]

| Secchi class | Characteristic spectrum | Examples |
| --- | --- | --- |
| I | White and blue stars with broad, strong hydrogen lines | Vega, Altair |
| I, Orion subtype | Blue stars with narrower lines than the broad hydrogen features of the main group | Rigel, Bellatrix |
| II | Weaker hydrogen lines and conspicuous metallic lines | Sun, Arcturus, Capella |
| III | Orange and red stars with prominent bands | Betelgeuse, Antares |
| IV | Carbon stars with characteristic carbon-bearing bands | Carbon stars identified by Secchi from 1868 |
| V | Stars with prominent emission lines | $\gamma$ Cassiopeiae, Sheliak |

The *Draper Catalogue of Stellar Spectra* (1890) subdivided the Secchi groups using letters. Williamina Fleming applied the classification to objective-prism photographic spectra at Harvard College Observatory under Edward C. Pickering. Anna Palmer Draper supported the work in memory of Henry Draper, who had photographed the spectrum of Vega. The link between the two schemes was approximate.[^ch09_class_history]

| Secchi class | Historical Draper types |
| --- | --- |
| I | A, B, C, D |
| II | E, F, G, H, I, K, L |
| III | M |
| IV | N |
| V | O |
| Planetary nebulae | P |
| Residual and peculiar spectra | Q |

### The Harvard spectral classification

In her 1901 classification of bright southern stars, Annie Jump Cannon consolidated and reordered the letter classes using the relative strengths of spectral features. The sequence that survives for ordinary stars is O, B, A, F, G, K, M. Some letters were retained for special spectra, including N for carbon stars in historical usage and P and Q for peculiar objects. The digits 0 to 9 order the subtypes within a class, so F2 falls near the hotter end of class F. The subdivisions do not imply equal steps in kelvin.

The nine-volume **Henry Draper Catalogue**, published by Cannon and Pickering in 1918–1924, gave spectral classifications for 225,300 stars. It reached approximately ninth magnitude in its photographic survey. The catalogue survives in identifiers such as HD 219134 ([Figure 35](fig35_spectroscopy_hdcatalogue)). The letter classes were empirical. Establishing how temperature controls their spectral features also made it possible to infer that stellar atmospheres are predominantly hydrogen and helium, as Cecilia Payne showed in 1925.[^ch09_class_history]

```{figure} _static/_chapter09/fig34_cannon.png
:width: 38%
:align: center
:name: fig34_spectroscopy_cannon

**Figure 34** Annie Jump Cannon developed the temperature-sensitive spectral sequence adopted in the Henry Draper Catalogue.
```

```{figure} _static/_chapter09/fig35_hdcatalogue.png
:width: 86%
:align: center
:name: fig35_spectroscopy_hdcatalogue

**Figure 35** A catalogue query for the star HD 219134. Its Henry Draper number identifies the object independently of the coordinate system used to report its position.
```


### The temperature sequence

The modern sequence runs from hot to cool, $\mathrm{O-B-A-F-G-K-M}$, with $\mathrm{L-T-Y}$ extending the sequence to cooler objects. The traditional mnemonic is *Oh Be A Fine Girl/Guy, Kiss Me*. **Early type** and **late type** describe position in this sequence and convey no age information. We group O, B, and A as early types for the following comparison. F, G, and K are the intermediate types discussed around the solar spectrum. The term *solar-type* is used more narrowly when a close resemblance to the Sun is required.

The spectral types are defined by comparison with standard spectra. Approximate temperatures describe the sequence, with some dependence on luminosity class, composition, and the calibration used. [Figure 36](fig36_spectroscopy_class_diagnostics) shows why one line usually cannot determine the type by itself. It is possible to obtain similar line strengths on both sides of a maximum, whereas a combination of features distinguishes the two regimes.[^ch09_harvard]

```{figure} _static/_chapter09/fig36_class_diagnostics.png
:width: 77%
:align: center
:name: fig36_spectroscopy_class_diagnostics

**Figure 36** Equivalent widths of selected spectral features along the temperature sequence. H I peaks near early A and molecular TiO becomes prominent at the cool end. Karttunen et al. (2017), Fig. 9.5, after Struve.
```


#### Early-type stars

| Type | Approximate $T_{\rm eff}$ | Characteristic optical features |
| --- | --- | --- |
| O | $\gtrsim30\,000\ \mathrm K$ | Blue. He II and lines of multiply ionized metals are conspicuous. He I strengthens towards late O, and the Balmer lines are comparatively weak. |
| B | $10\,000$–$30\,000\ \mathrm K$ | Blue-white. He II fades near the O–B boundary, with weak He II still detectable in the earliest B spectra. He I is strong near B2. The Balmer lines grow stronger towards A, and Ca II K becomes visible as the spectra cool. |
| A | $7500$–$10\,000\ \mathrm K$ | White. The Balmer lines reach maximum strength near early A. He I fades, Ca II H and K strengthen, and lines of neutral metals become visible. |

In [Figure 37](fig37_spectroscopy_ospectra), the balance of He I and He II changes across the O subtypes. The transition from late O to B is shown in [Figure 38](fig38_spectroscopy_obspectra). The spectra in [Figure 39](fig39_spectroscopy_baspectra) show the strengthening of the Balmer lines from B to A and the changing prominence of Ca II. The letters H and K in the Ca II doublet are the traditional Fraunhofer labels. The Ca II H line near $396.8\ \mathrm{nm}$ lies close to the hydrogen Balmer line $\mathrm{H}\epsilon$, so the two can blend.[^ch09_harvard]

```{figure} _static/_chapter09/fig37_ospectra.png
:width: 67%
:align: center
:name: fig37_spectroscopy_ospectra

**Figure 37** Main-sequence optical spectra from O4 to O9. Labels identify some of the helium and metal lines used to distinguish the subtypes. [Gray’s Digital Spectral Classification Atlas](https://ned.ipac.caltech.edu/level5/Gray/frames.html).
```

```{figure} _static/_chapter09/fig38_obspectra.png
:width: 67%
:align: center
:name: fig38_spectroscopy_obspectra

**Figure 38** Main-sequence optical spectra from O9 to B5. The relative strengths of the He I, He II, and Balmer lines change across the sequence. [Gray’s Digital Spectral Classification Atlas](https://ned.ipac.caltech.edu/level5/Gray/frames.html).
```

```{figure} _static/_chapter09/fig39_baspectra.png
:width: 67%
:align: center
:name: fig39_spectroscopy_baspectra

**Figure 39** Main-sequence optical spectra from B5 to A5. The broad Balmer absorption profiles are conspicuous in the A spectra. [Gray’s Digital Spectral Classification Atlas](https://ned.ipac.caltech.edu/level5/Gray/frames.html).
```


#### F, G, and K stars

| Type | Approximate $T_{\rm eff}$ | Characteristic optical features |
| --- | --- | --- |
| F | $6000$–$7500\ \mathrm K$ | Yellow-white. Balmer absorption weakens while Ca II H and K and many iron and other metal lines become prominent. |
| G | $4900$–$6000\ \mathrm K$ | Yellow. Metal lines are numerous, the CH G band is visible, and CN bands can be conspicuous, especially in giants. The Sun is a G star. |
| K | $3900$–$4900\ \mathrm K$ | Orange. Metal lines dominate the optical spectrum. Ca I near $422.7\ \mathrm{nm}$ and Ca II H and K are prominent. TiO bands begin to appear in some late K spectra. |

Here **metal lines** includes transitions from atoms and ions such as Ca I, Ca II, Fe I, and Fe II. The spectral sequence in [Figure 40](fig40_spectroscopy_fgkspectra) illustrates how the crowded metal-line spectrum develops as the hydrogen lines weaken.[^ch09_harvard]

```{figure} _static/_chapter09/fig40_fgkspectra.png
:width: 59%
:align: center
:name: fig40_spectroscopy_fgkspectra

**Figure 40** Main-sequence spectra from O5 V to M6 V in the near ultraviolet and violet. Compare the growing prominence of the metal-line spectrum in the F6 V, G5 V, and K5 V examples.
```


#### Late-type spectra

| Type | Approximate $T_{\rm eff}$ | Characteristic features |
| --- | --- | --- |
| M | $2400$–$3900\ \mathrm K$ | Red. Strong optical TiO bands, increasingly important VO in late M, and many neutral metal lines. |
| L | Roughly $1300$–$2300\ \mathrm K$ | TiO and VO fade along the sequence. Alkali lines such as Na I and K I are strong and broad in the optical, and metal hydrides and condensate clouds influence the spectra. |
| T | Roughly $500$–$1400\ \mathrm K$ | Brown dwarfs with strong near-infrared methane and water bands. |
| Y | Typically a few hundred kelvin | Very cool brown dwarfs distinguished by their near-infrared spectral morphology beyond late T. |

The boundaries are illustrative. The M–L and L–T transitions depend on gravity, composition, and atmospheric clouds. Some late-M objects are brown dwarfs and some early-L dwarfs sustain hydrogen fusion. The spectral type is assigned from the spectrum and does not by itself establish whether an object is stellar or substellar. [Figure 41](fig41_spectroscopy_ultracool) compares optical spectra across the M, L, and T sequence. Near-infrared spectra provide the strong $\mathrm{CH_4}$ and $\mathrm{H_2O}$ signatures of T dwarfs.[^ch09_ultracool]

```{figure} _static/_chapter09/fig41_ultracool.png
:width: 78%
:align: center
:name: fig41_spectroscopy_ultracool

**Figure 41** Optical spectra from late M through L and T. The labels identify molecular bands and atomic lines. Karttunen et al. (2017), Fig. 9.4b, from Kirkpatrick (2005).
```


#### Peculiar stars

The **C** and **S** classes describe cool stars whose chemistry produces different molecular bands at overlapping temperatures, often of order $3000\ \mathrm K$. In carbon-rich stars (C), strong $\mathrm{C}_2$, CN, and CH bands take the place of the prominent TiO absorption of oxygen-rich M stars. S stars show zirconium oxide (ZrO), often with bands of YO, LaO, or TiO ([Figure 42](fig42_spectroscopy_carbonstars) and [Figure 43](fig43_spectroscopy_sstars)). The carbon-to-oxygen ratio in an S-star atmosphere is typically nearer unity than in an ordinary oxygen-rich giant. Historical catalogues also used Q for some unusual spectra including novae, and P for planetary nebulae. Wolf–Rayet stars use separate classifications such as WN and WC.[^ch09_peculiar]

```{figure} _static/_chapter09/fig42_carbonstars.png
:width: 65%
:align: center
:name: fig42_spectroscopy_carbonstars

**Figure 42** Two examples of carbon-star spectra, 19 Psc and RS Cyg. The labels mark molecular and atomic features. [Gray’s Digital Spectral Classification Atlas](https://ned.ipac.caltech.edu/level5/Gray/frames.html).
```

```{figure} _static/_chapter09/fig43_sstars.png
:width: 65%
:align: center
:name: fig43_spectroscopy_sstars

**Figure 43** Two examples of S-star spectra, V Cnc and $\pi^1$ Ori. Bands of ZrO are prominent. [Gray’s Digital Spectral Classification Atlas](https://ned.ipac.caltech.edu/level5/Gray/frames.html).
```


#### Main-sequence properties

Mass, radius, and luminosity vary systematically along the **main sequence**, as illustrated below. The numerical ranges are representative and depend on age and composition. An evolved star of the same spectral type can have a very different radius and luminosity. The last column gives the order of magnitude of the fractions in a local census by number. The fractions depend on the sampled volume and the completeness for faint stars. In a bright apparent-magnitude-limited sample, luminous stars are represented over a much larger volume.[^ch09_census]

| Type | Approximate $T_{\rm eff}$ (K) | Colour | $M_\star/M_\odot$ | $R_\star/R_\odot$ | $L/L_\odot$ | Balmer lines | Approx. local fraction |
| --- | ---: | --- | ---: | ---: | ---: | --- | ---: |
| O | $\gtrsim30\,000$ | Blue | $\gtrsim16$ | $\gtrsim6.6$ | $\gtrsim3\times10^4$ | Weak | $\ll0.1\%$ |
| B | $10\,000$–$30\,000$ | Blue-white | $2.1$–$16$ | $1.8$–$6.6$ | $25$–$3\times10^4$ | Moderate | $\sim0.1\%$ |
| A | $7500$–$10\,000$ | White | $1.4$–$2.1$ | $1.4$–$1.8$ | $5$–$25$ | Strong | $\sim0.6\%$ |
| F | $6000$–$7500$ | Yellow-white | $1.0$–$1.4$ | $1.1$–$1.4$ | $1.5$–$5$ | Moderate | $\sim3\%$ |
| G | $4900$–$6000$ | Yellow | $0.8$–$1.0$ | $0.9$–$1.1$ | $0.6$–$1.5$ | Weak | $\sim8\%$ |
| K | $3900$–$4900$ | Orange | $0.45$–$0.8$ | $0.7$–$0.9$ | $0.08$–$0.6$ | Very weak | $\sim12\%$ |
| M | $2400$–$3900$ | Orange-red | $0.08$–$0.45$ | $\lesssim0.7$ | $\lesssim0.08$ | Very weak | $\sim76\%$ |

### The Yerkes spectral classification

William W. Morgan, Philip C. Keenan, and Edith Kellman developed a two-dimensional classification at Yerkes Observatory. The original system is known as **MKK** and its subsequent form as **MK**. The spectral type describes the temperature-sensitive morphology, and the luminosity class describes the gravity-sensitive morphology.

| Luminosity class | Description |
| --- | --- |
| Ia | More luminous supergiants |
| Iab | Intermediate supergiants |
| Ib | Less luminous supergiants |
| II | Bright giants |
| III | Giants |
| IV | Subgiants |
| V | Main-sequence stars, also called dwarfs |

At comparable effective temperature, a giant or supergiant has a larger radius and usually a lower surface gravity than a main-sequence star. The lower atmospheric pressure changes the ionization balance and broadening. Depending on the transition, an absorption feature can strengthen or weaken. The profiles of $\mathrm H\gamma$ in [Figure 44](fig44_spectroscopy_luminosityclass) illustrate the weaker and narrower Balmer absorption in the more luminous A-type example. Other criteria use the relative strengths of selected metal lines. The class is assigned by comparison with spectral standards. Combining the type and luminosity class gives, for example, G2 V for the Sun and A1 V for Sirius A. The white dwarf Sirius B belongs to a separate classification.[^ch09_mk]

```{figure} _static/_chapter09/fig44_luminosityclass.png
:width: 61%
:align: center
:name: fig44_spectroscopy_luminosityclass

**Figure 44** The H$\gamma$ line in three A-star spectra. The supergiant HD 223385 has $W=0.19\ \mathrm{nm}$, while the main-sequence example $\alpha^2$ Geminorum has $W=1.66\ \mathrm{nm}$. Karttunen et al. (2017), Fig. 9.6.
```


## The Hertzsprung–Russell diagram

Around 1910 Ejnar Hertzsprung and Henry Norris Russell independently studied the relation between spectral type and stellar absolute magnitude. A physical **Hertzsprung–Russell diagram** plots bolometric luminosity against effective temperature. Temperature increases towards the left and luminosity towards the top. Absolute magnitude and spectral type give a related observational representation, with brighter stars at smaller absolute magnitude.

The stars occupy recognisable regions ([Figure 45](fig45_spectroscopy_hr)). The **main sequence** goes from hot, luminous O stars to cool, faint M dwarfs. Low-temperature G, K, and M giants lie above dwarfs of the same type. **Supergiants** occupy a wide range of temperatures at high luminosities. **White dwarfs** can be hot and faint, as Sirius B illustrates. The Stefan–Boltzmann relation connects position in the diagram to radius,

$$
L=4\pi R_\star^2\sigma T_{\rm eff}^4.
$$

At a given $T_{\rm eff}$, greater $L$ therefore requires a larger radius. A supergiant such as Betelgeuse can be cool and luminous because it has a large emitting surface. The position of a star also depends on its mass, composition, and evolutionary state. A star changes position as its internal energy sources and structure evolve.[^ch09_hr]

```{figure} _static/_chapter09/fig45_hr.png
:width: 82%
:align: center
:name: fig45_spectroscopy_hr

**Figure 45** Hertzsprung–Russell diagram with the main sequence, giants, supergiants, and white dwarfs. Diagonal lines mark constant radius, and mass and lifetime labels along the main sequence are illustrative.
```


### Colour–magnitude diagrams and globular clusters

A **colour–magnitude diagram** (CMD) uses measured quantities. In [Figure 46](fig46_spectroscopy_cmd) we plot apparent $V$ against $B-V$, with brighter stars higher and bluer stars to the left. For the members of a cluster, distance is approximately common and contributes nearly the same distance modulus to every magnitude. If foreground extinction is approximately uniform, it shifts the CMD by nearly the same amount for each member. The cluster CMD then traces the distribution in luminosity and temperature up to the transformations from $V$ and $B-V$ to physical quantities. This is why a CMD can show narrow sequences even when the individual stellar distances are poorly known.[^ch09_cluster]

```{figure} _static/_chapter09/fig46_cmd.png
:width: 66%
:align: center
:name: fig46_spectroscopy_cmd

**Figure 46** A globular-cluster colour–magnitude diagram. Each point gives the apparent $V$ and colour $B-V$ of a star. The main sequence (MS), subgiant branch (SGB), red giant branch (RGB), horizontal branch (HB), asymptotic giant branch (AGB), and blue stragglers (BS) are labelled.
```

```{figure} _static/_chapter09/fig47_messier10.png
:width: 66%
:align: center
:name: fig47_spectroscopy_messier10

**Figure 47** The central region of the globular cluster Messier 10 (NGC 6254) observed with Hubble. Credit ESA/Hubble & NASA. [ESA/Hubble image record](https://esahubble.org/images/potw1225a/).
```


A **globular cluster** is a densely populated gravitationally bound stellar system, as shown by the Hubble image of Messier 10 ([Figure 47](fig47_spectroscopy_messier10)). Many Milky Way globular clusters are around ten billion years old or older. Their populations are approximately coeval for the purpose of reading the main-sequence turn-off. Several clusters contain subpopulations with measurable differences in helium and light-element abundances, even where iron is nearly uniform.

The **turn-off** is where the most massive stars still burning hydrogen in their cores leave the main sequence. Its location depends on the age and composition of the cluster. In an old cluster, stars in the mass range now evolving away from the turn-off can pass through the following regions.

1. **Subgiant branch (SGB).** After core hydrogen exhaustion, the envelope expands and the star moves towards cooler temperatures.
2. **Red giant branch (RGB).** The star becomes more luminous as hydrogen burns in a shell around an inert helium core.
3. **Horizontal branch (HB).** After helium ignition, helium burns in the core and hydrogen can continue burning in a shell. The range of envelope masses helps explain the spread in colour.
4. **Asymptotic giant branch (AGB).** After core helium exhaustion, stars that develop an AGB have hydrogen- and helium-burning shells around a largely inert carbon–oxygen core.

The **blue stragglers** (BS) lie above and to the blue of the turn-off. Collisions or mergers and mass transfer in binaries can produce stars more massive than the turn-off stars. The luminous young supergiants seen in diagrams of mixed populations are absent from a typical old globular cluster, where the massive short-lived progenitors have already evolved.[^ch09_cluster]

[^ch09_lines]: Karttunen et al. (2017), *Fundamental Astronomy*, §§5.1 and 16.2. Barbieri and Bertini (2021), *Fundamentals of Astronomy*, §17.5.
[^ch09_history]: Barbieri and Bertini (2021), §17.1, pp. 273–275 (PDF pp. 292–294). Seeds, Backman, and Wegryn (2026), *Foundations of Astronomy*, §7-3, pp. 143–145 (PDF pp. 164–166).
[^ch09_photosphere]: Hanslmeier (2023), *Introduction to Astronomy and Astrophysics*, §7.2.3, pp. 261–263 (PDF pp. 278–280), and §9.3. Seeds et al. (2026), §7-3, pp. 143–145 (PDF pp. 164–166).
[^ch09_nebulae]: Karttunen et al. (2017), §16.2. [NASA, NGC 2392 and its narrow-band images](https://science.nasa.gov/asset/hubble/ngc-2392/). [NASA, shock-excited gas in the Veil Nebula](https://science.nasa.gov/missions/hubble/uncovering-the-veil-nebula/).
[^ch09_resolution]: Karttunen et al. (2017), §9.1, pp. 227–229 (PDF pp. 236–238). [Robertson (2013), resolving power for different instrument profiles](https://arxiv.org/abs/1308.0871).
[^ch09_sampling]: [Robertson (2017), detector sampling of optical and infrared spectra](https://doi.org/10.1017/pasa.2017.29).
[^ch09_optics]: Barbieri and Bertini (2021), §17.1, pp. 274–276 (PDF pp. 293–295). Hanslmeier (2023), §5.5, pp. 145–149 (PDF pp. 162–166).
[^ch09_sn1987a]: [NASA, direct imaging of the rings of SN 1987A](https://science.nasa.gov/missions/hubble/hubble-finds-mysterious-ring-structure-around-supernova-1987a/). [STScI, Hubble Legacy Archive grism display](https://archive.stsci.edu/mug/mug_2008/hla_mug2008.pdf).
[^ch09_slit]: Barbieri and Bertini (2021), §17.1. [NASA, spectroscopy with Hubble and STIS](https://science.nasa.gov/mission/hubble/science/science-behind-the-discoveries/hubble-spectroscopy/).
[^ch09_echelle]: Hanslmeier (2023), §5.5, pp. 146–149 (PDF pp. 163–166). [ESO, ESPRESSO modes](https://eso.org/sci/facilities/paranal/instruments/espresso/overview.html). [STScI, STIS E140H](https://hst-docs.stsci.edu/stisihb/chapter-13-spectroscopic-reference-material/13-3-gratings/echelle-grating-e140h).
[^ch09_ifu]: [STScI, NIRSpec integral field unit](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-instrumentation/nirspec-integral-field-unit).
[^ch09_mos]: [ESO, FLAMES and GIRAFFE](https://www.eso.org/sci/facilities/paranal/instruments/flames/overview.html). [ESO, 4MOST on VISTA](https://eso.org/sci/facilities/paranal/instruments/4most.html).
[^ch09_analysis]: Hanslmeier (2023), §§9.6–9.7, pp. 364–367 (PDF pp. 381–384). Barbieri and Bertini (2021), §§17.2 and 17.5, pp. 277–279 and 288–291 (PDF pp. 296–298 and 307–310).
[^ch09_carbon]: [Jacobson et al. (2015), high-resolution spectroscopy of SkyMapper metal-poor candidates, Fig. 3](https://doi.org/10.1088/0004-637X/807/2/171).
[^ch09_ew]: Barbieri and Bertini (2021), §17.2, pp. 278–279 (PDF pp. 297–298). Hanslmeier (2023), §§9.5–9.6, pp. 359–366 (PDF pp. 376–383). [Sousa (2014), stellar parameters from equivalent widths](https://arxiv.org/abs/1407.5817).
[^ch09_doppler]: Seeds et al. (2026), §7-3, pp. 145–148 (PDF pp. 166–169).
[^ch09_class_history]: Karttunen et al. (2017), §9.2, pp. 229–232 (PDF pp. 238–241). [Pickering (1890), *The Draper Catalogue of Stellar Spectra*](https://books.google.com/books/about/The_Draper_Catalogue_of_Stellar_Spectra.html?id=gzwhAQAAMAAJ). [Harvard, Anna Palmer Draper and the catalogues](https://library.cfa.harvard.edu/women-at-hco/anna-palmer-draper). [Harvard, archival record of the 225,300 classifications](https://hollisarchives.lib.harvard.edu/catalog/hua27019). [Payne (1925), *Stellar Atmospheres*](https://ui.adsabs.harvard.edu/abs/1925PhDT.........1P/abstract).
[^ch09_harvard]: Karttunen et al. (2017), §9.2, pp. 229–232 (PDF pp. 238–241). Barbieri and Bertini (2021), §17.6, pp. 291–294 (PDF pp. 310–313). [Pecaut and Mamajek (2013), dwarf colour and temperature calibration](https://www.pas.rochester.edu/~mpecaut/tmp/pecaut_mamajek_2013.pdf).
[^ch09_ultracool]: Barbieri and Bertini (2021), §17.7, p. 294 (PDF p. 313). Seeds et al. (2026), §9-3, pp. 189–190 (PDF pp. 210–211). [Cushing et al. (2011), identification of the Y spectral class](https://arxiv.org/abs/1108.4678).
[^ch09_peculiar]: Karttunen et al. (2017), §§9.2 and 9.4, pp. 230 and 234–235 (PDF pp. 239 and 243–244). Barbieri and Bertini (2021), §17.9, pp. 295–296 (PDF pp. 314–315).
[^ch09_census]: Barbieri and Bertini (2021), §17.6, pp. 292–293 (PDF pp. 311–312). Seeds et al. (2026), §§9-3, 9-4, and 9-6. [Mamajek, mean dwarf spectral sequence](https://www.pas.rochester.edu/~emamajek/doc.html).
[^ch09_mk]: Karttunen et al. (2017), §9.3, pp. 232–234 (PDF pp. 241–243). Barbieri and Bertini (2021), §17.6, pp. 291–294 (PDF pp. 310–313). [SIMBAD, published classifications of Sirius A](https://simbad.u-strasbg.fr/simbad/sim-id?Ident=Sirius&submit=display+all+measurements).
[^ch09_hr]: Barbieri and Bertini (2021), §16.8, pp. 261–262 (PDF pp. 280–281). Karttunen et al. (2017), §9.5, pp. 235–237 (PDF pp. 244–246). Hanslmeier (2023), §8.5.2, pp. 320–321 (PDF pp. 337–338).
[^ch09_cluster]: Karttunen et al. (2017), §17.3, pp. 363–365 (PDF pp. 367–369). Seeds et al. (2026), §12-3 and Concept Art 12A, pp. 270–273 (PDF pp. 291–294). [Gratton, Carretta, and Bragaglia (2012), multiple populations](https://arxiv.org/abs/1201.6526). [Ferraro et al. (2009), two blue-straggler sequences in M30](https://arxiv.org/abs/1001.1096).
