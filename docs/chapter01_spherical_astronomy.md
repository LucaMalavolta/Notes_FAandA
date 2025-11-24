(chapter01\_spherical\_astronomy)=

# Spherical Astronomy

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
:align: center
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
- **Degrees (dms)**: it is a *sexagesimal* system where the angles still vary between $0$ and $360°$, but fractions of a degree are expressed as separate numbers rather than decimal figures. One degree is divided in $60$ *arcminutes* (denoted with the symbol $'$), one arcminute is divided in 60 *arcseconds* (symbol $''$). Fractions of arcseconds are expressed as decimal part. The conversion from decimal degrees to sexagesimal degrees is obtained through three steps: 
  1) $d = \int(\beta)$
  2) $m = \int( (\beta - d)*60) $
  3)  $s = ((\beta - d)*60 - m) * 60$
where $\int$ is the integer part of the number ($\int(24.9) = 24$). 
The inverse conversion is much simpler: $\beta = d + m/60 + s/3600$.
- **Hours (dhms)**: again a *sexagesimal* system, with angles measured between $0$ and $24$ *hours*. Thus, *one hour* corresponds  to *15 degrees*.
SSSSSSSSSSS 
The conversion from decimal degrees to sexagesimal degrees is obtained through three steps: 
  1) $h = \int(\beta / 15) 
  3) $m = \int( (\beta/15 - h)*60) $
  4) $s = ((\beta/15 - d)*60 - m) * 60$



