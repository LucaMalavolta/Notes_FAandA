(chapter02_transformation_of_coordinates)=

# Transformation of Coordinates

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

:::{danger}
This page still need sustantial revision to match the content presented during the lectures
:::

## From a direction to its coordinates

In the previous chapter, we introduced several ways of describing the position of an object on the celestial sphere. The same star can be identified by its equatorial coordinates, its ecliptic coordinates, or its altitude and azimuth. The direction of the star does not depend on our choice of coordinate system, but the numbers used to describe that direction do.

A **coordinate transformation** connects these different descriptions. For example, a stellar catalogue gives us the right ascension and declination of a target, while pointing a telescope with an altitude-azimuth mount requires its position relative to the local horizon. To connect the two, we need the orientation of the observer's vertical and meridian at the time of the observation.

We will first express transformations as rotations of Cartesian axes. We will then apply them to astronomical coordinates and use the results to describe the apparent motion of stars and of the Sun. Unless otherwise stated, we neglect atmospheric refraction, parallax, proper motion, precession, and nutation during the interval considered. These assumptions allow us to isolate the geometry; they do not imply that these effects are absent in precise observations.[^ch02_rotation]

The notation follows the previous chapter:

| Symbol | Meaning | Convention |
|---|---|---|
| $\alpha$, $\delta$ | Right ascension and declination | Right ascension increases eastward; declination is positive northward |
| $\lambda$, $\beta$ | Ecliptic longitude and latitude | Longitude increases eastward from the vernal point |
| $a$, $A$ | Altitude and azimuth | Altitude is positive above the horizon; azimuth increases **from South toward West** |
| $\phi$ | Observer's astronomical latitude | Positive in the Northern hemisphere |
| $t$ | Hour angle | Positive westward from the local upper meridian |
| $\Theta$ | Local sidereal time | Hour angle of the vernal point |
| $\varepsilon$ | Obliquity of the ecliptic | Approximately $23.44°$ for our examples |

With our azimuth convention, South is $A=0°$, West is $90°$, North is $180°$, and East is $270°$. A North-through-East azimuth, denoted here by $A_{\mathrm N}$, is related to ours by

$$
A=(A_{\mathrm N}-180°)\pmod{360°}.
$$

Both conventions occur in astronomical books and software. A formula written for one convention must be converted before it is used with the other. We also retain $a$ for altitude and $t$ for hour angle, since the symbol $h$ is used for either quantity in different sources. When differentiating with respect to elapsed time, we will use a separate symbol, $\tau$.

## Transformations through rotation matrices

### Cartesian coordinates and direction cosines

Consider two orthonormal, right-handed Cartesian systems with the same origin $O$. Let their unit vectors be $(\boldsymbol e_x,\boldsymbol e_y,\boldsymbol e_z)$ and $(\boldsymbol e_X,\boldsymbol e_Y,\boldsymbol e_Z)$. The position vector of a point $P$ can be written in either basis:

$$
\boldsymbol r=x\boldsymbol e_x+y\boldsymbol e_y+z\boldsymbol e_z
=X\boldsymbol e_X+Y\boldsymbol e_Y+Z\boldsymbol e_Z.
$$

Taking the scalar product with each new unit vector gives its corresponding coordinate. For example,

$$
X=x(\boldsymbol e_X\cdot\boldsymbol e_x)
+y(\boldsymbol e_X\cdot\boldsymbol e_y)
+z(\boldsymbol e_X\cdot\boldsymbol e_z).
$$

Since the basis vectors have unit length, their scalar products are the cosines of the angles between the axes. These quantities are called **direction cosines**. The three coordinate equations can be combined into a single matrix equation:

$$
\begin{pmatrix}X\\Y\\Z\end{pmatrix}
=R\begin{pmatrix}x\\y\\z\end{pmatrix},
\qquad
R_{ij}=\boldsymbol e'_i\cdot\boldsymbol e_j.
$$

Each row of $R$ contains the components of one new basis vector in the old system. Because both bases are orthonormal and have the same handedness,

$$
R^{\mathsf T}R=I,\qquad \det R=+1,
\qquad R^{-1}=R^{\mathsf T}.
$$

The superscript $\mathsf T$ denotes the **transpose**, obtained by interchanging rows and columns. Thus, reversing a rotation does not require a general matrix inversion: we can simply transpose its matrix.

A rotation preserves the distance from the origin,

$$
x^2+y^2+z^2=X^2+Y^2+Z^2=r^2,
$$

and the scalar product between any two vectors. Consequently, it preserves the angular separation between two stars. The coordinates change; the geometry does not.

```{figure} _static/_chapter02/fig01_rotated_axes.png
:width: 100%
:align: center
:name: ch02_fig01_rotated_axes

**Figure 1** Left: a point remains fixed while the reference axes rotate. Right: a direction described by a longitude $L$ and a latitude $B$ can be represented by three Cartesian components. Latitude is measured from the reference plane.
```

### Spherical coordinates and the unit sphere

Let $L$ and $B$ be a generic longitude and latitude, respectively. As in the previous chapter, latitude is measured from the reference plane, not from the polar axis. Then

$$
\begin{aligned}
x&=r\cos B\cos L,\\
y&=r\cos B\sin L,\\
z&=r\sin B.
\end{aligned}
$$

Substituting these expressions into the rotation equation shows that $r$ cancels from both sides. A transformation of directions can therefore be performed on the **unit sphere**:

$$
\begin{pmatrix}
\cos B'\cos L'\\
\cos B'\sin L'\\
\sin B'
\end{pmatrix}
=
R\begin{pmatrix}
\cos B\cos L\\
\cos B\sin L\\
\sin B
\end{pmatrix}.
$$

Once the rotated components $(X,Y,Z)$ have been calculated, we recover the angles through

$$
L'=\operatorname{atan2}(Y,X)\pmod{2\pi},
\qquad
B'=\operatorname{atan2}\!\left(Z,\sqrt{X^2+Y^2}\right).
$$

The two-argument function $\operatorname{atan2}(Y,X)$ uses the signs of both components to identify the correct quadrant. A simple $\arctan(Y/X)$ loses this information: a vector with $X>0$, $Y>0$ and one with $X<0$, $Y<0$ would give the same ratio. An inverse sine alone has a similar ambiguity for longitude. At a pole, $X=Y=0$, and longitude is undefined.

The cancellation of $r$ depends on the two systems having the **same origin**. If the new origin is displaced by a vector $\boldsymbol d$, expressed in the original basis, the transformation instead becomes

$$
\boldsymbol r'=R(\boldsymbol r-\boldsymbol d).
$$

The distance is then needed. A geocentric-to-topocentric transformation for the Moon, for example, cannot be represented by a rotation of a unit vector alone.

### Elementary rotations and their sequence

We will use a **passive rotation** convention: the axes rotate through a positive angle according to the right-hand rule, while the physical vector remains fixed. For rotations about the $x$, $y$, and $z$ axes, respectively, the coordinate matrices are

$$
R_x(\chi)=
\begin{pmatrix}
1&0&0\\
0&\cos\chi&\sin\chi\\
0&-\sin\chi&\cos\chi
\end{pmatrix},
$$

$$
R_y(\chi)=
\begin{pmatrix}
\cos\chi&0&-\sin\chi\\
0&1&0\\
\sin\chi&0&\cos\chi
\end{pmatrix},
\qquad
R_z(\chi)=
\begin{pmatrix}
\cos\chi&\sin\chi&0\\
-\sin\chi&\cos\chi&0\\
0&0&1
\end{pmatrix}.
$$

For example, rotating the $x$ and $y$ axes about $z$ gives

$$
X=x\cos\chi+y\sin\chi,
\qquad
Y=-x\sin\chi+y\cos\chi,
\qquad Z=z.
$$

These signs can be checked in [Figure 1](ch02_fig01_rotated_axes): a point on the original positive $x$ axis has a negative $Y$ component after the axes rotate counterclockwise through a small positive angle. Rotating the *vector* through $+\chi$ while holding the axes fixed would require the opposite signs, or equivalently $R_z(-\chi)$.

A general relative orientation can be described by three successive elementary rotations. If the coordinate vectors satisfy $\boldsymbol r_1=R_1\boldsymbol r_0$, $\boldsymbol r_2=R_2\boldsymbol r_1$, and $\boldsymbol r_3=R_3\boldsymbol r_2$, then

$$
\boldsymbol r_3=R_3R_2R_1\boldsymbol r_0.
$$

The matrix on the right acts first. The axes and angle convention of each step must be specified, especially when a rotation is taken about an axis of an intermediate frame. In general,

$$
R_2R_1\ne R_1R_2.
$$

For instance, applying $R_x(90°)$ and then $R_y(90°)$ to $(0,0,1)^{\mathsf T}$ gives $(0,1,0)^{\mathsf T}$; reversing the order gives $(-1,0,0)^{\mathsf T}$. To undo a sequence, we reverse both its order and the sign of each elementary rotation:

$$
(R_3R_2R_1)^{-1}=R_1^{\mathsf T}R_2^{\mathsf T}R_3^{\mathsf T}.
$$

## Equatorial and ecliptic coordinates

Equatorial and ecliptic coordinates share the direction of the **vernal point** $\gamma$. Choose this direction as the $x$ axis in both systems. The two reference planes are inclined by the obliquity $\varepsilon$, so a single rotation about $x$ is sufficient, provided that the origins and reference dates are compatible.[^ch02_ecliptic]

```{figure} _static/_chapter02/fig02_equatorial_ecliptic.png
:width: 75%
:align: center
:name: ch02_fig02_equatorial_ecliptic

**Figure 2** Equatorial and ecliptic axes viewed from the positive common $x$ axis toward the origin. The North Celestial Pole (NCP) and North Ecliptic Pole (NEP) are separated by $\varepsilon$, as are the corresponding reference planes.
```

From equatorial to ecliptic coordinates, we have

$$
\begin{pmatrix}
\cos\beta\cos\lambda\\
\cos\beta\sin\lambda\\
\sin\beta
\end{pmatrix}
=R_x(\varepsilon)
\begin{pmatrix}
\cos\delta\cos\alpha\\
\cos\delta\sin\alpha\\
\sin\delta
\end{pmatrix}.
$$

Writing the three components explicitly,

$$
\begin{aligned}
\cos\beta\cos\lambda&=\cos\delta\cos\alpha,\\
\cos\beta\sin\lambda&=\cos\delta\sin\alpha\cos\varepsilon
+\sin\delta\sin\varepsilon,\\
\sin\beta&=-\cos\delta\sin\alpha\sin\varepsilon
+\sin\delta\cos\varepsilon.
\end{aligned}
$$

The inverse transformation follows by replacing $\varepsilon$ with $-\varepsilon$:

$$
\begin{aligned}
\cos\delta\cos\alpha&=\cos\beta\cos\lambda,\\
\cos\delta\sin\alpha&=\cos\beta\sin\lambda\cos\varepsilon
-\sin\beta\sin\varepsilon,\\
\sin\delta&=\cos\beta\sin\lambda\sin\varepsilon
+\sin\beta\cos\varepsilon.
\end{aligned}
$$

There are three component equations for two angular coordinates because the three components obey a unit-length constraint. The two components in the reference plane are useful together: they determine the quadrant of longitude or right ascension.

As a check, consider a direction on the ecliptic with $\lambda=90°$ and $\beta=0°$. Its equatorial components are $(0,\cos\varepsilon,\sin\varepsilon)$, giving $\alpha=6^{\mathrm h}$ and $\delta=+\varepsilon$. For $\lambda=270°$, the result is $\alpha=18^{\mathrm h}$ and $\delta=-\varepsilon$. These are the ideal solar directions at the June and December solstices.

## Horizontal and equatorial coordinates

### The role of the observer's latitude

The equatorial plane and the local horizontal plane intersect along the **East–West direction**. Their relative inclination is determined by the observer's latitude $\phi$. In the Northern hemisphere, the North Celestial Pole has altitude $\phi$, and its angular distance from the zenith is $90°-\phi$ ([Figure 3](ch02_fig03_horizontal_equatorial)). In the Southern hemisphere, the South Celestial Pole is above the horizon at altitude $|\phi|$.[^ch02_horizontal]

```{figure} _static/_chapter02/fig03_horizontal_equatorial.png
:width: 80%
:align: center
:name: ch02_fig03_horizontal_equatorial

**Figure 3** A meridian section of the celestial sphere for a northern observer. The East–West line is perpendicular to the page. The altitude of the North Celestial Pole equals the observer's astronomical latitude $\phi$.
```

For the rotation, choose a right-handed horizontal basis pointing toward **South, East, and Zenith**. With azimuth measured from South toward West, the unit vector of the target in this basis is

$$
\boldsymbol u_{\mathrm{hor}}=
\begin{pmatrix}
\cos a\cos A\\
-\cos a\sin A\\
\sin a
\end{pmatrix}.
$$

The negative sign in the East component is necessary because azimuth increases toward West. Choose the corresponding equatorial basis with its first axis at the intersection of the celestial equator and the local upper meridian, its second axis toward East, and its third axis toward the North Celestial Pole. The same direction has components

$$
\boldsymbol u_{\mathrm{eq,local}}=
\begin{pmatrix}
\cos\delta\cos t\\
-\cos\delta\sin t\\
\sin\delta
\end{pmatrix}.
$$

The East axis is shared, and the transformation is

$$
\boldsymbol u_{\mathrm{eq,local}}=
\begin{pmatrix}
\sin\phi&0&\cos\phi\\
0&1&0\\
-\cos\phi&0&\sin\phi
\end{pmatrix}
\boldsymbol u_{\mathrm{hor}}.
$$

This is $R_y(\phi-90°)$ with our passive convention. Notice that using an East component has allowed both Cartesian bases to remain right-handed even though azimuth and hour angle increase westward.

### From altitude and azimuth to hour angle and declination

Expanding the matrix equation gives

$$
\begin{aligned}
\cos\delta\sin t&=\cos a\sin A,\\
\cos\delta\cos t&=\sin\phi\cos a\cos A+\cos\phi\sin a,\\
\sin\delta&=-\cos\phi\cos a\cos A+\sin\phi\sin a.
\end{aligned}
$$

The last equation determines the declination. The first two determine the hour angle through $\operatorname{atan2}$. To obtain right ascension, one additional quantity is required: the local sidereal time,

$$
\alpha=\Theta-t\pmod{24^{\mathrm h}}.
$$

An altitude and azimuth measured at an unknown time do not, by themselves, identify a fixed position in a stellar catalogue.

### From hour angle and declination to altitude and azimuth

Transposing the matrix gives the inverse transformation:

$$
\begin{aligned}
\cos a\sin A&=\cos\delta\sin t,\\
\cos a\cos A&=\sin\phi\cos\delta\cos t-\cos\phi\sin\delta,\\
\sin a&=\cos\phi\cos\delta\cos t+\sin\phi\sin\delta.
\end{aligned}
$$

Thus,

$$
a=\arcsin(\sin\phi\sin\delta+\cos\phi\cos\delta\cos t),
$$

$$
A=\operatorname{atan2}\!\left(
\cos\delta\sin t,
\sin\phi\cos\delta\cos t-\cos\phi\sin\delta
\right)\pmod{2\pi}.
$$

At the zenith or nadir, both arguments of the azimuth expression vanish. The altitude is still meaningful, but the azimuth is undefined.

The altitude relation also follows from spherical trigonometry. The **astronomical triangle** connects the North Celestial Pole $P$, the zenith $Z$, and the object $X$. Its sides have angular lengths $PZ=90°-\phi$, $PX=90°-\delta$, and $ZX=90°-a$. Applying the spherical cosine rule, with the angle at $P$ represented by the hour angle through its cosine, gives

$$
\cos(90°-a)=\cos(90°-\phi)\cos(90°-\delta)
+\sin(90°-\phi)\sin(90°-\delta)\cos t.
$$

The matrix and spherical-triangle methods therefore express the same geometry.

For example, take the latitude of Padova, $\phi=45.40643°$, and a star at $\alpha=8^{\mathrm h}$, $\delta=20°$. At $\Theta=10^{\mathrm h}$,

$$
t=2^{\mathrm h}=30°,
\qquad a\simeq54.58°,
\qquad A\simeq54.16°.
$$

The star lies west of the meridian, between South and West. Its positive hour angle tells us that upper culmination has already occurred. In all numerical work, the angles must be converted to radians before evaluating trigonometric functions.

### A modern approach to transformations

The `astropy.coordinates` package introduced in the presentation represents positions together with their units and reference frames. Its `SkyCoord` interface provides transformations between frames; a transformation to `AltAz` additionally needs the observation time and observing site. Astropy uses **North-through-East azimuth**, so its result must be shifted by $180°$ to follow our convention.[^ch02_astropy]

For example, once `target`, `observation_time`, and `site` have been defined with the appropriate frame, time scale, and units, the final operation is

```python
from astropy import units as u
from astropy.coordinates import AltAz

horizontal = target.transform_to(
    AltAz(obstime=observation_time, location=site, pressure=0 * u.hPa)
)
altitude = horizontal.alt
azimuth_from_south = (horizontal.az.to_value(u.deg) - 180.0) % 360.0
```

Here zero pressure disables atmospheric refraction. A complete catalogue-to-observed transformation includes more than the elementary rotations developed above, so it need not reproduce a calculation that neglects changes of frame and apparent direction. Reliable software still requires correctly specified input coordinates.

## Sidereal time

### Right ascension, hour angle, and the local meridian

Right ascension is measured eastward from the vernal point; hour angle is measured westward from the local upper meridian. The **local sidereal time** $\Theta$ connects these two angular origins:

$$
\Theta=\alpha+t\pmod{24^{\mathrm h}},
\qquad t=\Theta-\alpha.
$$

Geometrically, $\Theta$ is the hour angle of the vernal point. Equivalently, it is the right ascension of the equatorial direction currently on the upper meridian. At a star's upper transit, $t=0$, and therefore $\Theta=\alpha$.[^ch02_time]

```{figure} _static/_chapter02/fig04_sidereal_time.png
:width: 100%
:align: center
:name: ch02_fig04_sidereal_time

**Figure 4** Successive orientations of the local upper meridian, viewed from the North Celestial Pole. The illustrative star has $\alpha=18^{\mathrm h}38^{\mathrm m}10^{\mathrm s}$. Its right ascension is fixed while its hour angle increases. The three sidereal times follow the sequence used in the presentation.
```

For the star in [Figure 4](ch02_fig04_sidereal_time), the hour angles are

| Local sidereal time | Hour angle | Position relative to upper transit |
|---|---|---|
| $18^{\mathrm h}00^{\mathrm m}00^{\mathrm s}$ | $-0^{\mathrm h}38^{\mathrm m}10^{\mathrm s}$ | Before transit |
| $18^{\mathrm h}38^{\mathrm m}10^{\mathrm s}$ | $0^{\mathrm h}$ | At transit |
| $20^{\mathrm h}40^{\mathrm m}00^{\mathrm s}$ | $+2^{\mathrm h}01^{\mathrm m}50^{\mathrm s}$ | After transit |

The signed interval $-12^{\mathrm h}<t\leq12^{\mathrm h}$ is convenient for distinguishing the eastern and western sides of the meridian. A negative hour angle can also be expressed as a positive value modulo $24^{\mathrm h}$, but the signed form makes the geometry more immediate.

For terrestrial longitude $\lambda_{\mathrm{geo}}$, positive eastward,

$$
\Theta_{\mathrm{local}}=\Theta_{\mathrm{Greenwich}}
+\lambda_{\mathrm{geo}}\pmod{24^{\mathrm h}}.
$$

Longitude must be converted to hours if the sidereal times are expressed in hours. Padova's longitude, $11.87676°$ East, corresponds to approximately $0^{\mathrm h}47^{\mathrm m}30.42^{\mathrm s}$. At a given instant, its local sidereal time is ahead of Greenwich sidereal time by this amount.

The classical definition also requires a consistent equinox: **mean sidereal time** refers to the mean equinox, while **apparent sidereal time** refers to the true equinox, including nutation. For our elementary calculations we neglect this distinction. Precise work must use a right ascension and sidereal time referred to compatible origins; an ICRS catalogue right ascension cannot simply be treated as an apparent right ascension of date.

### Solar and sidereal days

A **sidereal day** is the interval between two successive upper passages of the vernal point across a local meridian. Neglecting the motion of the equinox and changes in a star's position, it is also approximately the interval between consecutive upper transits of that star.

A **solar day**, or synodic rotation period in this context, refers instead to consecutive upper transits of the Sun. During one rotation, the Earth advances along its orbit. The Sun therefore shifts eastward relative to the stars, and the Earth must rotate a little further before the Sun returns to the meridian.

```{figure} _static/_chapter02/fig05_solar_sidereal_day.png
:width: 100%
:align: center
:name: ch02_fig05_solar_sidereal_day

**Figure 5** The stellar reference direction is approximately fixed, whereas the direction toward the Sun changes as the Earth moves along its orbit. The difference is exaggerated to make the additional rotation visible. The panels follow the Earth and show directions, rather than an orbit drawn to scale.
```

For a uniformly rotating planet on a prograde circular orbit, let $\omega_{\mathrm{rot}}$ be its sidereal rotation rate and $n$ its orbital angular rate. The rotation relative to the Sun has angular rate $\omega_{\mathrm{rot}}-n$. Hence,

$$
\frac{1}{T_{\mathrm{solar}}}
=\frac{1}{T_{\mathrm{rot}}}-\frac{1}{P_{\mathrm{orb}}}.
$$

For the Earth, the orbital displacement is approximately $1°$ per day, requiring about four additional minutes of rotation. In the mean-time comparison,

$$
\begin{aligned}
24^{\mathrm h}\text{ of sidereal time}
&\simeq23^{\mathrm h}56^{\mathrm m}4.09^{\mathrm s}
\text{ of mean solar time},\\
24^{\mathrm h}\text{ of mean solar time}
&\simeq24^{\mathrm h}3^{\mathrm m}56.56^{\mathrm s}
\text{ of sidereal time}.
\end{aligned}
$$

The distinction between a rotation relative to fixed stars and a day referred to the moving equinox is very small at this level. The quoted sidereal-time conversion refers to the equinox-based convention.

A star consequently transits about $3^{\mathrm m}56^{\mathrm s}$ earlier on successive mean solar days, or approximately $27.5$ minutes earlier after one week. This explains the displacement illustrated by the Sun and Betelgeuse in the presentation. It also explains why different constellations are visible at a fixed evening hour in different seasons.

The **apparent solar day** is not strictly constant: the Earth's orbital speed varies, and the Sun moves along the inclined ecliptic rather than uniformly along the equator. **Mean solar time** uses a fictitious Sun moving uniformly along the equator. The difference between apparent and mean solar time is the **equation of time**. Neither local solar time nor local sidereal time is, in general, the civil time displayed by a clock.

## The movement of stars in the sky

### Diurnal circles and culmination

If $\alpha$ and $\delta$ are constant, the Earth's rotation changes only the hour angle in the local equatorial description. A star therefore follows a circle of constant declination, parallel to the celestial equator. On the unit sphere this is a small circle, except when $\delta=0°$, where it is the celestial equator itself.

Its altitude varies according to

$$
\sin a=\sin\phi\sin\delta+\cos\phi\cos\delta\cos t.
$$

For a non-polar observer and a star away from the celestial poles, the maximum altitude occurs at $t=0$, called **upper culmination**, and the minimum at $t=12^{\mathrm h}$, called **lower culmination**. The expressions valid in both hemispheres are

$$
a_{\mathrm{max}}=90°-|\phi-\delta|,
\qquad
a_{\mathrm{min}}=|\phi+\delta|-90°.
$$

The absolute values select the altitude in its allowed range, $-90°\leq a\leq90°$. Upper culmination is not necessarily on the southern side of the zenith. For a northern observer, a star with $\delta>\phi$ culminates to the North; one with $\delta<\phi$ culminates to the South. When $\delta=\phi$, it passes through the zenith.

```{figure} _static/_chapter02/fig06_diurnal_paths.png
:width: 100%
:align: center
:name: ch02_fig06_diurnal_paths

**Figure 6** Diurnal paths for four declinations at Padova. Left: altitude over one sidereal day, including the part below the horizon. Right: the visible portions projected on the local sky; the centre is the zenith and the outer circle is the horizon. The star at $\delta=60°$ is circumpolar, while the one at $\delta=-60°$ never rises.
```

### Rising and setting

An object crosses the geometric horizon when $a=0$. For $|\phi|<90°$ and $|\delta|<90°$,

$$
\cos t_0=-\tan\phi\tan\delta.
$$

If $-1<-\tan\phi\tan\delta<1$, there are two crossings during a sidereal day. Defining $0<t_0<180°$ through the inverse cosine, their hour angles are

$$
t_{\mathrm{rise}}=-t_0,
\qquad t_{\mathrm{set}}=+t_0.
$$

The corresponding local sidereal times are

$$
\Theta_{\mathrm{rise}}=\alpha-t_0,
\qquad
\Theta_{\mathrm{set}}=\alpha+t_0
\pmod{24^{\mathrm h}},
$$

with all quantities in the same angular units. The duration above the horizon is $2t_0$ in sidereal angular units, or $2t_0/15°$ sidereal hours when $t_0$ is in degrees. A conversion to a civil time additionally requires a date, longitude, and an appropriate time transformation.[^ch02_visibility]

At the horizon, the inverse coordinate transformation gives

$$
\cos A_0=-\frac{\sin\delta}{\cos\phi}.
$$

If $A_0=\arccos(-\sin\delta/\cos\phi)$ is taken between $0°$ and $180°$, then

$$
A_{\mathrm{rise}}=360°-A_0,
\qquad A_{\mathrm{set}}=A_0.
$$

The setting direction has $\sin A>0$, as required by a positive hour angle. For $\delta=0°$, the star rises at $A=270°$ (East) and sets at $A=90°$ (West). For positive declination, the crossings lie north of East and West; for negative declination, they lie south of them.

For our Padova example with $\alpha=8^{\mathrm h}$ and $\delta=20°$,

$$
\begin{aligned}
t_0&\simeq7.4443^{\mathrm h},\\
\Theta_{\mathrm{rise}}&\simeq0^{\mathrm h}33^{\mathrm m}21^{\mathrm s},\\
\Theta_{\mathrm{set}}&\simeq15^{\mathrm h}26^{\mathrm m}39^{\mathrm s},\\
A_{\mathrm{rise}}&\simeq240.85°,
\qquad A_{\mathrm{set}}\simeq119.15°.
\end{aligned}
$$

The star is geometrically above the horizon for approximately $14.89$ sidereal hours. Being above the horizon does not guarantee detectability: daylight, extinction, clouds, and the local landscape also matter.

### Circumpolar stars and stars that never rise

The culmination altitudes provide a direct visibility test. If $a_{\mathrm{min}}>0$, the star is **circumpolar above the horizon**; if $a_{\mathrm{max}}<0$, it never rises. In the remaining non-boundary cases it rises and sets.

For a northern observer, $0°<\phi<90°$,

| Declination | Geometric behaviour |
|---|---|
| $\delta>90°-\phi$ | Circumpolar above the horizon |
| $-(90°-\phi)<\delta<90°-\phi$ | Rises and sets |
| $\delta<-(90°-\phi)$ | Never rises |

For a southern observer, $-90°<\phi<0°$,

| Declination | Geometric behaviour |
|---|---|
| $\delta<-(90°+\phi)$ | Circumpolar above the horizon |
| $-(90°+\phi)<\delta<90°+\phi$ | Rises and sets |
| $\delta>90°+\phi$ | Never rises |

Equality at a boundary describes tangency to the horizon, not two distinct crossings. An equivalent statement for nonzero latitude is that a circumpolar star has the same sign of declination as the observer's latitude and $|\delta|>90°-|\phi|$. A never-rising star satisfies this absolute-value inequality with the opposite sign of declination.

```{figure} _static/_chapter02/fig07_visibility.png
:width: 85%
:align: center
:name: ch02_fig07_visibility

**Figure 7** Visibility as a function of observer latitude and stellar declination. The boundaries correspond to tangency at the geometric horizon. The dashed line marks Padova, where the limiting declinations are approximately $\pm44.59°$.
```

At the terrestrial equator, every non-polar star spends half a sidereal day above the horizon; the celestial poles lie on the horizon. At a terrestrial pole, each star has constant altitude: $a=\delta$ at the North Pole and $a=-\delta$ at the South Pole. The tangent formula should not be used there because its denominator vanishes.

For an observing limit $a_{\mathrm{lim}}$ above the geometric horizon, the corresponding crossing equation is

$$
\cos t_{\mathrm{lim}}
=\frac{\sin a_{\mathrm{lim}}-\sin\phi\sin\delta}
{\cos\phi\cos\delta}.
$$

This is useful when a telescope cannot observe at low altitude, or when the target must remain above a specified airmass limit. The same existence checks apply before taking the inverse cosine.

## The motion of the Sun in the sky

The Sun participates in the apparent daily rotation of the sky, but its equatorial coordinates also change during the year. In the approximation $\beta_{\odot}=0$, the ecliptic-to-equatorial transformation becomes

$$
\begin{aligned}
\cos\delta_{\odot}\cos\alpha_{\odot}&=\cos\lambda_{\odot},\\
\cos\delta_{\odot}\sin\alpha_{\odot}&=\cos\varepsilon\sin\lambda_{\odot},\\
\sin\delta_{\odot}&=\sin\varepsilon\sin\lambda_{\odot}.
\end{aligned}
$$

In particular,

$$
\alpha_{\odot}=\operatorname{atan2}
(\cos\varepsilon\sin\lambda_{\odot},\cos\lambda_{\odot}),
\qquad
\delta_{\odot}=\arcsin(\sin\varepsilon\sin\lambda_{\odot}).
$$

These equations explain why the solar declination varies between approximately $-\varepsilon$ and $+\varepsilon$. They also give $\tan\delta_{\odot}=\tan\varepsilon\sin\alpha_{\odot}$, but that relation alone does not determine the quadrant of right ascension.[^ch02_sun]

Substituting the solar declination into the horizon-crossing equation explains both the annual change in the sunrise and sunset directions and the changing duration of daylight. For Padova, treating the solar coordinates as constant during one day gives

| Solar direction | $\delta_{\odot}$ | Noon altitude | Sunrise azimuth | Sunset azimuth | Approximate daylight |
|---|---|---|---|---|---|
| March and September equinoxes | $0°$ | $44.59°$ | $270.00°$ | $90.00°$ | $12.00$ h |
| June solstice | $+23.44°$ | $68.03°$ | $235.49°$ | $124.51°$ | $15.48$ h |
| December solstice | $-23.44°$ | $21.15°$ | $304.51°$ | $55.49°$ | $8.52$ h |

Daylight here is estimated with a solar hour-angle rate of $15°$ per mean solar hour, rather than the sidereal rate appropriate to a fixed star. The table refers to the centre of the Sun crossing an unobstructed geometric horizon and neglects refraction.

```{figure} _static/_chapter02/fig08_solar_paths.png
:width: 100%
:align: center
:name: ch02_fig08_solar_paths

**Figure 8** Left: solar paths at Padova for the equinoxes and solstices, with azimuth measured from South toward West. Right: approximate geometric daylight as a function of solar ecliptic longitude. Longitude is not exactly proportional to elapsed time because the Earth's orbital speed varies.
```

Almanac sunrise and sunset usually refer to the **upper limb** of the solar disc. A commonly adopted approximation places the geometric centre at $a\simeq-50'$, combining approximately $16'$ of solar radius and $34'$ of atmospheric refraction at the horizon. This makes the conventional daylight interval longer than the geometric estimate. A precise prediction also accounts for the variation of the solar coordinates and the observing conditions.

At sufficiently high latitudes, the solar declination can satisfy the same circumpolar or never-rising conditions as a star. In the ideal geometry, the limiting latitude is $90°-\varepsilon\simeq66.56°$: poleward of this, there are seasons with midnight Sun and seasons with polar night. The seasons are reversed between the hemispheres.

## Angular velocities on the sky

### Sidereal angle as the independent variable

For a distant star with fixed equatorial coordinates,

$$
t=\Theta-\alpha,
\qquad \frac{\mathrm dt}{\mathrm d\Theta}=1,
\qquad \frac{\mathrm d\delta}{\mathrm d\Theta}=0.
$$

Here $t$ and $\Theta$ are angles in the same units. Their derivative is dimensionless; it is not a velocity in degrees per second. To obtain a rate with respect to elapsed time $\tau$, define

$$
\omega_{\mathrm{sid}}=\frac{\mathrm d\Theta}{\mathrm d\tau}
\simeq\frac{2\pi}{86164.09\ \mathrm s}.
$$

This is approximately $15.0411°$ per mean solar hour, or exactly $15°$ per sidereal hour in our angular convention. The use of distinct symbols prevents confusion between the hour angle $t$ and a time interval.[^ch02_rates]

### Velocity in altitude

Differentiate the altitude equation with respect to $\Theta$, using radians for the differentiation:

$$
\cos a\frac{\mathrm da}{\mathrm d\Theta}
=-\cos\phi\cos\delta\sin t.
$$

Since $\cos a\sin A=\cos\delta\sin t$,

$$
\frac{\mathrm da}{\mathrm d\Theta}=-\cos\phi\sin A,
\qquad
\frac{\mathrm da}{\mathrm d\tau}
=-\omega_{\mathrm{sid}}\cos\phi\sin A.
$$

The sign has a direct interpretation. In the eastern half of the sky, $180°<A<360°$, so $\sin A<0$ and the altitude increases. In the western half, $0°<A<180°$, the altitude decreases. At an ordinary culmination, $\sin A=0$, and the instantaneous altitude rate vanishes.

For a given observing latitude,

$$
\left|\frac{\mathrm da}{\mathrm d\Theta}\right|\leq\cos\phi\leq1.
$$

The altitude rate is zero at the terrestrial poles. The largest possible magnitude occurs for an equatorial observer and is $15°$ per sidereal hour. At Padova the bound is about $10.53°$ per sidereal hour. These statements assume a differentiable altitude coordinate; an exact passage through the zenith requires taking the one-sided limits.

### Velocity in azimuth

For a direction away from the zenith and nadir, set

$$
x=\cos a\cos A,
\qquad y=\cos a\sin A.
$$

Differentiating $A=\operatorname{atan2}(y,x)$ gives

$$
\frac{\mathrm dA}{\mathrm d\Theta}
=\frac{x\,\mathrm dy/\mathrm d\Theta-y\,\mathrm dx/\mathrm d\Theta}
{x^2+y^2}.
$$

Substitution of the horizontal components yields

$$
\frac{\mathrm dA}{\mathrm d\Theta}
=\frac{\cos\delta\left(\sin\phi\cos\delta
-\cos\phi\sin\delta\cos t\right)}{\cos^2 a}
=\sin\phi+\cos\phi\cos A\tan a.
$$

The corresponding rate with respect to elapsed time is

$$
\frac{\mathrm dA}{\mathrm d\tau}
=\omega_{\mathrm{sid}}
\left(\sin\phi+\cos\phi\cos A\tan a\right).
$$

At the geometric horizon, $a=0$, and therefore

$$
\left.\frac{\mathrm dA}{\mathrm d\Theta}\right|_{a=0}=\sin\phi.
$$

The azimuth rate at either crossing is positive in the Northern hemisphere, negative in the Southern hemisphere, and zero for an equatorial observer. Away from the horizon it depends on the position of the target, and it may change sign.

```{figure} _static/_chapter02/fig09_tracking_rates.png
:width: 100%
:align: center
:name: ch02_fig09_tracking_rates

**Figure 9** Altitude and coordinate rates near upper transit at Padova. The stars at $\delta=44°$ and $46°$ pass close to opposite sides of the zenith, producing large azimuth rates with opposite signs. The star at $\delta=20°$ remains farther from the zenith and requires a more moderate azimuth rate. Rates are expressed per sidereal hour.
```

### What happens close to the zenith?

At upper culmination, provided $\delta\ne\phi$,

$$
\left.\frac{\mathrm dA}{\mathrm d\Theta}\right|_{t=0}
=\frac{\cos\delta}{\sin(\phi-\delta)}.
$$

For a non-polar observer, its magnitude becomes arbitrarily large as the transit declination approaches the observer's latitude. This explains the large tracking rates in [Figure 9](ch02_fig09_tracking_rates).

An **exact zenith transit**, $\delta=\phi$, must be treated separately. At $t=0$, azimuth is undefined, and its limiting directions on the two sides of transit differ by $180°$. It is therefore inaccurate to assign an ordinary infinite derivative to the azimuth at that point. The small-angle altitude behaves as

$$
a\simeq\frac{\pi}{2}-\cos\phi\,|t|,
$$

with $a$ and $t$ in radians. The cusp reflects the coordinate description, while the stellar direction moves smoothly across the sky. An altitude-azimuth telescope operating with altitude at or below $90°$ must change its azimuth very rapidly near such a passage; finite drive speeds can create an inaccessible region around the zenith.

The distinction between **coordinate rate** and actual angular motion is seen from the metric of the unit sphere:

$$
\left(\frac{\mathrm ds}{\mathrm d\tau}\right)^2
=\left(\frac{\mathrm da}{\mathrm d\tau}\right)^2
+\cos^2a\left(\frac{\mathrm dA}{\mathrm d\tau}\right)^2
=\omega_{\mathrm{sid}}^2\cos^2\delta.
$$

The physical angular speed remains finite. Close to the zenith, a large change in azimuth can correspond to a small displacement because a parallel of constant altitude has a small radius, $\cos a$.

A related but distinct quantity is the **rotation of the field** relative to the horizontal frame. Define the parallactic angle $q$ as the oriented angle at the star from the direction toward the celestial pole to the direction toward the zenith, with the convention

$$
q=\operatorname{atan2}\!\left(
\sin t,\ \tan\phi\cos\delta-\sin\delta\cos t
\right).
$$

Away from the coordinate singularities, differentiation gives

$$
\frac{\mathrm dq}{\mathrm d\Theta}
=\frac{\cos\phi\cos A}{\cos a}.
$$

This expression describes **parallactic-angle rotation**, not $\mathrm dA/\mathrm d\Theta$. The final slide places it under the discussion of azimuthal velocity, so the two quantities need to be distinguished explicitly. The sign of an instrument's compensating rotation also depends on how its detector angle is defined. The distinction matters for telescope mounts: following the target with two axes does not by itself keep the orientation of the image fixed.[^ch02_field]

## References and figure sources

The topic sequence follows *Lesson 02 - Transformation of Coordinates*, slides 1–22. The explanations and derivations have been developed using the three supplied textbooks. Page ranges below distinguish **printed pages** from **PDF viewer pages**, counted from 1.

- **Barbieri, C., and Bertini, I. (2021)**, *Fundamentals of Astronomy*, second edition, CRC Press. Section 3.1, pp. 35–39 (PDF pp. 54–58), for matrix rotations, horizon transformations, and angular rates; Section 3.3, pp. 41–44 (PDF pp. 60–63), for field rotation and solar applications; Sections 4.2–4.4, pp. 48–53 (PDF pp. 67–72), for sidereal and solar time.
- **Karttunen, H., Kröger, P., Oja, H., Poutanen, M., and Donner, K. J. (eds., 2017)**, *Fundamental Astronomy*, sixth edition, Springer. Sections 2.5–2.7, pp. 17–22 (PDF pp. 30–35), for transformations, culmination, rising and setting; Section 2.13, pp. 34–37 (PDF pp. 47–50), for sidereal and solar time.
- **Hanslmeier, A. (2023)**, *Introduction to Astronomy and Astrophysics*, Springer, English translation of the fourth German edition. Section 2.1.6, pp. 10–12 (PDF pp. 31–33), for spherical coordinate transformations; Section 2.2.1, pp. 12–15 (PDF pp. 33–36), for time definitions and the solar–sidereal comparison.

All nine PNG figures are original diagrams or numerical plots created for this chapter. They follow the geometric constructions and teaching examples of the presentation, with a consistent South-through-West azimuth convention. The figure topics correspond to the slides as follows:

| Figure | Presentation reference | Content |
|---|---|---|
| 1 | Slides 2–5 | Rotated Cartesian axes and spherical components |
| 2 | Slide 6 | Equatorial–ecliptic rotation |
| 3 | Slide 7 | Horizon, celestial equator, and observer latitude |
| 4 | Slides 9–12 | Sidereal time and a moving local meridian |
| 5 | Slides 13–15 | Difference between solar and sidereal days |
| 6 | Slides 16–19 | Diurnal circles and altitude variation |
| 7 | Slides 18–19 | Visibility limits in both hemispheres |
| 8 | Slide 20 | Solar paths and seasonal daylight |
| 9 | Slides 21–22 | Altitude and azimuth rates near transit |

The plotting source is retained alongside the PNG files as `generate_figures.py`. The examples use an ideal geometric sky, the Padova latitude quoted in Chapter 1, and $\varepsilon=23.44°$; they are not date-specific observing predictions.

[^ch02_rotation]: Barbieri and Bertini (2021), Section 3.1, pp. 35–36 (PDF pp. 54–55). The passive convention and order of successive coordinate mappings are stated explicitly here.

[^ch02_ecliptic]: Barbieri and Bertini (2021), Section 3.1, p. 37 (PDF p. 56), and Karttunen et al. (2017), Section 2.7, pp. 21–22 (PDF pp. 34–35).

[^ch02_horizontal]: Barbieri and Bertini (2021), Section 3.1, pp. 37–38 (PDF pp. 56–57); Karttunen et al. (2017), Section 2.5, pp. 19–20 (PDF pp. 32–33); Hanslmeier (2023), Section 2.1.6, pp. 10–12 (PDF pp. 31–33). We use astronomical latitude; in the examples it is approximated by the geodetic latitude, neglecting the deflection of the vertical.

[^ch02_astropy]: Official Astropy documentation, [Astronomical Coordinate Systems](https://docs.astropy.org/en/stable/coordinates/index.html) and [AltAz reference](https://docs.astropy.org/en/stable/api/astropy.coordinates.AltAz.html), consulted for the software approach introduced on slide 8.

[^ch02_time]: Barbieri and Bertini (2021), Sections 4.2–4.4, pp. 48–53 (PDF pp. 67–72); Karttunen et al. (2017), Section 2.13, pp. 34–37 (PDF pp. 47–50); Hanslmeier (2023), Section 2.2.1, pp. 12–15 (PDF pp. 33–36).

[^ch02_visibility]: Karttunen et al. (2017), Sections 2.5–2.6, pp. 19–21 (PDF pp. 32–34). The hemisphere-independent culmination formulae are obtained from the altitude equation with its principal angular range. They also avoid the erroneous general circumpolar condition $|\delta|>|\phi|$ printed in Barbieri and Bertini (2021), p. 38: the relevant threshold is $90°-|\phi|$, together with the sign of declination.

[^ch02_sun]: Barbieri and Bertini (2021), Section 3.3, pp. 42–44 (PDF pp. 61–63), and Karttunen et al. (2017), Sections 2.6–2.7, pp. 20–22 (PDF pp. 33–35). Solar rise and set conventions must be distinguished from geometric centre crossings.

[^ch02_rates]: Barbieri and Bertini (2021), Section 3.1, p. 39 (PDF p. 58). The coordinate rates are rederived here, keeping sidereal angle and elapsed time distinct and separating near-zenith passages from an exact zenith transit.

[^ch02_field]: Barbieri and Bertini (2021), Section 3.3, p. 42 (PDF p. 61), equation (3.19). This is the source of the parallactic-angle rate that must be distinguished from the azimuth rate on slide 22.
