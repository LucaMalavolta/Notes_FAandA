(chapter06_measuring_the_time)=

# Measuring the Time

:::{danger}
This page still needs substantial revision to match the content presented during the lectures
:::

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

The daily motion of the sky, the succession of lunar phases, and the annual return of the seasons provide three natural ways of measuring time. They do not, however, define equivalent clocks. The Earth rotates at a slightly variable rate, the Moon follows a perturbed orbit, and the equinox moves with respect to the stars. A time scale intended to describe the orientation of a telescope therefore serves a different purpose from one used to integrate a planetary orbit or synchronize a navigation system.

We begin with the unit of time and its astronomical measurement, then distinguish sidereal and solar time. The Moon provides a further example of how the choice of reference direction changes a measured period. Universal, atomic, and dynamical times connect these cycles to precision timekeeping. Finally, calendars, seasons, and twilight show how astronomical time enters ordinary life. The notation follows the preceding chapters: $\alpha$ is right ascension, $HA$ is hour angle, and $\Theta$ is local sidereal time. We reserve $h$ for altitude, although some figures use it for hour angle.

## The second and the importance of consistent units

The **second**, symbol $\mathrm{s}$, is the SI unit of time. Its definition fixes the unperturbed ground-state hyperfine transition frequency of the caesium-133 atom to the exact value

$$
\Delta\nu_{\mathrm{Cs}}=9\,192\,631\,770\ \mathrm{Hz}.
$$

One second consequently corresponds to $9\,192\,631\,770$ periods of the radiation associated with that transition. The two hyperfine levels have total angular-momentum quantum numbers $F=4$ and $F=3$. This definition uses a reproducible quantum transition rather than the rotation or orbital motion of a celestial body. External fields, thermal effects, and motion must be accounted for when realizing it with a physical clock.[^ch06_second]

A clock's altitude does not enter the definition of the second. It does enter the comparison of clocks: gravitational potential and velocity affect their relative rates, so an international time scale requires relativistic corrections. Likewise, the conventional unit **day** is exactly

$$
\boxed{1\ \mathrm{d}=86\,400\ \mathrm{s}}.
$$

The actual duration of one rotation-based mean solar day can differ slightly from $86\,400$ SI seconds. Distinguishing a fixed unit from a measured astronomical cycle is essential throughout this chapter.

An engineering example illustrates the importance of units. **Mars Climate Orbiter**, launched on 11 December 1998, was lost during its arrival at Mars on 23 September 1999. Ground software supplied thruster impulse data in pound-force seconds, while the navigation software expected newton seconds. The conversion factor is approximately $4.45$. The resulting trajectory brought the spacecraft to an estimated altitude of only $57\ \mathrm{km}$, much lower than the intended passage at roughly $140$–$150\ \mathrm{km}$, where atmospheric interaction became destructive ([Figure 1](fig01_time_mars_climate_orbiter)). An otherwise meaningful numerical value becomes a different physical quantity when its unit is interpreted incorrectly.[^ch06_mars_orbiter]

```{figure} _static/_chapter06/fig01_mars_climate_orbiter.png
:width: 48%
:align: center
:name: fig01_time_mars_climate_orbiter

**Figure 1** Mars Climate Orbiter. Its loss during orbital insertion illustrates the consequences of inconsistent units in spacecraft navigation.
```

## Measuring time with a meridian telescope

Before atomic clocks, accurate timekeeping was closely connected to positional astronomy. A **meridian telescope** turns about a horizontal East–West axis, so its line of sight remains in the local meridian plane. The observer selects the appropriate altitude and records the instant at which a star crosses a reference line in the focal plane. The telescope changes declination along the meridian; it does not track the star through arbitrary hour angles.

The meridian room at **La Specola**, the historical astronomical observatory in Padova, provides a concrete example ([Figure 2](fig02_time_specola)). An opening in the wall allowed observations in the meridian plane. A star with known right ascension supplied a time reference through its transit. Conversely, a calibrated clock allowed an unknown right ascension to be measured. This reciprocal relation between position and time is the basis of classical transit astronomy.[^ch06_sidereal]

```{figure} _static/_chapter06/fig02_specola_meridian_room.png
:width: 75%
:align: center
:name: fig02_time_specola

**Figure 2** The meridian room at La Specola in Padova. The observing aperture constrained the view to the meridian, where stellar transits could be timed precisely.
```

## Sidereal time

Right ascension is measured eastward along the celestial equator from the vernal equinox $\gamma$. Hour angle is measured westward from the local meridian. The **local sidereal time** is the hour angle of the equinox itself:

$$
\Theta=HA(\gamma).
$$

The angular relations in [Figure 3](fig03_time_sidereal_geometry) give

$$
\boxed{\Theta=HA+\alpha},
\qquad
HA=\Theta-\alpha,
$$

with the result understood modulo $24\ \mathrm{h}$, or $360^\circ$. At upper meridian transit, $HA=0$, and therefore

$$
\boxed{\Theta_{\mathrm{transit}}=\alpha}.
$$

Before upper transit, a star on the eastern side of the meridian has a negative signed hour angle; afterwards, its hour angle is positive. For example, a star at $\alpha=6\ \mathrm{h}$ observed when $\Theta=5\ \mathrm{h}$ has $HA=-1\ \mathrm{h}$ and has yet to reach the meridian. The right ascension and sidereal time used in this relation must refer to the same equator and equinox. Precise observations require the appropriate apparent coordinates rather than an uncorrected catalogue position.[^ch06_sidereal_coordinates]

```{figure} _static/_chapter06/fig03_sidereal_geometry.png
:width: 65%
:align: center
:name: fig03_time_sidereal_geometry

**Figure 3** Right ascension $\alpha$, hour angle, and local sidereal time $\Theta$. The symbol $h$ in this diagram denotes hour angle. Their geometry gives $\Theta=HA+\alpha$.
```

A **sidereal day** is the interval between successive meridian passages of the equinox. To elementary accuracy, it can be identified with a full rotation relative to distant stars. A **solar day** is the interval between successive upper meridian passages of the Sun. During one terrestrial rotation, the Earth advances along its orbit. It must turn through an additional angle, approximately $1^\circ$, before the Sun returns to the same meridian ([Figure 4](fig04_time_day_lengths)). The mean solar day is consequently about four minutes longer than the sidereal day.

```{figure} _static/_chapter06/fig04_sidereal_solar_day.png
:width: 57%
:align: center
:name: fig04_time_day_lengths

**Figure 4** After rotating once relative to a distant celestial direction, the Earth must turn a little farther to face the Sun again. The orbital displacement is exaggerated for clarity.
```

Both kinds of day are conventionally divided into 24 hours, but a sidereal hour is shorter than a mean solar hour. Near the present epoch,

$$
24\ \mathrm{h\ of\ mean\ solar\ time}
\simeq24\ \mathrm{h}\ 3\ \mathrm{min}\ 56.56\ \mathrm{s\ of\ sidereal\ time}.
$$

Equivalently, 24 sidereal hours correspond to approximately **23 h 56 min 4 s** of mean solar time. These expressions compare the readings of two differently graduated clocks over the same physical interval; they do not imply that the SI second has two definitions.

### Apparent and mean sidereal time

The equinox is not fixed. Precession produces a slow, smooth displacement, while nutation adds shorter oscillations. The **true equinox** includes both effects; the **mean equinox** omits nutation while retaining precession. Their hour angles define **apparent sidereal time** $\Theta_{\mathrm{a}}$ and **mean sidereal time** $\Theta_{\mathrm{M}}$, respectively.

The difference is the **equation of the equinoxes**. Its leading term is

$$
\boxed{\Theta_{\mathrm{a}}-\Theta_{\mathrm{M}}
\simeq\Delta\psi\cos\varepsilon},
$$

where $\Delta\psi$ is nutation in longitude and $\varepsilon$ is the obliquity. The equation is expressed in angular units; an angular correction in arcseconds is divided by 15 to obtain seconds of sidereal time. Its magnitude is of order one second of time. More complete expressions include small additional terms.[^ch06_equation_equinoxes]

### Rotation and revolution

Let $P$ be a planet's orbital period, $\tau_*$ its rotation period relative to the stars, and $\tau$ its solar or **synodic day**, all in the same units. For prograde rotation, the number of stellar rotations in one revolution exceeds the number of solar days by one:

$$
\frac{P}{\tau_*}-\frac{P}{\tau}=1,
\qquad
\boxed{\frac{1}{\tau}=\frac{1}{\tau_*}-\frac{1}{P}}.
$$

Using $\tau=1\ \mathrm{d}$ and $P=365.2564\ \mathrm{d}$ gives

$$
\tau_*=\frac{P\tau}{P+\tau}
\simeq0.99727\ \mathrm{d}.
$$

For **retrograde rotation**, using positive period magnitudes,

$$
\frac{1}{\tau}=\frac{1}{\tau_*}+\frac{1}{P}.
$$

The distinction concerns the sense of rotation relative to orbital motion. These relations describe mean rates. At higher precision, a stellar rotation period and an equinox-based sidereal day must be distinguished because the equinox itself precesses.[^ch06_day_periods]

## Using the Sun to measure the year

The Sun's annual motion supplies two different years. The **sidereal year**, approximately $365.2564\ \mathrm{d}$, measures a complete revolution relative to distant stars. The **tropical year**, approximately $365.2422\ \mathrm{d}$, follows the moving equinox and therefore the seasonal cycle. It is shorter by approximately 20 minutes because the equinox moves westward, against the Sun's apparent eastward motion ([Figure 5](fig05_time_tropical_year)).[^ch06_years]

```{figure} _static/_chapter06/fig05_tropical_year.png
:width: 65%
:align: center
:name: fig05_time_tropical_year

**Figure 5** The moving equinox is reached before the Earth completes one revolution relative to the stars. The numerical annotations refer to an older reference epoch; the geometry explains the distinction between tropical and sidereal years.
```

At elementary level, a tropical year is described as the interval between successive vernal equinoxes. More precisely, the **mean tropical year** is the interval during which the Sun's mean ecliptic longitude, measured from the mean equinox of date, increases by $360^\circ$. An individual equinox-to-equinox interval differs slightly from this mean definition because of orbital perturbations and the changing geometry of the reference system.

The following historical intervals illustrate that the return of a particular equinox is not an invariant duration:

| Successive vernal equinoxes | Days | Hours | Minutes | Seconds |
|---|---:|---:|---:|---:|
| 1985–1986 | 365 | 5 | 48 | 58 |
| 1986–1987 | 365 | 5 | 49 | 15 |
| 1987–1988 | 365 | 5 | 46 | 38 |
| 1988–1989 | 365 | 5 | 49 | 42 |
| 1989–1990 | 365 | 5 | 51 | 6 |

The few-minute variation in these intervals should not be interpreted as a comparable annual variation of the mean tropical year. It concerns the timing of the particular apparent equinox passages used as endpoints.

## The mean Sun and mean solar time

The real Sun does not move uniformly in right ascension. Two effects contribute. First, it travels along the **ecliptic**, inclined to the celestial equator, so equal ecliptic arcs project into unequal right-ascension arcs. Second, the Earth's orbit is **elliptical**. Kepler's second law makes its orbital angular speed greater near perihelion, in early January, than near aphelion, in early July. The Sun's apparent angular speed reflects this variation. The geometries are illustrated in [Figures 6](fig06_time_sun_planes) and [7](fig07_time_elliptical_orbit).[^ch06_solar_time]

```{figure} _static/_chapter06/fig06_sun_ecliptic_equator.png
:width: 48%
:align: center
:name: fig06_time_sun_planes

**Figure 6** The Sun's annual path lies along the ecliptic rather than the celestial equator. Its varying declination accompanies a non-uniform increase of right ascension.
```

```{figure} _static/_chapter06/fig07_earth_elliptical_orbit.png
:width: 78%
:align: center
:name: fig07_time_elliptical_orbit

**Figure 7** The Earth's elliptical orbit, perihelion, aphelion, equinoxes, and solstices. Orbital eccentricity and axial inclination are independent contributions to the variation of apparent solar time.
```

For a Sun on the ecliptic, neglecting its small ecliptic latitude,

$$
\tan\alpha_\odot=\cos\varepsilon\tan\lambda_\odot,
\qquad
\sin\delta_\odot=\sin\varepsilon\sin\lambda_\odot.
$$

The appropriate quadrant must be retained when finding $\alpha_\odot$. Differentiating the first relation, with obliquity treated as constant over one year, gives

$$
\frac{d\alpha_\odot}{dt}
=\frac{\cos\varepsilon}{1-\sin^2\varepsilon\sin^2\lambda_\odot}
\frac{d\lambda_\odot}{dt}.
$$

Even a constant $d\lambda_\odot/dt$ would therefore produce a variable $d\alpha_\odot/dt$. Earth's eccentricity introduces a further variation in $d\lambda_\odot/dt$ itself.

To remove these annual irregularities, we introduce the **mean Sun**: a fictitious point that moves uniformly along the celestial equator and completes a circuit in one tropical year. The **local mean solar time** is

$$
\boxed{T_{\mathrm{M}}=HA_{\mathrm{M}}+12\ \mathrm{h}}.
$$

The addition of 12 hours places mean noon at $12\ \mathrm{h}$ and the change of date at midnight. The corresponding **apparent solar time**, approximately the time indicated by a correctly aligned sundial, is

$$
T_\odot=HA_\odot+12\ \mathrm{h}.
$$

The fictitious Sun removes the non-uniform annual motion of the real Sun from this definition. It does not remove irregularities in the Earth's rotation, which affect the meridian against which both hour angles are measured.

## The equation of time

The **equation of time** is the difference between apparent and mean solar time:

$$
\boxed{E=T_\odot-T_{\mathrm{M}}
=HA_\odot-HA_{\mathrm{M}}
=\alpha_{\mathrm{M}}-\alpha_\odot}.
$$

Here right ascensions and hour angles are expressed in time units. The last difference is taken as the small, continuous angular separation between the two Suns. Our sign convention is **apparent minus mean**; some references use the opposite convention. A positive $E$ means that a sundial is ahead of local mean solar time. To convert its reading, use

$$
T_{\mathrm{M}}=T_\odot-E.
$$

The eccentricity contribution has a main period of one year, while the obliquity contribution has a main period of half a year. Their superposition gives the characteristic curve in [Figure 8](fig08_time_equation). The equation of time reaches approximately $+16\ \mathrm{min}$ in early November and $-14\ \mathrm{min}$ in mid-February, and crosses zero about four times per year.[^ch06_equation_of_time]

```{figure} _static/_chapter06/fig08_equation_of_time.png
:width: 70%
:align: center
:name: fig08_time_equation

**Figure 8** Contributions of orbital eccentricity and axial inclination to the equation of time, and their combined effect. The ordinate is apparent solar time minus mean solar time, in minutes.
```

For example, if $E=+16\ \mathrm{min}$, the real Sun crosses the meridian when local mean solar time is approximately $11{:}44$. Apparent noon is then earlier than mean noon. This comparison concerns **local** time. A civil clock also includes the offset of the adopted time zone and, where applicable, daylight saving time; those conventions are considered below.

## The analemma

Observe the Sun from one location at the same mean solar time throughout a year. Its position changes in two coordinates: declination follows the seasonal north–south displacement, while the equation of time produces an east–west displacement. The resulting curve is the **analemma**. On Earth it resembles an unequal figure eight ([Figures 9](fig09_time_analemma) and [10](fig10_time_analemma_photo)). The apparent orientation of the figure depends on latitude and the time of day chosen for the observations.

```{figure} _static/_chapter06/fig09_analemma_diagram.png
:width: 42%
:align: center
:name: fig09_time_analemma

**Figure 9** The terrestrial analemma plotted in declination and equation of time. The dates label successive positions during the year; the horizontal axis identifies when the apparent Sun is fast or slow relative to mean time.
```

```{figure} _static/_chapter06/fig10_analemma_photograph.png
:width: 70%
:align: center
:name: fig10_time_analemma_photo

**Figure 10** A photographic composite of the Sun observed at a fixed clock time through the year. The positions trace the figure-eight analemma.
```

Three limiting cases separate the physical causes:

1. **No axial tilt and a circular orbit.** Declination is constant and the orbital speed is uniform. The Sun returns to the same position at the chosen mean solar time: the analemma reduces to a point.
2. **No axial tilt and an eccentric orbit.** Declination remains constant, but the equation of time changes. The Sun moves back and forth along a segment.
3. **Axial tilt and a circular orbit.** Declination varies, and projection onto the equator produces an equation of time even though the orbital speed is uniform. A symmetric figure eight results in a declination–time plot.

The Earth combines tilt and eccentricity. Their relative phase makes the two lobes unequal, as the annual example in [Figure 11](fig11_time_analemma_year) also shows. A fixed civil-clock observing time must be corrected for any seasonal clock change if it is to represent one fixed mean-time observing schedule.

```{figure} _static/_chapter06/fig11_analemma_2011.png
:width: 90%
:align: center
:name: fig11_time_analemma_year

**Figure 11** An annual example of the Earth's analemma, with dates and the orbital geometry that produces its unequal lobes.
```

### An analemma on Mars

The same reasoning applies to other planets. Mars has a larger orbital eccentricity than Earth, approximately $0.093$ rather than $0.017$, and an axial tilt of about $25^\circ$. A Martian year lasts about 687 terrestrial days, or 669 **sols**, where a sol is a Martian solar day ([Figure 12](fig12_time_mars_orbit)). The eccentricity contribution is sufficiently strong that the Martian analemma has a stretched, pear-like form rather than Earth's familiar figure eight.

```{figure} _static/_chapter06/fig12_mars_earth_orbits.png
:width: 60%
:align: center
:name: fig12_time_mars_orbit

**Figure 12** Comparison of the Earth and Mars orbital cycles. A Martian year contains approximately 687 Earth days or 669 Martian solar days.
```

[Figure 13](fig13_time_martian_analemma) is a simulation placed over the Mars Pathfinder panorama. It represents the Sun in the late afternoon at intervals of **30 sols**, beginning on Pathfinder sol 24, corresponding to 29 July 1997. The simulated sequence makes the planetary dependence of the analemma immediately visible.[^ch06_martian_analemma]

```{figure} _static/_chapter06/fig13_martian_analemma.png
:width: 80%
:align: center
:name: fig13_time_martian_analemma

**Figure 13** Simulated Martian analemma over the Pathfinder landing-site panorama, with one solar position every 30 sols. Digital illustration: Dennis Mammana; NASA Astronomy Picture of the Day, 30 December 2006.
```

## Measuring time with the Moon

The phases of the Moon supply another natural cycle. **New Moon** is defined as the instant when the geocentric ecliptic longitudes of the Moon and Sun are equal. This is a longitude alignment, not necessarily an exact angular overlap: the Moon can lie north or south of the ecliptic. A solar eclipse therefore does not occur at every New Moon.

The **synodic month**, or **lunation**, is the interval between successive New Moons. Its mean duration is approximately

$$
S=29.53059\ \mathrm{d}
\simeq29\ \mathrm{d}\ 12\ \mathrm{h}\ 44\ \mathrm{min}\ 3\ \mathrm{s}.
$$

The **sidereal month** is the Moon's orbital period relative to the distant stars:

$$
P_{\mathrm{Moon}}=27.32166\ \mathrm{d}
\simeq27\ \mathrm{d}\ 7\ \mathrm{h}\ 43\ \mathrm{min}\ 12\ \mathrm{s}.
$$

These are mean values, rather than identical durations for every individual cycle. During one sidereal month, the Earth–Moon system advances along its orbit around the Sun. The Moon must move farther around Earth to recover the original phase alignment ([Figure 14](fig14_time_lunar_months)). In the approximation of uniform, coplanar motion,

$$
\boxed{\frac{1}{S}=\frac{1}{P_{\mathrm{Moon}}}-\frac{1}{P_{\mathrm{Earth}}}}.
$$

Taking $P_{\mathrm{Earth}}\simeq365.2564\ \mathrm{d}$ recovers a synodic period close to $29.53\ \mathrm{d}$. This is the same relative-angular-speed argument used to distinguish the solar day from a stellar rotation period.[^ch06_lunar_periods]

```{figure} _static/_chapter06/fig14_lunar_sidereal_synodic.png
:width: 80%
:align: center
:name: fig14_time_lunar_months

**Figure 14** The Moon returns to the same stellar direction after about 27.32 days, but requires about 29.53 days to restore its alignment with the Sun. The Earth's orbital displacement changes the Sun's direction during the interval.
```

## Why lunations have different lengths

An individual lunation can differ from the mean by several hours. [Figure 15](fig15_time_lunation_short) shows this variability during 2008–2010. Its left axis gives the departure from the mean duration, while its right axis gives the Moon's **true anomaly** at New Moon. True anomaly is the angle measured from perigee to the Moon's instantaneous position, in the direction of orbital motion ([Figure 16](fig16_time_true_anomaly)).[^ch06_lunar_variations]

```{figure} _static/_chapter06/fig15_lunation_2008_2010.png
:width: 80%
:align: center
:name: fig15_time_lunation_short

**Figure 15** Departures of individual lunations from their mean duration during 2008–2010, compared with the Moon's true anomaly at New Moon. The two ordinates represent different quantities.
```

```{figure} _static/_chapter06/fig16_lunar_true_anomaly.png
:width: 75%
:align: center
:name: fig16_time_true_anomaly

**Figure 16** Perigee, apogee, the line of apsides, and true anomaly in an elliptical lunar orbit. The eccentricity is exaggerated to make the geometry clear.
```

The Moon moves faster near **perigee** and slower near **apogee**. The extra angular distance required to regain the Sun is therefore traversed at different speeds depending on where New Moon falls in the orbit. [Figure 17](fig17_time_synodic_geometry) compares two cases. In orbits **A–B**, New Moon occurs near perigee. After returning to the same position relative to perigee, the Moon covers the remaining arc rapidly. In orbits **C–D**, New Moon occurs near apogee, and the remaining arc takes longer.

```{figure} _static/_chapter06/fig17_lunar_synodic_geometry.png
:width: 80%
:align: center
:name: fig17_time_synodic_geometry

**Figure 17** Two geometries for restoring the New Moon alignment: A–B near perigee and C–D near apogee. The Earth moves along its solar orbit while the Moon completes its revolution; the extra lunar arc is crossed faster near perigee.
```

The distinction is a useful first explanation, rather than a complete prediction. The Earth's own variable orbital speed and the Sun's gravitational perturbation of the lunar orbit also contribute. The regular progression of true anomaly at successive New Moons reflects the fact that the phase cycle and the perigee cycle do not have the same period.

## The anomalistic month and apsidal precession

The **anomalistic month** is the interval between successive passages through perigee. Its mean duration is approximately

$$
A=27.55455\ \mathrm{d},
$$

about $0.23\ \mathrm{d}$ longer than the sidereal month. Perigee moves eastward in the same sense as the Moon's orbital motion, so the Moon must travel beyond one stellar revolution to encounter it again. [Figure 18](fig18_time_anomalistic) shows that individual perigee-to-perigee intervals also vary.

```{figure} _static/_chapter06/fig18_anomalistic_month.png
:width: 80%
:align: center
:name: fig18_time_anomalistic

**Figure 18** Variation of the anomalistic month during 2008–2010. The angular curves describe the relative orientation of the Sun and lunar perigee; the left axis gives departures of the perigee-to-perigee and apogee-to-apogee intervals from their mean.
```

The **line of apsides** joins the nearest and farthest points of an orbit: periapsis and apoapsis, called perigee and apogee for an Earth-centred orbit. Its gradual rotation is **apsidal precession** ([Figure 19](fig19_time_apsidal_precession)). The lunar line of apsides completes one prograde circuit in approximately **8.85 years**. If $P_{\mathrm{aps}}$ is that period, the mean-rate relation is

$$
\frac{1}{A}=\frac{1}{P_{\mathrm{Moon}}}-\frac{1}{P_{\mathrm{aps}}}.
$$

This rotation of the orbital ellipse must be distinguished from the axial precession of the Earth and from the regression of the lunar orbital nodes. A more eccentric ellipse makes the contrast between perigee and apogee more pronounced, but the rate of apsidal precession depends on the particular perturbing forces; it does not obey a universal rule of increasing with eccentricity.[^ch06_apsidal_period]

```{figure} _static/_chapter06/fig19_apsidal_precession.png
:width: 58%
:align: center
:name: fig19_time_apsidal_precession

**Figure 19** Apsidal precession changes the orientation of an elliptical orbit while leaving the central body near one focus. This schematic illustrates successive orientations of the major axis.
```

### The longer pattern of lunation lengths

The difference between the mean longitudes of the Sun and perigee measures their relative orientation. It determines whether the New Moon alignment falls near the fast or slow part of the lunar orbit. Because the synodic and anomalistic months have different lengths, a similar phase–perigee configuration recurs on a beat period of approximately

$$
P_{\mathrm{beat}}
=\left|\frac{1}{A}-\frac{1}{S}\right|^{-1}
\simeq412\ \mathrm{d}.
$$

The longer sequence in [Figure 20](fig20_time_lunation_long) also contains modulation associated with the Earth's eccentricity and the changing orientation of the lunar apsides. The 8.85-year apsidal period is measured relative to the stars. The orientation relative to the Earth's perihelion changes on a nearby period, while the angle from the Sun changes much faster during each annual revolution. These are different angular comparisons and should not be assigned one common period.

```{figure} _static/_chapter06/fig20_lunation_2008_2027.png
:width: 85%
:align: center
:name: fig20_time_lunation_long

**Figure 20** Variation of lunation length over 2008–2027. The rapid oscillations and their changing envelope reflect several interacting cycles, including lunar phase, lunar perigee, and the Earth's orbital motion.
```

## The draconic month

The lunar orbital plane is inclined by about $5.1^\circ$ to the ecliptic. The intersection of the two planes defines a **line of nodes**. At the **ascending node**, the Moon crosses from south to north of the ecliptic; at the descending node it crosses from north to south ([Figure 21](fig21_time_lunar_nodes)).

```{figure} _static/_chapter06/fig21_lunar_nodes.png
:width: 75%
:align: center
:name: fig21_time_lunar_nodes

**Figure 21** The inclined lunar orbital plane, ascending and descending nodes, and their retrograde motion. The nodal line completes a circuit in approximately 18.6 years.
```

The **draconic month**, also called the **draconitic** or **nodical month**, is the interval between successive passages through the ascending node. Its mean duration is

$$
D=27.21222\ \mathrm{d}
\simeq27\ \mathrm{d}\ 5\ \mathrm{h}\ 5\ \mathrm{min}\ 36\ \mathrm{s}.
$$

It is shorter than the sidereal month because the nodes regress westward, against the Moon's eastward motion. With a positive nodal regression period $P_{\mathrm{node}}\simeq18.6\ \mathrm{yr}$,

$$
\frac{1}{D}=\frac{1}{P_{\mathrm{Moon}}}+\frac{1}{P_{\mathrm{node}}}.
$$

The nodal period sets the mean difference from the sidereal month. Lunar eccentricity and the changing orientation of perigee relative to the nodes modulate individual crossing intervals ([Figure 22](fig22_time_draconic)). The draconic cycle is especially relevant to eclipses, which require a phase alignment to occur close to a node.[^ch06_draconic_period]

```{figure} _static/_chapter06/fig22_draconic_month.png
:width: 80%
:align: center
:name: fig22_time_draconic

**Figure 22** Departures of individual draconic months from the mean and the changing angle between lunar perigee and the ascending node. The larger-scale envelope accompanies their changing relative orientation.
```

## The Moon's changing orbital parameters

The lunar orbit is not one fixed Keplerian ellipse. A useful instantaneous description uses **osculating orbital elements**: the elements of the ellipse that matches the Moon's position and velocity at one instant. Solar perturbations change those elements continuously. Three examples complete the comparison of lunar periods.

First, **perigee and apogee distances vary** ([Figure 23](fig23_time_lunar_distances)). Changes in the orbit's shape and size alter the closest and farthest Earth–Moon separations. A quoted mean distance does not specify the distance at a particular perigee or apogee.

```{figure} _static/_chapter06/fig23_lunar_perigee_apogee.png
:width: 80%
:align: center
:name: fig23_time_lunar_distances

**Figure 23** Changes in lunar perigee and apogee distance during 2008–2010, shown with the eccentricity at perigee and the relative longitude of the Sun and lunar perigee. The left ordinate is in thousands of kilometres.
```

Second, the **eccentricity varies** ([Figure 24](fig24_time_lunar_eccentricity)). Its commonly quoted mean value, about $0.055$, summarizes a perturbed orbit rather than specifying an immutable ellipse. The changing eccentricity affects the speed contrast between perigee and apogee and therefore the durations of the various months.

```{figure} _static/_chapter06/fig24_lunar_eccentricity.png
:width: 80%
:align: center
:name: fig24_time_lunar_eccentricity

**Figure 24** Variation of instantaneous lunar eccentricity during 2008–2010. The superposed angular curves describe the solar orientation relative to lunar perigee.
```

Third, the **inclination and instantaneous nodal longitude vary** ([Figure 25](fig25_time_lunar_inclination)). A mean inclination near $5.1^\circ$ is sufficient for elementary geometry, but precision eclipse calculations require the time-dependent orbit. These graphs explain why the Moon is an effective natural calendar marker while its individual cycles are unsuitable as a uniform laboratory clock.

```{figure} _static/_chapter06/fig25_lunar_inclination.png
:width: 75%
:align: center
:name: fig25_time_lunar_inclination

**Figure 25** The lunar orbital inclination and instantaneous ascending-node longitude during 2008–2010. The inclination oscillates around its mean as the geometry of the solar perturbation changes.
```

For reference, the four mean lunar periods describe four different returns:

| Period | Reference used for the return | Approximate duration |
|---|---|---:|
| Synodic month | Sun–Moon phase alignment | $29.53059\ \mathrm{d}$ |
| Sidereal month | Distant stars | $27.32166\ \mathrm{d}$ |
| Anomalistic month | Perigee | $27.55455\ \mathrm{d}$ |
| Draconic month | Ascending node | $27.21222\ \mathrm{d}$ |

## Universal Time and Julian dates

The **mean solar time at Greenwich** supplies the traditional definition of **Universal Time**, UT:

$$
UT=HA_{\mathrm{M,Greenwich}}+12\ \mathrm{h}.
$$

At a site of longitude $\lambda$, positive east of Greenwich, the local mean solar time is approximately

$$
\boxed{T_{\mathrm{M}}(\lambda)=UT1+\lambda_{\mathrm{h}}},
\qquad
\lambda_{\mathrm{h}}=\frac{\lambda\ [\mathrm{degrees}]}{15}\ \mathrm{h},
$$

with the appropriate calendar-date adjustment if the result crosses midnight. For example, longitude $15^\circ$ east corresponds to a local mean time one hour ahead of Greenwich.

For precision work, the relevant rotation scale is **UT1**. It removes the observing-site dependence associated with polar motion from the older observational quantity UT0. Modern UT1 is obtained from measurements of the Earth's rotation angle, especially through **Very Long Baseline Interferometry** (VLBI) of distant extragalactic radio sources. UT1 therefore describes the actual orientation of Earth, whereas an atomic clock measures elapsed time independently of that rotation. The historical name **Greenwich Mean Time**, GMT, is closely connected to mean solar time, but precision astronomical calculations specify UT1 explicitly.[^ch06_universal]

### A continuous count of days

Calendar dates are inconvenient for calculating intervals: months have different lengths and years may contain leap days. The **Julian Date**, JD, replaces this structure with a continuous day count and a fractional day. Its conventional origin is **noon on 1 January 4713 BCE in the proleptic Julian calendar**, equivalent to astronomical year $-4712$.

The count changes integer value at noon rather than midnight. For example,

$$
\begin{aligned}
\text{2000 January 1, 00:00 UT1}&\longleftrightarrow JD_{UT1}=2\,451\,544.5,\\
\text{2000 January 1, 12:00 UT1}&\longleftrightarrow JD_{UT1}=2\,451\,545.0.
\end{aligned}
$$

The word *Julian* in Julian Date should not be confused with a calendar date written in the Julian calendar. A Gregorian date can be converted into JD without changing the instant it represents. The [US Naval Observatory Julian Date converter](https://aa.usno.navy.mil/data/JulianDate) provides this conversion for calendar dates expressed in UT1.[^ch06_julian_date]

JD is a **representation**, not a physical time scale. It must be associated with a scale, such as $JD_{UT1}$, $JD_{TT}$, or $JD_{TDB}$. In uniform atomic or dynamical scales, one Julian-date unit represents $86\,400$ seconds of that scale. UTC requires special care on a leap-second day. The **Modified Julian Date** is

$$
MJD=JD-2\,400\,000.5,
$$

so that its integer boundary falls at midnight and its values are shorter to write.

A **Julian year** contains exactly $365.25$ days, and a **Julian century** contains $36\,525$ days. The number of Julian centuries from the reference value $JD=2\,451\,545.0$ is

$$
\boxed{T_{\mathrm{cent}}=\frac{JD-2\,451\,545.0}{36\,525}}.
$$

The chosen time scale must match the application. Precession and dynamical expressions commonly use TT, while an expression for the Earth's rotation requires UT1. The formal reference epoch **J2000.0** is defined on TT, a distinction developed below.

## Why rotation-based time is not uniform

Removing the equation of time does not make Earth's rotation perfectly regular. Sidereal time and UT1 retain variations in the rotation rate. Three broad contributions can be distinguished.[^ch06_rotation]

1. **Secular slowing.** Tidal dissipation transfers angular momentum from Earth's rotation to the lunar orbit. The long-term increase of the length of day is of order a few milliseconds per century; about $2\ \mathrm{ms}$ per century is a useful approximate scale, rather than an exact constant applicable to every epoch.
2. **Seasonal variations.** Atmospheric circulation, oceanic motion, and other seasonal mass movements exchange angular momentum with the solid Earth. They produce changes in day length of order milliseconds.
3. **Irregular geophysical variations.** Exchange of angular momentum between the core and mantle, changes in mass distribution, and other processes introduce fluctuations that cannot be represented by a single periodic correction.

[Figure 26](fig26_time_tidal_rotation) illustrates the tidal mechanism. Earth's rotation carries its tidal deformation ahead of the Earth–Moon direction. The resulting torque slows terrestrial rotation and transfers angular momentum to the Moon's orbit. Other geophysical effects modify the observed long-term trend.

```{figure} _static/_chapter06/fig26_tides_rotation.png
:width: 68%
:align: center
:name: fig26_time_tidal_rotation

**Figure 26** Schematic tidal coupling of Earth's rotation and the Moon's orbit. The displaced tidal bulge exerts a torque, transferring angular momentum from terrestrial spin to lunar orbital motion.
```

A small change in the length of each day accumulates into a much larger difference between rotation time and a uniform reference. Ancient eclipse observations therefore constrain the historical difference between these scales: an eclipse prediction depends on both the Moon's orbit and which terrestrial longitude was turned toward it. For precision dynamics we need a reference whose rate is established independently of Earth's rotation.

## International Atomic Time

**International Atomic Time**, TAI, from the French *Temps atomique international*, is a continuous time scale built from atomic-clock measurements. Its unit is the SI second, realized through atomic frequency standards. The **Bureau International des Poids et Mesures** (BIPM) combines clock and time-transfer data from laboratories around the world rather than relying on one privileged clock. The ensemble contains hundreds of clocks; primary and secondary frequency standards calibrate its rate.[^ch06_atomic_time]

In Italy, **INRiM**, the *Istituto Nazionale di Ricerca Metrologica* in Torino, contributes to TAI and maintains the national realization UTC(IT). Clock comparisons use satellite links, including GNSS, as well as other calibrated transfer techniques. GPS and Galileo disseminate timing information, but their system times and their relations to UTC must be distinguished. Historically, terrestrial radio-navigation systems such as Loran-C and Omega also supplied timing signals; they should not be taken as a description of the present international clock network.[^ch06_inrim]

The historical origin of atomic time was aligned with Universal Time at the beginning of **1 January 1958**. Its later divergence from rotation time reflects the different rates of the two physical references. The modern system of atomic seconds and leap-second-based civil time was adopted in **1972**.[^ch06_atomic_history]

A relative frequency difference of $2\times10^{-13}$ illustrates the precision involved. If it persisted for a day, the accumulated timing difference would be

$$
\delta t=(2\times10^{-13})(86\,400\ \mathrm{s})
=1.728\times10^{-8}\ \mathrm{s}
\simeq17\ \mathrm{ns}.
$$

This is an illustrative conversion between fractional frequency and accumulated time error, not a fixed specification of every atomic clock or of TAI. Stability, systematic accuracy, and the uncertainty of time transfer are different quantities. Atomic time is exceptionally regular, but a real realization always has measurement uncertainty. Relativistic rate corrections are also necessary when clocks occupy different gravitational potentials or have different velocities.

## Coordinated Universal Time

Civil time uses **Coordinated Universal Time**, UTC. Between adjustments, UTC has the same rate as TAI and differs from it by an integer number of seconds:

$$
\boxed{\Delta AT=TAI-UTC},
\qquad
UTC=TAI-\Delta AT.
$$

Under the leap-second system introduced in 1972, UTC is kept within $0.9\ \mathrm{s}$ of UT1:

$$
\left|UT1-UTC\right|<0.9\ \mathrm{s}.
$$

The difference $DUT1=UT1-UTC$ is measured and published; it is not the same as $\Delta AT$. A **leap second** changes $\Delta AT$ when needed. Positive leap seconds have usually been inserted at the end of 30 June or 31 December. A negative leap second is allowed in principle if the measured rotation requires one. Their scheduling follows observations and official announcements rather than a fixed annual rule.[^ch06_utc]

[Figure 27](fig27_time_ut1_utc) shows the resulting sawtooth history of $UT1-UTC$. Between adjustments, variable Earth rotation changes the difference. At an adjustment, the UTC labeling changes by one second relative to the continuous atomic scale. A positive leap-second day contains $86\,401$ SI seconds and includes the label $23{:}59{:}60$.

```{figure} _static/_chapter06/fig27_ut1_utc_history.png
:width: 90%
:align: center
:name: fig27_time_ut1_utc

**Figure 27** Historical variation of $UT1-UTC$. The one-second steps mark leap-second adjustments, while the intervening slopes reflect changes in the Earth's rotation rate.
```

[Figure 28](fig28_time_atomic_rotation) compares UT1 and UTC with TAI over an earlier interval. UTC remains piecewise parallel to TAI, while UT1 follows terrestrial rotation. These historical curves illustrate the mechanism; they do not provide the offsets for a new observation.

```{figure} _static/_chapter06/fig28_atomic_rotational_times.png
:width: 70%
:align: center
:name: fig28_time_atomic_rotation

**Figure 28** UT1 and UTC relative to TAI in a historical record. The staircase in $UTC-TAI$ and the smoother, irregular change of $UT1-TAI$ arise from different definitions of the scales.
```

UTC is practical for timestamps and civil coordination. Elapsed intervals that span a leap second must be evaluated with a leap-second-aware conversion, or in a continuous scale such as TAI. The $0.9$-second condition describes the established leap-second system. A **2022 CGPM resolution** decided that the permitted difference between UT1 and UTC will be increased in or before **2035**, so this condition should not be assumed to be a permanent definition for all future epochs.[^ch06_utc_future]

## Standard time zones

Local mean solar time changes continuously with longitude. For civil purposes, neighbouring places adopt a common **standard time**. A nominal one-hour difference corresponds to $15^\circ$ of longitude, but actual time-zone boundaries follow political and practical choices. Some offsets include half hours or quarter hours, so there is no exact division into 24 equal geographical strips.

Civil time can be written schematically as

$$
T_{\mathrm{civil}}=UTC+\text{adopted offset},
$$

including a date change where necessary. Italy uses **Central European Time**, CET, at $UTC+1\ \mathrm{h}$, and **Central European Summer Time**, CEST, at $UTC+2\ \mathrm{h}$. Neither is the local mean solar time of every Italian town. The historical map in [Figure 29](fig29_time_zones) illustrates the geographical arrangement, but time-zone boundaries and legal offsets can change.[^ch06_civil_time]

```{figure} _static/_chapter06/fig29_time_zones.png
:width: 100%
:align: center
:name: fig29_time_zones

**Figure 29** Historical world time-zone map. Irregular boundaries and fractional-hour offsets show that civil time is a geographical convention superposed on astronomical time.
```

Longitude, equation of time, and daylight saving are separate corrections. Combining the approximate relation between local mean time and UT1 with $E=T_\odot-T_{\mathrm{M}}$ gives

$$
T_\odot-T_{\mathrm{civil}}
\simeq E+\lambda_{\mathrm{h}}
-\text{adopted offset}+DUT1.
$$

All terms must be expressed in the same time units. For example, at $15^\circ$ east, CET approximately coincides with local mean solar time; apparent solar time still differs by $E$. Under CEST, the civil clock gains another hour without any corresponding change in the Sun's motion.

## The International Date Line

If successive zones increase their clock reading eastward, a full circuit accumulates 24 hours. One boundary must therefore separate two different calendar dates. The **International Date Line** lies mainly in the Pacific Ocean near longitude $180^\circ$, with deviations that keep territories and island groups on the same civil date ([Figure 30](fig30_time_date_line)).

```{figure} _static/_chapter06/fig30_international_date_line.png
:width: 43%
:align: center
:name: fig30_time_date_line

**Figure 30** The International Date Line and nearby time zones in a historical map. Its departures from the $180^\circ$ meridian preserve the civil unity of territories and island groups.
```

Crossing the line **westward**, a traveller advances the calendar date by one day; crossing **eastward**, the traveller moves the date back by one day. This is a change of date convention, not a discontinuity in elapsed physical time. The date line completes the bookkeeping required by a globe covered with local civil times.[^ch06_date_line]

## Daylight saving time

**Daylight saving time** advances the civil clock, usually by one hour, during part of the year. Its purpose is to shift scheduled activities toward the daylight available in the evening. It changes clock labels and human schedules; it does not lengthen the astronomical day or alter sunrise in local solar time.

[Figure 31](fig31_time_daylight_saving) distinguishes northern-summer use in blue, southern-summer use in orange, former use in light grey, and no use in dark grey. The map is a historical illustration rather than a current catalogue of national rules. Different jurisdictions can use different transition dates, and some do not change their clocks at all.[^ch06_daylight_saving]

```{figure} _static/_chapter06/fig31_daylight_saving_regions.png
:width: 95%
:align: center
:name: fig31_time_daylight_saving

**Figure 31** Historical distribution of daylight saving time. Blue and orange identify seasonal use in the Northern and Southern Hemispheres; the grey shades distinguish former use from no use.
```

An observing record should specify its time scale and offset. A clock time such as $02{:}30$ can occur twice when clocks are moved back, or fail to occur when they are moved forward. UTC timestamps avoid this local ambiguity, while precise elapsed-time calculations must still account for leap seconds.

## From Ephemeris Time to Terrestrial Time

Before atomic clocks supplied a practical uniform reference, astronomers introduced **Ephemeris Time**, ET, as the time argument of gravitational equations of motion. An **ephemeris** tabulates the positions of celestial bodies as functions of time. The astronomical observations used to determine ET also established its difference from rotation-based Universal Time. Its realization therefore depended on dynamical models and measured celestial positions.[^ch06_terrestrial]

ET was replaced as the argument of modern ephemerides from **1984** by dynamical time scales. The geocentric scale was called **Terrestrial Dynamical Time**, TDT; the name **Terrestrial Time**, TT, was adopted in **1991**. Its origin preserves continuity with the former ephemeris scale. In its realization based on TAI,

$$
\boxed{TT(TAI)=TAI+32.184\ \mathrm{s}}.
$$

The notation $TT(TAI)$ emphasizes that TAI is a physical realization of the ideal TT scale. For most applications at the precision of this course, we write simply $TT=TAI+32.184\ \mathrm{s}$. Combining this with the UTC offset gives

$$
\boxed{TT=UTC+\Delta AT+32.184\ \mathrm{s}}.
$$

For an epoch with $\Delta AT=37\ \mathrm{s}$, the corresponding offset is $TT-UTC=69.184\ \mathrm{s}$. The constant $32.184\ \mathrm{s}$ is a conventional origin offset; it is not a periodically changing relativistic correction.

Another quantity is

$$
\boxed{\Delta T=TT-UT1}.
$$

It relates dynamical ephemerides to terrestrial rotation and varies because Earth's rotation is irregular. It must be distinguished from both $\Delta AT$ and $DUT1$. They satisfy

$$
\Delta T\simeq32.184\ \mathrm{s}+\Delta AT-DUT1,
$$

at the accuracy of the TAI realization used here. Predicting a celestial position at a specified TT and predicting which terrestrial meridian faces it are thus related calculations with different time arguments.[^ch06_delta_t]

## Proper time and coordinate time

Relativity requires a distinction between a clock reading and the time coordinate used to describe a system. **Proper time**, $\tau_{\mathrm{proper}}$, is measured by a clock following a particular observer's worldline. **Coordinate time**, $t$, labels events in a specified spacetime coordinate system. Clocks at different places or moving at different velocities need not accumulate the same proper time between selected events.

In special relativity, a clock moving at speed $v$ in an inertial frame satisfies

$$
d\tau_{\mathrm{proper}}=dt\sqrt{1-\frac{v^2}{c^2}}.
$$

The moving clock accumulates less proper time than the inertial-frame coordinate interval. [Figure 32](fig32_time_special_relativity) illustrates the comparison. For $v\ll c$, the fractional difference begins at order $v^2/(2c^2)$.

```{figure} _static/_chapter06/fig32_special_relativity.png
:width: 44%
:align: center
:name: fig32_time_special_relativity

**Figure 32** Illustration of clocks carried by observers with different motions. Their accumulated proper times depend on their trajectories; a reunion permits a direct comparison.
```

General relativity adds the effect of gravitational potential. In a weak field, using the Newtonian potential $\Phi<0$ and an appropriate coordinate frame,

$$
\frac{d\tau_{\mathrm{proper}}}{dt}
\simeq1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}.
$$

A clock deeper in a gravitational potential runs more slowly relative to this coordinate time, other conditions being equal. [Figure 33](fig33_time_general_relativity) is a qualitative visualization of spacetime curvature, rather than a literal surface on which clocks sit.

```{figure} _static/_chapter06/fig33_general_relativity.png
:width: 58%
:align: center
:name: fig33_time_general_relativity

**Figure 33** Schematic visualization of spacetime curvature around Earth. Gravitational potential and motion both affect the comparison of physical clock rates.
```

Coordinate time provides a consistent variable for the equations in the chosen frame; it does not abolish relativistic effects. Those effects enter the relation between coordinates, clock readings, and observations. Two spatially separated events assigned the same coordinate time are simultaneous **in that coordinate convention**. Simultaneity is not independent of the chosen frame.[^ch06_relativistic]

## Terrestrial and barycentric dynamical time

The **Geocentric Celestial Reference System** provides a relativistic description centred on Earth. Its coordinate time is **TCG**, Geocentric Coordinate Time. TT is defined as a linearly scaled version of TCG:

$$
\frac{dTT}{dTCG}=1-L_G,
\qquad
L_G=6.969290134\times10^{-10}.
$$

The scaling makes the rate of TT close to the proper time of clocks on the terrestrial geoid. **TT is a coordinate time scale**, not the proper time of one clock at Earth's centre. A terrestrial clock at a different altitude or velocity requires corrections before its readings realize that common scale.[^ch06_terrestrial_scale]

Solar-system dynamics is naturally described in a **barycentric** reference system, centred on the solar-system centre of mass. Its coordinate time is **TCB**, Barycentric Coordinate Time. **Barycentric Dynamical Time**, TDB, is a linearly scaled form of TCB chosen so that it remains close to TT near Earth. The difference $TDB-TT$ is dominated by periodic terms associated with Earth's orbital motion and has an amplitude of about $1.7\ \mathrm{ms}$. It is therefore small, but relevant for observations requiring millisecond accuracy or better.[^ch06_coordinate_scales]

A useful approximate geocentric expression is

$$
TDB-TT\simeq0.001658\ \mathrm{s}\,
\sin\!\left(g+0.0167\sin g\right),
$$

where $g$ is the Earth's orbital mean anomaly. The trigonometric arguments are in radians. This expression illustrates the main periodic correction; detailed transformations use more complete models and the observer's location and motion.[^ch06_time_transformations]

[Figure 34](fig34_time_scale_relations) collects the connections between rotation, atomic, civil, and dynamical time. Some relations are constant offsets, some require measured Earth-orientation corrections, and others require relativistic transformations. The diagram uses the older label TDT for the scale now called TT.

```{figure} _static/_chapter06/fig34_time_scales.png
:width: 72%
:align: center
:name: fig34_time_scale_relations

**Figure 34** Relations among astronomical time scales in historical notation. TAI–UTC depends on leap seconds, TDT–TAI is the fixed 32.184-second offset, and TDB–TDT contains small periodic relativistic corrections. UT0, UT1, and the historical smoothed scale UT2 refer to Earth rotation.
```

An observing calculation consequently needs both the time scale and the frame. UTC can identify when data were recorded, UT1 specifies terrestrial rotation, TT provides the usual argument for geocentric ephemerides, and TDB or TCB supplies a barycentric dynamical argument. A barycentric light-travel-time correction is a separate operation from the transformation between TT and TDB.

## Tropical years, Besselian epochs, and Julian epochs

The tropical year describes the seasonal cycle, but stellar catalogues also need an agreed **epoch** to specify when positions or reference directions apply. Older catalogues often use **Besselian epochs**. The Besselian year begins when the mean solar longitude, with the historical aberration convention and referred to the mean equinox of date, reaches $280^\circ$. Its start lies close to the beginning of the civil year.[^ch06_epochs]

The notation **B1950.0** identifies the start of the Besselian year 1950, while **B1950.45678** specifies a fractional epoch. The conventional conversion is

$$
B=1900.0+\frac{JD-2\,415\,020.31352}{365.242198781}.
$$

The numerical denominator is the conventional Besselian-year interval used for this conversion. It should not be interpreted as an exact, immutable duration of the real seasonal cycle. The epoch B1950.0 corresponds to

$$
JD_{TT}\simeq2\,433\,282.42346,
$$

or approximately **1949 December 31, 22:09:47 TT**.

Modern catalogue work uses **Julian epochs**, based on an exact interval of $365.25\ \mathrm{d}$:

$$
\boxed{J=2000.0+\frac{JD_{TT}-2\,451\,545.0}{365.25}}.
$$

The fundamental epoch **J2000.0** is

$$
\boxed{JD_{TT}=2\,451\,545.0
\quad\longleftrightarrow\quad
\text{2000 January 1, 12:00 TT}}.
$$

It is noon in **TT**, not noon in UT1 or UTC. At that epoch it corresponds to 11:58:55.816 UTC. The identical numerical JD at noon UT1 labels a different instant. Similarly, J1950.0 is exactly $18\,262.5$ days before J2000.0 and corresponds to **1950 January 1, 00:00 TT**, about 1 h 50 min after B1950.0. The prefixes B and J therefore carry physical and conventional information; they cannot be dropped from a precise catalogue epoch.[^ch06_j2000]

[Figure 35](fig35_time_catalogue_epochs) uses **HD 219134** to illustrate coordinate labels referring to different systems and epochs. Its appreciable proper motion makes an epoch especially important. An equinox specifies the orientation of a classical coordinate system; a position epoch specifies the instant at which a moving star's position is stated. ICRS axes do not need an equinox, although ICRS catalogue positions still have an epoch.

```{figure} _static/_chapter06/fig35_catalogue_epochs.png
:width: 95%
:align: center
:name: fig35_time_catalogue_epochs

**Figure 35** Catalogue information for HD 219134, with coordinates in different reference systems, epoch labels, and proper-motion components. B1950 and J2000 must be interpreted with their respective conventions.
```

## The civil calendar and the Julian reform

The daily, monthly, and yearly cycles are not integer multiples of one another. A civil calendar must therefore choose how to approximate the seasonal year with a whole number of days. Adding occasional days or months is an **intercalation**. A calendar rule is an approximation to astronomical cycles, rather than a law governing those cycles.[^ch06_calendars]

In **46 BCE**, Julius Caesar reformed the Roman calendar after consulting astronomers and mathematicians, including **Sosigenes of Alexandria**. The transitional year was extended to **445 days** to restore the seasonal alignment, and the new calendar took effect on **1 January 45 BCE**. The **Julian calendar** uses ordinary years of 365 days and a leap day every fourth year, giving

$$
\langle Y_{\mathrm{Julian}}\rangle
=365+\frac{1}{4}
=365.25\ \mathrm{d}.
$$

The name *bissextile* recalls the Roman practice of repeating a day identified as the sixth day before the calends of March. In the modern numbering of dates, the added day is 29 February.

Extending a calendar's rules to dates before its adoption produces a **proleptic calendar**. Historical BCE/CE chronology has no year zero: 1 BCE is followed directly by 1 CE. **Astronomical year numbering** instead includes year 0, corresponding to 1 BCE; year $-1$ corresponds to 2 BCE. Under a proleptic every-four-years Julian rule, astronomical year 0 is a leap year. These numbering systems must be distinguished when evaluating intervals across the BCE/CE boundary.

## The Gregorian calendar

The Julian average year exceeds the near-present tropical year by approximately

$$
365.25-365.2422=0.0078\ \mathrm{d},
$$

about 11 minutes per year. This accumulates to roughly one day in **128 years**. Equinoxes consequently drift toward earlier Julian calendar dates.

In **1582**, Pope **Gregory XIII** introduced a reform that removed ten calendar dates to restore the spring equinox near its conventional March date. In the first adopting countries, **Thursday 4 October was followed by Friday 15 October** ([Figure 36](fig36_time_gregorian)). The sequence of weekdays remained continuous. Adoption occurred at different times in different countries, so a historical date must be interpreted in its local calendar context.[^ch06_gregorian_calendar]

```{figure} _static/_chapter06/fig36_gregorian_reform.png
:width: 65%
:align: center
:name: fig36_time_gregorian

**Figure 36** The October 1582 calendar transition in the first countries to adopt the Gregorian reform. The date advanced from 4 to 15 October while the weekday sequence continued.
```

The **Gregorian leap-year rule** retains years divisible by 4, except century years, which are leap years only when divisible by 400. Thus 1600 and 2000 are leap years, while 1700, 1800, 1900, and 2100 are not. There are 97 leap years in a 400-year cycle, so

$$
\boxed{\langle Y_{\mathrm{Gregorian}}\rangle
=365+\frac{97}{400}
=365.2425\ \mathrm{d}}.
$$

The cycle contains

$$
400\times365+97=146\,097\ \mathrm{d}
=20\,871\ \mathrm{weeks}.
$$

The same dates therefore return to the same weekdays every 400 years in the proleptic Gregorian calendar.

The calendar remains an approximation. Comparing $365.2425\ \mathrm{d}$ with the rounded tropical value $365.2422\ \mathrm{d}$ gives a discrepancy of order one day in **three millennia**. A precise long-term estimate depends on the epoch and the astronomical year being compared, because the seasonal cycle itself changes. No additional Gregorian leap-year exception beyond the 400-year rule is part of the standard calendar.

## The seasons

The **astronomical seasons** are defined by the apparent geocentric ecliptic longitude of the Sun. In the Northern Hemisphere they begin at

$$
\begin{array}{c|c|c}
\lambda_\odot & \text{Event} & \text{Northern season beginning}\\
\hline
0^\circ & \text{March equinox} & \text{Spring}\\
90^\circ & \text{June solstice} & \text{Summer}\\
180^\circ & \text{September equinox} & \text{Autumn}\\
270^\circ & \text{December solstice} & \text{Winter}
\end{array}
$$

The season names are reversed in the Southern Hemisphere. These events use the **apparent Sun**, not the fictitious uniformly moving mean Sun. Equal $90^\circ$ longitude intervals consequently take different amounts of time. Near a solstice, one hemisphere is tilted toward the Sun and receives longer days and a higher midday Sun ([Figure 37](fig37_time_solstice)). At an equinox, the Sun lies on the celestial equator and the ideal illumination boundary passes through the terrestrial poles ([Figure 38](fig38_time_equinox)).[^ch06_seasons]

```{figure} _static/_chapter06/fig37_solstice_geometry.png
:width: 75%
:align: center
:name: fig37_time_solstice

**Figure 37** Illumination near the June solstice. The Northern Hemisphere is tilted toward the Sun, with continuous daylight inside part of the Arctic region.
```

```{figure} _static/_chapter06/fig38_equinox_geometry.png
:width: 75%
:align: center
:name: fig38_time_equinox

**Figure 38** Ideal illumination at an equinox. The Sun lies on the equator and the day–night boundary passes through both poles. Refraction and the finite solar disk make observed daylight slightly longer than the geometric twelve hours.
```

The following rounded examples illustrate the relation between seasonal events and civil dates. A decimal day such as **20.3 March** means 0.3 day, or 7.2 hours, after the beginning of 20 March. The values are approximate calendar illustrations; precise event times require an ephemeris and a specified time scale.

| Northern season | Approximate start, 1950 | Illustrative duration (days) | Approximate start, 2000 | Approximate start, 2096 |
|---|---|---:|---|---|
| Spring | 21.2 March | 92.81 | 20.3 March | 19.5 March |
| Summer | 22.0 June | 93.62 | 21.0 June | 20.1 June |
| Autumn | 23.1 September | 89.82 | 22.7 September | 21.9 September |
| Winter | 22.4 December | 89.00 | 21.5 December | 20.9 December |

These durations sum to approximately one tropical year and show the unequal division of the annual cycle. In successive ordinary years, a seasonal event tends to occur about **5 h 49 min later** on the civil clock because the year exceeds 365 days. A leap day then shifts the calendar placement back by nearly a day. The four-year pattern is modified by century rules and slow astronomical changes, as the comparison of 1950, 2000, and 2096 indicates.

## Differences between the hemispheres

The axial tilt is the principal cause of the seasons, but orbital eccentricity changes both their durations and the incident solar flux. Earth reaches aphelion in early July, during northern summer, and perihelion in early January, during southern summer. It moves more slowly near aphelion, so **northern spring and summer together last about seven days longer** than southern spring and summer.

Solar irradiance at distance $r$ varies as $r^{-2}$. For orbital eccentricity $e$, with $r_{\mathrm{peri}}=a(1-e)$ and $r_{\mathrm{aph}}=a(1+e)$,

$$
\frac{F_{\mathrm{aph}}}{F_{\mathrm{peri}}}
=\left(\frac{1-e}{1+e}\right)^2
\simeq0.935
\qquad(e\simeq0.0167).
$$

The incident flux at aphelion is therefore about **6.5% lower**, often rounded to **7%**, than at perihelion. [Figure 39](fig39_time_hemisphere_flux) shows the different annual patterns of total solar power intercepted by the two hemispheres. These totals should not be confused with the irradiance received by a particular horizontal surface.[^ch06_hemisphere_seasons]

```{figure} _static/_chapter06/fig39_hemispheric_solar_flux.png
:width: 65%
:align: center
:name: fig39_time_hemisphere_flux

**Figure 39** Seasonal variation of solar power intercepted by the Northern and Southern Hemispheres. Axial tilt redistributes the incoming energy between them, while orbital eccentricity changes the total received by Earth.
```

The present alignment of perihelion with southern summer is temporary. Precession changes the orientation of the seasonal cycle relative to the orbit. Roughly half an axial precession cycle is about **13,000 years**, giving the scale on which the alignment can reverse. A precise calculation must also include the precession of the orbital apsides; the relative climatic-precession cycle is therefore not identical to the axial-precession period.

### Land, oceans, and the annual temperature cycle

The two hemispheres do not respond identically to the same seasonal forcing. The Northern Hemisphere contains much more land, while the Southern Hemisphere is dominated by oceans ([Figure 40](fig40_time_land_ocean)). For comparable absorbed energy, the temperature of the shallow layer participating in heating over land changes more rapidly than that of the ocean, whose large heat capacity, mixing, and evaporation spread the response over greater depths and longer times.

```{figure} _static/_chapter06/fig40_hemispheric_land_ocean.png
:width: 100%
:align: center
:name: fig40_time_land_ocean

**Figure 40** Distribution of land and oceans, with the equator and tropics marked. The Northern Hemisphere contains a much larger share of the terrestrial land area.
```

The global mean near-surface temperature is typically higher in July than in January by roughly **2–3°C**, despite Earth receiving less solar irradiance near July aphelion. The larger and faster seasonal response of northern land areas contributes strongly to this annual cycle. This difference is a climatic average, not a universal temperature offset between the hemispheres on a particular day. Ocean and atmospheric circulation, clouds, surface properties, and thermal storage also matter.[^ch06_hemisphere_temperature]

[Figure 41](fig41_time_temperature_cycle) illustrates the annual temperature pattern for several selected years. Its ordinate combines seasonal departures from an annual reference with differences among years. The seasonal cycle must be distinguished from the longer-term change of the annual mean. Winds and ocean currents transport energy between regions and hemispheres, while the planet's radiation balance and stored heat determine its evolving thermal state.

```{figure} _static/_chapter06/fig41_global_temperature_cycle.png
:width: 64%
:align: center
:name: fig41_time_temperature_cycle

**Figure 41** Illustration of the monthly global temperature cycle for selected historical years. The warmer mid-year months reflect the hemispheric asymmetry of land and ocean; vertical differences between yearly curves represent a separate change of the temperature baseline. Graphic credit: Statista; data source identified in the graphic as NASA.
```

## Twilight

The sky does not become dark as soon as the solar disk disappears. Sunlight still reaches the upper atmosphere and is scattered into lower layers and toward the observer. This interval is **twilight**. Its conventional boundaries use the **geometric altitude of the centre of the Sun**, without adding the horizon refraction correction to these thresholds.[^ch06_twilight]

| Twilight boundary | Geometric solar altitude | Solar zenith distance |
|---|---:|---:|
| Civil | $-6^\circ$ | $96^\circ$ |
| Nautical | $-12^\circ$ | $102^\circ$ |
| Astronomical | $-18^\circ$ | $108^\circ$ |

In the evening, **civil twilight ends** when the solar centre reaches $-6^\circ$, **nautical twilight ends** at $-12^\circ$, and **astronomical twilight ends** at $-18^\circ$. Morning twilight follows the reverse sequence: astronomical twilight begins at $-18^\circ$, nautical twilight at $-12^\circ$, and civil twilight at $-6^\circ$. [Figure 42](fig42_time_twilight_limits) summarizes the intervals.

```{figure} _static/_chapter06/fig42_twilight_definitions.png
:width: 75%
:align: center
:name: fig42_time_twilight_limits

**Figure 42** Evening twilight classified by the geometric depression of the solar centre. The boundaries at 6°, 12°, and 18° define civil, nautical, and astronomical twilight, respectively.
```

Civil twilight generally leaves enough natural illumination for many ordinary outdoor activities. Nautical twilight historically allows the horizon and selected stars to be seen together for navigation. Beyond the astronomical boundary, scattered sunlight is conventionally small enough for the sky to be treated as astronomically dark. Actual observing conditions also depend on the Moon, clouds, aerosols, artificial lighting, and the natural night-sky background.

```{figure} _static/_chapter06/fig43_observatory_twilight.png
:width: 75%
:align: center
:name: fig43_time_observatory_twilight

**Figure 43** An observatory during twilight. The solar disk is below the horizon, while scattered sunlight still illuminates the sky and limits faint-object observations.
```

Twilight duration depends on latitude and season. If the Sun descends steeply through the horizon, the three boundaries follow each other rapidly. At high latitude it can remain close to the horizon for hours, or never reach $-18^\circ$, so an entire night may lack astronomical darkness. The geometric distinction between evening **dusk** and morning **dawn** is illustrated in [Figure 44](fig44_time_dawn_dusk).

```{figure} _static/_chapter06/fig44_dawn_dusk.png
:width: 70%
:align: center
:name: fig44_time_dawn_dusk

**Figure 44** Dusk and dawn on either side of the nighttime interval. Twilight accompanies the Sun's passage below the horizon in the evening and its approach to the horizon in the morning.
```

The horizontal-coordinate relation connects these definitions to an observing calculation:

$$
\sin h_\odot
=\sin\phi\sin\delta_\odot
+\cos\phi\cos\delta_\odot\cos HA_\odot.
$$

At a chosen twilight boundary $h_\odot=-6^\circ$, $-12^\circ$, or $-18^\circ$,

$$
\cos HA_\odot
=\frac{\sin h_\odot-\sin\phi\sin\delta_\odot}
{\cos\phi\cos\delta_\odot}.
$$

The evening solution has positive hour angle and the morning solution negative hour angle. If the right-hand side lies outside $[-1,1]$, that altitude is not crossed for the assumed declination and site. Precise event times require the Sun's changing coordinates and the relevant conversion between rotation time and the adopted civil time scale.

## References

- **Barbieri, C., and Bertini, I. (2021)**, *Fundamentals of Astronomy*, second edition, Chapter 4, especially §§4.2–4.9, printed pp. 48–55 (PDF pp. 67–74), and Chapter 10, printed pp. 145–155 (PDF pp. 164–174).
- **Karttunen, H., Kröger, P., Oja, H., Poutanen, M., and Donner, K. J. (eds., 2017)**, *Fundamental Astronomy*, sixth edition, §§2.13–2.15, printed pp. 34–41 (PDF pp. 47–54).
- **Hanslmeier, A. (2023)**, *Introduction to Astronomy and Astrophysics*, §2.2, “The Time”, printed pp. 13–16 (PDF pp. 34–37).
- **BIPM**, [SI second](https://www.bipm.org/en/si-base-units/second), [international time-scale production](https://www.bipm.org/en/time-department/utc), and [Resolution 4 of the 27th CGPM (2022)](https://www.bipm.org/en/-/resolution-cgpm-27-4).
- **International Astronomical Union, Division A**, [Resolutions on reference systems and time scales](https://iau-a3.gitlab.io/res.html), especially the 2000 definition of TT and 2006 definition of TDB.
- **Kaplan, G. H. (2005)**, [*The IAU Resolutions on Astronomical Reference Systems, Time Scales, and Earth Rotation Models*](https://arxiv.org/abs/astro-ph/0602086), US Naval Observatory Circular 179, §2.2, for the relation between proper and coordinate time and the geocentric time scales.
- **US Naval Observatory**, [Julian Date converter](https://aa.usno.navy.mil/data/JulianDate), [Terrestrial Time](https://aa.usno.navy.mil/faq/TT), and [Rise, Set, and Twilight Definitions](https://aa.usno.navy.mil/faq/RST_defs).
- **Espenak, F., and Meeus, J.**, [Eclipses and the Moon's Orbit](https://eclipse.gsfc.nasa.gov/SEhelp/moonorbit.html), NASA Goddard Space Flight Center, for the lunar-orbit graphs and their astronomical context.
- **NASA**, [*Deep Space Chronicle*](https://www.nasa.gov/wp-content/uploads/2023/04/sp-4524.pdf), entry on Mars Climate Orbiter; [Martian Analemma](https://science.nasa.gov/image-article/apod-2006-december-30-martian-analemma/), Astronomy Picture of the Day, 30 December 2006.
- **INRiM**, [Time and frequency](https://www.inrim.it/en/research/scientific-sectors/time-and-frequency), for the Italian realization of atomic time and its contribution to the international system.
- **Sanz Subirana, J., Juan Zornoza, J. M., and Hernández-Pajares, M. (2011)**, [Transformations between Time Systems](https://gssc.esa.int/navipedia/index.php/Transformations_between_Time_Systems), ESA Navipedia.

[^ch06_second]: [BIPM, SI second](https://www.bipm.org/en/si-base-units/second). The definition uses the unperturbed atomic transition; comparison with a common terrestrial time scale additionally requires corrections for gravitational potential and motion.

[^ch06_mars_orbiter]: [NASA, *Deep Space Chronicle*](https://www.nasa.gov/wp-content/uploads/2023/04/sp-4524.pdf), Mars Climate Orbiter entry, for dates and estimated altitude; the [Mishap Investigation Board report](https://discovery.larc.nasa.gov/discovery/PDF_FILES/mars_climate_orbiter_phaseII.pdf) discusses the impulse-unit mismatch. The low-altitude passage was part of the failed arrival trajectory, not a successfully established final mapping orbit.

[^ch06_sidereal]: Barbieri and Bertini (2021), §§4.2 and 10.1, printed pp. 48 and 145 (PDF pp. 67 and 164); Karttunen et al. (2017), §2.13, printed pp. 34–35 (PDF pp. 47–48). Apparent right ascension and apparent sidereal time must use matching reference directions.

[^ch06_sidereal_coordinates]: Barbieri and Bertini (2021), §§4.2 and 10.1, printed pp. 48 and 145 (PDF pp. 67 and 164); Karttunen et al. (2017), §2.13, printed pp. 34–35 (PDF pp. 47–48). Apparent right ascension and apparent sidereal time must use matching reference directions.

[^ch06_equation_equinoxes]: Barbieri and Bertini (2021), §§4.2 and 10.1, printed pp. 48 and 145 (PDF pp. 67 and 164); Karttunen et al. (2017), §2.13, printed pp. 34–35 (PDF pp. 47–48). Apparent right ascension and apparent sidereal time must use matching reference directions.

[^ch06_day_periods]: Karttunen et al. (2017), §2.13, printed p. 35 (PDF p. 48); Barbieri and Bertini (2021), §10.1, printed p. 145 (PDF p. 164), for the precision distinction between stellar and sidereal days.

[^ch06_years]: Barbieri and Bertini (2021), §§4.5 and 10.3, printed pp. 52–53 and 147–149 (PDF pp. 71–72 and 166–168); Hanslmeier (2023), §2.2, printed p. 15 (PDF p. 36).

[^ch06_solar_time]: Barbieri and Bertini (2021), §4.3, printed pp. 48–52 (PDF pp. 67–71); Karttunen et al. (2017), §2.13, printed pp. 35–36 (PDF pp. 48–49). The equation-of-time sign adopted here is apparent minus mean.

[^ch06_equation_of_time]: Barbieri and Bertini (2021), §4.3, printed pp. 48–52 (PDF pp. 67–71); Karttunen et al. (2017), §2.13, printed pp. 35–36 (PDF pp. 48–49). The equation-of-time sign adopted here is apparent minus mean.

[^ch06_martian_analemma]: [NASA APOD, Martian Analemma, 30 December 2006](https://science.nasa.gov/image-article/apod-2006-december-30-martian-analemma/). The illustrated sequence uses intervals of 30 **Martian solar days**, rather than 30 Earth days.

[^ch06_lunar_periods]: The mean periods and the distinctions between stellar, phase, apsidal, and nodal reference directions are discussed by [Espenak and Meeus, Eclipses and the Moon's Orbit](https://eclipse.gsfc.nasa.gov/SEhelp/moonorbit.html). The relative-rate equations in the text are mean-motion approximations; the changing reference directions are also described in Barbieri and Bertini (2021), Chapter 5, printed pp. 59–64 (PDF pp. 78–83).

[^ch06_apsidal_period]: The mean periods and the distinctions between stellar, phase, apsidal, and nodal reference directions are discussed by [Espenak and Meeus, Eclipses and the Moon's Orbit](https://eclipse.gsfc.nasa.gov/SEhelp/moonorbit.html). The relative-rate equations in the text are mean-motion approximations; the changing reference directions are also described in Barbieri and Bertini (2021), Chapter 5, printed pp. 59–64 (PDF pp. 78–83).

[^ch06_draconic_period]: The mean periods and the distinctions between stellar, phase, apsidal, and nodal reference directions are discussed by [Espenak and Meeus, Eclipses and the Moon's Orbit](https://eclipse.gsfc.nasa.gov/SEhelp/moonorbit.html). The relative-rate equations in the text are mean-motion approximations; the changing reference directions are also described in Barbieri and Bertini (2021), Chapter 5, printed pp. 59–64 (PDF pp. 78–83).

[^ch06_lunar_variations]: Lunar plots credited to Fred Espenak and Jean Meeus, [NASA Eclipse Web Site](https://eclipse.gsfc.nasa.gov/SEhelp/moonorbit.html). Each graph's angular ordinate has its own definition: true anomaly, Sun–perigee longitude difference, or perigee–node longitude difference. Those quantities must not be interchanged.

[^ch06_universal]: Barbieri and Bertini (2021), §§4.4, 10.2, and 10.6, printed pp. 52, 146–147, and 153–155 (PDF pp. 71, 165–166, and 172–174); Karttunen et al. (2017), §2.14, printed pp. 38–40 (PDF pp. 51–53).

[^ch06_julian_date]: [US Naval Observatory, Julian Date converter](https://aa.usno.navy.mil/data/JulianDate); Barbieri and Bertini (2021), §4.9, printed p. 55 (PDF p. 74). The modified count subtracts **2,400,000.5**, and any JD used in a precision calculation must identify its time scale.

[^ch06_rotation]: Barbieri and Bertini (2021), §§10.1 and 10.4, printed pp. 145–146 and 149–152 (PDF pp. 164–165 and 168–171). The secular day-length trend and shorter-term fluctuations should not be interpreted as one constant slowing rate.

[^ch06_atomic_time]: [BIPM, international time-scale production](https://www.bipm.org/en/time-department/utc); Barbieri and Bertini (2021), §10.5, printed pp. 152–153 (PDF pp. 171–172), for the historical development. Current clock numbers and transfer methods evolve; the international scale is an ensemble result.

[^ch06_atomic_history]: [BIPM, international time-scale production](https://www.bipm.org/en/time-department/utc); Barbieri and Bertini (2021), §10.5, printed pp. 152–153 (PDF pp. 171–172), for the historical development. Current clock numbers and transfer methods evolve; the international scale is an ensemble result.

[^ch06_inrim]: [INRiM, Time and frequency](https://www.inrim.it/en/research/scientific-sectors/time-and-frequency). INRiM maintains UTC(IT), contributes clock and frequency-standard data to TAI, and supports Galileo timing activities.

[^ch06_utc]: Karttunen et al. (2017), §2.14, printed pp. 39–40 (PDF pp. 52–53); [BIPM, Resolution 4 of the 27th CGPM](https://www.bipm.org/en/-/resolution-cgpm-27-4), for the established $0.9$-second limit. Leap-second announcements and Earth-orientation data are published in the [IERS Bulletins](https://data.iers.org/bulletins.php).

[^ch06_utc_future]: [BIPM, Resolution 4 of the 27th CGPM (2022)](https://www.bipm.org/en/-/resolution-cgpm-27-4). It decides to increase the permitted UT1–UTC difference in or before 2035; it does not make the old bound an eternal property of UTC.

[^ch06_civil_time]: Karttunen et al. (2017), §2.13, printed pp. 36–38 (PDF pp. 49–51); Hanslmeier (2023), §2.2, printed pp. 14–16 (PDF pp. 35–37). The maps illustrate the geographical conventions and should not be used as current legal time-zone or daylight-saving tables.

[^ch06_date_line]: Karttunen et al. (2017), §2.13, printed pp. 36–38 (PDF pp. 49–51); Hanslmeier (2023), §2.2, printed pp. 14–16 (PDF pp. 35–37). The maps illustrate the geographical conventions and should not be used as current legal time-zone or daylight-saving tables.

[^ch06_daylight_saving]: Karttunen et al. (2017), §2.13, printed pp. 36–38 (PDF pp. 49–51); Hanslmeier (2023), §2.2, printed pp. 14–16 (PDF pp. 35–37). The maps illustrate the geographical conventions and should not be used as current legal time-zone or daylight-saving tables.

[^ch06_terrestrial]: [US Naval Observatory, Terrestrial Time](https://aa.usno.navy.mil/faq/TT); Karttunen et al. (2017), §2.14, printed p. 39 (PDF p. 52). The constant offset applies to the TAI realization of TT. More accurate retrospective realizations, such as TT(BIPM), can differ slightly from TT(TAI).

[^ch06_delta_t]: [US Naval Observatory, Terrestrial Time](https://aa.usno.navy.mil/faq/TT); Karttunen et al. (2017), §2.14, printed p. 39 (PDF p. 52). The constant offset applies to the TAI realization of TT. More accurate retrospective realizations, such as TT(BIPM), can differ slightly from TT(TAI).

[^ch06_relativistic]: Barbieri and Bertini (2021), Chapter 10, printed pp. 145 and 152 (PDF pp. 164 and 171), for the need to distinguish proper and coordinate time. The weak-field expression uses a negative Newtonian gravitational potential and retains only first-order potential and second-order velocity terms.

[^ch06_terrestrial_scale]: [Kaplan (2005), USNO Circular 179](https://arxiv.org/abs/astro-ph/0602086), §2.2, printed pp. 8–9 (PDF pp. 22–23), for TT as scaled geocentric coordinate time and its approximate correspondence to proper time on the geoid.

[^ch06_coordinate_scales]: [IAU Division A, resolutions on reference systems and time scales](https://iau-a3.gitlab.io/res.html), Resolution B3 (2006). TDB is scaled TCB and remains within approximately 2 ms of TT near Earth over several millennia around the present epoch.

[^ch06_time_transformations]: [ESA Navipedia, Transformations between Time Systems](https://gssc.esa.int/navipedia/index.php/Transformations_between_Time_Systems), equation (19). The displayed expression gives the principal periodic term, not the complete transformation for an arbitrary observer.

[^ch06_epochs]: Barbieri and Bertini (2021), §§4.7 and 10.3.2, printed pp. 53–54 and 148 (PDF pp. 72–73 and 167), for the historical Besselian convention. The explicit TT labels distinguish the time scale from the numerical epoch representation.

[^ch06_j2000]: [US Naval Observatory, Terrestrial Time](https://aa.usno.navy.mil/faq/TT), for J2000.0 and its equivalent UTC timestamp. A calendar date at noon UT1 and J2000.0 can share the numerical value 2451545.0 on their respective scales while referring to different instants.

[^ch06_calendars]: Barbieri and Bertini (2021), §4.6, printed p. 53 (PDF p. 72); Karttunen et al. (2017), §2.15, printed pp. 40–41 (PDF pp. 53–54); Hanslmeier (2023), §2.2, printed pp. 15–16 (PDF pp. 36–37). The drift estimates are calculated here from the quoted mean year lengths; they depend on which astronomical year and epoch are used.

[^ch06_gregorian_calendar]: Barbieri and Bertini (2021), §4.6, printed p. 53 (PDF p. 72); Karttunen et al. (2017), §2.15, printed pp. 40–41 (PDF pp. 53–54); Hanslmeier (2023), §2.2, printed pp. 15–16 (PDF pp. 36–37). The drift estimates are calculated here from the quoted mean year lengths; they depend on which astronomical year and epoch are used.

[^ch06_seasons]: Barbieri and Bertini (2021), §4.8 and Table 4.1, printed pp. 54–55 (PDF pp. 73–74), for the illustrative dates, season lengths, and hemisphere comparison. The table is retained as a rounded orbital illustration rather than a precision ephemeris. Actual equinoxes and solstices use the apparent Sun's longitude.

[^ch06_hemisphere_seasons]: Barbieri and Bertini (2021), §4.8 and Table 4.1, printed pp. 54–55 (PDF pp. 73–74), for the illustrative dates, season lengths, and hemisphere comparison. The table is retained as a rounded orbital illustration rather than a precision ephemeris. Actual equinoxes and solstices use the apparent Sun's longitude.

[^ch06_hemisphere_temperature]: Barbieri and Bertini (2021), §4.8, printed pp. 54–55 (PDF pp. 73–74), gives an approximate July–January global mean temperature contrast of $2.3^\circ\mathrm{C}$. Its magnitude depends on the dataset and averaging interval; the land–ocean contrast explains the dominant hemispheric asymmetry without constituting a complete climate model.

[^ch06_twilight]: [US Naval Observatory, Rise, Set, and Twilight Definitions](https://aa.usno.navy.mil/faq/RST_defs). The boundaries use the geometric solar centre at zenith distances $96^\circ$, $102^\circ$, and $108^\circ$; the evening and morning crossings define the end and beginning, respectively, of the named twilight stages.
