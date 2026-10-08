(chapter03_telescope_mounts)=

# Telescope Mounts

:::{danger}
This page still need sustantial revision to match the content presented during the lectures
:::

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

A telescope mount supports the optical system, points it at a celestial target, and follows that target while the Earth rotates. Its axes are therefore a mechanical expression of the coordinate systems introduced in the previous chapters. An **equatorial mount** has an axis parallel to the Earth's rotation axis; an **altitude-azimuth mount** has one vertical and one horizontal axis. A meridian transit instrument is a particularly instructive limiting case: it has only one pointing axis and waits for the sky to carry a star through its field of view.

We begin with meridian instruments, then examine the principal altazimuthal and equatorial designs, compare their operation, and consider the Giant Magellan Telescope and ESO's Extremely Large Telescope. The horizontal azimuth $A$ used in the equations is measured from South toward West, as in {doc}`Chapter 2 <chapter02_transformation_of_coordinates>`. Some diagrams use the more common North-through-East convention; their geometry is unaffected by this change of zero point.

## From sky coordinates to a mechanical axis

The right ascension $\alpha$ and declination $\delta$ of a star refer to the celestial equator and its pole. Altitude $h$ and azimuth $A$ refer to the observer's horizon and zenith ([Figure 1](fig01_mounts_horizontal_coordinates)). At a given site, a star's equatorial coordinates are nearly constant over one night, whereas its horizontal coordinates vary continuously. The hour angle $H$ connects the two descriptions:

$$
H=\Theta-\alpha,
$$

where $\Theta$ is local sidereal time. For a star, $H$ grows at approximately $15^\circ$ per sidereal hour. The mount must cancel this apparent motion by rotating about appropriately oriented axes. Throughout this chapter, “tracking” means keeping the selected celestial direction fixed in the telescope's field despite the Earth's rotation; real instruments also correct small effects such as refraction, flexure, and pointing errors.[^mount_sources]

```{figure} _static/_chapter03/fig01_horizontal_coordinates.png
:width: 65%
:align: center
:name: fig01_mounts_horizontal_coordinates

**Figure 1** The local horizon, meridian, zenith, altitude, and azimuth. The azimuth zero point in the diagram should be distinguished from the South-through-West convention used in the equations here.
```

## Meridian transit telescopes

The earliest accurate positional catalogues relied heavily on **meridian circles** or **transit telescopes**. Their optical tubes turn about a horizontal East-West axis, so the line of sight remains in the local meridian plane ([Figure 2](fig02_mounts_transit_telescope)). The instrument changes altitude, but does not follow a star in azimuth. Instead, it is set to the expected transit altitude and the star crosses the field as the Earth rotates.

```{figure} _static/_chapter03/fig02_transit_telescope.png
:width: 35%
:align: center
:name: fig02_mounts_transit_telescope

**Figure 2** Historical meridian transit telescope. Its horizontal axis permits motion only within the meridian plane.
```

At **upper meridian transit**, $H=0$, and therefore

$$
\boxed{\Theta_{\mathrm{transit}}=\alpha}.
$$

Recording the time at which a star of known right ascension crosses the meridian determines local sidereal time. Conversely, a well-calibrated sidereal clock supplies the star's right ascension from the observed transit time. This is the relation illustrated in [Figure 3](fig03_mounts_meridian_geometry).

```{figure} _static/_chapter03/fig03_meridian_geometry.png
:width: 50%
:align: center
:name: fig03_mounts_meridian_geometry

**Figure 3** Right ascension, hour angle, and sidereal time on the celestial sphere. The relation $\Theta=H+\alpha$ reduces to $\Theta=\alpha$ on the upper meridian.
```

The meridian altitude supplies declination. For an observer at latitude $\phi$, the ideal upper-transit altitude is

$$
\boxed{h_{\mathrm{upper}}=90^\circ-|\phi-\delta|}.
$$

The absolute value matters: a star may cross the meridian to either side of the zenith. One must know which side was observed to infer $\delta$ from $h$. The shortcut $h=\delta+\phi$ is not the general upper-transit relation. The formula above assumes the geometric horizon and ignores atmospheric refraction.[^transit_geometry]

The focal plane of a classical transit instrument contains a finely marked **reticle**. Timing the passage of the stellar image across its reference line is more precise than estimating the centre of an unmarked field. [Figure 4](fig04_mounts_meridian_instrument) shows such an instrument, while [Figure 5](fig05_mounts_specola) shows the meridian room at *La Specola* in Padova. There, a narrow opening gave the telescope a view along the meridian; the instrument could change its elevation while its observing plane remained fixed.

```{figure} _static/_chapter03/fig04_meridian_instrument.png
:width: 55%
:align: center
:name: fig04_mounts_meridian_instrument

**Figure 4** Meridian telescope with a mechanically constrained pointing direction.
```

```{figure} _static/_chapter03/fig05_specola_meridian_room.png
:width: 70%
:align: center
:name: fig05_mounts_specola

**Figure 5** Meridian room at *La Specola*, Padova. The opening in the wall defines the observing direction.
```

The same principle is not restricted to optical instruments. The **Northern Cross** radio telescope at Medicina, shown in [Figure 6](fig06_mounts_northern_cross), is a meridian radio instrument. Its large fixed structure gains collecting area and mechanical stability at the cost of access to only those directions that pass through its observing region as the sky turns.

```{figure} _static/_chapter03/fig06_northern_cross.png
:width: 80%
:align: center
:name: fig06_mounts_northern_cross

**Figure 6** Northern Cross radio telescope at Medicina.
```

## Altitude-azimuth mounts

An **altazimuthal mount** rotates about a vertical azimuth axis and a horizontal altitude axis. The first axis selects a direction around the horizon; the second lifts the line of sight toward the zenith. The axes remain naturally related to gravity, which makes the arrangement mechanically straightforward ([Figure 7](fig07_mounts_types)). Telescopes as different as a small amateur instrument and a large observatory telescope can use this geometry.

```{figure} _static/_chapter03/fig07_mount_types.png
:width: 80%
:align: center
:name: fig07_mounts_types

**Figure 7** Comparison of an altitude-azimuth mount, a Dobsonian arrangement, and an equatorial mount.
```

For a target with fixed $\alpha$ and $\delta$, both $A$ and $h$ generally change during the night. Their tracking rates are not constant. A controller must evaluate the target's horizontal coordinates at the observing site and time, then drive both axes continuously. Modern electronics make this routine, although the mechanical speeds and accelerations still constrain observations near the zenith.[^mount_sources]

### The Dobsonian arrangement

The **Dobsonian mount** is a simple altazimuthal support, usually built as a low, rigid base carrying a large reflecting telescope. Its large bearings and simple structure permit substantial apertures at relatively low cost. Such telescopes can be large, portable, and home-built apart from the demanding optical work of making or obtaining the mirror ([Figure 8](fig08_mounts_dobsonian)).

```{figure} _static/_chapter03/fig08_dobsonian.png
:width: 55%
:align: center
:name: fig08_mounts_dobsonian

**Figure 8** A portable Dobsonian reflecting telescope.
```

A manually moved Dobsonian does not provide the continuous two-axis tracking or the field counter-rotation required for straightforward long-exposure astrophotography. Equatorial platforms or motorised Dobsonian systems can provide tracking, so the limitation belongs to the basic manual arrangement, not to every telescope of this kind.[^mount_sources]

## Equatorial mounts

In an **equatorial mount**, the polar or hour-angle axis is aligned with the Earth's rotation axis. The second axis, perpendicular to it, sets declination. Once the telescope is pointed at a star, ideal sidereal tracking needs only a steady rotation of the polar axis at the rate of the apparent daily motion. The declination axis remains fixed during ideal tracking, although a real telescope may make small corrections. Different equatorial designs solve the engineering problem of supporting these two axes in different ways.

### German equatorial mount

The **German equatorial mount** places the telescope on one side of the declination axis and a counterweight on the other. The polar axis is inclined by the observer's latitude. This arrangement is familiar on amateur instruments, but it can also support an observatory telescope, as illustrated by the example from Hvar Observatory in Croatia ([Figure 9](fig09_mounts_german_hvar)). [Figure 10](fig10_mounts_german) makes the counterweighted geometry especially clear.

```{figure} _static/_chapter03/fig09_german_hvar.png
:width: 75%
:align: center
:name: fig09_mounts_german_hvar

**Figure 9** German equatorial telescope at Hvar Observatory, Croatia.
```

```{figure} _static/_chapter03/fig10_german_mount.png
:width: 45%
:align: center
:name: fig10_mounts_german

**Figure 10** Compact German equatorial mount showing the tube, polar axis, and counterweight.
```

The counterweight balances the torque of the telescope about the declination axis. On many German mounts, a target crossing the meridian eventually requires a **meridian flip**: the tube and counterweight exchange sides to avoid collision with the pier or mount. The exact accessible range depends on the instrument's mechanical clearances.

### Open fork mount

In an **open fork**, the telescope tube lies between two fork arms. The fork rotates about the polar axis, while the tube turns between the arms about the declination axis. This leaves one end of the telescope comparatively accessible and avoids the long external counterweight shaft of a German mount. The *Telescopio Copernico* at Cima Ekar, Asiago, illustrates this arrangement ([Figure 11](fig11_mounts_copernico)).

```{figure} _static/_chapter03/fig11_copernico_fork.png
:width: 55%
:align: center
:name: fig11_mounts_copernico

**Figure 11** The *Telescopio Copernico* at Cima Ekar, Asiago, mounted in an open equatorial fork.
```

### English or yoke mount

In an **English**, or **yoke**, mount the polar axis is supported at both ends of a long frame, and the telescope turns across the frame about its declination axis. The two supports provide stiffness for a heavy telescope, but the closed end of the yoke obstructs directions close to the celestial pole. The 2.5-m Hooker Telescope at Mount Wilson, California, is a historical example ([Figure 12](fig12_mounts_hooker)). Its pole obstruction is a property of this layout, not of all equatorial mounts.

```{figure} _static/_chapter03/fig12_hooker_yoke.png
:width: 70%
:align: center
:name: fig12_mounts_hooker

**Figure 12** Hooker Telescope at Mount Wilson in an English or yoke mount. The supporting frame limits access to the celestial pole.
```

### Horseshoe mount

A **horseshoe mount** opens one end of the yoke into a large curved bearing. The opening allows the telescope to point much closer to the celestial pole while preserving substantial support for the polar axis. The Mayall 4-m Telescope at Kitt Peak, Arizona, and NASA's MCAT telescope illustrate this design ([Figures 13](fig13_mounts_mayall) and [14](fig14_mounts_mcat)).

```{figure} _static/_chapter03/fig13_mayall_horseshoe.png
:width: 70%
:align: center
:name: fig13_mounts_mayall

**Figure 13** Mayall 4-m Telescope, Kitt Peak, illustrating a large equatorial horseshoe bearing.
```

```{figure} _static/_chapter03/fig14_mcat_horseshoe.png
:width: 40%
:align: center
:name: fig14_mounts_mcat

**Figure 14** NASA MCAT telescope, another horseshoe-mount example.
```

### Cross-axis mount

In a **cross-axis mount**, the polar axis is supported at both ends and the declination axis meets it near the middle. Loads are carried through a cross-shaped structure instead of a long unsupported arm. The *Telescopio Galileo* at Asiago illustrates this arrangement ([Figure 15](fig15_mounts_galileo)). The different geometries of the German, fork, yoke, horseshoe, and cross-axis designs all preserve the central equatorial idea: one axis is parallel to the Earth's spin axis.

```{figure} _static/_chapter03/fig15_galileo_cross_axis.png
:width: 70%
:align: center
:name: fig15_mounts_galileo

**Figure 15** *Telescopio Galileo* at Asiago, illustrating the cross-axis equatorial mount.
```

## Return to large altazimuthal telescopes

The *Telescopio Nazionale Galileo* (TNG) has the same two basic pointing axes as a Dobsonian, although it is a fully engineered observatory instrument with precision drives and field-rotation compensation ([Figure 16](fig16_mounts_tng)). Barbieri and Bertini describe its altitude and azimuth axes and the counter-rotation of the field at its Nasmyth focus.[^mount_sources]

```{figure} _static/_chapter03/fig16_tng_altaz.png
:width: 70%
:align: center
:name: fig16_mounts_tng

**Figure 16** The TNG altitude-azimuth structure. Its two principal axes are evident despite the much larger scale than the preceding Dobsonian example.
```

The Very Large Telescope (VLT) of the European Southern Observatory and the Gran Telescopio Canarias (GTC) continue the same design line ([Figures 17](fig17_mounts_vlt) and [18](fig18_mounts_gtc)). Their size makes the structural advantages of keeping one axis vertical and the other horizontal especially important. This geometry can use compact load paths and a more economical enclosure than a comparable, large inclined equatorial structure. The benefit is an engineering tendency, rather than a theorem about every telescope building.

```{figure} _static/_chapter03/fig17_vlt_altaz.png
:width: 50%
:align: center
:name: fig17_mounts_vlt

**Figure 17** An ESO VLT unit telescope with a large altazimuthal mount.
```

```{figure} _static/_chapter03/fig18_gtc_altaz.png
:width: 65%
:align: center
:name: fig18_mounts_gtc

**Figure 18** The Gran Telescopio Canarias, another large altazimuthal telescope.
```

## Equatorial and altazimuthal mounts compared

The consequences of axis orientation provide a basis for comparing the two designs. Neither mount is universally best: the choice depends on aperture, stiffness, enclosure, tracking, instrumentation, and cost.

### Pointing and tracking

An equatorial mount is naturally parameterised by hour angle and declination. After a target is acquired, ideal sidereal tracking requires the polar axis to move steadily. An altazimuthal mount requires the current $A$ and $h$ for every target and continuously changing speeds on both axes. The transformation from $(\alpha,\delta)$ to $(A,h)$ was derived in {doc}`Chapter 2 <chapter02_transformation_of_coordinates>`; computers can perform it accurately, so the operational difference is in the required motion, not in any inability to calculate the pointing.

The curves in [Figure 19](fig19_mounts_tracking_rates) show that tracks at different distances from the zenith can demand very different horizontal-axis rates. The blue and green examples pass especially close to the zenith. There, azimuth becomes undefined: a tiny displacement on the sky can correspond to a very large change in $A$. For a track approaching arbitrarily close to the exact zenith, the required azimuth rate can grow without bound in the ideal coordinates; a real mount has finite speed and acceleration and therefore a **zenith avoidance region**. The star itself does not acquire an infinite angular velocity.[^zenith_geometry]

```{figure} _static/_chapter03/fig19_tracking_rates.png
:width: 100%
:align: center
:name: fig19_mounts_tracking_rates

**Figure 19** Horizontal-coordinate tracks and apparent angular rates for several targets. The polar panel is labelled with North-through-East azimuth; the rate argument also applies to the South-through-West convention.
```

### Rotation of the observed field

An ideal equatorial mount rotates with the celestial sphere. If its polar alignment and tracking are accurate, the orientation of the stellar field remains fixed relative to the camera during an exposure ([Figure 20](fig20_mounts_equatorial_field)). An altazimuthal mount can hold the *centre* of the field on target while the surrounding stars rotate about that centre relative to a detector rigidly attached to the telescope ([Figure 21](fig21_mounts_altaz_field)). Long exposures therefore require an instrument or field rotator, or a later combination of suitably short exposures. Tracking both axes alone does not remove field rotation.[^mount_sources]

```{figure} _static/_chapter03/fig20_equatorial_field.png
:width: 90%
:align: center
:name: fig20_mounts_equatorial_field

**Figure 20** Successive fields carried by an equatorial mount: the detector orientation follows the sky.
```

```{figure} _static/_chapter03/fig21_altaz_field.png
:width: 90%
:align: center
:name: fig21_mounts_altaz_field

**Figure 21** Successive fields on an altazimuthal mount: the detector frame remains tied to altitude and azimuth while the stellar pattern rotates.
```

The changing field orientation can be described by the **parallactic angle** $q$, the angle at the target between the great circles toward the celestial pole and toward the zenith. With hour angle positive westward, one convenient expression is

$$
q=\operatorname{atan2}\!\left(\sin H,\,\tan\phi\cos\delta-\sin\delta\cos H\right).
$$

The required counter-rotation rate is the negative of the field's rate, $-\dot q$, for this choice of angle sense. The formula also shows why the precise centre of the zenith region needs special care: the direction toward the zenith is not defined when the target itself is at the zenith. In practice, the instrument rotator is coordinated with both pointing axes.

### Structures, domes, and scale

As the aperture increases, the mass of the mirrors, tube, support structure, and instruments grows. An equatorial mount must support and turn a large structure about an inclined polar axis. An altazimuthal mount distributes loads around vertical and horizontal bearings, which is generally easier to make stiff at great size. The *Telescopio Galileo* at Asiago and the much larger GTC illustrate this difference in scale ([Figure 22](fig22_mounts_gtc_dome)). Altazimuthal structures can also permit relatively compact enclosures.

```{figure} _static/_chapter03/fig22_gtc_dome.png
:width: 50%
:align: center
:name: fig22_mounts_gtc_dome

**Figure 22** The GTC inside its dome. Mount geometry affects the size and shape of the surrounding enclosure.
```

There is **no physical aperture limit** near 2.5 m for an equatorial mount: the Mayall Telescope in [Figure 13](fig13_mounts_mayall) has a 4-m mirror and an equatorial horseshoe mount. Altazimuthal mounting nevertheless becomes increasingly attractive as aperture and structural mass increase. The table summarises the comparison.

| Aspect | Equatorial mount | Altazimuthal mount |
| --- | --- | --- |
| Principal axes | Polar/hour axis and declination axis | Azimuth and altitude axes |
| Ideal sidereal tracking | Mainly one axis at nearly constant rate | Both axes at time-dependent rates |
| Near the celestial pole or zenith | Access depends on equatorial design; a closed yoke has a pole obstruction | Azimuth is singular at the zenith; finite drives impose an avoidance region |
| Stellar field during tracking | Approximately fixed relative to the instrument | Rotates unless compensated |
| Very large structures | Inclined axis and support become demanding | Vertical and horizontal bearings are generally easier to scale |

## The Giant Magellan Telescope and the Extremely Large Telescope

Two extremely large observatories show where mount design and mirror technology meet. The **Giant Magellan Telescope** (GMT) uses seven circular primary-mirror segments, each 8.4 m in diameter, arranged across a 25.4-m span. [Figure 24](fig24_mounts_gmt_mirrors) shows the distinctive seven-mirror pattern. The **Extremely Large Telescope** (ELT) of ESO uses a 39-m segmented primary mirror comprising 798 segments ([Figures 23](fig23_mounts_elt_concept) and [25](fig25_mounts_elt_mirror_segments)). Both projects use altitude-azimuth mounting: supporting and moving an inclined equatorial assembly of this size would be exceptionally difficult.[^large_telescopes]

```{figure} _static/_chapter03/fig23_elt_concept.png
:width: 75%
:align: center
:name: fig23_mounts_elt_concept

**Figure 23** Design rendering of ESO's ELT and its enclosure.
```

```{figure} _static/_chapter03/fig24_gmt_mirrors.png
:width: 55%
:align: center
:name: fig24_mounts_gmt_mirrors

**Figure 24** The seven primary mirrors of the GMT.
```

```{figure} _static/_chapter03/fig25_elt_mirror_segments.png
:width: 85%
:align: center
:name: fig25_mounts_elt_mirror_segments

**Figure 25** Full-scale layout conveying the number and arrangement of the ELT primary-mirror segments.
```

Mirror segmentation solves a different problem from the mount: it permits a collecting surface larger than a single practical monolithic mirror. Each segment must be supported and kept aligned so that the primary acts as one optical system. The mount must then carry this mirror assembly, the secondary optics, and the instruments while tracking precisely. Thus optical design, active support, and mechanical mounting have to be designed together.[^large_telescopes]

### Construction at Cerro Armazones

The photographs trace construction at the ELT site on Cerro Armazones, Chile. They begin with summit preparation and foundation work ([Figures 26](fig26_mounts_elt_site_preparation)–[28](fig28_mounts_elt_civil_works)), then show the rising telescope structure and dome ([Figures 29](fig29_mounts_elt_structure)–[31](fig31_mounts_elt_site_later)). They make the engineering scale tangible: an altazimuthal telescope of this size is a building-sized moving structure, not simply a larger version of the small mount in [Figure 7](fig07_mounts_types).

```{figure} _static/_chapter03/fig26_elt_site_preparation.png
:width: 65%
:align: center
:name: fig26_mounts_elt_site_preparation

**Figure 26** Early summit preparation at the ELT site.
```

```{figure} _static/_chapter03/fig27_elt_foundations.png
:width: 55%
:align: center
:name: fig27_mounts_elt_foundations

**Figure 27** The circular foundations and site works at Cerro Armazones.
```

```{figure} _static/_chapter03/fig28_elt_civil_works.png
:width: 75%
:align: center
:name: fig28_mounts_elt_civil_works

**Figure 28** Later civil works at Cerro Armazones.
```

```{figure} _static/_chapter03/fig29_elt_structure.png
:width: 75%
:align: center
:name: fig29_mounts_elt_structure

**Figure 29** The ELT dome structure taking shape.
```

```{figure} _static/_chapter03/fig30_elt_dome.png
:width: 75%
:align: center
:name: fig30_mounts_elt_dome

**Figure 30** A later view inside the partly completed ELT enclosure.
```

```{figure} _static/_chapter03/fig31_elt_site_later.png
:width: 75%
:align: center
:name: fig31_mounts_elt_site_later

**Figure 31** The developing ELT enclosure at Cerro Armazones.
```

ESO dates the blasting of the summit to June 2014. Its current project schedule lists telescope test observations in 2029 and first scientific observations with instruments in December 2030; these are **planned milestones**, not completed events.[^elt_schedule]

A LEGO model of the ELT ([Figure 32](fig32_mounts_lego_elt)) is a useful reminder that a mount is a geometric construction as well as a system of motors. Even at model scale, one can identify the vertical azimuth axis, the altitude-bearing arrangement, and the enclosure surrounding the moving telescope.

```{figure} _static/_chapter03/fig32_lego_elt.png
:width: 75%
:align: center
:name: fig32_mounts_lego_elt

**Figure 32** LEGO model of the ELT, showing the principal moving structure and its enclosure.
```

## References

The scientific explanations and technical details were checked against these sources:

- **Barbieri, C., and Bertini, I. (2021)**, *Fundamentals of Astronomy*, second edition, Section 2.4, “Telescope Mounts.”
- **Karttunen, H., Kröger, P., Oja, H., Poutanen, M., and Donner, K. J. (eds., 2017)**, *Fundamental Astronomy*, sixth edition, Chapter 3, “Mountings of Telescopes.”
- **Giant Magellan Telescope**, [Primary Mirrors](https://giantmagellan.org/telescope-primary-mirrors/), for the seven-mirror design.
- **ESO**, [Facts about the ELT](https://elt.eso.org/about/facts/), [project timeline](https://elt.eso.org/about/timeline/), and [The Road to the ELT](https://elt.eso.org/about/road/), for mirror dimensions, the planned schedule, and site history.

[^mount_sources]: Barbieri and Bertini (2021), Section 2.4; Karttunen et al. (2017), Chapter 3, “Mountings of Telescopes.” These sources distinguish the one-axis sidereal tracking of equatorial mounts from the two varying axis rates and field rotation of altazimuthal mounts.

[^transit_geometry]: The altitude follows from the angular separation $|\phi-\delta|$ between the zenith and the star at upper culmination. See the spherical-astronomy relations in {doc}`Chapter 2 <chapter02_transformation_of_coordinates>`.

[^zenith_geometry]: See the discussion of horizontal angular velocities and the zenith singularity in {doc}`Chapter 2 <chapter02_transformation_of_coordinates>`. The divergence concerns azimuth coordinates and drive requirements, not the physical speed of the star.

[^large_telescopes]: [GMT primary-mirror description](https://giantmagellan.org/telescope-primary-mirrors/) and [ESO ELT facts](https://elt.eso.org/about/facts/). The stated 25.4-m GMT span is the diameter of the segment arrangement, not the diameter of a filled circular mirror.

[^elt_schedule]: [ESO project timeline](https://elt.eso.org/about/timeline/) and [ESO history](https://elt.eso.org/about/road/), consulted in October 2026. The schedule is a project plan and can change.
