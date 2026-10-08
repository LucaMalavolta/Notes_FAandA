(chapter04_perturbation_of_coordinates)=

# Perturbations of Coordinates

:::{danger}
This page still nneeds substantial revision to match the content presented during the lectures
:::

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

The coordinate transformations developed in {doc}`Chapter 2 <chapter02_transformation_of_coordinates>` relate directions expressed in different reference systems. An actual observation involves an additional question: does the measured direction coincide with the direction from the observer to the object? In general it does not. The atmosphere bends incoming light; the motion of the observer changes its apparent direction; and a nearby object is seen from different directions when the observing position changes. These effects are called **refraction**, **aberration**, and **parallax**. Each has a distinct physical cause, time dependence, and angular scale.

We shall consider refraction first, then annual and diurnal aberration, and finally the forms of parallax that lead to the direct measurement of stellar distances. Precession, nutation, polar motion, and stellar proper motion also change coordinates with time, but they describe changes in the reference axes or the source position rather than the three effects developed here.

## Atmospheric refraction

The **refractive index** of a medium is $n=c/v_{\rm ph}$, where $c$ is the speed of light in vacuum and $v_{\rm ph}$ is the phase speed in the medium. At the boundary between two homogeneous media, the incoming and refracted rays obey **Snell's law**:

$$
n_1\sin i=n_2\sin r,
$$

where $i$ and $r$ are measured from the normal to the boundary. The terrestrial atmosphere is not a single uniform layer. Its pressure and density generally decrease upward, and its refractive index approaches the vacuum value $n=1$ at high altitude. Temperature also affects $n$, although temperature itself need not decrease monotonically with height. The stack of layers in [Figure 1](fig01_refraction_layers) is a useful approximation: as a ray travels downward into denser air, it bends gradually toward the local vertical.[^refraction]

```{figure} _static/_chapter04/fig01_atmospheric_layers.png
:width: 50%
:align: center
:name: fig01_refraction_layers

**Figure 1** A ray crossing atmospheric layers of increasing refractive index. The successive changes of direction approximate the continuously curved path through the real atmosphere.
```

The observer sees the star along the direction in which the light *arrives*, as though its final path were extended backward in a straight line. If $z_{\rm true}$ is the zenith distance in the absence of the atmosphere and $z_{\rm obs}$ is the observed zenith distance, the **astronomical refraction** is

$$
R=z_{\rm true}-z_{\rm obs}=h_{\rm obs}-h_{\rm true}.
$$

Thus a celestial object normally appears **higher** than its geometric position. In the plane-parallel, small-refraction approximation, Snell's law gives

$$
R\simeq(n_0-1)\tan z_{\rm obs},
$$

where $n_0$ is the refractive index near the observer. This expression explains why refraction grows rapidly as one approaches the horizon; it must not be used at $z=90^\circ$, where its divergence is an artefact of the flat-layer approximation. For a standard sea-level atmosphere, a commonly adopted value at the horizon is about $34'$—comparable to the Sun's apparent diameter. The actual correction depends on pressure, temperature, wavelength, and the vertical structure of the atmosphere.[^horizon_refraction]

By symmetry, a stratified atmosphere produces zero *systematic* refraction exactly at the zenith. Local turbulence can still make an image wander and blur. Long-exposure star trails close to the horizon can show changes in the apparent path as the light traverses a longer and more variable atmospheric column ([Figure 2](fig02_refraction_trails)). Clouds and the landscape in the same photograph also remind us that the visible horizon is an observational scene, whereas the astronomical horizon is a geometric plane.

```{figure} _static/_chapter04/fig02_refracted_star_trails.png
:width: 85%
:align: center
:name: fig02_refraction_trails

**Figure 2** Star trails above a low horizon. The trails near the horizon show how atmospheric conditions can affect the apparent paths of stars.
```

## Aberration of light

Even in a vacuum, a moving observer measures a direction that differs from the direction measured by an observer at rest in the chosen reference frame. During the finite travel time of a photon through a telescope, the telescope moves. The familiar analogy is rain falling vertically for a stationary observer but appearing to arrive obliquely for someone who runs through it. A telescope must similarly be pointed slightly toward the direction of its motion to receive the light from a star ([Figure 3](fig03_aberration)).

```{figure} _static/_chapter04/fig03_stellar_aberration.png
:width: 62%
:align: center
:name: fig03_aberration

**Figure 3** Aberration of starlight: the telescope moves laterally while light traverses it, so its apparent pointing direction is displaced toward the observer's motion.
```

For speed $v\ll c$, let $v_\perp$ be the component of the observer's velocity perpendicular to the incoming stellar direction. The small angular displacement is approximately

$$
\Delta\theta\simeq\frac{v_\perp}{c} \quad\text{(radians)}.
$$

The greatest displacement occurs when the velocity is perpendicular to the line of sight; a velocity parallel to it produces no first-order change in direction. More generally, if $\boldsymbol{s}$ is the unit vector *toward* the source in the rest frame and $\boldsymbol{v}$ is the observer's velocity, then, to first order in $v/c$,

$$
\boldsymbol{s}_{\rm app}-\boldsymbol{s}
\simeq\frac{\boldsymbol{v}-(\boldsymbol{v}\cdot\boldsymbol{s})\boldsymbol{s}}{c}.
$$

The term on the right is the projection of velocity onto the tangent plane of the celestial sphere. This vector form specifies the direction of the shift as well as its size. It is a first-order approximation to relativistic aberration, sufficient for the angular scales considered here.[^aberration]

### Annual and diurnal aberration

The Earth's orbital velocity is approximately $30\ {\rm km\,s^{-1}}$. The corresponding maximum annual aberration is $v_\oplus/c\simeq20.5''$, called the **constant of aberration** to the accuracy needed here. As the direction of orbital velocity changes during the year, the apparent position of a fixed star describes a small ellipse. For a star at the ecliptic pole, the locus is nearly a circle with angular radius about $20.5''$; for a star near the ecliptic plane, it becomes nearly a line segment. The approximately $41''$ end-to-end span is twice the angular amplitude, not the amplitude itself.[^aberration]

The rotation of the Earth gives an observatory a second velocity. At geodetic latitude $\phi$, its magnitude is approximately

$$
v_{\rm rot}=\omega_\oplus R_\oplus\cos\phi,
$$

with $R_\oplus$ the Earth's equatorial radius. The maximum speed at the equator is about $0.465\ {\rm km\,s^{-1}}$, producing a maximum **diurnal aberration** of about $0.32''$. The effect decreases with latitude and vanishes at a pole for an observer fixed to the rotating Earth. Its instantaneous value also depends on the direction to the object because only the transverse component of velocity changes the apparent direction.

Aberration must not be confused with parallax. Aberration depends primarily on the **velocity** of the observer and affects even objects so distant that their parallax is negligible. Parallax depends on the observer's **position** relative to a source at finite distance.

## Parallax: changing the observing position

Hold a finger at arm's length and view it alternately with the left and right eye. The finger seems to move against objects in the distance ([Figure 4](fig04_finger_parallax)). Its apparent displacement is greater when the finger is closer, or when the two observing positions are farther apart. A stereoscopic film exploits the same geometry: two cameras record slightly different views, and each eye is shown its corresponding image ([Figure 5](fig05_stereo_camera)). Three-dimensional cinema glasses separate these left-eye and right-eye views, whether they use colour, polarisation, or another optical method.

```{figure} _static/_chapter04/fig04_finger_parallax.png
:width: 60%
:align: center
:name: fig04_finger_parallax

**Figure 4** A nearby finger changes apparent position against a distant background when the observing eye is changed.
```

```{figure} _static/_chapter04/fig05_stereo_camera.png
:width: 60%
:align: center
:name: fig05_stereo_camera

**Figure 5** A stereoscopic camera records two views from slightly separated positions, reproducing the geometry used by our two eyes.
```

Let an object be at distance $r$ and let the observer's position change by a baseline $b$. Only the component $b_\perp$ perpendicular to the line of sight contributes to the first-order angular shift:

$$
\Delta\theta\simeq\frac{b_\perp}{r} \quad\text{(radians)}.
$$

This immediately gives the two practical rules: a longer baseline gives a larger parallax, and a more distant source gives a smaller one. When describing a *parallax amplitude*, the baseline is measured from the chosen central origin to one observing position. The total displacement between two positions on opposite sides of that origin can be twice as large. The distinction between amplitude and full excursion is essential in the examples below.[^parallax]

### Diurnal parallax

A terrestrial observer is displaced from the Earth's centre by approximately one Earth radius. For Solar System objects this displacement can make a measurable difference between a geocentric direction and a **topocentric** direction. As the Earth rotates, the observer's position changes relative to the distant object, giving **diurnal parallax** ([Figure 6](fig06_diurnal_geometry)). The precise shift depends on the object's distance, the observer's location and hour angle, and the angle between the Earth-centre-to-observer vector and the line of sight.

```{figure} _static/_chapter04/fig06_diurnal_geometry.png
:width: 58%
:align: center
:name: fig06_diurnal_geometry

**Figure 6** Directions from two positions on the Earth's surface to the same object $P$. Their difference is the topocentric parallax.
```

The standard reference baseline for **horizontal parallax** is the Earth's equatorial radius, $R_\oplus\simeq6378\ {\rm km}$ ([Figure 8](fig08_earth_radius)). For an object at geocentric distance $r$, the horizontal parallax $\pi_{\rm h}$ is defined by

$$
\sin\pi_{\rm h}=\frac{R_\oplus}{r}.
$$

At the Moon's typical distance, about $384,400\ {\rm km}$, this is nearly $57'$, large enough that observers at different terrestrial locations can see the Moon in noticeably different directions. The simultaneous images in [Figure 7](fig07_lunar_parallax) illustrate how the Moon's location against the background differs between observing sites. The baseline here is a radius measured from the Earth's centre; it is not the full distance traversed by a surface observer over a day.

```{figure} _static/_chapter04/fig07_lunar_parallax.png
:width: 55%
:align: center
:name: fig07_lunar_parallax

**Figure 7** Composite of the Moon photographed simultaneously from separated sites during a lunar eclipse. Its apparent position relative to background stars depends on the observer's location.
```

```{figure} _static/_chapter04/fig08_earth_radius_baseline.png
:width: 60%
:align: center
:name: fig08_earth_radius

**Figure 8** The Earth-centre-to-observer radius supplies the reference baseline for horizontal parallax.
```

### Annual parallax

For a star, the Earth's radius is usually too small a baseline. The motion of the Earth around the Sun supplies a much larger one: approximately **one astronomical unit** from the Solar System barycentre to the Earth, or about $2\ {\rm au}$ between observations made on opposite sides of the orbit. The astronomical unit is defined to be exactly $149,597,870,700\ {\rm m}$.[^au] Against much more distant stars, a nearby star then executes an annual apparent displacement ([Figure 9](fig09_annual_parallax)).

```{figure} _static/_chapter04/fig09_annual_parallax.png
:width: 73%
:align: center
:name: fig09_annual_parallax

**Figure 9** A nearby star appears in different directions from opposite parts of the Earth's orbit. The annual parallax is the angular amplitude associated with a one-au baseline.
```

**Annual parallax**, generally called simply **stellar parallax**, is the angle $\pi$ subtended by one astronomical unit at the star. The apparent track can be an ellipse or nearly a line depending on the star's ecliptic latitude. Its angular size shrinks inversely with stellar distance. It is independent of the star's luminosity, so it provides a geometric distance measurement rather than one based on an assumed intrinsic brightness.

### Secular parallax

The Sun also moves through the Galaxy. Over sufficiently long intervals its displacement can provide a baseline longer than the Earth's orbit, producing what is called **secular parallax** ([Figure 10](fig10_secular_parallax)). The Sun completes an orbit around the Milky Way in roughly $230$ million years.[^solar_motion] Unlike the controlled one-year geometry of annual parallax, a secular measurement is entangled with the stars' own motions. Its interpretation therefore requires a model of relative velocities; one cannot infer an individual stellar distance from the Solar displacement alone.

```{figure} _static/_chapter04/fig10_solar_galactic_motion.png
:width: 65%
:align: center
:name: fig10_secular_parallax

**Figure 10** The Sun's motion around the Milky Way provides a progressively longer baseline for secular parallax.
```

## Trigonometric distances and the parsec

The geometry of stellar parallax is represented in [Figure 11](fig11_parallax_triangle). If $r$ is the distance to a star and $\pi$ is the small angle subtended by a transverse baseline of one au, then

$$
\tan\pi=\frac{1\ {\rm au}}{r}
\qquad\Longrightarrow\qquad
r\simeq\frac{1\ {\rm au}}{\pi\ [{\rm radians}]}.
$$

Because stellar parallaxes are tiny, the differences between $\tan\pi$, $\sin\pi$, and $\pi$ in radians are negligible for the present purpose. This is why **trigonometric parallax** is a direct geometric method of measuring stellar distance.[^parallax]

```{figure} _static/_chapter04/fig11_parallax_triangle.png
:width: 45%
:align: center
:name: fig11_parallax_triangle

**Figure 11** The angle $\pi$ subtended by a one-au baseline at a star a distance $r$ away.
```

A **parsec** is the distance corresponding to a parallax of one arcsecond for a one-au baseline. Since one radian contains $206,264.806$ arcseconds,

$$
1\ {\rm pc}\simeq206,265\ {\rm au}
\simeq3.086\times10^{16}\ {\rm m},
\qquad
\boxed{r\ [{\rm pc}]\simeq\frac{1}{\pi\ [\mathrm{arcsec}]}}.
$$

The second expression applies to a positive, well-measured parallax after the relevant astrometric corrections. A noisy or even formally negative fitted parallax cannot simply be inverted into a physical distance; its uncertainty and the statistical model must be considered.

The nearest-star examples show the scale. A parallax of $0.762''$ corresponds to $1/0.762\simeq1.31\ {\rm pc}$, approximately the distance of **Proxima Centauri**. A parallax of $0.747''$ gives $1.34\ {\rm pc}$ for the **Alpha Centauri** system. These are rounded illustrative values; precise catalogue measurements can differ slightly. At $15\ {\rm pc}$ the parallax has already fallen to about $0.067''$. Even an angular uncertainty of $0.006''$ is therefore significant at this distance. Terrestrial atmospheric image motion and instrumental calibration make such small angles difficult to measure from the ground, motivating space astrometry. Parsec is the usual unit for this work; a light-year remains a valid distance unit, but it is less convenient for the parallax equation.

## Space astrometry: Hipparcos

**Hipparcos**—the *High Precision Parallax Collecting Satellite*—was ESA's first space astrometry mission ([Figure 12](fig12_hipparcos)). Its name also recalls Hipparchus, the ancient astronomer associated with the discovery of precession. It was launched in August 1989 and observed for about three and a half years. Its planned geostationary orbit was not reached because an apogee motor failed; the spacecraft nevertheless operated in a highly elliptical Earth orbit. Its annual stellar parallax still arose predominantly from the Earth's motion around the Sun, not from the radius of the spacecraft's Earth orbit.[^hipparcos]

```{figure} _static/_chapter04/fig12_hipparcos.png
:width: 62%
:align: center
:name: fig12_hipparcos

**Figure 12** Artist's view of the Hipparcos satellite, which brought precise stellar astrometry above the Earth's atmosphere.
```

The **Hipparcos Catalogue** contains $118,218$ stars with astrometry at roughly the milliarcsecond level. Its auxiliary star mapper produced the **Tycho Catalogue** with about $1.06$ million stars, generally at lower precision; the later **Tycho-2 Catalogue** contains about $2.54$ million stars.[^hipparcos] A milliarcsecond (mas) is $10^{-3}$ arcsecond. At this scale, measuring a star's apparent position at several epochs is essential: the solution must separate a constant position, a nearly linear **proper motion**, and the annually repeating parallax signature.

## Gaia: a global astrometric survey

ESA's **Gaia** mission extended this method to an enormous stellar sample ([Figure 13](fig13_gaia)). The name originally expanded to *Global Astrometric Interferometer for Astrophysics*, although the flown design is a scanning astrometry mission rather than the proposed interferometer. Launched in December 2013, Gaia carried out science observations from July 2014 until January 2025. Gaia Data Release 3, published in June 2022, provides full astrometric solutions—positions, parallaxes, and proper motions—for about $1.46$ billion sources. The precision depends strongly on source brightness, colour, crowding, and the number and geometry of observations; no single uncertainty describes the whole catalogue.[^gaia_status]

```{figure} _static/_chapter04/fig13_gaia_spacecraft.png
:width: 70%
:align: center
:name: fig13_gaia

**Figure 13** Gaia, designed to measure the positions and motions of stars across the entire sky.
```

### Two viewing directions and a common focal plane

Gaia used two telescopes with rectangular primary mirrors approximately $1.45\times0.50\ {\rm m}$ in size. Their lines of sight were separated by a fixed **basic angle** of $106.5^\circ$. Light from the two fields was directed onto one common focal plane ([Figure 14](fig14_gaia_optics)). Measuring angular separations between widely spaced regions of sky ties local observations into a single global astrometric solution. The stability and calibration of the basic angle were therefore central to the mission.[^gaia_instrument]

```{figure} _static/_chapter04/fig14_gaia_optics.png
:width: 70%
:align: center
:name: fig14_gaia_optics

**Figure 14** Optical layout of Gaia's two telescopes and their common focal-plane assembly.
```

The focal plane contained **106 CCD detectors**, together providing about $938$ million pixels ([Figure 15](fig15_gaia_ccd)). As Gaia rotated, stellar images crossed the detector array; their transit times supplied exceptionally precise position information along the scan direction. Repeated measurements from different scan angles made it possible to solve jointly for stellar positions, proper motions, parallaxes, the spacecraft attitude, and instrumental calibration.[^gaia_instrument]

```{figure} _static/_chapter04/fig15_gaia_focal_plane.png
:width: 78%
:align: center
:name: fig15_gaia_ccd

**Figure 15** The layout of Gaia's CCD focal plane. The different detector strips support source detection, astrometry, photometry, and spectroscopy.
```

### Location near L2 and the parallax baseline

Gaia observed from a Lissajous-type orbit around the Sun–Earth **L2** region, roughly $1.5$ million kilometres beyond the Earth in the direction away from the Sun ([Figure 16](fig16_l2)). This location permitted a stable thermal environment and efficient, repeated observations of the sky. An orbit about L2 requires station-keeping; the L2 equilibrium is not dynamically stable. The distance from the Earth to L2 is **not** Gaia's annual parallax baseline. Like a terrestrial observatory, Gaia follows the Earth around the Sun, so the annual geometric baseline remains of order one au.[^gaia_orbit]

```{figure} _static/_chapter04/fig16_lagrange_points.png
:width: 61%
:align: center
:name: fig16_l2

**Figure 16** The Sun–Earth Lagrange points. Gaia observed near L2, beyond the Earth as viewed from the Sun.
```

### Scanning the celestial sphere

Gaia did not point at one selected target for a long exposure. It rotated once every approximately **six hours**, sweeping its two fields of view along great circles. Its spin axis maintained an angle of about $45^\circ$ to the Sun and precessed around the Sun direction in about **63 days**. Combined with the Earth's annual motion, this scanning law repeatedly covered the entire sky with different orientations ([Figure 17](fig17_gaia_scanning)). The time-dependent pattern of observations is what separates annual parallax from proper motion in the global fit.[^gaia_scanning]

```{figure} _static/_chapter04/fig17_gaia_scanning_law.png
:width: 70%
:align: center
:name: fig17_gaia_scanning

**Figure 17** Gaia's scanning geometry: two lines of sight, spacecraft spin, and slow precession of the spin axis.
```

### Turning measurements into a catalogue

The spacecraft's measurements were only the beginning of the astrometric result. The **Gaia Data Processing and Analysis Consortium** (DPAC) designed simulations and reduction algorithms, calibrated the instruments and attitude, processed the very large data volume, validated the results, and prepared the public catalogues. Its work drew on scientists, engineers, and software specialists across more than twenty countries ([Figure 18](fig18_dpac)).[^dpac] The scientific lifetime of an astrometric mission extends beyond the spacecraft's operating lifetime: Gaia stopped observing in 2025, while further processing and data releases continue. As of October 2026, ESA lists Data Release 4 as planned for December 2026 and the final Data Release 5 no earlier than the end of 2030; these are schedules, not completed releases.[^gaia_status]

```{figure} _static/_chapter04/fig18_dpac_map.png
:width: 48%
:align: center
:name: fig18_dpac

**Figure 18** Historical map of the European distribution of contributors to Gaia data analysis. Producing an astrometric catalogue is a large collaborative computation as well as a space observation.
```

## References

- **Barbieri, C., and Bertini, I. (2021)**, *Fundamentals of Astronomy*, second edition, Chapters 2–3, for coordinate systems and positional effects.
- **Karttunen, H., Kröger, P., Oja, H., Poutanen, M., and Donner, K. J. (eds., 2017)**, *Fundamental Astronomy*, sixth edition, Chapter 2, for refraction, aberration, and parallax.
- **Hanslmeier, A. (2023)**, *Introduction to Astronomy and Astrophysics*, Chapter 2, for astronomical coordinates and apparent motions.
- **International Astronomical Union**, [Resolution B2 (2012)](https://www.iau.org/static/resolutions/IAU2012_English.pdf), for the exact astronomical-unit definition.
- **US Naval Observatory**, [Rise, Set, and Twilight Definitions](https://aa.usno.navy.mil/faq/RST_defs), for the conventional mean horizon-refraction correction.
- **European Space Agency**, [Hipparcos mission](https://www.cosmos.esa.int/web/Hipparcos), [Gaia mission](https://www.esa.int/content/view/full/416066), [Gaia DR3 contents](https://www.cosmos.esa.int/web/gaia/dr3), and [Gaia scanning law](https://gea.esac.esa.int/archive/documentation/GDR2/Introduction/chap_cu0int/cu0int_sec_mission/cu0int_ssec_scanning_law.html), for mission history, instrumentation, and data.

[^refraction]: Barbieri and Bertini (2021), Chapters 2–3; Karttunen et al. (2017), Chapter 2. The layered picture is an approximation to a continuously varying refractive index.

[^horizon_refraction]: [US Naval Observatory, Rise, Set, and Twilight Definitions](https://aa.usno.navy.mil/faq/RST_defs) and [First Sunrise of the New Year](https://aa.usno.navy.mil/faq/first_sunrise.html). The $34'$ value is an adopted average at sea level, not a fixed correction for every atmosphere.

[^aberration]: Karttunen et al. (2017), Chapter 2; Barbieri and Bertini (2021), Chapter 3. The quoted annual constant is rounded; the derivation uses only the first-order term in $v/c$.

[^parallax]: Barbieri and Bertini (2021), Chapters 2–3; Karttunen et al. (2017), Chapter 2; [US Naval Observatory glossary](https://aa.usno.navy.mil/faq/asa_glossary) for the parsec definition.

[^au]: [IAU Resolution B2 (2012)](https://www.iau.org/static/resolutions/IAU2012_English.pdf).

[^solar_motion]: [NASA, Sun: Facts](https://science.nasa.gov/sun/facts/) gives a Galactic orbital period of approximately $230$ million years.

[^hipparcos]: [ESA, Hipparcos mission](https://www.cosmos.esa.int/web/Hipparcos) for catalogue sizes and duration; [ESA, Hipparcos facts](https://www.cosmos.esa.int/web/hipparcos/faqs-facts) for the name and Hipparchus; [ESA, launch and operations](https://www.cosmos.esa.int/web/hipparcos/launch-and-operations-phase) for the orbit and apogee-motor failure.

[^gaia_status]: [ESA, Gaia mission](https://www.esa.int/content/view/full/416066) for mission dates and planned releases; [ESA, Gaia overview](https://www.esa.int/Science_Exploration/Space_Science/Gaia_overview) for the original acronym and change of design; [ESA, Gaia DR3 contents](https://www.cosmos.esa.int/web/gaia/dr3) for the number of full astrometric solutions.

[^gaia_instrument]: [ESA, Gaia spacecraft documentation](https://gea.esac.esa.int/archive/documentation/GDR2/Introduction/chap_cu0int/cu0int_sec_mission/cu0int_ssec_spacecraft_intro.html) and [ESA, Eye of Gaia](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Eye_of_Gaia_billion-pixel_camera_to_map_Milky_Way).

[^gaia_orbit]: [ESA, Gaia mission numbers](https://www.cosmos.esa.int/web/gaia/mission-numbers) and [Gaia end of observations](https://www.cosmos.esa.int/web/gaia/end-of-observations).

[^gaia_scanning]: [ESA, Gaia scanning-law documentation](https://gea.esac.esa.int/archive/documentation/GDR2/Introduction/chap_cu0int/cu0int_sec_mission/cu0int_ssec_scanning_law.html) and [Spinning in space](https://www.esa.int/Science_Exploration/Space_Science/Gaia/Spinning_in_space).

[^dpac]: [ESA, Gaia Data Processing and Analysis Consortium](https://www.cosmos.esa.int/web/gaia/dpac).
