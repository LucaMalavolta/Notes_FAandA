(chapter01\_spherical\_astronomy)=

# Spherical Astronomy and Coordinate Systems

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

## The Celestial Sphere

Historically speaking, the **Celestial Sphere** was the apparent surface of the heavens, on which the stars seem to be fixed.
Nowadays, the term *Celestial sphere* refers to an abstract construct used to describe the locations of objects in the sky.


The Celestial Sphere has an infinite radius, in the sense that all the objects on it are at the same endless distance. In other words, the distance of an object is not required to describe its position in the sky. For obvious mathematical reasons, it is easier to deal with a sphere with a *unitary* radius (think about trigonometry) rather than an infinite one. The centre of the Earth is the centre of the celestial sphere, and the sphere's pole and equatorial plane are coincident with those of the Earth.


Dealing with a sphere with unitary radius is not dissimilar to dealing with a circle with unitary radius, which is the goal of *trigonometry*. For this reason,  we talk about **spherical trigonometry**, also called **spherical astronomy** when referring to the Celestial Sphere.

## Trigonometry

Trigonometry is the branch of mathematics concerned with specific functions of angles and their application to calculations. 
Considering a circle with radius $r$, the arc $s$ subtended on the circle by an angle $\theta$ is equal to the radius multiplied by the angle $s = r \theta$.
The first plot in [Figure 1](fig01_trigonometry) exemplifies this case.  For this to work, the angle $\theta$ must be a dimensionless quantity. We can see that $s=r$ for $\theta = 1$, we thus define *one radian* as the angle formed at the centre of a circle by an arc whose length is equal to the radius of the circle (second plot in [Figure 1](fig01_trigonometry)). Following this definition, an angle of 360° is equal to $2 \pi$, thus  1 radian = 57.296°. 

```{figure} _static/_chapter01/fig01_trigonometry.png
:width: 100%
:align: centre
:name: fig01_trigonometry

Basic concepts of trigonometry.
```

[Figure 2](fig02_trigonometric_functions) shows the relationship among the *sine* ($\sin$), *cosine* ($\cos$), and *tangent* ($\tan$) trigonometric functions. The *secant* function ($\sec$), equivalent to the inverse of the cosine, is of relevance for Astronomy.


```{figure} _static/_chapter01/fig02_trigonometric_functions.png
:width: 70%
:align: center
:name: fig02_trigonometric_functions

The most essential trigonometric functions[^margin_trigonometric_functions]
```

[^margin_trigonometric_functions]: {-} [Wikipedia link to trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions)


There are four standards to represent angles in Astronomy:
- **Radians**: the standard way. Angles are measured between $0$ and $2 \pi$ radians. Radians are the only accepted input by trigonometric functions.
- **Decimal degrees**: angles vary between $0$ and $360°$. Given $\alpha$ the value of the angle in radians and $\beta$ the same angle in decimal degrees, the relationship between the two is $\beta = \alpha * 180 / \pi$
- **Degrees (dms)**: it is a *sexagesimal* system where the angles still vary between $0$ and $360°$, but fractions of a degree are expressed as separate numbers rather than decimal figures. One degree is divided in $60$ *arcminutes* (denoted with the symbol $'$), one arcminute is divided in 60 *arcseconds* (symbol $''$). Fractions of arcseconds are expressed as a decimal part. The conversion from decimal degrees to sexagesimal degrees is obtained through several steps: 
 	1) The whole number part of your decimal degrees gives you the *degrees* in *dms* system.
 	2) Multiply by 60 the decimal part of your decimal degrees. The whole number part of the result is arcminutes.
 	3) Multiply the decimal part of the last result by 60 to convert it to arcseconds.
The sign is positioned before the degrees. The *whole number part* is the part before the decimal sign (e.g., $47$ in $47.73$, $-17$ in $-17.43$), the *decimal part* is the one *after* the decimal sign.
The inverse conversion is much simpler: $\beta = d + m/60 + s/3600$.

- **Hours (dhms)**: again a *sexagesimal* system, with angles measured between $0$ and $24$ *hours*. Thus, *one hour* corresponds to *15 degrees*.
To avoid confusion with the degree (dms) system, the units composing an hour are called *minutes* and *seconds* rather than arcminutes and arcseconds.
The conversion from decimal degrees to sexagesimal degrees is obtained through four steps: 
 1) Divide the decimal degrees by 24 to get the value in *decimal hours*.
 2) The whole number part of your decimal hours gives you the *hours* in *hms* system.
 3) Multiply by 60 the decimal part of your decimal hours. The whole number part of the result is the *minutes*.
 4) Multiply the decimal part of the last result by 60 to convert it to *seconds*.

The inverse conversion is much simpler: $\beta = (h + m/60 + s/3600) * 15$.


```{figure} _static/_chapter01/fig03_angles.png
:width: 70%
:align: center
:name: fig03_angles

Graphical representation of angles in degrees, radians, and hours.
```


## Spherical trigonometry
 
Consider a sphere with radius $r$ and centred at $C$. \
A plane passing through the centre of the sphere $C$ divides the sphere into two identical parts, called **hemispheres**. The intersection of this plane with the sphere is called a **great circle**. A great circle always separates two hemispheres. Consider now the perpendicular (or *normal*) to the same plane and passing to the center $C$: the intersection $P$ and $P'$ between this normal and the sphere are called **poles** .\
The intersection between the sphere and any other plane **not** passing through the centre $C$ is called a **small circle**. \
The shortest path between two points on a sphere $Q$ and $Q'$ is always **along a great circle**. 

```{figure} _static/_chapter01/fig04_sphere_planes.png
:width: 50%
:align: center
:name: fig04_sphere_planes

Representation of a *great circle* and a *small circle*.
```


If you identify three points on the surface of the sphere, and connect them with great circles, you obtain a **spherical triangle**. Considering the spherical triangle in the figure, the angle *c* subtended by the arc *AB* is called the **central angle** and is measured in radians or degrees. \
The length of the arc *AB* is equal to the radius of the sphere multiplied by the subtended central angle, $AB = r* c$. If we consider a sphere with unit radius ($r=1$), then $AB = c$, and we can measure the arc *AB* in radians or degrees.


```{figure} _static/_chapter01/fig05_spherical_triangle.png
:width: 70%
:align: center
:name: fig05_spherical_triangle

A spherical triangle $ABC$ identified by the three arcs $a$, $b$, $c$ and the corresponding central angles.
```


Other properties of spherical triangles:

- The sum of the internal angles is always greater than $2 \pi$ ($180°$). 
- The spherical excess $E$ is defined as the sum of the internal angles of the spherical triangle, minus $2 \pi$, $E = A + B + C - 2\pi$. 
- The **area of the spherical triangle** is equal to $E r^2$.
- The **area of the sphere* is equal to $4\pi r^2$

If we assume $r=1$, as for example with the celestial sphere, we have that a portion of the sky identified by a spherical triangle has area equal to $E$. Equivalently to the radians for an arc length, we can measure this area as **steradians**, if the central angles are expressed in radians. The area of the celestial sphere is then equal to $4 \pi$ *steradians*. 

From now on, we will always assume $r=1$.
 
## Coordinate systems

 To describe the position of points in space using numbers (called *coordinates*), we need to define a reference structure so that every point can be uniquely identified. This mathematical framework is called *coordinate system*. 

Let's suppose we want to identify the position of a point *on the surface of a sphere* with unit radius. In this specific case, we need only two ingredients to define a coordinate system:

- The direction of the perpendicular of a plane passing through the centre of the sphere ($z$ in the figure).
- The direction of one axis lying on the plane ($x$ in the figure)

The perpendicular is often called *normal*. The definition of the plane alone is not sufficient; we also need to define the positive and negative sides of the hemispheres identified by the plane.


```{figure} _static/_chapter01/fig06_polar_coordinates.png
:width: 70%
:align: center
:name: fig06_polar_coordinates

The angles $\psi$ and $theta$ uniquely identify a point P on the sphere, assuming that the size of the sphere is fixed. Transformations to a new coordinate system can be obtained by rotating two axes around the third one, for example, by rotating $y$ and $z$ by an angle $\chi$ to $y'$ and $z'$ on the plane perpendicular to the axis $x$.
```


In such a system, a given point $P$ is uniquely identified by two angles, $\psi$ and $\theta$, in [Figure 6](fig06_polar_coordinates). In a three-dimensional space, you would need three coordinates to constrain the position of an object uniquely. In our specific case, two coordinates are sufficient because we assumed we are on the two-dimensional surface of a fixed sphere. The third coordinate, i.e., the radial distance from the centre, is always equal to $1$. 

Coordinate transformations can be obtained by successive rotations around a single axis. In [Figure 6](fig06_polar_coordinates), the $x$ is kept fixed (thus coinciding with $x'$), while the $y$ and $z$ axes are rotated around the origin by an angle $\chi$ on the plane perpendicular to $x$. 

```{figure} _static/_chapter01/fig07_coordinates_physics.png
:width: 70%
:align: center
:name: fig07_coordinates_physics

There is no general agreement on the definition of angles among disciplines. In Physics and Mathematics, the *polar coordinate* $\theta$ is measured starting from the normal to the plane, rather than the plane itself. In Mathematics, the angles' names $\theta$ and $\psi$ are swapped.
```

The definitions of angles can vary across disciplines. [Figure 7](fig07_coordinates_physics) shows the standard definition in Mathematics and Physics. 

## Geographic Coordinate Systems

### Geocentric coordinate system 

In this system, the Earth is assumed to be a perfect sphere. The plane perpendicular to the *rotational axis* of the planet and passing through its centre is called the **Equatorial plane**, and it is the **reference plane** in this system. The intersection between the Equatorial plane and the sphere (in this case, the Earth) identifies the **Equator**. \
The rotational axis intersects the Earth at two points: the *North Pole* in the Northern Hemisphere and the **South Pole** in the Southern Hemisphere.                                                                                                                                                 The angular momentum vector of Earth points to the North Pole, following the right-hand rule. When viewed from the North Pole, Earth rotates counterclockwise.  \
**Meridians** are semi-circle from one pole to the opposite one. **Parallels** are small circles parallel to the Equator. \

The meridian passing through the Royal Observatory Greenwich defines the direction of the *x* axis on the equatorial plane. For this reason, this meridian takes the name of **Prime Meridian**.

The distance of a point on the surface of Earth (i.e., on the surface of the sphere) from the Equator, by definition measured across a great circle and hence through a great circle passing through the poles (as the arc connecting this point to the Equator must be perpendicular to the latter) is called **Latitude**. The latitude $\phi$ is positive for points in the Northern hemisphere, and negative for points in the Southern hemisphere. Sometimes the letters *N* and *S* are used as a replacement for the sign. $\phi$ is comprised between $-90°$ and $90°$. All the points on a Parallel have the same Latitude. 

The **Longitude** is the distance from the Prime Meridian of the projection of the point on the Equator. First, you identify the projection on the Equator as the intersection between the Equator itself and a meridian passing through your point. Then, you measure the distance (over the surface of the sphere) from the Prime Meridian along the Equator. Longitude $\lambda$ is measured counterclockwise on a range between $-180°$ and $180°$: it is positive for points East of the Prime Meridian, and negative for points West of the Prime Meridian. Sometimes, the sign is replaced by $E$ for positive values, and $W$ for negative values. 

```{figure} _static/_chapter01/fig08_geocentric_system.jpg
:width: 70%
:align: center
:name: fig08_geocentric_system

Geocentric coordinate system, with representation of **Latitude** $\phi$ and **Longitude** $\lambda$, **Equator** (latitude equal to zero) and **Prime Meridian** (longitude equal to zero).
```

When reporting coordinates, Latitude is conventionally expressed first. The coordinates of Padova are :

| Latitude  | Longitude  |
|---|---|
| $45.40643°$  | $11.87676°$  | 
| $45°\, 24' \, 23.17'' $  | $11°\, 52' \,  36.34'' $  |
| $45°\, 24' \, 23.17'' $ N | $11°\, 52' \,  36.34'' $ W |

Latitudes and Longitudes are both expressed in degrees, either in decimal form or in $dms$ format. 

### Geodetic coordinate system

The Geocentric coordinate system assumes that the Earth is a perfect sphere. However, all rotating bodies depart from a perfect sphere because their rotation creates centrifugal force that bulges them at the equator and flattens them at the poles. As a consequence, the **equatorial radius** (the distance of the surface from the centre, measured at the equator) will be greater than the **polar radius** (the distance of the surface from the centre, measured at one of the two poles). In a first approximation, we can assume axial symmetry around the rotation axis (all the *parallels* are perfect circles); in this case, the solid is called a **oblate spheroid**, or more commonly, just **ellipsoid** or **spheroid**. (Note: a *prolate spheroid* would have the polar radius larger than the equatorial radius.) The last two terms are the most common, though not entirely accurate. On our planet, the ellipsoid approximates the equilibrium shape of the oceans, as the real figure of Earth is more complicated than a simple rotationally symmetric solid. \
The amount of flattening of a planet primarily depends on its composition and the time it takes to perform a full rotation around its axis (rotational period). The amount of flattening is usually parametrised at the fraction difference between the equatorial and polar radii, i.e., (equatorial-polar)/equatorial. See [Figure 9](fig09_saturn) for an extreme case in the Solar System. \


|Planet | Equatorial radius (Km)  | Polar Radius (Km)  | Difference (Km) | Flattening | 
|---|---|---|---|---|
|Earth | $6378.137$ | $6356.752$ | $21.385$ | $3.35 \cdot 10^{-3}$ |
| Saturn | $60268$ | $54364$ | $5904$ | $0.10$ |


```{figure} _static/_chapter01/fig09_saturn.png
:width: 70%
:align: center
:name: fig09_saturn

The planet Saturn has a mean density below that of water, and it completes a rotation in 10 hours and 34 minutes. As a consequence, its flattening can be seen with the naked eye. The purple circle and the two orange axes highlight the 10\%  flattening of the planet. 
```

The oblateness of our planet introduces a problem in measuring the coordinates of an object when its distance from the surface changes.
In a sphere, we can increase or decrease the distance of a point along any line passing through the centre without changing its geocentric coordinates. In other words, the coordinates are independent of the object's altitude, measured as a distance from the surface along a vertical (a line perpendicular to the surface). This is no longer the case in an ellipsoid, as illustrated in [Figure 10](fig10_geodetic_coordinates): for example, compare the angle with respect to the ellipsoid's centre for an object on the surface (green line) with the same object at altitude $h$ (blue line). $\phi_c$ changes with the altitudes of an object, i.e., the latitude changes even if the object is moving vertically to the surface. 



```{figure} _static/_chapter01/fig10_geodetic_coordinates.png
:width: 70%
:align: center
:name: fig10_geodetic_coordinates

Geodetic coordinates.
```

To solve this problem, a 

Ellipsoid vs. Geoid
Ellipsoid: A mathematical model that represents the Earth as a smooth, slightly flattened sphere. It ignores variations in the Earth's gravitational field.
Geoid: The true, irregular shape that represents the mean sea level in a state of equilibrium. It is more accurately described as a "level" surface, meaning it is everywhere perpendicular to the local direction of gravity. 

