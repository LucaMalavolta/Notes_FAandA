(chapter08_photometric_concepts)=

# Photometric Concepts

:::{danger}
This page still needs substantial revision to match the content presented during the lectures
:::

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

**Photometry** is the quantitative measurement of light. The stellar field in [Figure 1](fig01_photometry_stellar_field) shows stars with different apparent brightnesses and colours. Turning these differences into measurements requires us to specify both the radiation arriving at the telescope and the instrument's response. We begin with the geometrical definition of intensity, then develop the magnitude scale and the use of photometric bands. These quantities allow us to compare stellar temperatures, estimate distances, and describe the brightness of extended objects.

```{figure} _static/_chapter08/fig01_stellar_field.png
:width: 82%
:align: center
:name: fig01_photometry_stellar_field

**Figure 1** A crowded stellar field. The range of apparent brightnesses and colours motivates measurements in more than one photometric band.
```

## Measuring radiation

### Specific intensity

Consider a small surface element $\mathrm{d}A$ with a specified normal. Radiation crossing the element in a direction that makes an angle $\theta$ with the normal passes through the projected area $\mathrm{d}A_\perp=\mathrm{d}A\cos\theta$ ([Figure 2](fig02_photometry_specific_intensity_geometry)). Choose a small solid angle $\mathrm{d}\omega$ about this direction and a frequency interval $[\nu,\nu+\mathrm{d}\nu]$. The energy crossing the element in time $\mathrm{d}t$ is

$$
\mathrm{d}E
=I_\nu\,\cos\theta\,\mathrm{d}A\,\mathrm{d}\omega\,\mathrm{d}\nu\,\mathrm{d}t .
$$

The **specific intensity** $I_\nu$, also called **spectral radiance**, is the radiant power per unit projected area, per unit solid angle, and per unit frequency. It is a function of the position, direction, and frequency at which we measure the radiation field. Its SI unit is $\mathrm{W\,m^{-2}\,Hz^{-1}\,sr^{-1}}$. Integrating over frequency gives the **bolometric intensity**,

$$
I=\int_0^\infty I_\nu\,\mathrm{d}\nu,
\qquad [I]=\mathrm{W\,m^{-2}\,sr^{-1}}.
$$

A wavelength density $I_\lambda$ describes the same radiation. The bin widths satisfy $I_\nu\,|\mathrm{d}\nu|=I_\lambda\,|\mathrm{d}\lambda|$, with $\nu=c/\lambda$. Both densities therefore give the same bolometric intensity when integrated over their respective variables.[^ch08_intensity]

```{figure} _static/_chapter08/fig02_specific_intensity_geometry.png
:width: 45%
:align: center
:name: fig02_photometry_specific_intensity_geometry

**Figure 2** Radiation crossing an area $\mathrm{d}A$ within a solid angle $\mathrm{d}\omega$. The angle $\theta$ is measured from the normal to the surface. Karttunen et al. (2017), Fig. 4.1.
```

### The Sun as an example

Take $\mathrm{d}A$ on the solar photosphere and an observer at a distance $r$ much larger than the solar radius. Near the centre of the apparent disc the line of sight is nearly normal to the surface. Towards the limb the same physical area has a smaller projection, $\mathrm{d}A\cos\theta$, and subtends an apparent solid angle $\mathrm{d}\omega_{\rm src}=\mathrm{d}A\cos\theta/r^2$ at the observer. In the emission geometry the detector, viewed from the emitting element, instead subtends $\mathrm{d}\omega_{\rm det}\simeq\mathrm{d}A_{{\rm det},\perp}/r^2$. The solid angle in the definition is always taken about the rays at the position where the intensity is specified. A change in the measured intensity across the visible disc can also come from the solar atmosphere itself, as in limb darkening.[^ch08_sun]

The appearance of the Sun changes with the wavelength of the observation ([Figure 3](fig03_photometry_sun_multiband)). Visible light reveals the photosphere. Ultraviolet and X-ray measurements can probe hotter plasma above it, with the sampled structures depending on the band. Solar Orbiter illustrates how a single mission can combine measurements in several spectral regions ([Figure 4](fig04_photometry_solar_orbiter)).

```{figure} _static/_chapter08/fig03_sun_multiband.png
:width: 55%
:align: center
:name: fig03_photometry_sun_multiband

**Figure 3** Composite view of the Sun. The visible disc and the higher-energy emission show different structures. The colours distinguish the wavelength regions in this representation.
```

```{figure} _static/_chapter08/fig04_solar_orbiter.png
:width: 52%
:align: center
:name: fig04_photometry_solar_orbiter

**Figure 4** The Solar Orbiter spacecraft. Its instruments observe the Sun in several spectral regions. [ESA mission overview](https://www.esa.int/Science_Exploration/Space_Science/Solar_Orbiter).
```

### An isotropic field and an isotropic source

A radiation field is **isotropic** at a point if $I_\nu$ has the same value in every direction there. An ideal blackbody cavity in equilibrium is an example ([Figure 5](fig05_photometry_isotropic_radiation_field)). Every ray crossing a small plane has an equal counterpart crossing it in the opposite direction, so the net flux through the plane is zero even though the intensity is nonzero.

An **isotropic source** emits the same power per unit solid angle in every direction. A spherically symmetric star is described this way when viewed from far outside its surface. At an exterior point, photons from the star reach the observer from the directions occupied by its disc and propagate away from the star ([Figure 6](fig06_photometry_isotropic_source)). For a distant unresolved source this reduces to a beam along the radial direction.

```{figure} _static/_chapter08/fig05_isotropic_radiation_field.png
:width: 48%
:align: center
:name: fig05_photometry_isotropic_radiation_field

**Figure 5** Directions of propagation in a schematic isotropic radiation field. At a given point there is no preferred direction.
```

```{figure} _static/_chapter08/fig06_isotropic_source.png
:width: 48%
:align: center
:name: fig06_photometry_isotropic_source

**Figure 6** Radiation propagating away from a source that emits equally in all directions. The direction of propagation at each exterior point is radial.
```

### Flux density

The **spectral flux density** $F_\nu$ is obtained by integrating the intensity over propagation directions, with the projection factor for the surface of interest. For net flux through an oriented plane we integrate over all directions, so incoming and outgoing contributions carry opposite signs. For the outward flux from a stellar surface we integrate the emergent intensity over the outward hemisphere. For incident flux through a detector, orient the normal into the detector so that rays entering from the source have a positive projection. In the corresponding angular domain $\Omega$ we can write

$$
F_\nu=\int_\Omega I_\nu\cos\theta\,\mathrm{d}\omega,
\qquad
F=\int_0^\infty F_\nu\,\mathrm{d}\nu .
$$

For example, a direction-independent intensity over the outward hemisphere gives $F_\nu=\pi I_\nu$. The two flux units are $[F_\nu]=\mathrm{W\,m^{-2}\,Hz^{-1}}$ and $[F]=\mathrm{W\,m^{-2}}$. The **jansky** is a unit of spectral flux density, frequently used in radio and infrared astronomy,

$$
1\ \mathrm{Jy}=10^{-26}\ \mathrm{W\,m^{-2}\,Hz^{-1}}.
$$

The steradian remains in the unit of $I_\nu$ until the angular integration is performed.

The arrows in [Figure 7](fig07_photometry_inverse_square_law) illustrate why the received flux from a point source decreases as $r^{-2}$ in free space. The power within a fixed solid angle is conserved. The area occupied by the bundle grows as $r^2$, so the power received by a fixed unit area falls as $r^{-2}$.

```{figure} _static/_chapter08/fig07_inverse_square_law.png
:width: 68%
:align: center
:name: fig07_photometry_inverse_square_law

**Figure 7** Geometrical dilution. The same bundle of rays covers areas in the ratio $1:4:9$ at distances $r$, $2r$, and $3r$.
```

The Sun provides a numerical example. The nominal total solar irradiance at $1\ \mathrm{au}$ above the Earth's atmosphere is $1361\ \mathrm{W\,m^{-2}}$ on a plane perpendicular to the rays. This reference value is often called the *solar constant*. The irradiance at Earth changes through the year because the orbit is eccentric. Its geometrical dependence is $F_\odot(r)=F_\odot(1\,\mathrm{au})(1\,\mathrm{au}/r)^2$, apart from changes in the Sun's output.[^ch08_solar_units]

### Radiant power and luminosity

At distance $r$, an area of a spherical surface subtending a solid angle $\omega$ at the source is $r^2\omega$. If the radial flux $F$ is uniform over that area, the power passing through it is $P_\omega=Fr^2\omega$. The **luminosity** $L$ is the total radiant power emitted by the source. For a steady isotropic source surrounded by a transparent medium, the same power passes through every sphere centred on it ([Figure 8](fig08_photometry_flux_and_luminosity)). Hence

$$
\boxed{L=4\pi r^2F},
\qquad
L_\nu=4\pi r^2 F_\nu .
$$

Here $L$ is in watts and $L_\nu$ in $\mathrm{W\,Hz^{-1}}$. The nominal solar luminosity is $L_\odot^{\rm N}=3.828\times10^{26}\ \mathrm{W}$. It is consistent with the nominal irradiance at $1\ \mathrm{au}$ to the quoted precision.

```{figure} _static/_chapter08/fig08_flux_and_luminosity.png
:width: 55%
:align: center
:name: fig08_photometry_flux_and_luminosity

**Figure 8** A star of luminosity $L$ illuminates a sphere of area $4\pi r^2$. The received flux $F$ is the power per unit area of the sphere.
```

:::{note}
Astronomers frequently use *flux* for power per unit area and *flux density* for the spectral quantity per hertz or per unit wavelength. In this chapter $F$ is a flux in $\mathrm{W\,m^{-2}}$, $F_\nu$ and $F_\lambda$ are spectral flux densities, and $L$ is a luminosity in watts. Some texts use *radiant flux* for power itself.
:::

## The magnitude scale

### Definition of magnitude

The historical classification of naked-eye stars into six brightness classes is traditionally associated with Hipparchus and survives in Ptolemy's catalogue. First-magnitude stars were the brightest and sixth-magnitude stars the faintest visible. These classes describe apparent brightness. In 1856 Norman R. Pogson formalised the scale by assigning exactly a factor of $100$ in received flux to a difference of five magnitudes. In the Weber–Fechner law, a change in perceived sensation is proportional to $\ln(S/S_0)$, where $S$ is the physical stimulus and $S_0$ is a reference stimulus. This relation gives historical context for the logarithmic scale. The coefficient $2.5$ in the modern scale follows from Pogson's convention, $2.5\log_{10}100=5$.[^ch08_magnitude]

Let $F_0$ be the flux corresponding to magnitude zero for a specified measurement. Then the **apparent magnitude** is

$$
\boxed{m=-2.5\log_{10}\!\left(\frac{F}{F_0}\right)}.
$$

The argument of the logarithm is dimensionless. Greater received flux gives a smaller magnitude. Sources brighter than the zero point have negative magnitudes. The successive traditional classes are illustrated in [Figure 9](fig09_photometry_pogson_scale).

```{figure} _static/_chapter08/fig09_pogson_scale.png
:width: 52%
:align: center
:name: fig09_photometry_pogson_scale

**Figure 9** The six traditional magnitude classes on the Pogson scale. The graphic gives rounded brightness factors. Each step towards fainter magnitudes divides the received flux by $100^{1/5}$. Credit space.fm.
```

### Comparing apparent magnitudes

For two sources measured at the same wavelength, or through the same photometric band, the zero point cancels. Writing $F_1$ and $F_2$ for the two consistently defined fluxes or flux densities gives

$$
m_1-m_2=-2.5\log_{10}\!\left(\frac{F_1}{F_2}\right),
\qquad
\frac{F_1}{F_2}=10^{-0.4(m_1-m_2)}.
$$

If source 1 is brighter, $m_1<m_2$. In the table the positive difference is defined as $\Delta m=m_2-m_1$.

| $\Delta m$ | $F_1/F_2$ |
|:---:|---:|
| $1$ | $100^{1/5}\simeq 2.512$ |
| $2.5$ | $10$ |
| $5$ | $100$ |

[Figure 10](fig10_photometry_apparent_magnitudes) places familiar objects on the scale. The full Moon is near $-13$, Sirius near $-1.5$, and Polaris near $+2$. A commonly quoted naked-eye limit is about $+6$ under good conditions. A limiting magnitude is a property of an observation as well as of the instrument. Sky brightness, exposure time, wavelength band, and the required significance of the detection all affect it.

```{figure} _static/_chapter08/fig10_apparent_magnitudes.png
:width: 78%
:align: center
:name: fig10_photometry_apparent_magnitudes

**Figure 10** Examples of apparent magnitudes, including the full Moon, the brightest planets, and bright stars. The limiting magnitudes for binoculars and telescopes are illustrative. [OpenStax, *Astronomy 2e*, Fig. 17.2](https://openstax.org/books/astronomy-2e/pages/17-1-the-brightness-of-stars).
```

### Bolometric magnitude

The **bolometric magnitude** corresponds to the flux integrated over the whole electromagnetic spectrum. Even above the atmosphere, an observation generally covers a limited range of wavelengths. Observations from the ground also lose access to regions where the atmosphere absorbs strongly. To estimate the bolometric magnitude, we can start from a standard-band magnitude such as $V$ and use a **bolometric correction**. We adopt the convention[^ch08_bolometric]

$$
\boxed{BC_V=m_{\rm bol}-V},
\qquad
m_{\rm bol}=V+BC_V.
$$

The correction depends on the fraction of the radiation sampled by the band and on the zero points of the two scales. With the IAU bolometric scale the zero point for apparent bolometric magnitude is $F_{{\rm bol},0}\simeq2.5180\times10^{-8}\ \mathrm{W\,m^{-2}}$. For the Sun, the nominal irradiance gives $m_{{\rm bol},\odot}\simeq-26.832$. A zero correction assigned to an F5 reference star belongs to a historical calibration. With a specified contemporary zero point its value follows from the adopted $V$ system and the stellar spectrum.

Hot stars emit a substantial fraction of their power shortward of the visual band. Cool stars emit a substantial fraction in the infrared. [Figure 11](fig11_photometry_bolometric_correction) illustrates how $BC_V$ can become more negative at either end of the temperature range. Estimating the correction requires an effective temperature or a calibrated proxy such as colour. The calibration can also depend on surface gravity and chemical composition.

```{figure} _static/_chapter08/fig11_bolometric_correction.png
:width: 62%
:align: center
:name: fig11_photometry_bolometric_correction

**Figure 11** Visual bolometric correction plotted against $\log_{10}(T_{\rm eff}/\mathrm{K})$ for several luminosity classes. The plotted sign corresponds to $BC_V=m_{\rm bol}-V$. The temperature axis runs from hot to cool.
```

## Photometric systems

### Why the passband matters

A **spectral energy distribution** (SED) describes how the energy flux from a source is distributed with wavelength or frequency. The stellar spectra in [Figure 12](fig12_photometry_stellar_spectra) have different continuum shapes and absorption features. Two stars with the same measured flux in one band can therefore have different fluxes in another. A photometric system specifies its passbands and the magnitude zero point for each band. In a system based on a reference star, the reference signal itself depends on the response of the band. Other systems can use a mathematically defined reference spectrum.

Historically, reproducing a system meant reproducing or calibrating the response of a particular combination of telescope optics, filters, and detector. Small differences matter because their effects depend on the shape of the observed spectrum.[^ch08_systems]

```{figure} _static/_chapter08/fig12_stellar_spectra.png
:width: 78%
:align: center
:name: fig12_photometry_stellar_spectra

**Figure 12** Optical spectra of stars spanning several temperatures and luminosity classes. The curves are offset vertically. The continuum shapes and absorption features vary across the wavelength interval.
```

### Visual, photographic, and photovisual magnitudes

The **visual magnitude** $m_{\rm v}$ represents observations with the eye. Under daylight conditions the standard photopic response peaks at about $555\ \mathrm{nm}$. Dark-adapted vision has a different response, with the scotopic peak near $507\ \mathrm{nm}$.

Early unfiltered photographic emulsions were relatively sensitive to blue and near-ultraviolet light. They gave the **photographic magnitude** $m_{\rm pg}$. A suitable combination of filter and emulsion could reproduce a response closer to visual observations and yielded the **photovisual magnitude** $m_{\rm pv}$. [Figure 13](fig13_photometry_historical_spectral_sensitivity) illustrates a historical photographic response with silver-nitrate collodion. Its comparison curve is for a conventional digital camera. The response of each recording system is specific to its materials and optics.[^ch08_detectors]

```{figure} _static/_chapter08/fig13_historical_spectral_sensitivity.png
:width: 68%
:align: center
:name: fig13_photometry_historical_spectral_sensitivity

**Figure 13** Relative spectral sensitivities of a silver-nitrate collodion camera and a standard digital single-lens reflex camera. The collodion response extends farther into the ultraviolet and falls off sharply towards the red.
```

### Calibration and synthetic photometry

A modern system is characterised by the **total spectral response** of the observing system and by its zero points. Observations of standard stars with known magnitudes tie instrumental measurements to the standard scale. For ground-based observations, standards can also help determine the extinction with airmass. When the instrumental and standard passbands differ slightly, the transformation often includes a colour term. Such a term is calibrated over the range of colours represented by the standards and works best for spectra similar to those of the calibration stars.

The Landolt standards illustrate the use of a network of stars with measured magnitudes and colours ([Figure 14](fig14_photometry_landolt_standards)). The T Phe field shown here is well south of the equator and is part of the wider set of Landolt standards. Measurements in several bands allow one to calibrate both a zero point and a term that varies with stellar colour.[^ch08_landolt]

```{figure} _static/_chapter08/fig14_landolt_standards.png
:width: 100%
:align: center
:name: fig14_photometry_landolt_standards

**Figure 14** Standard-star magnitudes and colours in the T Phe field. The rows give positions, $V$ magnitudes, colour indices, and measurement uncertainties. The field is at a declination of about $-46^\circ$.
```

With a known response, we can also start from an observed or model spectrum and predict a magnitude. This procedure is called **synthetic photometry**. To compare a theoretical stellar population with observations, for example, one integrates the model spectra through the chosen observational bands and applies the corresponding zero points. [Figure 15](fig15_photometry_population_synthesis_spectra) compares population spectra computed with two sets of evolutionary tracks. The CMD interface applies synthetic transformations to stellar models to produce isochrones in a chosen photometric system. The revised Gaia DR2 curves provide an example of the response required for such a calculation ([Figure 19](fig19_photometry_gaia_dr2_passbands)). [CMD interface](https://stev.oapd.inaf.it/cmd)

```{figure} _static/_chapter08/fig15_population_synthesis_spectra.png
:width: 85%
:align: center
:name: fig15_photometry_population_synthesis_spectra

**Figure 15** Synthetic spectra of stellar populations at several ages, calculated with Geneva and Padova evolutionary tracks. Their different spectral shapes lead to different synthetic colours when integrated through the same passbands.
```

### The Johnson–Morgan system

The early Johnson–Morgan system introduced three broad bands, $U$ for ultraviolet, $B$ for blue, and $V$ for visual ([Figure 16](fig16_photometry_ubv_passbands)). The width and shape of each passband are important. A single representative wavelength is useful when describing the spectral region sampled by a measurement, but several definitions are possible.[^ch08_ubv]

```{figure} _static/_chapter08/fig16_ubv_passbands.png
:width: 63%
:align: center
:name: fig16_photometry_ubv_passbands

**Figure 16** Illustrative transmission curves for the Johnson–Morgan $U$, $B$, and $V$ bands. The bands span finite wavelength intervals and overlap.
```

In the table, $\Delta\lambda$ is the indicative wavelength interval of the response, FWHM is its full width at half maximum, and $\lambda_{\max}$ is the wavelength of maximum response. The mean wavelength $\langle\lambda\rangle$ weights each wavelength by the response. The effective wavelength $\lambda_{\rm eff}$ further weights it by the source spectrum. For a weighting function $W(\lambda)$ used to define the band signal,

$$
\langle\lambda\rangle
=\frac{\int \lambda W(\lambda)\,\mathrm{d}\lambda}
       {\int W(\lambda)\,\mathrm{d}\lambda},
\qquad
\lambda_{\rm eff}
=\frac{\int \lambda\,F_\lambda W(\lambda)\,\mathrm{d}\lambda}
       {\int F_\lambda W(\lambda)\,\mathrm{d}\lambda}.
$$

The tabulated values use the convention of Barbieri and Bertini, in which the weighting function is the adopted band response. For a photon-counting signal one uses the corresponding photon weighting. The effective wavelength specifies the mean wavelength of the weighted signal under that convention. The full passband still determines the magnitude.

| Band | $\Delta\lambda$ | FWHM | $\lambda_{\max}$ | $\langle\lambda\rangle$ | $\lambda_{\rm eff}$ at $25\,000 / 10\,000 / 4\,000\ \mathrm{K}$ |
|:---:|:---:|---:|---:|---:|:---:|
| $U$ | 3100–4000 | 600 | 3670 | 3680 | 3550 / 3650 / 3800 |
| $B$ | 3750–5350 | 1000 | 4295 | 4450 | 4330 / 4400 / 4500 |
| $V$ | 4950–6350 | 850 | 5450 | 5460 | 5470 / 5480 / 5510 |

All wavelengths and widths are in ångströms. These are indicative values for a particular realisation. The $U$ example makes the dependence on the incident spectrum clear: the effective wavelength moves from about $3550$ to $3800\ \text{Å}$ as the temperature in the tabulation falls from $25\,000$ to $4\,000\ \mathrm{K}$.

### The Johnson–Cousins–Glass system

The Johnson system was extended to red and infrared wavelengths. In the commonly used combined nomenclature, $UBV$ comes from Johnson–Morgan, $R_{\rm C}$ and $I_{\rm C}$ refer to the Cousins realisation of the red optical bands, and $JHKL$ designate near-infrared bands with distinct historical realisations, including those associated with Glass. The Cousins optical bands and the infrared systems originated in photoelectric photometry. Modern CCDs can reproduce the optical bands with suitable calibration, while the longer infrared bands need infrared detectors.

[Figure 17](fig17_photometry_optical_infrared_passbands) compares this family of bands with other systems. Ground-based infrared observations use atmospheric windows, for example in $J$, $H$, and $K$, and at suitable sites also in $L$. Strong absorption between the windows leaves some spectral intervals accessible only from above much of the atmosphere.

```{figure} _static/_chapter08/fig17_optical_infrared_passbands.png
:width: 82%
:align: center
:name: fig17_photometry_optical_infrared_passbands

**Figure 17** Examples of optical and infrared passbands. The Johnson–Cousins–Glass bands are shown with several other systems and reference spectra. The wavelength scale is logarithmic.
```

### The Strömgren system

The Strömgren $uvby$ system uses four intermediate-width bands, narrower than broad-band $BVR$ ([Figure 18](fig18_photometry_stromgren_passbands)). Their different responses to spectral features are useful for estimating stellar parameters. For example, $b-y$ is a temperature-sensitive colour, and

$$
m_1=(v-b)-(b-y)
$$

measures the depression of the $v$-band flux by groups of absorption lines relative to the neighbouring bands. It is sensitive to metallicity within an appropriate calibration. The index $c_1=(u-v)-(v-b)$ samples the Balmer discontinuity and has a dependence on temperature and surface gravity.[^ch08_stromgren]

```{figure} _static/_chapter08/fig18_stromgren_passbands.png
:width: 72%
:align: center
:name: fig18_photometry_stromgren_passbands

**Figure 18** Broad $BVR$ response curves (upper panel) and the narrower Strömgren $uvby$ bands (lower panel). The $v$ band samples a region rich in metal absorption lines.
```

### Instrument-specific magnitudes

A space mission can define its own system through the response of its instrument. Gaia DR2 provides magnitudes in a broad $G$ band and in the blue and red bands $G_{\rm BP}$ and $G_{\rm RP}$ ([Figure 19](fig19_photometry_gaia_dr2_passbands)). The latter integrate the dispersed signals of the blue and red photometers. The response curves and zero points must refer to the data release used. In a different application, missions such as CHEOPS, Kepler, and TESS use broad photometric responses to collect many photons for precise time-series measurements. Their wavelength weightings are different ([Figure 20](fig20_photometry_space_mission_passbands)), so a star of a given colour will give different relative signals in the different instruments.[^ch08_gaia]

```{figure} _static/_chapter08/fig19_gaia_dr2_passbands.png
:width: 70%
:align: center
:name: fig19_photometry_gaia_dr2_passbands

**Figure 19** Revised Gaia DR2 passbands. Green denotes $G$, blue $G_{\rm BP}$, and red $G_{\rm RP}$. [ESA/Gaia/DPAC, revised DR2 passbands](https://www.cosmos.esa.int/web/gaia/iow_20180316).
```

```{figure} _static/_chapter08/fig20_space_mission_passbands.png
:width: 65%
:align: center
:name: fig20_photometry_space_mission_passbands

**Figure 20** Normalised response curves for MOST, CoRoT, Kepler, CHEOPS, and TESS. The shape of the response determines how strongly each instrument weights different parts of the spectrum.
```

## Colour indices

Consider two bands $X$ and $Y$ with representative wavelengths $\lambda_X<\lambda_Y$. The **colour index** is the difference between the magnitudes in those bands. Write $F_X$ and $F_Y$ for consistently defined band signals on a linear scale, with reference values $F_{X,0}$ and $F_{Y,0}$. Then

$$
\begin{aligned}
X-Y
&=-2.5\log_{10}\!\left(\frac{F_X/F_{X,0}}{F_Y/F_{Y,0}}\right)\\
&=c_{XY}-2.5\log_{10}\!\left(\frac{F_X}{F_Y}\right),
\qquad
c_{XY}=2.5\log_{10}\!\left(\frac{F_{X,0}}{F_{Y,0}}\right).
\end{aligned}
$$

For an unresolved spherical star with radius $R_\star$, the flux received in the absence of extinction is $(R_\star/r)^2$ times its emergent surface flux at each wavelength. The geometrical factor cancels in the colour. Thus the colour is independent of distance along a transparent path and independent of radius for a fixed surface spectrum. Interstellar extinction can change the colour because it attenuates the two bands by different amounts.[^ch08_colours]

In the traditional Vega-like calibration, the zero points make the colours of suitable unreddened A0 reference stars approximately zero. For example, $U-B$, $B-V$, $V-R$, and $R-I$ are near zero by construction on the corresponding reference scales. This convention concerns the ratios of signals relative to their reference values. Each photometric system has its own zero points.

### Colour and temperature

[Figure 21](fig21_photometry_colour_temperature) compares blackbody spectra at $10\,000$ and $5\,000\ \mathrm{K}$ at wavelengths representative of $B$ and $V$. The hotter spectrum puts relatively more flux into $B$ than into $V$. Its larger $F_B/F_V$ corresponds to a smaller $B-V$. Actual photometry integrates over the two passbands, and stellar spectra contain lines and discontinuities. A calibrated colour is therefore an estimator of effective temperature, with an accuracy that depends on chemical composition, surface gravity, and reddening.

```{figure} _static/_chapter08/fig21_colour_temperature.png
:width: 65%
:align: center
:name: fig21_photometry_colour_temperature

**Figure 21** A comparison of two blackbody spectra at $10\,000$ and $5\,000\ \mathrm{K}$. The vertical lines indicate representative wavelengths for $B$ and $V$. The ratio of the two intensities changes with temperature.
```

A **colour–magnitude diagram** puts a colour on the horizontal axis and a magnitude on the vertical axis. [Figure 22](fig22_photometry_colour_magnitude_diagram) uses $M_V-M_I$ and $M_I$, with brighter stars towards the top. The main sequence runs from brighter, bluer stars to fainter, redder stars. Luminous red stars form a separate concentration towards the upper right. For a population at a common distance one can also use apparent magnitudes, since the common distance modulus shifts the vertical scale by the same amount for every star if attenuation is the same.

```{figure} _static/_chapter08/fig22_colour_magnitude_diagram.png
:width: 64%
:align: center
:name: fig22_photometry_colour_magnitude_diagram

**Figure 22** A stellar colour–magnitude diagram with $M_V-M_I$ on the horizontal axis and $M_I$ on the vertical axis. More negative magnitudes are plotted upwards. The diagonal main sequence is distinct from the concentration of luminous red stars to the upper right.
```

## Absolute magnitude and distance modulus

Apparent magnitude depends on both the light output of the source and its distance. The **absolute magnitude** $M$ is the apparent magnitude the source would have at $10\ \mathrm{pc}$ in the same band in the absence of extinction. Using the inverse-square law,

$$
\frac{F(r)}{F(10\ \mathrm{pc})}
=\left(\frac{10\ \mathrm{pc}}{r}\right)^2.
$$

Taking the logarithm then gives the **distance modulus** in a transparent medium,[^ch08_distances]

$$
\boxed{m-M=5\log_{10}\!\left(\frac{r}{10\ \mathrm{pc}}\right)}
=5\log_{10}\!\left(\frac{r}{1\ \mathrm{pc}}\right)-5 .
$$

The second form is often written $m-M=5\log_{10} r-5$, with $r$ understood as the numerical distance in parsecs. A distance of $10\ \mathrm{pc}$ gives $m=M$. At $100\ \mathrm{pc}$ the flux has decreased by a factor of $100$ relative to its value at $10\ \mathrm{pc}$, and the apparent magnitude has increased by five.

An absolute magnitude in one band measures the source's light output in that band. The **absolute bolometric magnitude** measures the total luminosity through

$$
M_{\rm bol}=-2.5\log_{10}\!\left(\frac{L}{L_0}\right),
\qquad
L_0=3.0128\times10^{28}\ \mathrm{W}
$$

on the IAU scale. With the nominal solar luminosity, $M_{{\rm bol},\odot}\simeq4.74$.

## Extinction and optical depth

Material along the line of sight can absorb photons or scatter them out of the beam. These two losses to the direct beam constitute **extinction**. Absorbed energy can subsequently be emitted at another wavelength. The attenuation derived here applies to the direct beam when emission into the beam and scattering into it can be neglected.[^ch08_extinction]

Consider the power $P_\nu$ carried in a narrow bundle of rays. Since we follow the power in the bundle, its geometrical spreading is accounted for separately. Over a short length $\mathrm{d}s$, let $\alpha_\nu(s)$ be the extinction coefficient in $\mathrm{m^{-1}}$. The power lost is proportional to the power present and to the length traversed,

$$
\mathrm{d}P_\nu=-\alpha_\nu(s)P_\nu\,\mathrm{d}s.
$$

The **optical depth**, also called optical thickness for the complete path, is the dimensionless integral

$$
\tau_\nu(r)=\int_0^r\alpha_\nu(s)\,\mathrm{d}s.
$$

Since $\mathrm{d}P_\nu/P_\nu=-\mathrm{d}\tau_\nu$, the direct flux density received at $r$ is

$$
P_\nu(r)=P_\nu(0)e^{-\tau_\nu(r)},
\qquad
F_{\nu,{\rm obs}}(r)=F_{\nu,{\rm unext}}(r)e^{-\tau_\nu(r)}.
$$

Here $F_{\nu,{\rm unext}}(r)$ is the flux density that would be measured at the same distance in a transparent medium. The increase in magnitude produced by attenuation at a single frequency is

$$
A_\nu=-2.5\log_{10}\!\left(e^{-\tau_\nu}\right)
     =2.5\log_{10}e\,\tau_\nu
     \simeq1.086\,\tau_\nu .
$$

In a finite band $X$, define $A_X$ using the ratio of attenuated to unattenuated band signals. To obtain it, integrate both the attenuated and unattenuated spectra with the same response and apply the magnitude definition to their ratio. A monochromatic value can approximate the result when extinction varies little across the band. The observed modulus is

$$
\boxed{m_X-M_X=5\log_{10}\!\left(\frac{r}{10\ \mathrm{pc}}\right)+A_X}.
$$

Extinction usually affects the blue band more than the visual band in the interstellar medium. The resulting **colour excess** is $E(B-V)=(B-V)_{\rm obs}-(B-V)_0=A_B-A_V$. The geometric distance term cancels as before. The colour excess can make a star appear cooler if interpreted with an unreddened colour–temperature relation.

## Surface brightness

An extended source covers a measurable solid angle. Its **surface brightness** is its received flux per unit solid angle. For a patch with flux $F_X$ in band $X$ and angular area $\omega$, the mean linear surface brightness is $F_X/\omega$. Locally, it is the observed intensity integrated over the band.

[Figure 23](fig23_photometry_surface_brightness_geometry) follows a fixed angular aperture. At twice the distance it encloses four times the projected physical area in the small-angle limit. For a uniform region each physical unit of area contributes one quarter as much received flux. The flux per angular area therefore stays the same. Equivalently, if we follow one fixed physical patch, its flux and angular area both fall as $r^{-2}$. This result applies in Euclidean geometry to resolved emission in a transparent medium.[^ch08_brightness]

```{figure} _static/_chapter08/fig23_surface_brightness_geometry.png
:width: 65%
:align: center
:name: fig23_photometry_surface_brightness_geometry

**Figure 23** The same angular aperture intercepts an area $A$ at distance $r$ and an area $4A$ at distance $2r$. The greater projected area compensates for the decrease in received flux from each unit of area.
```

Astronomers often express surface brightness in **magnitudes per square arcsecond**. Let $\omega_{\rm as}$ be the number of square arcseconds covered by a patch of integrated apparent magnitude $m_X$. Its mean surface brightness in magnitudes per square arcsecond is

$$
\mu_X=m_X+2.5\log_{10}\omega_{\rm as}.
$$

As with point-source magnitudes, a smaller number means a brighter signal per unit angular area. A very dark night sky may have $\mu_V\simeq21.8\ \mathrm{mag\,arcsec^{-2}}$. This is a representative value for a dark site and favourable conditions. Actual values depend on airglow, moonlight, and artificial light, among other contributions.[^ch08_sky]

A galaxy generally has a varying surface brightness across its image. **Isophotes** trace the contours of equal surface brightness and show how the shape of the source changes with brightness level ([Figure 24](fig24_photometry_galaxy_isophotes)).

```{figure} _static/_chapter08/fig24_galaxy_isophotes.png
:width: 45%
:align: center
:name: fig24_photometry_galaxy_isophotes

**Figure 24** Galaxy images and corresponding isophotes, shown as red contours. Each contour connects points of equal surface brightness in the image.
```

## Operational definition of magnitude

An optical detector records a weighted integral of the incident spectrum. We now specify the factors that enter that integral, in the order in which they describe the source and the measurement.

1. **Spectral flux density.** $F_\lambda(\lambda)$ gives the energy incident per unit collecting area, per unit time, and per unit wavelength. The different spectral shapes in [Figure 12](fig12_photometry_stellar_spectra) illustrate why a single value of $F_\lambda$ generally cannot describe the signal in a whole band.
2. **Optical reflectivity.** For $n$ reflecting mirrors, the throughput of the mirrors is $\prod_{j=1}^n R_j(\lambda)$. This becomes $R^n(\lambda)$ when all mirrors have the same reflectivity. The Subaru examples in [Figure 25](fig25_photometry_subaru_mirror_reflectivity) show that different optical paths give different efficiencies. The loss also varies with wavelength.
3. **Detector quantum efficiency.** $\mathrm{QE}(\lambda)$ is the mean number of primary photoelectrons collected per incident photon. The curves in [Figure 26](fig26_photometry_detector_quantum_efficiency) illustrate how the sensitivity of a CCD depends on its architecture and on wavelength.
4. **Filter transmission.** $T_X(\lambda)$ weights the radiation that enters band $X$. A published passband can already include the full response of the optics and detector, as in the Gaia example in [Figure 19](fig19_photometry_gaia_dr2_passbands). In that case the published response must be used with its specified weighting convention.

```{figure} _static/_chapter08/fig25_subaru_mirror_reflectivity.png
:width: 70%
:align: center
:name: fig25_photometry_subaru_mirror_reflectivity

**Figure 25** Wavelength-dependent optical efficiencies for several Subaru Telescope mirror configurations. The curves show the effect of combining the reflectivities of different mirrors. [Subaru Telescope, reflectivity measurements](https://subarutelescope.org/Telescope/Parameters/Reflectivity/).
```

```{figure} _static/_chapter08/fig26_detector_quantum_efficiency.png
:width: 70%
:align: center
:name: fig26_photometry_detector_quantum_efficiency

**Figure 26** Examples of wavelength-dependent quantum efficiency for electron-multiplying and intensified CCDs. The curves illustrate how the detector changes the wavelength weighting of a measurement.
```

Let $A_{\rm tel}$ be the telescope's collecting area and let $S_X(\lambda)=T_X(\lambda)\,\mathrm{QE}(\lambda)\prod_j R_j(\lambda)$ be the dimensionless instrumental throughput for this model. A photon of wavelength $\lambda$ carries energy $hc/\lambda$. Dividing the incoming energy by this energy converts the energy flux density into a photon flux density. For a photon-counting CCD the expected rate of primary photoelectrons is therefore

$$
\boxed{
\dot N_{{\rm e},X}=A_{\rm tel}\int_{\lambda_1}^{\lambda_2}
  F_\lambda(\lambda)\,
  \frac{\lambda}{hc}\,
  S_X(\lambda)\,\mathrm{d}\lambda
}.
$$

The limits span the band response. With $F_\lambda$ in $\mathrm{W\,m^{-2}\,m^{-1}}$, $\lambda$ and $\mathrm{d}\lambda$ in metres, the integral with $A_{\rm tel}$ gives a rate in $\mathrm{s^{-1}}$. For an energy-measuring detector the signal is proportional to a weighted energy integral with its own response function. A response tabulated per unit incident energy may already include the conversion factor.[^ch08_counting]

Using a standard source with assigned magnitude $m_{X,\rm ref}$ and the corresponding reference signal $\dot N_{{\rm e},X,\rm ref}$ gives

$$
\boxed{m_X=m_{X,\rm ref}
-2.5\log_{10}\!\left(\frac{\dot N_{{\rm e},X}}
                           {\dot N_{{\rm e},X,\rm ref}}\right)}.
$$

Here both signals refer to the same band and calibration. With a linear detector and stable count rate, the measured counts divided by the exposure time estimate that rate after background subtraction and detector calibration. The magnitude refers to the entire passband. Its effective wavelength can be quoted as a supplementary description of the measurement.

For a ground-based instrument, $F_\lambda$ at the telescope equals the flux density just above the atmosphere multiplied by the **atmospheric transmission**. In the simple direct-beam model this factor is $e^{-\tau_{\rm atm}(\lambda)}$, with optical depth along the observing path. For both ground and space, extinction along the astronomical path can have already modified the flux that reaches the Earth or spacecraft. For example, interstellar extinction affects a stellar spectrum before the atmosphere or instrument acts on it.

### A mission performance example

The PLATO Performance Team uses the same connection between source flux and instrumental signal to assess mission requirements. A payload model such as PlatoSim follows the conversion of incident stellar light into simulated detector measurements. Together with a model of the instrument and its noise, the expected signal can be used to assess photometric precision and test whether the observations meet the scientific requirements. The team also assesses instrument performance and coordinates requirements that depend on both the hardware and the intended science ([Figure 27](fig27_photometry_plato_performance_team)).[^ch08_plato]

```{figure} _static/_chapter08/fig27_plato_performance_team.png
:width: 82%
:align: center
:name: fig27_photometry_plato_performance_team

**Figure 27** PLATO Performance Team activities, including guidance performance, instrument and science performance, and noise simulation. [PLATO Mission Consortium](https://platomission.com/the-plato-consortium/plato-performance-team/).
```

## References

- **Barbieri, C., and Bertini, I. (2021)**, *Fundamentals of Astronomy*, 2nd ed., §§16.1–16.3 and §§16.5–16.8, printed pp. 241–252 and 255–263 (PDF pp. 260–271 and 274–282).
- **Hanslmeier, A. (2023)**, *Introduction to Astronomy and Astrophysics*, §7.1.6, printed pp. 255–256 (PDF pp. 272–273), and §§8.1.1–8.1.4, printed pp. 303–308 (PDF pp. 320–325).
- **Karttunen, H., et al. (eds., 2017)**, *Fundamental Astronomy*, 6th ed., Chapter 4, printed pp. 91–101 (PDF pp. 103–113).
- **Seeds, M. A., Backman, D. E., and Wegryn, E. (2026)**, *Foundations of Astronomy*, 15th ed., §9-2, printed pp. 185–187 (PDF pp. 206–208).

[^ch08_intensity]: Karttunen et al. (2017), §4.1, printed pp. 91–93 (PDF pp. 103–105), for intensity, integration over direction, the jansky, and luminosity.

[^ch08_sun]: [ESA, Solar Orbiter's visible and extreme-ultraviolet views of the Sun](https://www.esa.int/Science_Exploration/Space_Science/Solar_Orbiter/New_full_Sun_views_show_sunspots_fields_and_restless_plasma). Hanslmeier (2023), §8.1, discusses the geometrical quantities used for stellar photometry.

[^ch08_solar_units]: [IAU 2015 Resolution B3](https://arxiv.org/abs/1605.09788) gives the nominal total solar irradiance and luminosity in SI units. Barbieri and Bertini (2021), §16.6, printed p. 257 (PDF p. 276), give the solar bolometric flux to three significant figures.

[^ch08_magnitude]: Karttunen et al. (2017), §4.2, printed pp. 93–94 (PDF pp. 105–106), and Barbieri and Bertini (2021), §16.1, printed pp. 241–243 (PDF pp. 260–262). For historical attribution see [Verbunt and van Gent, *Accuracy of magnitudes in pre-telescopic star catalogs*](https://doi.org/10.1002/asna.202013803).

[^ch08_bolometric]: Barbieri and Bertini (2021), §§16.2 and 16.7, printed pp. 243 and 259–260 (PDF pp. 262 and 278–279), use the additive convention. Karttunen et al. (2017), §4.3, printed pp. 94–95 (PDF pp. 106–107), describe an older subtractive convention with a zero near type F5. [IAU 2015 Resolution B2](https://arxiv.org/abs/1510.06262) specifies the bolometric zero points.

[^ch08_systems]: Barbieri and Bertini (2021), §16.2, printed pp. 243–249 (PDF pp. 262–268), and Karttunen et al. (2017), §4.3, printed pp. 94–96 (PDF pp. 106–108). The [Asiago Database on Photometric Systems](https://ulisse.pd.astro.it/Astro/ADPS/list_4.html) identifies specific implementations, including the Glass near-infrared bands.

[^ch08_detectors]: Barbieri and Bertini (2021), §16.2.2, printed pp. 246–249 (PDF pp. 265–268), discuss the visual, photographic, and electronic detector responses. [ISO/CIE 23539:2023, *The CIE system of physical photometry*](https://www.iso.org/standard/83178.html) specifies the photopic and scotopic response functions.

[^ch08_landolt]: [Landolt (1992), *UBVRI Photometric Standard Stars Around the Celestial Equator*](https://doi.org/10.1086/113329). Barbieri and Bertini (2021), §16.2.1, printed pp. 244–246 (PDF pp. 263–265), discuss colour terms between instrumental systems. For the southern field in Figure 14 see the [Nordic Optical Telescope catalogue](https://www.not.iac.es/instruments/stancam/photstd/).

[^ch08_ubv]: [Johnson and Morgan (1953), *Fundamental Stellar Photometry for Standards of Spectral Type*](https://doi.org/10.1086/145697). The indicative wavelengths are from Barbieri and Bertini (2021), §16.2.1, Table 16.1, printed pp. 245–246 (PDF pp. 264–265).

[^ch08_stromgren]: [Strömgren (1966), *Spectral Classification Through Photo-Electric Narrow-Band Photometry*](https://www.annualreviews.org/content/journals/10.1146/annurev.aa.04.090166.002245). See also Barbieri and Bertini (2021), §17.8, on photometric parameters and stellar classification.

[^ch08_gaia]: [Evans et al. (2018), *Gaia Data Release 2. Photometric content and validation*](https://doi.org/10.1051/0004-6361/201832756).

[^ch08_colours]: Barbieri and Bertini (2021), §§16.5–16.6, printed pp. 255–258 (PDF pp. 274–277), and Karttunen et al. (2017), §4.3, printed pp. 95–96 (PDF pp. 107–108).

[^ch08_distances]: Karttunen et al. (2017), §4.4, printed pp. 96–97 (PDF pp. 108–109). Hanslmeier (2023), §8.1.3, printed pp. 305–307 (PDF pp. 322–324), and Seeds et al. (2026), §9-2, printed pp. 185–187 (PDF pp. 206–208), discuss the distinction between apparent and absolute magnitude.

[^ch08_extinction]: Karttunen et al. (2017), §4.5, printed pp. 97–99 (PDF pp. 109–111). Barbieri and Bertini (2021), §16.3, printed pp. 249–252 (PDF pp. 268–271), treat the wavelength dependence of atmospheric extinction.

[^ch08_brightness]: Karttunen et al. (2017), §§4.1 and 4.6, printed pp. 92–93 and 100 (PDF pp. 104–105 and 112).

[^ch08_sky]: The IAC compilation reports $V$-band values near $21.8\ \mathrm{mag\,arcsec^{-2}}$ at sites such as La Silla and Cerro Tololo. [IAC, night sky background measurements](https://iac.edu.es/en/observatorios-de-canarias/sky-quality/sky-quality-parameters/night-sky-background)

[^ch08_counting]: Barbieri and Bertini (2021), §16.2, printed pp. 243–249 (PDF pp. 262–268), discuss the response integral and its instrumental factors. For an explicit division by photon energy in the response integral, see [Lund (2019), *Bolometric corrections of stellar oscillation amplitudes*](https://doi.org/10.1093/mnras/stz2010).

[^ch08_plato]: [PLATO Mission Consortium, PLATO Performance Team](https://platomission.com/the-plato-consortium/plato-performance-team/). [Jannsen et al. (2024), *PlatoSim*](https://doi.org/10.1051/0004-6361/202346701).
