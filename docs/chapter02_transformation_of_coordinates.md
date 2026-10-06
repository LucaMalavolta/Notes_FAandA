(chapter02_transformation_of_coordinates)=

# Transformation of Coordinates

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

The coordinate systems introduced in the previous chapter describe the same physical direction using different reference planes, poles, and zero points. A star does not move merely because we replace right ascension and declination with ecliptic longitude and latitude; only its numerical description changes. The purpose of a **coordinate transformation** is to perform this change without altering the geometric direction represented by the coordinates.

In this chapter, **all transformations between systems with the same origin are treated as rotations**. We first develop the Cartesian description of a rotation, then apply it to spherical coordinates. The same formalism leads naturally to the transformations between equatorial, ecliptic, and horizontal coordinates. The final sections use these relations to discuss sidereal time, rising and setting, the annual motion of the Sun, and the apparent angular velocity of a celestial target.

Unless explicitly stated otherwise, angles appearing in trigonometric functions are understood to be in radians. Numerical angles may also be quoted in degrees or hours for convenience.

## Transformations through rotation matrices

Consider two right-handed orthogonal Cartesian frames, $xyz$ and $XYZ$, with the same origin $O$. Let the position vector of a point $P$ have components

$$
\boldsymbol{e}=
\begin{pmatrix}
e_x\\ e_y\\ e_z
\end{pmatrix}
$$

in the first frame and

$$
\boldsymbol{f}=
\begin{pmatrix}
f_X\\ f_Y\\ f_Z
\end{pmatrix}
$$

in the second one. The vector itself is unchanged. Only the axes onto which it is projected have been rotated ([Figure 1](fig01_rotation_frames)).

```{figure} _static/_chapter02/fig01_rotation_frames.png
:width: 70%
:align: center
:name: fig01_rotation_frames

**Figure 1** The same point $P$ described in two Cartesian frames that share the origin. The lowercase and uppercase axes are related by a rigid rotation. 
```

Let $\theta_{xX}$ be the angle between the positive $x$ and $X$ axes, and define the other angles between pairs of old and new axes in the same way. The new components are the projections of the vector onto the new axes:

$$
\begin{aligned}
f_X &= e_x\cos\theta_{xX}+e_y\cos\theta_{yX}+e_z\cos\theta_{zX},\\
f_Y &= e_x\cos\theta_{xY}+e_y\cos\theta_{yY}+e_z\cos\theta_{zY},\\
f_Z &= e_x\cos\theta_{xZ}+e_y\cos\theta_{yZ}+e_z\cos\theta_{zZ}.
\end{aligned}
$$

These three equations can be written as

$$
\boldsymbol{f}=\mathbf{R}\boldsymbol{e},
$$

where

$$
\mathbf{R}=
\begin{pmatrix}
\cos\theta_{xX} & \cos\theta_{yX} & \cos\theta_{zX}\\
\cos\theta_{xY} & \cos\theta_{yY} & \cos\theta_{zY}\\
\cos\theta_{xZ} & \cos\theta_{yZ} & \cos\theta_{zZ}
\end{pmatrix}.
$$

The elements of $\mathbf{R}$ are called **direction cosines**. Each row contains the components of one new unit axis expressed in the old frame. Because both frames are orthonormal, the rows and columns of $\mathbf{R}$ are mutually orthogonal unit vectors. Therefore,

$$
\mathbf{R}^{\mathsf T}\mathbf{R}
=\mathbf{R}\mathbf{R}^{\mathsf T}
=\mathbf{I},
\qquad
\det\mathbf{R}=+1.
$$

The inverse transformation is consequently particularly simple:

$$
\boldsymbol{e}=\mathbf{R}^{-1}\boldsymbol{f}
=\mathbf{R}^{\mathsf T}\boldsymbol{f}.
$$

Thus, for a proper rotation,

$$
\boxed{\mathbf{R}^{-1}=\mathbf{R}^{\mathsf T}}.
$$

Changing the sign of the rotation angle produces the inverse rotation, $\mathbf{R}^{-1}(\vartheta)=\mathbf{R}(-\vartheta)$. These equations describe a **passive rotation**: the physical vector is fixed while the coordinate axes are rotated. An active rotation of the vector through the same geometric angle uses the inverse matrix. This distinction is the source of many apparently contradictory sign conventions.[^rotation_reference]

## Polar coordinates

Astronomical positions are most naturally expressed using spherical, or polar, coordinates. In the first frame, let the point $P$ be represented by the distance $r$, the longitude-like angle $\lambda$, and the latitude-like angle $\beta$ ([Figure 2](fig02_polar_coordinates)). Here $\beta$ is measured from the $xy$ plane, not from the positive $z$ axis.

```{figure} _static/_chapter02/fig02_polar_coordinates.png
:width: 55%
:align: center
:name: fig02_polar_coordinates

**Figure 2** Definition of the polar coordinates $(r,\lambda,\beta)$ used in this chapter. The latitude-like angle $\beta$ is measured from the reference plane. 
```

The corresponding Cartesian components are

$$
\begin{aligned}
e_x&=r\cos\beta\cos\lambda,\\
e_y&=r\cos\beta\sin\lambda,\\
e_z&=r\sin\beta.
\end{aligned}
$$

After rotating the axes, let the polar coordinates of the same point be $(r,\Lambda,B)$. A rotation preserves lengths, so the radial coordinate is unchanged:

$$
\begin{aligned}
f_X&=r\cos B\cos\Lambda,\\
f_Y&=r\cos B\sin\Lambda,\\
f_Z&=r\sin B.
\end{aligned}
$$

Substitution into $\boldsymbol{f}=\mathbf{R}\boldsymbol{e}$ gives

$$
\begin{pmatrix}
\cos B\cos\Lambda\\
\cos B\sin\Lambda\\
\sin B
\end{pmatrix}
=
\mathbf{R}
\begin{pmatrix}
\cos\beta\cos\lambda\\
\cos\beta\sin\lambda\\
\sin\beta
\end{pmatrix}.
$$

The factor $r$ cancels. A transformation between angular coordinates therefore depends only on the direction of the point and is equally valid on the unit celestial sphere. To recover the longitude without a quadrant ambiguity, both its sine and cosine components must be used. Numerically, this means using $\operatorname{atan2}(y,x)$ rather than an inverse sine or inverse cosine alone.

## Sequences of rotations

Any proper rotation in three-dimensional space can be represented by three successive elementary rotations. The precise angles are called **Euler angles**, although several competing Euler-angle conventions exist. The order of the rotations and the axes about which they are performed must therefore always be stated.

We use the passive convention of the presentation. A rotation of the coordinate axes through $\phi_1$ about the first axis leaves the $x$ component unchanged ([Figure 3](fig03_rotation_x)):

```{figure} _static/_chapter02/fig03_rotation_x.png
:width: 42%
:align: center
:name: fig03_rotation_x

**Figure 3** A passive rotation about the common $x=X$ axis.
```

The relevant direction angles are

$$
\begin{aligned}
&\theta_{xX}=0,\qquad \theta_{yX}=\frac{\pi}{2},\qquad \theta_{zX}=\frac{\pi}{2},\\
&\theta_{xY}=\frac{\pi}{2},\qquad \theta_{yY}=\phi_1,
\qquad \theta_{zY}=\frac{3\pi}{2}+\phi_1,\\
&\theta_{xZ}=\frac{\pi}{2},\qquad \theta_{yZ}=\frac{\pi}{2}+\phi_1,
\qquad \theta_{zZ}=\phi_1.
\end{aligned}
$$

Using $\cos(3\pi/2+\phi_1)=\sin\phi_1$ and $\cos(\pi/2+\phi_1)=-\sin\phi_1$, we obtain

$$
\mathbf{R}_1(\phi_1)=
\begin{pmatrix}
1&0&0\\
0&\cos\phi_1&\sin\phi_1\\
0&-\sin\phi_1&\cos\phi_1
\end{pmatrix}.
$$

The corresponding passive rotations about the second and third axes are

$$
\mathbf{R}_2(\phi_2)=
\begin{pmatrix}
\cos\phi_2&0&-\sin\phi_2\\
0&1&0\\
\sin\phi_2&0&\cos\phi_2
\end{pmatrix},
$$

and

$$
\mathbf{R}_3(\phi_3)=
\begin{pmatrix}
\cos\phi_3&\sin\phi_3&0\\
-\sin\phi_3&\cos\phi_3&0\\
0&0&1
\end{pmatrix}.
$$

If the three matrices act successively on a column vector in the order $\mathbf{R}_1$, $\mathbf{R}_2$, and $\mathbf{R}_3$, the total transformation is

$$
\boldsymbol{f}
=\mathbf{R}_3(\phi_3)\mathbf{R}_2(\phi_2)\mathbf{R}_1(\phi_1)\boldsymbol{e}.
$$

The matrix on the right acts first. Rotations do not generally commute, so interchanging two factors changes the final orientation. [Figure 4](fig04_successive_rotations) illustrates a sequence of rotations about coordinate axes.

```{figure} _static/_chapter02/fig04_successive_rotations.png
:width: 75%
:align: center
:name: fig04_successive_rotations

**Figure 4** An example of three successive rotations. The order is an essential part of the definition. 
```

## From equatorial to ecliptic coordinates

The **equatorial system** $(\alpha,\delta)$ and the **ecliptic system** $(\lambda,\beta)$ share the same origin and the same positive $x$ axis, directed toward the vernal point $\gamma$. Their reference planes are inclined by the obliquity of the ecliptic,

$$
\varepsilon\simeq23^\circ26'=23.43^\circ\simeq0.409\ \mathrm{rad}.
$$

Only one rotation, about the common $x$ axis, is required ([Figure 5](fig05_equatorial_ecliptic)).

```{figure} _static/_chapter02/fig05_equatorial_ecliptic.png
:width: 65%
:align: center
:name: fig05_equatorial_ecliptic

**Figure 5** The celestial equator and ecliptic share the vernal direction but have different poles. Their relative orientation is a rotation through the obliquity $\varepsilon$. 
```

With the passive convention introduced above, the transformation from equatorial to ecliptic Cartesian components is

$$
\mathbf{R}(\varepsilon)=
\begin{pmatrix}
1&0&0\\
0&\cos\varepsilon&\sin\varepsilon\\
0&-\sin\varepsilon&\cos\varepsilon
\end{pmatrix}
\simeq
\begin{pmatrix}
1&0&0\\
0&0.9174&0.3907\\
0&-0.3907&0.9174
\end{pmatrix}.
$$

Therefore, from equatorial to ecliptic coordinates,

$$
\begin{aligned}
\cos\beta\cos\lambda&=\cos\delta\cos\alpha,\\
\cos\beta\sin\lambda&=\cos\delta\sin\alpha\cos\varepsilon
                         +\sin\delta\sin\varepsilon,\\
\sin\beta&=-\cos\delta\sin\alpha\sin\varepsilon
             +\sin\delta\cos\varepsilon.
\end{aligned}
$$

The inverse transformation is obtained by transposing the matrix, or equivalently by replacing $\varepsilon$ with $-\varepsilon$:

$$
\begin{aligned}
\cos\delta\cos\alpha&=\cos\beta\cos\lambda,\\
\cos\delta\sin\alpha&=\cos\beta\sin\lambda\cos\varepsilon
                         -\sin\beta\sin\varepsilon,\\
\sin\delta&=\cos\beta\sin\lambda\sin\varepsilon
              +\sin\beta\cos\varepsilon.
\end{aligned}
$$

Although only two angular coordinates are unknown, three component equations are retained. Together they determine the signs and therefore the correct quadrants of both angles. These transformations assume that the equatorial and ecliptic coordinates refer to compatible origins, epochs, and reference planes.[^ecliptic_transform_reference]

## From horizontal to equatorial coordinates

Before checking the transformation between the **horizontal** and **equatorial** systems, we must remeber that the horizontal system is a *topocentric* system, i.e., it is centered on the observer (usually but not necessarily on the surface of the planet) while the equatorial system is *geocentric*, i.e., centered on the barycenter of our planet. To simplyfy the equations, we translate the observer to the center of Earth, noting that celetials objects are usually so far that  a shift of thousands of kilometers should not matter. This may not be true for objects in a Low Earth Orbit.

The **horizontal** and **equatorial** reference planes intersect along the East--West direction. Their relative inclination is fixed by the observer's astronomical latitude $\phi$: the altitude of the North Celestial Pole is $\phi$ in the Northern hemisphere.


### Hour angle

The **hour angle** $HA$ of an object is measured from the local upper meridian **westward** along the **equator**. Its direction of increase is opposite to that of right ascension. 

We express $HA$ in the interval $-12^{\mathrm h}<t\leq12^{\mathrm h}$: a negative value then places the object east of the meridian, before upper transit, and a positive value places it west of the meridian, after upper transit. At **upper culmination**, when the target is passing through the local meridian on the South side, $HA=0$. 

```{figure} _static/_chapter02/fig06a_horizontal_system.png
:width: 65%
:align: center
:name: fig06a_horizontal_system

**Figure 6** The hour angle $HA$ simplify the transformation between the equatorial and the horizontal system, by allowing a rotation around the East-West axis.
```

### Adopted azimuth convention

Throughout this chapter, as in Chapter 1, the azimuth $A$ is measured **from South toward West**:

$$
S=0^\circ,\qquad W=90^\circ,\qquad N=180^\circ,\qquad E=270^\circ,
\qquad 0^\circ\leq A<360^\circ.
$$

The altitude is denoted by $h$, with $-90^\circ\leq h\leq90^\circ$.  The hour angle is denoted by $HA$ and increases westward from the local meridian.

### Transformations

With these conventions, the transformation from horizontal coordinates $(A,h)$ to hour angle and declination $(HA,\delta)$ is

$$
\begin{aligned}
\cos\delta\sin HA
  &=\cos h\sin A,\\
\cos\delta\cos HA
  &=\cos h\cos A\sin\phi+\sin h\cos\phi,\\
\sin\delta
  &=-\cos h\cos A\cos\phi+\sin h\sin\phi.
\end{aligned}
$$

The first two relations determine the hour angle with the correct quadrant,

$$
H=\operatorname{atan2}\!\left(
\cos h\sin A,
\cos h\cos A\sin\phi+\sin h\cos\phi
\right),
$$

while the third gives the declination.

The inverse transformation, from $(HA,\delta)$ to $(A,h)$, is

$$
\begin{aligned}
\cos h\sin A
  &=\cos\delta\sin HA,\\
\cos h\cos A
  &=\cos\delta\cos HA\sin\phi-\sin\delta\cos\phi,\\
\sin h
  &=\cos\delta\cos HA\cos\phi+\sin\delta\sin\phi.
\end{aligned}
$$

Thus,

$$
A=\operatorname{atan2}\!\left(
\cos\delta\sin HA,
\cos\delta\cos HA\sin\phi-\sin\delta\cos\phi
\right)
$$

reduced to $0^\circ\leq A<360^\circ$. An inverse sine or cosine alone cannot distinguish, for example, a rising object in the East from a setting object in the West. The transformation also makes explicit that horizontal coordinates require both the observer's latitude and the orientation of the local meridian, which is supplied by sidereal time.[^horizontal_transform_reference]

## A modern approach to coordinate transformations

For an ideal rotation, the matrices above are sufficient. Accurate astronomical work must additionally specify the reference frame, epoch, observation time, observer location, Earth orientation, atmospheric refraction, and sometimes the distance and velocity of the target. Modern software packages keep these pieces of information attached to the coordinates and apply a chain of transformations rather than relying on a pair of unlabeled angles.

The `astropy.coordinates` package, shown in [Figure 7](fig06_astropy_coordinates), represents positions with objects such as `SkyCoord` and transforms them between explicitly defined frames. A conversion to a topocentric `AltAz` frame, for example, requires an observing time and an Earth location.[^astropy_coordinates]

```{figure} _static/_chapter02/fig06_astropy_coordinates.png
:width: 100%
:align: center
:name: fig06_astropy_coordinates

**Figure 7** The coordinate-system documentation of Astropy, as shown in slide 8.
```

There is an important convention change: Astropy's `AltAz` azimuth is measured eastward from North, so $N=0^\circ$ and $E=90^\circ$. If $A_{\mathrm{Astropy}}$ is returned by Astropy, the convention used in this chapter is obtained from

$$
A=\left(A_{\mathrm{Astropy}}+180^\circ\right)\bmod360^\circ.
$$

The same conversion applies in the opposite direction. Refraction is another explicit choice: in Astropy's `AltAz` frame it is disabled when the pressure is set to zero and included when a non-zero atmospheric pressure is supplied.

## Sidereal time

Right ascension, hour angle, and sidereal time are three angles measured on the celestial equator ([Figure 8](fig07_sidereal_geometry)):

- the **right ascension** $\alpha$ is measured eastward, or counterclockwise when viewed from the North Celestial Pole, from the vernal point to the object's hour circle;
- the **hour angle** $HA$ is measured westward, or clockwise in the same view, from the local meridian to the object's hour circle;
- the **local sidereal time** $\Theta$ is the hour angle of the vernal point, equivalently the right ascension currently crossing the local upper meridian.

```{figure} _static/_chapter02/fig07_sidereal_geometry.png
:width: 70%
:align: center
:name: fig07_sidereal_geometry

**Figure 8** Geometric relation among right ascension, hour angle, and local sidereal time.
```

Sidereal time is tied to the rotation of the Earth relative to the celestial reference directions. It is not the civil time shown by an ordinary clock. A sidereal day is approximately $23^{\mathrm h}56^{\mathrm m}4^{\mathrm s}$ of mean solar time. The difference arises because the Earth also moves around the Sun while it rotates.

For a terrestrial longitude $\lambda$ taken as positive eastward, the local and Greenwich sidereal times satisfy

$$
\Theta_{\mathrm{local}}=\Theta_{\mathrm{Greenwich}}+\lambda,
$$

with the longitude converted to hours if the sidereal times are in hours, and the result reduced modulo $24^{\mathrm h}$. This relation expresses why two observers at different longitudes see different objects on their meridians at the same instant.


Because right ascension and hour angle increase in opposite directions,

$$
\boxed{\Theta=HA+\alpha},
\qquad
\boxed{HA=\Theta-\alpha}.
$$

All three quantities must be expressed in the same angular unit. It is often convenient to use hours, with $24^{\mathrm h}=360^\circ$. A star on the upper meridian has $H=0$ and therefore $\alpha=\Theta$. Before upper culmination its hour angle is negative; after culmination it is positive. Angles may instead be reduced to the interval $0^{\mathrm h}\leq HA<24^{\mathrm h}$, but the signed interval $-12^{\mathrm h}<HA\leq12^{\mathrm h}$ makes the before/after distinction more transparent.[^sidereal_reference]

### Example: the passage of Vega across the meridian

The presentation follows Vega from Padova using the approximate equatorial coordinates

$$
\alpha=18^{\mathrm h}37^{\mathrm m}43.2^{\mathrm s},
\qquad
\delta=+38^\circ48'23''.
$$

At $\Theta=18^{\mathrm h}00^{\mathrm m}00^{\mathrm s}$,

$$
HA=-0^{\mathrm h}37^{\mathrm m}43.2^{\mathrm s},
$$

so Vega is still east of the meridian. The horizontal transformation for $\phi\simeq45.4^\circ$ gives approximately $a=80.4^\circ$ and $A=310^\circ$ in the South-through-West convention, as illustrated in [Figure 9](fig08_sidereal_1800).

```{figure} _static/_chapter02/fig08_sidereal_1800.png
:width: 90%
:align: center
:name: fig08_sidereal_1800

**Figure 9** Vega shortly before upper culmination, when the local sidereal time is $18^{\mathrm h}$. The Stellarium azimuth readout in this extracted slide image uses North through East; the text of this chapter converts it to South through West.
```

At $\Theta=18^{\mathrm h}38^{\mathrm m}10^{\mathrm s}$, the hour angle is only about $+27$ seconds of time. Vega is therefore essentially on the upper meridian ([Figure 10](fig09_sidereal_183810)). Its altitude is

$$
h_{\mathrm{upper}}=90^\circ-|\phi-\delta|
\simeq83.4^\circ,
$$

and its azimuth is close to $A=0^\circ$, due South.

```{figure} _static/_chapter02/fig09_sidereal_183810.png
:width: 90%
:align: center
:name: fig09_sidereal_183810

**Figure 10** Vega at upper culmination. Its right ascension is nearly equal to the local sidereal time. The displayed software azimuth follows the North-through-East convention.
```

Finally, at $\Theta=20^{\mathrm h}40^{\mathrm m}00^{\mathrm s}$ ([Figure 11](fig10_sidereal_204000)),

$$
HA\simeq+2^{\mathrm h}02^{\mathrm m}17^{\mathrm s},
$$

so Vega has moved west of the meridian. The ideal transformation gives approximately $a=66.5^\circ$ and $A=84.6^\circ$, close to the West direction in our convention.

```{figure} _static/_chapter02/fig10_sidereal_204000.png
:width: 90%
:align: center
:name: fig10_sidereal_204000

**Figure 11** Vega after upper culmination, at local sidereal time $20^{\mathrm h}40^{\mathrm m}$. The software azimuth must again be shifted by $180^\circ$ to match this chapter.
```

The small differences between the values calculated above and the values visible in the screenshots can arise from the exact site coordinates, epoch, precession, nutation, refraction settings, and the equatorial coordinates adopted by the software.

## Solar and sidereal time

A **solar day** is the interval between two consecutive passages of the Sun across the same meridian. Because the apparent solar motion is not perfectly uniform, civil time uses a mean solar day of exactly $24$ hours. In the broader language of orbital motion, the solar day is a synodic rotation period: it measures the Earth's rotation relative to the moving Sun.

A **sidereal day** is the interval between two consecutive meridian passages of a distant reference direction. Its duration in mean solar time is approximately

$$
23^{\mathrm h}56^{\mathrm m}04.1^{\mathrm s}.
$$

During one sidereal day the Earth completes one rotation relative to the stars, but it has also advanced along its orbit. It must rotate by about one additional degree before the Sun returns to the meridian. The solar day is consequently about $3^{\mathrm m}56^{\mathrm s}$ longer than the sidereal day ([Figure 12](fig11_sidereal_solar_day)).

```{figure} _static/_chapter02/fig11_sidereal_solar_day.png
:width: 55%
:align: center
:name: fig11_sidereal_solar_day

**Figure 11** The sidereal day ends when a distant reference star returns to the meridian. The mean solar day ends only after the additional rotation needed to compensate for the Earth's orbital motion. 
```

Equivalently, at a fixed civil time the local sidereal time advances by almost four minutes from one date to the next. A given star therefore crosses the meridian approximately four minutes earlier on each successive solar day.

### Example: the Sun and Betelgeuse

On 20 June in the example from the presentation, the Sun and Betelgeuse lie close to the local meridian at the selected civil time ([Figure 13](fig12_betelgeuse_june20)).

```{figure} _static/_chapter02/fig12_betelgeuse_june20.png
:width: 90%
:align: center
:name: fig12_betelgeuse_june20

**Figure 13** The Sun and Betelgeuse close to the local meridian on 20 June. The azimuth readout uses the software's North-through-East convention.
```

One week later, at the same civil time, the local sidereal time has advanced by approximately

$$
7\times3^{\mathrm m}56^{\mathrm s}\simeq27^{\mathrm m}32^{\mathrm s}.
$$

Betelgeuse has therefore already crossed the meridian, while the Sun is again close to it ([Figure 14](fig13_betelgeuse_june27)). This is the observational meaning of the statement that the sidereal clock runs faster than the solar clock.

```{figure} _static/_chapter02/fig13_betelgeuse_june27.png
:width: 90%
:align: center
:name: fig13_betelgeuse_june27

**Figure 14** At the same civil time one week later, Betelgeuse is already west of the meridian. 
```

## The apparent daily motion of the stars

The altitude of the North Celestial Pole equals the observer's latitude $\phi$. As the Earth rotates, a star with fixed declination describes a small circle parallel to the celestial equator. Its altitude generally changes continuously, but its angular distance from the celestial pole remains constant.

A star reaches an extremum of altitude whenever it crosses the meridian. The **upper culmination** is the transit closest to the zenith and normally provides the greatest altitude. The **lower culmination** occurs twelve sidereal hours later, on the opposite branch of the meridian. [Figure 15](fig14_daily_star_motion) shows these daily circles, while [Figure 16](fig15_star_trails) records them as star trails around the celestial pole.

```{figure} _static/_chapter02/fig14_daily_star_motion.png
:width: 55%
:align: center
:name: fig14_daily_star_motion

**Figure 15** Daily paths of stars at different declinations. A sufficiently high positive declination produces a circumpolar path for an observer in the Northern hemisphere. 
```

```{figure} _static/_chapter02/fig15_star_trails.png
:width: 90%
:align: center
:name: fig15_star_trails

**Figure 16** Long-exposure star trails centred approximately on a celestial pole.
```

If the entire daily circle remains above the horizon, the star is **circumpolar**. If the entire circle remains below the horizon, the star never rises. The intermediate case is a star that rises and sets once during each sidereal day.

## Rising and setting stars

Given $(\alpha,\delta)$ and the local sidereal time, the first step is always

$$
HA=\Theta-\alpha.
$$

The altitude $h$ then follows from

$$
\sin h=\cos\delta\cos HA\cos\phi+\sin\delta\sin\phi.
$$

An ideal point source is on the astronomical horizon when $h=0$. Setting $\sin h=0$ gives the hour angle at rising or setting:

$$
\boxed{\cos HA_0=-\tan\phi\tan\delta}.
$$

When a crossing exists, $HA=-HA_0$ is the rising solution and $HA=+HA_0$ is the setting solution. The corresponding horizon azimuth satisfies

$$
\boxed{\cos A_0=-\frac{\sin\delta}{\cos\phi}}.
$$

The sign of $\sin A$ selects the event. Since a rising star has $HA<0$, it also has $\sin A<0$; a setting star has $HA>0$ and $\sin A>0$. In the South-through-West convention,

$$
A_{\mathrm{rise}}=360^\circ-\arccos\!\left(-\frac{\sin\delta}{\cos\phi}\right),
$$

and

$$
A_{\mathrm{set}}=\arccos\!\left(-\frac{\sin\delta}{\cos\phi}\right).
$$

Only a star on the celestial equator, $\delta=0$, rises exactly in the East $(A=270^\circ)$ and sets exactly in the West $(A=90^\circ)$. Positive declination shifts both points northward; negative declination shifts them southward.

These are geometric results for a point source and a perfectly level astronomical horizon. Atmospheric refraction, the finite apparent radius of the Sun or Moon, and the local landscape alter observed rise and set times.

### Northern hemisphere

For $\phi>0$:

- the star is circumpolar if $\delta\geq90^\circ-\phi$;
- it rises and sets if $-(90^\circ-\phi)<\delta<90^\circ-\phi$;
- it never rises if $\delta\leq-(90^\circ-\phi)$.

At either equality the daily circle is tangent to the horizon, so the boundary case should be treated separately in numerical work.

### Southern hemisphere

For $\phi<0$:

- the star is circumpolar around the South Celestial Pole if $\delta\leq-90^\circ-\phi$;
- it rises and sets if $-90^\circ-\phi<\delta<90^\circ+\phi$;
- it never rises if $\delta\geq90^\circ+\phi$.

The criteria are the mirror image of the Northern-hemisphere case. A compact statement is that a star is circumpolar when $\phi$ and $\delta$ have the same sign and $|\delta|\geq90^\circ-|\phi|$; it never rises when they have opposite signs and the same absolute-value condition is satisfied.

### Altitudes at meridian passage

At upper and lower culmination, the geometric altitudes are

$$
\boxed{h_{\mathrm{upper}}=90^\circ-|\phi-\delta|},
$$

and

$$
\boxed{h_{\mathrm{lower}}=|\phi+\delta|-90^\circ}.
$$

The labels are important: the first expression is the maximum altitude and the second is the minimum. Thus:

- a circumpolar star has $h_{\mathrm{lower}}\geq0$;
- a rising and setting star has $h_{\mathrm{upper}}>0>h_{\mathrm{lower}}$;
- a star that never rises has $h_{\mathrm{upper}}\leq0$.

For Padova, $\phi\simeq45.4^\circ$, so the circumpolar limit is $\delta\simeq+44.6^\circ$. A star at $\delta=+60^\circ$ is circumpolar, a star on the celestial equator rises and sets, and a star at $\delta=-60^\circ$ never rises. Vega, with $\delta\simeq+38.8^\circ$, lies below the circumpolar limit and therefore sets for an ideal observer at Padova, even though it spends a large fraction of the sidereal day above the horizon.[^rising_setting_reference]

## The motion of the Sun on the sky

During the year the Sun moves eastward along the ecliptic while its daily apparent motion carries it westward across the local sky. Since the Sun lies approximately on the ecliptic, $\beta_\odot=0$. The ecliptic-to-equatorial transformation then gives

$$
\sin\delta_\odot=\sin\varepsilon\sin\lambda_\odot,
$$

and

$$
\cos\delta_\odot\sin\alpha_\odot
=\cos\varepsilon\sin\lambda_\odot.
$$

Dividing these relations yields the expression highlighted in the presentation:

$$
\boxed{\sin\alpha_\odot=\frac{\tan\delta_\odot}{\tan\varepsilon}}.
$$

At the equinoxes $\delta_\odot=0$; at the June solstice $\delta_\odot\simeq+\varepsilon$; and at the December solstice $\delta_\odot\simeq-\varepsilon$. The changing declination alters the maximum solar altitude, the azimuths of sunrise and sunset, and the interval for which the Sun remains above the horizon ([Figures 17](fig16_sun_paths_solstices) and [18](fig17_sun_paths_year)).

```{figure} _static/_chapter02/fig16_sun_paths_solstices.png
:width: 60%
:align: center
:name: fig16_sun_paths_solstices

**Figure 17** The daily solar paths at the summer and winter solstices for a Northern-hemisphere observer. Extracted from slide 20.
```

```{figure} _static/_chapter02/fig17_sun_paths_year.png
:width: 60%
:align: center
:name: fig17_sun_paths_year

**Figure 18** Seasonal change in the Sun's path across the local sky. Extracted from slide 20.
```

As a geometric example, take $\phi=45.4^\circ$ and neglect refraction and the finite angular radius of the Sun. At the equinoxes, sunrise occurs at $A=270^\circ$ and sunset at $A=90^\circ$, with a $12$-hour interval between them. At the June solstice, the equations give approximately

$$
A_{\mathrm{rise}}=235.5^\circ,
\qquad
A_{\mathrm{set}}=124.5^\circ,
$$

so the Sun rises north of East and sets north of West. The geometric day lasts about $15.48$ hours. At the December solstice,

$$
A_{\mathrm{rise}}=304.5^\circ,
\qquad
A_{\mathrm{set}}=55.5^\circ,
$$

and the geometric day lasts about $8.52$ hours. Published sunrise and sunset times differ from these ideal values because standard almanacs include atmospheric refraction, the solar radius, and a precise solar ephemeris.[^solar_motion_reference]

## Angular velocities in horizontal coordinates

We finally ask how rapidly the horizontal coordinates change as the Earth rotates. Let the independent variable be the local sidereal angle $\Theta$, measured in radians, and define a dot by

$$
\dot{q}\equiv\frac{\mathrm{d}q}{\mathrm{d}\Theta}.
$$

For a distant star, neglecting proper motion and other slow perturbations over one night,

$$
HA=\Theta-\alpha,
\qquad
\dot{HA}=1,
\qquad
\dot\delta=0.
$$

[Figure 18](fig18_altaz_targets) shows examples of horizontal-coordinate tracks for several targets. Its polar diagram follows the widespread North-through-East azimuth convention, so every plotted azimuth must be shifted by $180^\circ$ to obtain the convention used in the equations below. This constant shift changes the zero point of $A$, but not the magnitude of its angular velocity.

```{figure} _static/_chapter02/fig18_altaz_targets.png
:width: 90%
:align: center
:name: fig18_altaz_targets

Examples of target motion in apparent altitude and azimuth. Extracted from slide 22. The original plot uses $N=0^\circ$, $E=90^\circ$; the text and equations of this chapter use $S=0^\circ$, $W=90^\circ$.
```

### Altitude velocity

Differentiate

$$
\sin h=\cos\delta\cos H\cos\phi+\sin\delta\sin\phi
$$

with respect to $\Theta$:

$$
\dot h\cos h=-\cos\delta\sin HA\cos\phi.
$$

Using $\cos h\sin A=\cos\delta\sin HA$, we obtain

$$
\boxed{\dot h=-\sin A\cos\phi}.
$$

The altitude is stationary on the meridian, where $\sin A=0$. It increases for a rising target and decreases for a setting target. Since $|\sin A|\leq1$,

$$
|\dot h|\leq|\cos\phi|\leq1.
$$

The value $1$ means one radian of altitude per radian of sidereal rotation, equivalent to $15^\circ$ per sidereal hour. The greatest possible altitude rate occurs at the equator. At either terrestrial pole, $\cos\phi=0$, every star moves parallel to the horizon and its altitude remains constant.

### Azimuth velocity

Differentiating the remaining horizontal relations and eliminating $HA$ and $\delta$ gives

$$
\boxed{\dot A=\sin\phi+\cos A\tan h\cos\phi}.
$$

An equivalent form that is useful close to the zenith is

$$
\boxed{
\dot A=
\frac{\sin\phi-\sin\delta\sin h}{\cos^2 h}
}.
$$

At the horizon, $h=0$, so

$$
\dot A_{\mathrm{horizon}}=\sin\phi.
$$

The azimuth rate is therefore positive at rising and setting in the Northern hemisphere, negative in the Southern hemisphere, and zero at the equator. At Padova it is approximately $0.712$ radians per radian of sidereal rotation, or $10.7^\circ$ per sidereal hour.

At the zenith, $\cos a=0$ and azimuth is undefined. A target passing very close to the zenith can consequently require an extremely rapid change of azimuth even though its true angular speed on the celestial sphere remains finite. This is the familiar **zenith blind spot** of an altitude-azimuth mount, illustrated qualitatively by the trails in [Figure 19](fig19_star_trails_zenith). The divergence is a coordinate singularity, not a physical infinite velocity.

```{figure} _static/_chapter02/fig19_star_trails_zenith.png
:width: 90%
:align: center
:name: fig19_star_trails_zenith

Star trails passing near the zenith. An altitude-azimuth description changes azimuth very rapidly for tracks close to the zenith. Extracted from slide 22.
```

These angular rates concern the coordinate axes of an ideal altitude-azimuth system. A real telescope must also account for tracking errors, atmospheric refraction, mechanical acceleration limits, and field rotation.

## Summary of the transformation procedure

For a practical coordinate transformation, the following sequence is reliable:

1. State the origin, reference frame, epoch, and angle conventions.
2. Convert spherical coordinates to a Cartesian unit vector.
3. Apply the required rotation matrices in the stated order.
4. Recover latitude from the final $z$ component and longitude with $\operatorname{atan2}$.
5. For horizontal coordinates, supply the observer's latitude and local sidereal time.
6. Check the result at a geometrically simple direction, such as a pole, equinox, meridian transit, or horizon crossing.

Most sign errors in spherical astronomy can be traced to a missing convention: an active rotation used in place of a passive one, matrices multiplied in the wrong order, a longitude measured in the opposite direction, or an azimuth measured from a different origin. In this chapter, the horizontal equations consistently use azimuth from South toward West.

## References and figure sources

The order of the topics follows *Lesson 02 - Transformation of Coordinates*, slides 1--22. All figures in this chapter were extracted from that presentation and converted to PNG without changing their visual content. Formulae and explanations were checked and expanded using the following sources; page numbers refer to the printed pages of the supplied editions.

- **Barbieri, C., and Bertini, I. (2021)**, *Fundamentals of Astronomy*, second edition, CRC Press. Sections 2.2--2.5 for celestial systems and sidereal time, and Sections 3.1--3.2 for coordinate transformations.
- **Karttunen, H., Kröger, P., Oja, H., Poutanen, M., and Donner, K. J. (eds., 2017)**, *Fundamental Astronomy*, sixth edition, Springer. Chapter 2, especially Sections 2.5--2.7 on equatorial coordinates, time, and transformations.
- **Hanslmeier, A. (2023)**, *Introduction to Astronomy and Astrophysics*, Springer. Chapter 2, particularly Sections 2.1--2.3 on astronomical coordinates, time, and apparent motion.
- **Astropy Project**, [Astronomical Coordinate Systems](https://docs.astropy.org/en/latest/coordinates/index.html) and [`AltAz` frame](https://docs.astropy.org/en/latest/api/astropy.coordinates.AltAz.html), consulted for the modern software workflow and its azimuth and refraction conventions.

The presentation reverses the labels attached to the upper- and lower-culmination altitude formulae on slide 18; the geometrically correct labels are used here. The last alternative expression for the azimuth velocity on slide 22 is also replaced by the form obtained directly from the stated South-through-West transformation equations.

[^rotation_reference]: Barbieri and Bertini (2021), Section 3.1, pp. 36--39. The distinction between active and passive rotations is made explicit here because the matrices in the presentation rotate coordinate axes.

[^ecliptic_transform_reference]: Barbieri and Bertini (2021), Section 3.2; Hanslmeier (2023), Sections 2.1.4 and 2.1.6. The numerical matrix uses the approximate obliquity stated in the presentation.

[^horizontal_transform_reference]: Barbieri and Bertini (2021), Section 3.1, pp. 36--39; Karttunen et al. (2017), Sections 2.5--2.6, pp. 17--23. All signs have been written for azimuth measured from South toward West.

[^astropy_coordinates]: The official Astropy documentation describes `SkyCoord`, frame transformations, and the observer-dependent `AltAz` frame. Astropy measures azimuth eastward from North, unlike the convention adopted here.

[^sidereal_reference]: Barbieri and Bertini (2021), Sections 2.2--2.3, pp. 25--29; Karttunen et al. (2017), Sections 2.5--2.6, pp. 17--23; Hanslmeier (2023), Section 2.2.

[^rising_setting_reference]: Karttunen et al. (2017), Chapter 2; Barbieri and Bertini (2021), Section 3.1. The equality cases correspond to a daily circle tangent to the ideal horizon.

[^solar_motion_reference]: Barbieri and Bertini (2021), Sections 2.5 and 3.2; Hanslmeier (2023), Chapter 2. The numerical day lengths are purely geometric and exclude the standard observational corrections applied in almanacs.
