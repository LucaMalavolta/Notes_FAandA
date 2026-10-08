(chapter05_movements_of_the_earth)=

# Movements of the Earth

:::{danger}
This page still need sustantial revision to match the content presented during the lectures
:::

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

The Earth's rotation and revolution establish the familiar daily and yearly cycles, but neither the terrestrial axis nor the orbital plane remains exactly fixed. The direction of the axis changes through **precession** and **nutation**; the rotation pole also moves with respect to the solid Earth. These changes alter the equator, the equinox, and therefore the coordinates assigned to a celestial object. A star has its own motion as well. To predict where it will appear at a telescope, we must distinguish motion of the reference system from motion of the star and from observational effects such as parallax, aberration, and refraction.

## Sidereal and tropical cycles

A **solar day** is the interval between successive passages of the Sun across the local meridian. Because the apparent Sun moves at a variable rate during the year, successive *apparent* solar days are not all equal. The **mean solar day**, defined using a uniformly moving fictitious Sun, is the approximately 24-hour unit used below. A **sidereal day** measures one rotation with respect to a nearly fixed celestial direction. During one solar day, the Earth has advanced in its orbit and must rotate a little more than one full turn to bring the Sun back to the meridian. Consequently, the sidereal day is shorter than the mean solar day.[^time_cycles]

Let $\tau$ be the mean solar day, $\tau_*$ the sidereal day, and $P_*$ the sidereal year, all expressed in the same units. In the circular-orbit approximation, the Earth's rotation rate with respect to the stars is the sum of its rotation rate with respect to the mean Sun and its orbital rate:

$$
\frac{1}{\tau_*}=\frac{1}{\tau}+\frac{1}{P_*}.
$$

Taking $\tau=1$ mean solar day and $P_*\simeq365.2564$ mean solar days gives $\tau_*\simeq0.99727$ day, or approximately **23 h 56 min 4 s**. This relation describes mean rates: the exact interval between observed transits of a particular star is affected by the definitions of the celestial reference direction and by small changes in Earth rotation.

Two different orbital years are needed. The **sidereal year** is the time for the Sun's apparent direction to return to the same orientation relative to the distant stars; equivalently, it measures one terrestrial revolution in an approximately fixed frame. The **tropical year** follows the cycle of seasons. In elementary geometry it is described as the interval between successive passages of the Sun through the **vernal equinox**, the intersection at which the Sun passes from south to north of the celestial equator. More precisely, the *mean* tropical year is defined by a $360^\circ$ increase of the Sun's mean ecliptic longitude measured from the moving equinox. These definitions must be distinguished when precision better than a few minutes is required.[^time_cycles]

```{figure} _static/_chapter05/fig01_tropical_sidereal_year.png
:width: 75%
:align: center
:name: fig01_earth_year_geometry

**Figure 1** The moving equinox is reached before Earth completes a full revolution relative to the distant stars. The schematic compares the shorter tropical year with the sidereal year.
```

Near the present epoch, the sidereal year is about $365.2564$ days and the mean tropical year about $365.2422$ days. Using more digits, the difference is approximately **20 min 24 s**. The tropical year is shorter because the vernal equinox slowly moves *against* the Sun's apparent eastward annual motion. The different year lengths are thus the first observable consequence of precession.

## Discovery of the precession of the equinox

Around 129 BCE, **Hipparchus of Nicaea** compared his measurement of the position of Spica ($\alpha$ Virginis) with observations attributed to **Timocharis** roughly 144 years earlier. Its ecliptic longitude had changed by about $2^\circ$, while its ecliptic latitude was nearly unchanged. The same systematic longitude shift appeared for other stars. An interpretation in which all stars moved together was less economical than one in which the coordinate origin—the vernal equinox, traditionally denoted $\gamma$—had moved along the ecliptic.[^precession]

Two degrees in 144 years corresponds to about $50''$ per year. Seen from the north ecliptic pole, the Sun moves eastward along the ecliptic over a year, whereas the equinox shifts westward. The Sun therefore reaches the moving equinox a little *before* completing a full circuit relative to the stars. This westward displacement is the **precession of the equinox**. The zodiac diagram in [Figure 2](fig02_equinox_zodiac) provides a geometric picture of the equinox moving against the stellar background.

```{figure} _static/_chapter05/fig02_zodiac_equinox.png
:width: 52%
:align: center
:name: fig02_equinox_zodiac

**Figure 2** The ecliptic and celestial equator cross at the equinoxes. Precession changes the stellar background against which their intersection is seen.
```

The vernal equinox lay in the constellation Aries in antiquity and is now in Pisces; its continuing westward motion will eventually carry it into Aquarius ([Figure 3](fig03_equinox_sky)). The names of the twelve astrological signs are conventional $30^\circ$ divisions of the ecliptic and do not track the present boundaries of the astronomical constellations.

```{figure} _static/_chapter05/fig03_vernal_equinox_map.png
:width: 85%
:align: center
:name: fig03_equinox_sky

**Figure 3** A sky map locating the vernal equinox against the present-day stars of Pisces. The equinox is a geometric direction, not a fixed star.
```

## Reference planes and the changing orientation of Earth

Ecliptic longitude $\lambda$ and latitude $\beta$ use the plane of the Earth's orbit as their reference; right ascension $\alpha$ and declination $\delta$ use the celestial equator, perpendicular to the Earth's rotation axis. The angle between these planes is the **obliquity** $\varepsilon$, approximately $23.4^\circ$ at present ([Figure 4](fig04_earth_planes)). A distant-star reference provides a useful way to recognize changes in the orientation of either plane. Over historical timescales the ecliptic changes much more slowly than the equator, but it is not perfectly fixed.[^precession]

```{figure} _static/_chapter05/fig04_equator_ecliptic_axes.png
:width: 70%
:align: center
:name: fig04_earth_planes

**Figure 4** The Earth's tilted rotation axis defines the celestial equator; its orbital motion defines the ecliptic. The lunar orbital plane is inclined to the ecliptic by about $5.1^\circ$.
```

For high-precision work, the orbital motion of the Earth–Moon system is described through its barycentre and a specified reference plane and epoch. The Moon's monthly displacement of Earth around that barycentre must not be mistaken for a corresponding monthly change of the *mean* ecliptic. Likewise, a real observatory uses a terrestrial reference frame tied to Earth and a celestial frame tied to distant objects. The transformation between them requires the measured orientation and rotation of Earth, rather than a single immutable axis.[^earth_orientation]

The Earth's mass is not distributed spherically. Rotation produces an equatorial bulge, while continents, oceans, atmosphere, and internal structures introduce further departures from a simple ellipsoid. [Figure 5](fig05_earth_mass) visualizes variations in the gravity field that reflect this uneven distribution. The **geoid** is an equipotential surface of that field; an oblate ellipsoid is a convenient simpler approximation to Earth's figure. Winds, ocean currents, tides, and earthquakes redistribute mass and can change the rotation rate and the orientation of the instantaneous rotation axis. Even the duration of a day is therefore not exactly constant over arbitrarily long intervals.[^earth_orientation]

```{figure} _static/_chapter05/fig05_earth_mass_distribution.png
:width: 70%
:align: center
:name: fig05_earth_mass

**Figure 5** Exaggerated view of spatial variations in the terrestrial gravity field. It illustrates why the real Earth cannot be represented exactly by a uniform sphere.
```

## Lunisolar precession

The Moon and Sun exert gravitational forces on the Earth's equatorial bulge. Because their directions are generally outside the equatorial plane, the forces on opposite parts of the bulge create a **torque**. For a rotating body, a torque changes the direction of angular momentum rather than simply pushing the axis toward the disturbing body. The spinning-top analogy in [Figure 6](fig06_precession_top) illustrates this response. The detailed direction of the terrestrial torque differs from that on a top under gravity, so the analogy is one of gyroscopic motion rather than an exact force diagram.[^precession]

```{figure} _static/_chapter05/fig06_spinning_top_precession.png
:width: 48%
:align: center
:name: fig06_precession_top

**Figure 6** A spinning top whose axis traces a cone under an external torque. Earth's axis undergoes an analogous slow change of orientation under lunar and solar torques.
```

The celestial pole consequently describes, to first approximation, a circle around the north ecliptic pole. The angular radius is approximately the obliquity, $23.4^\circ$, and a circuit takes about **26,000 years**. The equinox shifts in the opposite sense along the ecliptic at about $50.3''$ per year. These are approximate, epoch-dependent numbers: the exact path is modified by nutation and by slow changes in the ecliptic itself. [Figure 7](fig07_pole_path) shows why different stars serve as pole stars at different epochs.

```{figure} _static/_chapter05/fig07_precessing_celestial_pole.png
:width: 65%
:align: center
:name: fig07_pole_path

**Figure 7** Approximate path of the north celestial pole against the stars over many millennia. Its changing location follows from precession of the terrestrial axis.
```

The relevant torque is approximately proportional to the disturbing body's mass and to the inverse cube of its distance, $M/r^3$, for a given terrestrial figure. The Sun is about $2.7\times10^7$ times as massive as the Moon but about $400$ times farther away. The distance-cube ratio is about $400^3=6.4\times10^7$, making the lunar contribution roughly $6.4/2.7\simeq2.4$ times the solar one. This order-of-magnitude calculation explains the name **lunisolar precession**. A precise rate also depends on the Earth's moments of inertia, obliquity, and the orbits of the perturbing bodies.[^precession]

## Nutation: periodic motion around the mean axis

A smooth precession cone assumes an averaged, regular lunar and solar torque. In reality, the lunar orbit is inclined by about $5.1^\circ$ to the ecliptic, and its line of nodes rotates with a period of about **18.6 years**. The Moon and Sun also change distance from Earth during their orbits. The torque therefore has periodic components. The resulting shorter-period changes of the celestial pole and equator are collectively called **nutation**. The instantaneous pole follows a small wavering path around the precessing mean pole ([Figure 8](fig08_nutation_cone)).[^nutation]

```{figure} _static/_chapter05/fig08_nutation_cone.png
:width: 65%
:align: center
:name: fig08_nutation_cone

**Figure 8** The small wavering path of the rotation axis superposed on its much larger precessional cone. The amplitudes of the two motions are not drawn to scale.
```

The importance of changing distance can be appreciated without a full orbital calculation. The Earth's distance from the Sun ranges approximately from $147.1$ to $152.1$ million kilometres over an orbit, a difference of about $3.4\%$ relative to the smaller distance. The Moon's distance ranges approximately from $356,700$ to $406,300$ km, a difference of about $14\%$ relative to perigee. The visual difference between lunar perigee and apogee is shown in [Figure 9](fig09_moon_distance). Since the torque varies approximately as $r^{-3}$, these distance changes contribute periodic terms. They are not, by themselves, the explanation for the 18.6-year principal term: that period is associated with regression of the lunar nodes.[^nutation]

```{figure} _static/_chapter05/fig09_lunar_perigee_apogee.png
:width: 78%
:align: center
:name: fig09_moon_distance

**Figure 9** The Moon photographed near perigee and apogee. The difference in apparent size reflects the change in Earth–Moon distance.
```

Let $N$ be the ascending node at which the Moon crosses the ecliptic from south to north, and let $N'$ be the corresponding crossing of the celestial equator ([Figure 10](fig10_lunar_nodes)). These directions differ because the ecliptic and equator are inclined. Solar perturbations cause the lunar node to regress around the ecliptic, so the orientation of the lunar orbital plane and the direction of its torque change continuously.

```{figure} _static/_chapter05/fig10_lunar_nodes.png
:width: 68%
:align: center
:name: fig10_lunar_nodes

**Figure 10** The ecliptic, equator, and inclined lunar orbit. Their distinct intersections identify the lunar nodes used to describe the changing orientation of the Moon's orbit.
```

James Bradley detected the principal nutation observationally through a long series of stellar positions. In a simple leading-term approximation, with $\Omega$ the ecliptic longitude of the Moon's ascending node, the nutation in ecliptic longitude and obliquity is[^nutation]

$$
\boxed{\Delta\psi\simeq-17.2''\sin\Omega,\qquad
\Delta\varepsilon\simeq+9.2''\cos\Omega.}
$$

The two amplitudes refer to *different angles*: $17.2''$ in longitude and $9.2''$ in obliquity. Their common principal period is about $18.6$ years. A full nutation theory includes many additional terms, so these two expressions are explanatory approximations rather than a precision ephemeris.

## Motion of the ecliptic and obliquity

The ecliptic is itself affected by planetary perturbations, particularly from the massive planets. This slow change is called **planetary precession**. It combines with lunisolar precession in the **general precession** used to describe the motion of the equinox. The diagram in [Figure 11](fig11_ecliptic_motion) separates a moving equator from a moving ecliptic: either change can displace their intersection. Planetary terms also have periodic components, often called planetary nutation.[^precession]

```{figure} _static/_chapter05/fig11_moving_ecliptic.png
:width: 70%
:align: center
:name: fig11_ecliptic_motion

**Figure 11** The equatorial plane and the ecliptic can both change orientation. Their moving intersection is the equinox, the classical zero point of right ascension.
```

Near J2000.0 the **mean obliquity** decreases by about $0.47''$ per year, or $47''$ per century. This is a local rate, not a law to extrapolate linearly for tens of thousands of years. The long-term behaviour of the Earth's orbital and rotational planes is more complex, and modern precession models represent it with epoch-dependent series.[^obliquity]

## Free wobble and polar motion

Precession and nutation describe the orientation of the axis **in celestial space** under external torques. A different question concerns the location of the instantaneous rotation pole **within a frame attached to the Earth**. A rotating body whose spin axis is slightly displaced from a principal axis of inertia can exhibit a free wobble. Euler's rigid-body analysis predicts such a motion; [Figure 12](fig12_euler_wobble) depicts the changing relation between angular momentum, angular velocity, and the body's figure axis. The real Earth is deformable, with a fluid core and mobile oceans and atmosphere, so its observed free oscillation differs from the ideal rigid-body result.[^polar_motion]

```{figure} _static/_chapter05/fig12_euler_wobble.png
:width: 72%
:align: center
:name: fig12_euler_wobble

**Figure 12** Free wobble of a rotating body. Its angular-momentum direction, instantaneous spin axis, and principal figure axis need not coincide.
```

The observed wandering of the pole relative to Earth is **polar motion**. One important component, the **Chandler wobble**, has a period of about $430$ days, or roughly 14 months. An annual component is associated with seasonal redistribution of mass in the atmosphere, oceans, and hydrosphere. The amplitudes vary with time; excursions of order a few tenths of an arcsecond correspond to several metres on Earth's surface. For scale, $0.3''$ at a terrestrial radius of $6370$ km is approximately $9$ m. Smaller forced components and a slower drift are also present.[^polar_motion]

The observed path is consequently not a perfect circle ([Figures 13](fig13_polar_motion_record) and [14](fig14_polar_motion_path)). It combines the Chandler and annual components with irregular excitation and longer-term changes. Measurements of the pole coordinates, often written $x_p$ and $y_p$, are supplied as Earth-orientation parameters and are needed to connect terrestrial station positions to celestial directions.[^earth_orientation]

```{figure} _static/_chapter05/fig13_polar_motion_record.png
:width: 90%
:align: center
:name: fig13_polar_motion_record

**Figure 13** Examples of observed polar-motion paths in coordinates attached to Earth. The mixture of periodic components and variable excitation produces an irregular trajectory.
```

```{figure} _static/_chapter05/fig14_polar_motion_path.png
:width: 62%
:align: center
:name: fig14_polar_motion_path

**Figure 14** A detailed polar-coordinate track over successive years. Its loops arise chiefly from the superposition of the annual and Chandler oscillations.
```

The distinction between the two frames is essential. Precession and nutation move the celestial pole with respect to an approximately inertial celestial frame; polar motion changes the relation between the pole and points fixed on the Earth. A complete Earth-orientation model must include both, together with the spin angle and its variations.

## Mean and true fundamental planes

At two dates $t_1$ and $t_2$, the equator and ecliptic have slightly different orientations. Their intersections define different equinox directions $\gamma_1$ and $\gamma_2$; their mutual inclinations give different obliquities $\varepsilon_1$ and $\varepsilon_2$. [Figure 15](fig15_fundamental_planes) illustrates the shift of the equator and equinox between two nearby epochs. The change in a general orientation angle $J$ can be separated conceptually into a smooth part and a periodic part:

$$
J(t)=J(t_0)+a(t-t_0)+b(t-t_0)^2+\cdots
       +n(t)-n(t_0),
$$

where the polynomial approximates the slowly varying precessional contribution near $t_0$, and $n(t)$ contains nutation. This is a local representation, not a claim that precession is exactly polynomial for all time.[^mean_true]

```{figure} _static/_chapter05/fig15_fundamental_planes.png
:width: 68%
:align: center
:name: fig15_fundamental_planes

**Figure 15** The equator at two nearby dates intersects the reference ecliptic in different equinox directions. The geometric angles entering the coordinate system are therefore functions of time.
```

The **mean equator and equinox of date** retain the smooth precessional motion but omit the short-period nutation. The **true equator and equinox of date** include nutation at that instant. Accordingly one distinguishes mean and true obliquity, and mean and true equinox. “Mean” here identifies a defined reference system; it does not mean that an observed coordinate has merely been averaged over several nights. Modern IAU reference frames may use origins independent of the equinox, but the mean/true distinction remains useful for understanding classical equatorial coordinates and sidereal time.[^mean_true]

## Precession of right ascension and declination

A catalogue position referred to an equator and equinox at one date cannot be used unchanged in a mean equatorial system at a later date. **Precessing coordinates** rotates the reference axes between the two dates while representing the same stellar direction. A commonly used standard epoch is **J2000.0**, defined as Julian Date $2451545.0$ in Terrestrial Time (TT), or 2000 January 1 at 12:00 TT. At that historical instant, it was 11:59:27.816 TAI and 11:58:55.816 UTC.[^j2000]

For a short interval $t$ in years from J2000.0, one classical first-order approximation to the change of *mean* equatorial coordinates is

$$
\begin{aligned}
\alpha(t)&\simeq\alpha_0+\left(m+n\sin\alpha_0\tan\delta_0\right)t,\\
\delta(t)&\simeq\delta_0+n\cos\alpha_0\,t,
\end{aligned}
$$

with representative J2000.0 coefficients $m\simeq46.1''\,{\rm yr}^{-1}$ and $n\simeq20.0''\,{\rm yr}^{-1}$. Right ascension in these expressions is an **angle**, so its increment is initially obtained in arcseconds, not in seconds of time; $15''$ of angle corresponds to one second of right ascension. The coefficients are convention-dependent and slowly vary with epoch. These relations isolate precession and assume that the star's own motion has been treated separately. Their $\tan\delta$ term becomes ill-conditioned near a celestial pole, where right ascension itself is poorly defined. For accurate work or large date intervals, one instead rotates a Cartesian unit vector with the adopted precession model.[^precession_coordinates]

## Proper motions of stars

The stars are only approximately fixed markers. Their velocities relative to the Sun have a component along the line of sight, measured as **radial velocity**, and a component across the line of sight, observed as **proper motion**. Proper motion is an *angular rate*, usually given in arcseconds or milliarcseconds per year. At distance $d$ parsecs, a total proper motion $\mu$ arcseconds per year corresponds to transverse speed

$$
v_\perp\simeq4.74047\,\mu\,[{\rm arcsec\,yr^{-1}}],d\,[{\rm pc}]
\quad{\rm km\,s^{-1}}.
$$

The two tabulated components are usually $\mu_{\alpha *}=\dot\alpha\cos\delta$ and $\mu_\delta=\dot\delta$, with $\mu=\sqrt{\mu_{\alpha *}^2+\mu_\delta^2}$. The factor $\cos\delta$ converts a rate in right ascension into a true angular rate along the small circle at that declination. The radial and transverse components together describe the star's three-dimensional velocity ([Figure 16](fig16_velocity_components)).[^proper_motion]

```{figure} _static/_chapter05/fig17_space_velocity.png
:width: 72%
:align: center
:name: fig16_velocity_components

**Figure 16** A star's space velocity decomposed into a radial component along the sightline and a transverse component on the sky. The transverse component produces proper motion.
```

**Barnard's star**, a nearby red dwarf at about $1.8$ pc, provides a conspicuous example. Its proper motion is about $10.3''$ per year, unusually large because it is nearby and has substantial transverse velocity. In a series of images taken years apart, its position shifts against the more distant stellar background ([Figure 17](fig17_barnard_motion)). On a finer annual timescale, its position also oscillates because Earth observes it from changing points on its orbit. Thus a measured astrometric track combines an approximately linear proper-motion trend with annual parallax and the relevant observational corrections. Proper motion and parallax are physically distinct even when both are visible in one sequence.[^proper_motion]

```{figure} _static/_chapter05/fig16_barnards_star.png
:width: 72%
:align: center
:name: fig17_barnard_motion

**Figure 17** Successive positions of Barnard's star against background stars. The large long-term displacement is proper motion; annual parallax adds a smaller periodic displacement.
```

## Catalogue coordinates and the position seen by an observer

A catalogue must state both the coordinate **frame** and the **reference epoch** of a stellar position. The epoch tells us when the listed position applies; proper motion transports the star's direction to a different time. For coordinates tied to a moving equator and equinox, the reference equinox or date of the axes must also be specified. A label such as “J2000” alone should not be taken to describe every part of an astrometric record: modern ICRS coordinates use axes designed to remain fixed, although their source positions still have reference epochs.[^catalogues]

The catalogue excerpt in [Figure 18](fig18_catalogue_example) illustrates these distinctions. It gives one star's coordinates in several frames and lists proper-motion components in milliarcseconds per year. The numbers are a snapshot of a catalogue entry; the example demonstrates why a position and a proper motion must be read together, rather than treating the displayed direction as timeless.

```{figure} _static/_chapter05/fig18_simbad_catalogue.png
:width: 90%
:align: center
:name: fig18_catalogue_example

**Figure 18** Example stellar catalogue entry for HD 219134, showing coordinates in different frames and the two components of proper motion. The frame and epoch labels are part of the coordinate information.
```

To predict the direction actually observed, first propagate the source's astrometric position and, where significant, distance and velocity to the required date. Then transform the reference axes to the date and apply the relevant geometric and light-propagation effects, including precession, nutation, parallax, aberration, and any required gravitational deflection. Finally, specify the observing site and account for Earth rotation, polar motion, diurnal effects, and atmospheric refraction. These operations depend on the desired accuracy and on whether the target is a star or a Solar System body. Their purpose is to transform a well-defined catalogue position into the **apparent**, and ultimately **topocentric observed**, direction needed to point a telescope.[^catalogues]

## References

- **Barbieri, C., and Bertini, I. (2021)**, *Fundamentals of Astronomy*, second edition, Chapters 4–6 for astronomical time, the moving fundamental planes, and Earth-rotation dynamics; Chapter 9 for proper motions; and Chapter 10 for astronomical years and time scales.
- **Karttunen, H., Kröger, P., Oja, H., Poutanen, M., and Donner, K. J. (eds., 2017)**, *Fundamental Astronomy*, sixth edition, Chapter 2, for positional astronomy, time, and apparent positions.
- **Hanslmeier, A. (2023)**, *Introduction to Astronomy and Astrophysics*, Chapter 2, for astronomical coordinates and the apparent motions of celestial objects.
- **US Naval Observatory**, [Glossary](https://aa.usno.navy.mil/faq/asa_glossary), [Terrestrial Time](https://aa.usno.navy.mil/faq/TT), and [Explanatory Supplement, Chapter 15](https://aa.usno.navy.mil/downloads/c15_usb_online.pdf), for standard definitions of years, epochs, and astrometric positions.
- **International Earth Rotation and Reference Systems Service**, [glossary of precession, nutation, and polar motion](https://www.iers.org/iers/en/service/glossary/functions/glossary/P) and [Earth-orientation data](https://datacenter.iers.org/eop.php), for the distinction between celestial and terrestrial pole motion.
- **European Space Agency**, [Proper motion](https://www.esa.int/Science_Exploration/Space_Science/Gaia/Proper_motion), for the Barnard's-star example.

[^time_cycles]: [USNO glossary](https://aa.usno.navy.mil/faq/asa_glossary), entries for sidereal and tropical year; [USNO, Explanatory Supplement, Chapter 15](https://aa.usno.navy.mil/downloads/c15_usb_online.pdf), for the distinction between the mean tropical year and successive equinox passages. The day-length equation assumes uniform mean rates.

[^precession]: Barbieri and Bertini (2021), Chapters 5–6; Karttunen et al. (2017), Chapter 2. Approximate rates and periods are rounded because precession depends on epoch and model.

[^earth_orientation]: [IERS Earth-orientation data](https://datacenter.iers.org/eop.php); [IAU Commission A2](https://www.iau.org/CommissionA2/CommissionA2/Scientific-Objectives.aspx). The latter explains why a time-dependent transformation is required between terrestrial and celestial reference frames.

[^nutation]: Barbieri and Bertini (2021), Sections 5.5–5.6; Karttunen et al. (2017), Chapter 2; [IERS glossary](https://www.iers.org/iers/en/service/glossary/functions/glossary/P). The two sinusoidal terms are the largest terms of a longer nutation series.

[^obliquity]: [USNO precession and nutation report](https://aa.usno.navy.mil/downloads/reports/Kaplan2005b.pdf), which gives a J2000 mean obliquity of $84381.406''$ and an epoch-dependent precession formulation.

[^polar_motion]: [IERS glossary](https://www.iers.org/iers/en/service/glossary/functions/glossary/P) identifies the Chandler component near 430 days and the annual term; [IERS Technical Note 30](https://www.iers.org/SharedDocs/Publikationen/EN/IERS/Publications/tn/TechnNote30/tn30.pdf?__blob=publicationFile&v=2) discusses its variable amplitude and excitation.

[^mean_true]: [USNO sidereal-time explanation](https://aa.usno.navy.mil/data/siderealtime) distinguishes mean and true equinox; [USNO glossary](https://aa.usno.navy.mil/faq/asa_glossary) gives the corresponding coordinate terminology.

[^j2000]: [USNO, Terrestrial Time](https://aa.usno.navy.mil/faq/TT) states the definition of J2000.0 and the equivalent TAI and UTC readings at that epoch.

[^precession_coordinates]: The first-order formula is the classical short-interval approximation associated with precession in equatorial coordinates; see Barbieri and Bertini (2021), Section 5.4, and [USNO, precession and nutation](https://aa.usno.navy.mil/downloads/reports/Kaplan2005b.pdf) for modern vector-based treatment.

[^proper_motion]: Barbieri and Bertini (2021), Chapter 9; [ESA, Proper motion](https://www.esa.int/Science_Exploration/Space_Science/Gaia/Proper_motion) gives Barnard's star's angular rate; [ESA Gaia high-proper-motion examples](https://www.cosmos.esa.int/web/gaia/iow_20250513) gives catalogue context. The transverse-speed relation follows from $1$ au per Julian year $=4.74047\ {\rm km\,s^{-1}}$ and the definition of the parsec.

[^catalogues]: [USNO glossary](https://aa.usno.navy.mil/faq/asa_glossary) defines mean and apparent places and the ICRS; [USNO, Geocentric Positions](https://aa.usno.navy.mil/data/geocentric) illustrates apparent coordinates referred to the true equator and equinox of date. A practical pipeline must follow the conventions of its chosen catalogue and reference frame.
