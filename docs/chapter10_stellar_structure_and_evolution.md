(chapter10_stellar_structure_and_evolution)=

# Stellar Structure and Evolution

:::{danger}
This page still needs substantial revision to match the content presented during the lectures
:::

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

A star's spectrum and position in the Hertzsprung–Russell (HR) diagram tell us about its surface. To explain how that position changes, we need a model of the interior. We start from the balance between gravity and pressure and ask how a star supplies the energy that escapes from its surface. We then follow stars from molecular clouds to the main sequence, through central and shell burning, and finally to their remnants.

## The structure of a star

In the simplest model, a star is a self-gravitating sphere whose density $\rho$, pressure $P$, temperature $T$, and composition depend only on the distance $r$ from the centre. Spherical symmetry is a useful starting point when rotation and magnetic stresses are small. A model for a given stage can also hold the mass fixed if wind loss is negligible on the timescale of interest. The Sun illustrates the distinction between the energy-generating core, the overlying layers that transport the energy, and the atmosphere from which radiation escapes.[^ch10_structure]

```{figure} _static/_chapter10/fig01_solar_structure.png
:width: 88%
:align: center
:name: fig_ch10_solar_structure
:alt: Cutaway of the Sun showing the core, the radiative interior, and the convective envelope

**Figure 1** Cutaway of the Sun showing the core, the radiative interior, and the convective envelope. The photosphere is the visible surface, with the chromosphere and corona above it.
```

### What are stars made of?

Astronomers describe the bulk composition by the mass fractions $X$ of hydrogen, $Y$ of helium, and $Z$ of all heavier elements, with $X+Y+Z=1$. Roughly three quarters hydrogen and one quarter helium is a first approximation for hydrogen-rich material. The fractions vary with the composition of the parent gas and change locally when nuclear reactions consume fuel. A carbon–oxygen white dwarf and a neutron star illustrate how different the composition of a remnant can be from that of its progenitor. Unusual surface abundances can also occur in stars that are still burning hydrogen. For scale, the Sun has about $109.2$ Earth radii and $333\,000$ Earth masses.[^ch10_composition]

```{figure} _static/_chapter10/fig02_stellar_sizes.png
:width: 69%
:align: center
:name: fig_ch10_stellar_sizes
:alt: Relative sizes of main-sequence stars and cool evolved stars

**Figure 2** Relative sizes of main-sequence stars and cool evolved stars. The Sun and Earth provide a scale at the small end of the comparison.
```

### Hydrostatic equilibrium

Consider a thin spherical shell. The gravitational acceleration has magnitude $Gm(r)/r^2$, where $m(r)$ is the mass enclosed by the shell. Pressure acts on both faces. The outward force per unit volume is $-\mathrm{d}P/\mathrm{d}r$, because the pressure is greater on the inner face. With zero radial acceleration, the local equations are

$$
\boxed{\frac{\mathrm{d}P}{\mathrm{d}r}=-\frac{Gm(r)\rho(r)}{r^2}},
\qquad
\frac{\mathrm{d}m}{\mathrm{d}r}=4\pi r^2\rho(r).
$$

The second equation gives the mass in a shell of thickness $\mathrm{d}r$. The pressure in the first equation is the total pressure. Thermal motions of ions and electrons supply most of it in the Sun. Radiation pressure can matter in massive stars, and electron degeneracy pressure becomes important in dense cores. Hydrostatic equilibrium is a statement about forces at a given time. A star can pass through a succession of nearly hydrostatic states while contracting or expanding slowly.

```{figure} _static/_chapter10/fig03_hydrostatic.png
:width: 54%
:align: center
:name: fig_ch10_hydrostatic
:alt: The inward gravitational force on a fluid element is balanced by the outward force from the pressure gradient.

**Figure 3** The inward gravitational force on a fluid element is balanced by the outward force from the pressure gradient.
```

### Stellar energy sources and timescales

The **free-fall time** of a uniform, initially stationary sphere of mean density $\bar\rho$ is

$$
t_{\rm ff}=\left(\frac{3\pi}{32G\bar\rho}\right)^{1/2}.
$$

For the mean solar density this gives about $1\,800\ \mathrm{s}$, or half an hour. It estimates the timescale of a dynamical response if pressure support were removed. For a centrally concentrated star the collapse time can vary among shells.

A star that radiates without a sustained nuclear source can draw energy from contraction. The **Kelvin–Helmholtz time** compares the gravitational energy scale with the luminosity,

$$
t_{\rm KH}\sim\frac{GM^2}{RL}
\quad\Longrightarrow\quad
t_{{\rm KH},\odot}\sim 3\times10^7\ \mathrm{yr}.
$$

The density profile and the fraction of the released energy that heats the gas enter the coefficient. Chemical reactions yield far too little energy to account for the Sun's age, and the inventory of radioactive nuclei cannot sustain the observed solar luminosity.

Converting hydrogen to helium releases about $0.007$ of the original hydrogen rest-mass energy. Burning a mass $fM$ of hydrogen at a representative luminosity $L$ gives

$$
t_{\rm nuc}\sim\frac{0.007 fMc^2}{L}.
$$

:::{note}
With $f=1$ this gives an energy-budget scale of order $10^{11}\ \mathrm{yr}$ for the Sun. Only a fraction of the star's mass is available as hydrogen fuel in its central burning region. With an effective $f\sim0.1$, the estimate is of order $10^{10}\ \mathrm{yr}$. Nuclear energy maintains the thermal budget as radiation escapes. Hydrostatic balance itself follows from the pressure gradient.
:::

### Thermonuclear fusion

A nucleus of $Z$ protons and $N$ neutrons has mass number $A=Z+N$. For nucleus mass $m(Z,N)$, the **mass defect** and the **binding energy per nucleon** are

$$
\Delta m=Zm_p+Nm_n-m(Z,N),
\qquad
\frac{B}{A}=\frac{\Delta m\,c^2}{A}.
$$

The mass defect has units of mass, $B$ has units of energy, and $B/A$ is an energy per nucleon. Here $Z$ is the nuclear charge number, distinct from the symbol $Z$ for the stellar metal mass fraction. Fusion of light nuclei into more tightly bound nuclei releases energy. At temperatures of millions of kelvins, nuclei have a distribution of kinetic energies. A small fraction of encounters can reach nuclear distances by quantum tunnelling through the Coulomb barrier. The steep dependence of the reaction rate on $T$ follows in part from this barrier.[^ch10_fusion]

```{figure} _static/_chapter10/fig04_binding_energy.png
:width: 83%
:align: center
:name: fig_ch10_binding_energy
:alt: Binding energy per nucleon rises steeply among the light nuclei, peaks in the iron-group region, and declines gradually towards very heavy nuclei.

**Figure 4** Binding energy per nucleon rises steeply among the light nuclei, peaks in the iron-group region, and declines gradually towards very heavy nuclei.
```

### Energy transport

**Radiation** carries energy by diffusion in the opaque interior. Photons are repeatedly absorbed or scattered, with a net flux towards cooler layers. At a given flux, greater opacity requires a steeper temperature gradient. For a layer of uniform composition, convection sets in when the gradient required for radiative transport exceeds the adiabatic gradient, $\nabla_{\rm rad}>\nabla_{\rm ad}$, with $\nabla=\mathrm{d}\ln T/\mathrm{d}\ln P$. An upwardly displaced parcel then stays warmer and less dense than its surroundings and keeps rising. **Convection** transports energy with moving material and mixes the composition where the flow reaches. **Conduction** is usually weak in ordinary stellar gas. It is important in dense, electron-degenerate material, such as a white-dwarf interior.[^ch10_transport]

```{figure} _static/_chapter10/fig05_energy_transport.png
:width: 73%
:align: center
:name: fig_ch10_energy_transport
:alt: Familiar examples of convection in a heated fluid, conduction through a solid, and radiation from a hot source

**Figure 5** Familiar examples of convection in a heated fluid, conduction through a solid, and radiation from a hot source. In an opaque stellar interior the radiative flux is diffusive.
```

In the Sun most energy generation is concentrated in the core. Radiation transports energy across the core and the surrounding radiative interior up to about $0.71R_\odot$. Convection dominates outside that boundary until close to the surface. The extent and location of convective regions change with stellar mass and evolutionary stage.

### Evolutionary tracks and isochrones

An **evolutionary track** follows one model, of specified initial mass and composition, through time in the HR diagram. An **isochrone** joins models of different initial masses at a fixed age and composition. The former describes how one star changes. The latter predicts where a coeval population such as a star cluster should lie. Temperature increases to the left in the HR diagrams used here.[^ch10_tracks]

```{figure} _static/_chapter10/fig06_tracks_isochrones.png
:width: 56%
:align: center
:name: fig_ch10_tracks_isochrones
:alt: Evolutionary tracks (blue) follow individual masses towards the main sequence

**Figure 6** Evolutionary tracks (blue) follow individual masses towards the main sequence. Isochrones (red) connect different masses at the indicated ages.
```

The **Vogt–Russell theorem** is a useful guide to model construction. For a spherical, hydrostatic and thermally equilibrated star, the mass and interior composition profile strongly constrain the structure once the microphysics and boundary conditions have been specified. The stellar structure equations admit exceptions to uniqueness. Evolution also changes the composition profile, and rotation, magnetic fields, winds, and mixing can affect the result. A grid of tracks must therefore specify the physical assumptions used to calculate it.

## Pre-main-sequence evolution

### Stellar nurseries

A **molecular cloud** is a cold component of the interstellar medium. Its hydrogen is largely molecular ($\mathrm{H}_2$), and its gas contains other species such as CO as well as solid dust grains. Shielded gas often has temperatures of $10$–$20\ \mathrm{K}$. Number densities vary from hundreds of particles per cubic centimetre in extended gas to $10^4$–$10^6\ \mathrm{cm^{-3}}$ in dense cores. Even $10^6\ \mathrm{cm^{-3}}$ is about thirteen orders of magnitude below the density of terrestrial air near sea level, $2.5\times10^{19}\ \mathrm{cm^{-3}}$. Dust obscures background light and emits at infrared and longer wavelengths. Cold molecular gas is often mapped with millimetre CO lines, because cold $\mathrm{H}_2$ radiates weakly. A cloud can also be seen by its silhouette at visible wavelengths.[^ch10_clouds]

```{figure} _static/_chapter10/fig07_stellar_nurseries.png
:width: 83%
:align: center
:name: fig_ch10_stellar_nurseries
:alt: Molecular clouds in visible light

**Figure 7** Molecular clouds in visible light. A dark pillar in the Horsehead Nebula (left) appears in silhouette, while in the region on the right dust scatters starlight and obscures the background.
```

The **Pillars of Creation** in the Eagle Nebula (M16) show how the information changes with wavelength. In the Hubble visible-light image the denser columns are silhouetted against glowing gas. Webb's **Near-Infrared Camera** (NIRCam) reveals many more stars through the surrounding dust and some of the embedded young sources. The **Mid-Infrared Instrument** (MIRI) emphasises different dust structures and shows fewer of the ordinary stars that are prominent in the near infrared. Dense clumps can remain opaque even in infrared images.[^ch10_pillars]

```{figure} _static/_chapter10/fig08_pillars_hubble_nircam.png
:width: 94%
:align: center
:name: fig_ch10_pillars_hubble_nircam
:alt: Pillars of Creation in visible light with Hubble (left) and in the near infrared with Webb/NIRCam (right)

**Figure 8** Pillars of Creation in visible light with Hubble (left) and in the near infrared with Webb/NIRCam (right). Credit NASA, ESA, CSA, and STScI. [NASA comparison](https://science.nasa.gov/mission/webb/star-lifecycle/).
```

```{figure} _static/_chapter10/fig09_pillars_miri_nircam.png
:width: 94%
:align: center
:name: fig_ch10_pillars_miri_nircam
:alt: Webb views of the Pillars of Creation with MIRI (left) and NIRCam (right)

**Figure 9** Webb views of the Pillars of Creation with MIRI (left) and NIRCam (right). Credit NASA, ESA, CSA, and STScI. [NASA image record](https://science.nasa.gov/asset/webb/pillars-of-creation-nircam-and-miri-composite-image/).
```

### The distribution of molecular clouds

In the Milky Way, most molecular material lies in a thin layer near the Galactic plane. Spiral arms host many large cloud complexes, and molecular material is also present between the arms and in the central Galaxy. Maps across the electromagnetic spectrum trace different parts of the interstellar medium. **Planck** surveyed the full sky in nine bands with nominal centres between $30$ and $857\ \mathrm{GHz}$ (about $10$ to $0.35\ \mathrm{mm}$). **Herschel** mapped cold dust in the far infrared and submillimetre, while **Spitzer** probed warm dust and embedded sources in the infrared. The terrestrial **Atacama Large Millimeter/submillimeter Array** (ALMA) resolves individual clouds and disks with an interferometer. Its receiver bands collectively span approximately $35$–$950\ \mathrm{GHz}$ ($8.6$–$0.32\ \mathrm{mm}$), with gaps between bands. The interval $84$–$950\ \mathrm{GHz}$ starts at Band 3.[^ch10_surveys]

```{figure} _static/_chapter10/fig10_planck_sky.png
:width: 83%
:align: center
:name: fig_ch10_planck_sky
:alt: Planck all-sky image in Galactic coordinates

**Figure 10** Planck all-sky image in Galactic coordinates. Bright emission along the Galactic plane includes dust in the interstellar medium. Credit ESA.
```

```{figure} _static/_chapter10/fig11_alma_array.png
:width: 78%
:align: center
:name: fig_ch10_alma_array
:alt: ALMA antennas on the Chajnantor plateau

**Figure 11** ALMA antennas on the Chajnantor plateau. The array synthesises an aperture from the separations between antennas.
```

### Perturbations and the formation of protostars

Giant molecular clouds can extend over tens to more than a hundred parsecs. The illustrative span of $600$ light years corresponds to about $184\ \mathrm{pc}$. The mass range is broad and includes complexes of $10^5$–$10^6M_\odot$ and above. Comparing clouds with young populations suggests lifetimes of order tens of millions of years in many environments. A cloud's position near a spiral arm alone gives no unique lifetime. Turbulence, converging flows, or compression by nearby stars may produce overdensities. A sufficiently self-gravitating region collapses when pressure, turbulence, and other support fail to counter gravity. A compact, isolated dusty cloud appears as a **Bok globule** against a bright background. **Dark nebula** is an observational description for clouds seen in extinction and covers a wide range of masses.

```{figure} _static/_chapter10/fig12_dark_clouds.png
:width: 94%
:align: center
:name: fig_ch10_dark_clouds
:alt: A compact Bok globule silhouetted against bright gas (left) and a more extended dark nebula that obscures background stars (right).

**Figure 12** A compact Bok globule silhouetted against bright gas (left) and a more extended dark nebula that obscures background stars (right).
```

Early in collapse, radiation can remove much of the compressional heat, so the gas remains approximately isothermal. Where gravity dominates, infall approaches free fall. As the centre grows opaque to its cooling radiation, heat raises the temperature and pressure and a first hydrostatic core can form. In a typical low-mass collapse, dissociation of $\mathrm{H}_2$ then absorbs energy and triggers a second collapse. The compact central object that forms accretes material while the outer envelope continues to fall. Subsequent contraction can supply luminosity on the Kelvin–Helmholtz timescale. Deuterium burning can occur before sustained hydrogen burning, and lithium is destroyed in layers that attain sufficiently high temperatures.

:::{note}
The change from roughly $100\ \mathrm{au}$ to $0.3\ \mathrm{au}$ illustrates the scale change from a collapsing inner cloud to a compact, pressure-supported region. The photospheric radius of an accreting protostar depends on its mass, accretion history, and evolutionary stage.
:::

```{figure} _static/_chapter10/fig13_collapse_protostar.png
:width: 88%
:align: center
:name: fig_ch10_collapse_protostar
:alt: Stages of collapse from left to right

**Figure 13** Stages of collapse from left to right. Infall initially reaches small radii, the central region becomes pressure-supported, and an accreting protostar forms while the surrounding gas continues to fall in.
```

### Protoplanetary disks

A cloud core generally has some initial angular momentum. As a parcel moves inwards, approximate conservation of its specific angular momentum increases its rotational speed. Gas can dissipate energy in shocks and settle towards the plane perpendicular to the net angular momentum, forming an **accretion disk**. Further accretion requires outward transport of angular momentum or its removal in an outflow. Dust and gas remaining in the disk provide the material for planets.

```{figure} _static/_chapter10/fig14_disk_formation.png
:width: 72%
:align: center
:name: fig_ch10_disk_formation
:alt: A rotating cloud contracts and flattens

**Figure 14** A rotating cloud contracts and flattens. Infall more nearly parallel to the rotation axis can reach smaller radii than material with substantial angular momentum.
```

The infrared spectral energy distribution helps classify **young stellar objects**. Embedded objects have strong long-wavelength emission from their envelopes (Classes 0 and I). Class II sources typically show excess emission from a disk and Class III sources have weak excesses. Inclination and extinction affect this observational classification. The underlying evolutionary picture is the gradual dispersal of the envelope and then of the disk.

```{figure} _static/_chapter10/fig15_young_stellar_classes.png
:width: 61%
:align: center
:name: fig_ch10_young_stellar_classes
:alt: Schematic sequence from a collapsing cloud core through an embedded protostar and a disk-bearing young star to disk dispersal

**Figure 15** Schematic sequence from a collapsing cloud core through an embedded protostar and a disk-bearing young star to disk dispersal. The spectra illustrate changes in the infrared excess.
```

### T Tauri stars and Herbig–Haro objects

**T Tauri stars** are young low-mass and some intermediate-mass pre-main-sequence stars, typically less than about $10\ \mathrm{Myr}$ old. The upper mass boundary depends on the convention. Many still accrete from a disk. Magnetic activity and changing accretion produce variability and emission lines in classical T Tauri stars. In this phase the star's luminosity can draw on contraction, accretion, and early light-element burning while the centre approaches sustained hydrogen fusion.

Magnetised rotating disks and young stars can launch collimated, bipolar jets roughly perpendicular to the disk. A **Herbig–Haro object** is a luminous shock knot where a jet encounters ambient material or where faster ejecta overtake slower ejecta. The knot changes as it propagates. The jet, the shock, and the wind-carved cavity probe different parts of the outflow.

```{figure} _static/_chapter10/fig16_protostellar_jets.png
:width: 94%
:align: center
:name: fig_ch10_protostellar_jets
:alt: A disk and bipolar jet, images showing changes in a young jet, and shock-excited Herbig–Haro structure

**Figure 16** A disk and bipolar jet, images showing changes in a young jet, and shock-excited Herbig–Haro structure. The Hubble/WFPC2 panels include changes in the HH 30 jet from 1995 to 2000 and views of HH 30, HH 34, and HH 47.
```

ALMA's image of **HL Tauri** resolves a different part of a young system. Bright rings and dark gaps show variations in the millimetre continuum from dust in its disk.

```{figure} _static/_chapter10/fig17_hl_tau.png
:width: 39%
:align: center
:name: fig_ch10_hl_tau
:alt: Dust emission from the HL Tauri protoplanetary disk

**Figure 17** Dust emission from the HL Tauri protoplanetary disk. Credit ALMA (ESO, NAOJ, NRAO). [ALMA image record](https://www.almaobservatory.org/en/press-releases/revolutionary-alma-image-reveals-planetary-genesis/).
```


## Main-sequence evolution

### The onset of sustained hydrogen burning

A star reaches the **zero-age main sequence** (ZAMS) when sustained hydrogen fusion in its centre supplies essentially its luminosity. It reaches the **terminal-age main sequence** (TAMS) when central hydrogen is nearly exhausted. Its luminosity and effective temperature can change appreciably between the two points. For hydrogen-rich compositions, the lower mass limit is about $0.075$–$0.08M_\odot$. Below it, electron degeneracy limits the rise in temperature during contraction, and the object cools as a **brown dwarf**. Deuterium can burn transiently above a representative threshold of $13$ Jupiter masses ($\simeq0.012M_\odot$). The precise threshold depends on composition and on how much deuterium is required to burn.[^ch10_main_sequence]

```{figure} _static/_chapter10/fig18_zams_tams.png
:width: 52%
:align: center
:name: fig_ch10_zams_tams
:alt: Zero-age and terminal-age main-sequence loci on a colour–magnitude diagram

**Figure 18** Zero-age and terminal-age main-sequence loci on a colour–magnitude diagram. Tracks between the two loci show how individual stellar models change during central hydrogen burning.
```

:::{note}
A mass of $120M_\odot$ is a useful upper entry for a model grid. Stars of about $150M_\odot$ and above have been inferred in young clusters. Radiation pressure and winds are central to their evolution, and the inferred masses depend on the adopted stellar and atmospheric models.[^ch10_upper_mass]
:::

### The proton–proton chain

The pp chain dominates hydrogen fusion in the Sun. Its first step involves a weak interaction that converts one of the protons into a neutron. A proton in the solar centre can undergo innumerable encounters before successfully participating in this step. The mean time for the initiating reaction is of order billions to ten billion years under solar-core conditions. The positron subsequently annihilates with an electron, ordinarily producing two photons. The emitted $\nu_e$ is an electron neutrino and can escape the star.[^ch10_pp]

The principal low-temperature branch, **pp I**, proceeds through

$$
\begin{aligned}
{}^1\mathrm H+{}^1\mathrm H&\longrightarrow{}^2\mathrm H+e^++\nu_e,\\
{}^2\mathrm H+{}^1\mathrm H&\longrightarrow{}^3\mathrm{He}+\gamma,\\
{}^3\mathrm{He}+{}^3\mathrm{He}&\longrightarrow{}^4\mathrm{He}+2\,{}^1\mathrm H.
\end{aligned}
$$

The first two reactions occur twice per completion of the pp I branch. The less common **pep** reaction, $p+e^-+p\rightarrow{}^2\mathrm H+\nu_e$, provides an alternative first step shared by the branches. Accounting for positrons and their annihilation, the net conversion of four hydrogen atoms into one helium atom releases about $26.7\ \mathrm{MeV}$, including the energy taken by neutrinos.

```{figure} _static/_chapter10/fig19_pp_chain.png
:width: 48%
:align: center
:name: fig_ch10_pp_chain
:alt: The pp I chain

**Figure 19** The pp I chain. Two paths make helium-3, and the final reaction combines the two helium-3 nuclei, returning two protons to the gas.
```

The other branches begin when $^3\mathrm{He}+{}^4\mathrm{He}\rightarrow{}^7\mathrm{Be}+\gamma$. Subsequent reactions distinguish **pp II** and **pp III**.

$$
\begin{aligned}
\text{pp II}\qquad{}^7\mathrm{Be}+e^-&\longrightarrow{}^7\mathrm{Li}+\nu_e,\\
{}^7\mathrm{Li}+{}^1\mathrm H&\longrightarrow 2\,{}^4\mathrm{He},\\[0.4em]
\text{pp III}\qquad{}^7\mathrm{Be}+{}^1\mathrm H&\longrightarrow{}^8\mathrm B+\gamma,\\
{}^8\mathrm B&\longrightarrow{}^8\mathrm{Be}^{*}+e^++\nu_e,\\
{}^8\mathrm{Be}^{*}&\longrightarrow 2\,{}^4\mathrm{He}.
\end{aligned}
$$

In the Sun, pp I accounts for most terminations, roughly nine in ten as an order-of-magnitude description. The fraction depends on the solar model and on whether one counts branch terminations or weights them by their heating of the star. The pp III contribution is very small, but its $^8\mathrm B$ decay produces neutrinos with energies extending to about $14\ \mathrm{MeV}$. The relative contribution of pp II and pp III increases with temperature. Textbook crossover temperatures such as $14$ and $23\ \mathrm{MK}$ depend on local composition, density, and reaction rates and refer to competition **within** the pp chain. The CNO cycle can supply most of the hydrogen-burning luminosity before pp III dominates the pp terminations.

### The CNO cycle

When the temperature is higher, hydrogen can fuse through a sequence involving carbon, nitrogen, and oxygen. Carl Friedrich von Weizsäcker and Hans Bethe developed early descriptions of this mechanism in the late 1930s. The pp reaction was also worked out in that period by Bethe and Charles Critchfield.[^ch10_cno]

$$
\begin{aligned}
{}^{12}\mathrm C+p&\longrightarrow{}^{13}\mathrm N+\gamma,\\
{}^{13}\mathrm N&\longrightarrow{}^{13}\mathrm C+e^++\nu_e,\\
{}^{13}\mathrm C+p&\longrightarrow{}^{14}\mathrm N+\gamma,\\
{}^{14}\mathrm N+p&\longrightarrow{}^{15}\mathrm O+\gamma,\\
{}^{15}\mathrm O&\longrightarrow{}^{15}\mathrm N+e^++\nu_e,\\
{}^{15}\mathrm N+p&\longrightarrow{}^{12}\mathrm C+{}^4\mathrm{He}.
\end{aligned}
$$

The carbon-12 nucleus is regenerated. The cycle as a whole converts four protons into a helium nucleus, with two positrons and two neutrinos among the products. The neutrinos carry off a larger fraction of the released energy than in the pp I branch. The relatively slow capture $^{14}\mathrm N(p,\gamma){}^{15}\mathrm O$ controls the pace of the cycle under main-sequence conditions. An illustrative reaction time of order $10^6\ \mathrm{yr}$ at $20\ \mathrm{MK}$ also assumes a representative proton density. The cycle's steep temperature dependence makes it competitive with pp burning near $18$–$20\ \mathrm{MK}$ for approximately solar composition. The crossover mass, around $1.3$–$1.5M_\odot$ in illustrative models, depends strongly on the abundance of CNO nuclei. In the Sun, **Borexino** measured neutrinos produced by the cycle, whose power contribution is of order one per cent.

:::{note}
The decay of $^{15}\mathrm O$ is a $\beta^+$ decay. A positron carries away the positive charge lost by the nucleus.
:::

```{figure} _static/_chapter10/fig20_cno_cycle.png
:width: 67%
:align: center
:name: fig_ch10_cno_cycle
:alt: The principal CNO cycle

**Figure 20** The principal CNO cycle. Nitrogen-13 and oxygen-15 decay by positron emission. The last step returns carbon-12 and releases an alpha particle.
```

```{figure} _static/_chapter10/fig21_borexino.png
:width: 48%
:align: center
:name: fig_ch10_borexino
:alt: The Gran Sasso massif in Italy

**Figure 21** The Gran Sasso massif in Italy. The Borexino experiment used a low-background liquid scintillator in the underground laboratories to detect electrons recoiling from interactions with solar neutrinos.
```

### Mass, luminosity, and effective temperature

A rough scaling follows from hydrostatic equilibrium. For gas pressure support, $P_{\rm c}/\rho_{\rm c}$ scales as $GM/R$. Via the ideal-gas law this sets a scale $k_{\rm B}T_{\rm c}\sim \mu m_{\rm u}GM/R$, where $\mu$ is the mean molecular weight in units of the atomic mass unit $m_{\rm u}$. The coefficients depend on structure, and radiation pressure becomes significant in massive stars. Along the main sequence, central temperatures generally rise with mass, making nuclear energy generation more effective. The star adjusts its structure so that, in thermal equilibrium, the energy released and retained from fusion supplies its surface luminosity. With $L=4\pi R^2\sigma T_{\rm eff}^4$, the larger luminosities of massive main-sequence stars are accompanied by larger radii and higher effective temperatures. Their radii grow enough that their mean densities are generally smaller than those of low-mass dwarfs. The trend can be followed along the sequence from $0.1$ and $0.3M_\odot$, through $1$ and $2M_\odot$, to $6$ and $10M_\odot$ in representative models.

```{figure} _static/_chapter10/fig22_mass_temperature_hr.png
:width: 59%
:align: center
:name: fig_ch10_mass_temperature_hr
:alt: Main-sequence positions for several masses

**Figure 22** A Hertzsprung–Russell diagram with the main sequence and several named stars. The upper-left portion contains the hotter and more luminous stars.
```

A useful piecewise approximation is $L/L_\odot\simeq b(M/M_\odot)^a$. The coefficients describe broad ranges and give only approximate luminosities for individual stars.

| Mass range in $M_\odot$ | $b$ | $a$ |
| --- | ---: | ---: |
| Below $0.43$ | $0.23$ | $2.3$ |
| Approximately $0.43$ to $2$ | $1.0$ | $4.0$ |
| Approximately $2$ to $55$ | $1.4$ | $3.5$ |

The intervals meet at approximate transition masses. The relation varies with age and composition and should only be applied in the intended main-sequence regime. As a first estimate of the lifetime, $t_{\rm MS}\propto fM/L$. Using $L\propto M^{3.5}$ and holding the effective fuel fraction fixed would give $t_{\rm MS}\propto M^{-2.5}$. The fuel fraction itself depends on the size and mixing of the burning region.

### Internal structure and lifetime along the main sequence

**Higher masses.** CNO burning is concentrated in a small central region, so the luminosity carried per unit mass there is high. The radiative temperature gradient can exceed the adiabatic gradient, giving a **convective core** and a mostly radiative envelope. Convection mixes hydrogen through the core more rapidly than fusion consumes it. The radiative envelope supplies fuel much less efficiently, although overshooting, rotation, and other mixing processes can extend the mixed region. In the mass coordinate $m(r)/M$, the centre is $0$ and the surface is $1$. The horizontal portions of the hydrogen profiles show the mixed central material. The profile just outside the core records how the extent of mixing has evolved.

```{figure} _static/_chapter10/fig23_pp_cno_rates.png
:width: 70%
:align: center
:name: fig_ch10_pp_cno_rates
:alt: Hydrogen-burning energy generation rises with temperature for both pp and CNO burning

**Figure 23** Hydrogen-burning energy generation rises with temperature for both pp and CNO burning. The CNO curve is steeper. The crossover is specific to the composition and density used for these curves.
```

```{figure} _static/_chapter10/fig24_massive_hydrogen_profile.png
:width: 68%
:align: center
:name: fig_ch10_massive_hydrogen_profile
:alt: Hydrogen mass fraction in a 5M_odot model as a function of enclosed mass fraction

**Figure 24** Hydrogen mass fraction in a $5M_\odot$ model as a function of enclosed mass fraction. The numbered profiles progress from the ZAMS to central hydrogen exhaustion. The nearly flat central segment is mixed by convection.
```

The following examples give the scale of hydrogen-burning lifetimes. The spectral types and numerical lifetimes are indicative model values.

| Mass ($M_\odot$) | Main-sequence lifetime | Representative spectral type |
| ---: | ---: | :--- |
| $60$ | $3\ \mathrm{Myr}$ | O3 |
| $30$ | $11\ \mathrm{Myr}$ | O7 |
| $10$ | $32\ \mathrm{Myr}$ | B4 |
| $3$ | $370\ \mathrm{Myr}$ | A5 |
| $1.5$ | $3\ \mathrm{Gyr}$ | F5 |

**Sun-like stars.** With the weaker temperature sensitivity of the pp reactions, energy production extends over a broader central region. The centre can transport the energy radiatively, while higher opacity and partial ionization favour convection in the cool envelope. In a one-solar-mass model the radiative centre develops a smooth hydrogen gradient because there is no large convectively mixed core. The Sun is about $4.6\ \mathrm{Gyr}$ old, roughly halfway through an expected main-sequence lifetime of about $10\ \mathrm{Gyr}$.

```{figure} _static/_chapter10/fig25_solar_hydrogen_profiles.png
:width: 87%
:align: center
:name: fig_ch10_solar_hydrogen_profiles
:alt: Comparison of the hydrogen abundance profiles of 1M_odot (left) and 5M_odot (right) models

**Figure 25** Comparison of the hydrogen abundance profiles of $1M_\odot$ (left) and $5M_\odot$ (right) models. The horizontal coordinate is enclosed mass in units of each star's total mass.
```

**The lowest masses.** For representative compositions, stars below about $0.35M_\odot$ are fully convective on the ZAMS. Cool, opaque material favours convection, which mixes a large fraction of the stellar hydrogen into the burning region. Their weak pp burning and small luminosity allow lifetimes of hundreds of billions to trillions of years. The Universe is about $13.8\ \mathrm{Gyr}$ old, so even very early examples of these long-lived stars can still be on the main sequence. Such stars are also abundant at birth. An **initial mass function** gives the distribution of stellar birth masses in a population. It predicts that low-mass stars can dominate the surviving main-sequence population at great ages, while old remnants of short-lived stars coexist with them.

```{figure} _static/_chapter10/fig26_initial_mass_functions.png
:width: 60%
:align: center
:name: fig_ch10_initial_mass_functions
:alt: Several parameterizations of the stellar initial mass function

**Figure 26** Several parameterizations of the stellar initial mass function. Their differences illustrate uncertainty in the distribution of birth masses.
```

```{figure} _static/_chapter10/fig27_zams_convection.png
:width: 86%
:align: center
:name: fig_ch10_zams_convection
:alt: Kippenhahn diagram for a family of ZAMS models with X=0.70 and Z=0.02

**Figure 27** Kippenhahn diagram for a family of ZAMS models with $X=0.70$ and $Z=0.02$. Grey areas are convective. The vertical coordinate $m/M$ runs from the centre to the surface for each mass on the horizontal axis.
```

The diagram gives the approximate transition from full convection to a radiative centre near $0.35M_\odot$, and the appearance of a convective core near $1.2M_\odot$ for this composition. Low or high opacity and the local luminosity per unit enclosed mass affect the transport criterion. The shaded layout also allows thin convective regions near the surface of some high-mass models. These transition masses vary with composition and age.

### Properties of main-sequence stars

The temperatures, luminosities, and radii below refer to the beginning of the main sequence. The lifetime $\tau_{\rm MS}$ is the duration of central hydrogen burning. The solar-mass ZAMS entry therefore describes a younger, fainter model than the present Sun. The table and the previous examples provide independent estimates and illustrate the sensitivity to model assumptions.

| $M/M_\odot$ | $\tau_{\rm MS}$ | $T_{\rm eff}$ (K) | Spectral type | $\log_{10}(L/L_\odot)$ | $R/R_\odot$ |
| ---: | ---: | ---: | :--- | ---: | ---: |
| $120$ | $2.56\ \mathrm{Myr}$ | $53\,300$ | O3 V | $+6.25$ | $16$ |
| $60$ | $3.45\ \mathrm{Myr}$ | $48\,200$ | O4 V | $+5.73$ | $10$ |
| $25$ | $6.51\ \mathrm{Myr}$ | $37\,900$ | O8 V | $+4.89$ | $6.5$ |
| $12$ | $16.0\ \mathrm{Myr}$ | $28\,000$ | B0.2 V | $+4.01$ | $4.3$ |
| $5$ | $94.5\ \mathrm{Myr}$ | $17\,200$ | B5 V | $+2.74$ | $2.7$ |
| $2.5$ | $585\ \mathrm{Myr}$ | $10\,700$ | B9 V | $+1.60$ | $1.8$ |
| $1.25$ | $4.91\ \mathrm{Gyr}$ | $6380$ | F5 V | $+0.32$ | $1.2$ |
| $1.0$ | $9.84\ \mathrm{Gyr}$ | $5640$ | G8 V | $-0.16$ | $0.9$ |
| $0.8$ | $25.0\ \mathrm{Gyr}$ | $4860$ | K2 V | $-0.61$ | $0.7$ |
| $0.5$ | $100\ \mathrm{Gyr}$ | $3890$ | M0 V | $-1.42$ | $0.4$ |
| $0.2$ | $4000\ \mathrm{Gyr}$ | $3300$ | M4 V | $\sim-2.2$ | $0.2$ |
| $0.1$ | $10\,000\ \mathrm{Gyr}$ | $2900$ | M7 V | $\sim-3.0$ | $0.1$ |

:::{note}
The luminosity at $25M_\odot$ follows from the tabulated $T_{\rm eff}$ and radius. In solar units the Stefan–Boltzmann law gives $(6.5)^2(37\,900/5772)^4\simeq7.9\times 10^4$, hence $\log_{10}(L/L_\odot)\simeq4.89$.
:::

### H II regions

Massive stars, above roughly $8M_\odot$ in representative models, can reach the ZAMS while still accreting. Hot O stars and early B stars provide photons above the hydrogen ionization threshold of $13.6\ \mathrm{eV}$, creating an **H II region** in the surrounding gas. Its temperature is typically of order $10^4\ \mathrm K$, compared with tens to about $100\ \mathrm K$ in the nearby neutral material. After ionization, the gas expands because of its higher pressure. It can drive a shock and pile up a surrounding neutral shell. Infrared images trace heated dust and molecules at the interface as well as material inside the ionized region. The ring **RCW 120** illustrates this geometry.[^ch10_hii]

```{figure} _static/_chapter10/fig28_rcw120.png
:width: 71%
:align: center
:name: fig_ch10_rcw120
:alt: Spitzer infrared view of RCW 120 (left) and a model of an H II region (right)

**Figure 28** Spitzer infrared view of RCW 120 (left) and a model of an H II region (right). The bands illustrate how emission from the interior and from the surrounding material traces different structures. Image credit NASA/JPL-Caltech.
```


## Post-main-sequence evolution

### The giant phase

At central hydrogen exhaustion, a star that has developed a distinct helium core leaves the main sequence. The inert core contracts and heats, and hydrogen continues to fuse in a shell around it. The envelope responds by expanding. The surface cools as the radius grows, and the star first crosses the **subgiant branch** and then, for low-mass giant progenitors, ascends the **red giant branch** (RGB). The **main-sequence turn-off** of a cluster marks the region where stars of its turn-off mass have begun this transition. A giant can have a lower effective temperature than a main-sequence star and still be more luminous because of its larger emitting area, $4\pi R^2$.[^ch10_giants]

```{figure} _static/_chapter10/fig29_giant_size.png
:width: 57%
:align: center
:name: fig_ch10_giant_size
:alt: A scale comparison between a Sun-like main-sequence star and its much larger red-giant configuration.

**Figure 29** A scale comparison between a Sun-like main-sequence star and its much larger red-giant configuration.
```

```{figure} _static/_chapter10/fig30_giant_turnoff.png
:width: 56%
:align: center
:name: fig_ch10_giant_turnoff
:alt: Composite colour–magnitude diagram with the turn-off, subgiant branch, and red giant branch identified

**Figure 30** Composite colour–magnitude diagram with the turn-off, subgiant branch, and red giant branch identified. Clusters of different ages have different turn-off locations.
```

The initial masses used in the following discussion refer to the beginning of stellar evolution. A star can lose an appreciable fraction of that mass in winds or by transferring material to a companion. The boundaries between evolutionary regimes are therefore approximate.

### Initial masses below about $0.5M_\odot$

M dwarfs near the low-mass end of the main sequence retain deep convective envelopes or are fully convective. Mixing supplies fresh hydrogen to the centre and can keep the composition nearly uniform over much of their evolution. Their main-sequence lifetimes exceed the present age of the Universe. Trillions of years apply to the lowest masses, while the lifetime near $0.5M_\odot$ is of order $10^{11}\ \mathrm{yr}$. Isolated stars that never reach the conditions for helium ignition ultimately leave helium white dwarfs.[^ch10_red_dwarfs]

:::{note}
The late evolution of red dwarfs depends strongly on their mass. Calculations for the least massive red dwarfs predict evolution towards hotter, compact objects before white-dwarf cooling. The helium white dwarfs observed today can form much sooner when a companion strips a more massive progenitor's envelope before helium ignites.
:::

### Low- and intermediate-mass stars

For initial masses roughly between $0.5$ and $8M_\odot$, the following stages describe the evolution of a star that ignites helium and ultimately loses its envelope. A $1M_\odot$ model serves as a reference for the subgiant and red-giant phases. More massive stars in this range differ in the conditions of helium ignition and in their subsequent tracks.

#### Hydrogen-shell burning and mass loss

On the **subgiant branch** of the one-solar-mass track, the transition from central hydrogen burning to hydrogen-shell burning is gradual. From B to C the inert helium core contracts, the shell adds helium ash to it, and the envelope expands. At the base of the RGB (C) much of the envelope has become convective. The convection reaches into material previously affected by nuclear burning and can alter surface abundances. This is the **first dredge-up**.

```{figure} _static/_chapter10/fig31_solar_track.png
:width: 70%
:align: center
:name: fig_ch10_solar_track
:alt: Evolution of a 1M_odot model in the HR diagram

**Figure 31** Evolution of a $1M_\odot$ model in the HR diagram. B to C covers the subgiant branch, C to F the ascent of the red giant branch, and the track after F approaches stable helium burning as the envelope contracts.
```

```{figure} _static/_chapter10/fig32_solar_shell_burning.png
:width: 66%
:align: center
:name: fig_ch10_solar_shell_burning
:alt: Interior of a 1M_odot model as a function of age and enclosed mass

**Figure 32** Interior of a $1M_\odot$ model as a function of age and enclosed mass. Shading marks convection, and the thin nuclear-burning region moves outward in mass as ashes accumulate below it.
```

From C to F, the red giant grows in radius at nearly constant effective temperature, so its luminosity rises. The outer layers are loosely bound, and the wind removes mass. In low-mass stars the helium core becomes electron-degenerate, even while the envelope is convective. These are distinct regions. The onset and strength of degeneracy depend on the initial mass and composition.

#### Helium ignition and the triple-alpha reaction

Near the RGB tip of a low-mass star, the core reaches a temperature of order $10^8\ \mathrm K$ and a density of order $10^6\ \mathrm{g\,cm^{-3}}$. In stars with initial masses above about $2M_\odot$, helium ignition takes place in a much less degenerate core, at densities that can be nearer $10^4\ \mathrm{g\,cm^{-3}}$. The transition mass depends on the model. A pair of alpha particles (helium-4 nuclei) briefly forms unstable beryllium-8, which can capture a third alpha particle before it decays:

$$
{}^4\mathrm{He}+{}^4\mathrm{He}\rightleftharpoons{}^8\mathrm{Be},
\qquad
{}^8\mathrm{Be}+{}^4\mathrm{He}\longrightarrow{}^{12}\mathrm C+\gamma.
$$

The net **triple-alpha reaction** yields carbon-12 and releases about $7.27\ \mathrm{MeV}$. Even though $^8\mathrm{Be}$ survives for only a time of order $10^{-16}\ \mathrm{s}$, a small equilibrium abundance is present at the densities and temperatures of helium burning.[^ch10_helium]

```{figure} _static/_chapter10/fig33_triple_alpha.png
:width: 70%
:align: center
:name: fig_ch10_triple_alpha
:alt: Triple-alpha burning

**Figure 33** Triple-alpha burning. Two helium-4 nuclei temporarily form beryllium-8, and capture of a third alpha particle produces carbon-12.
```

In a strongly degenerate core the pressure responds weakly to heating. Once helium burning begins, an increase in temperature accelerates the reactions before expansion can regulate them. This **helium flash** lifts degeneracy, and the core expands and settles into stable burning. The energy is used largely to restructure the core. In a sufficiently massive, nondegenerate core, expansion can regulate burning from the start and ignition is gradual.

#### Stable helium burning and the horizontal branch

In the solar-mass track the core expands and the envelope contracts after the RGB tip (F towards H). The luminosity drops as the hydrogen shell adjusts to the changed structure. The star now has a helium-burning core and a hydrogen-burning shell. **Horizontal branch** refers to the locus of core-helium-burning stars in colour–magnitude diagrams of old populations. The colour depends on the envelope mass as well as the chemical composition, including the helium abundance. In populations where many such stars lie together at the cool end of the branch, they form the **red clump**. More massive core-helium-burning stars can instead make **blue loops**, moving to higher effective temperature and later returning towards the cool side of the diagram.

```{figure} _static/_chapter10/fig34_horizontal_branch.png
:width: 80%
:align: center
:name: fig_ch10_horizontal_branch
:alt: Observed colour–magnitude diagram and comparison with stellar models

**Figure 34** Observed colour–magnitude diagram and comparison with stellar models. The core-helium-burning population spans a range of colours.
```

#### Carbon and oxygen during helium burning

Triple-alpha burning first makes carbon. Once it is abundant, the reaction $^{12}\mathrm C(\alpha,\gamma){}^{16}\mathrm O$ builds oxygen. The two reaction rates determine the carbon-to-oxygen ratio together with the temperature, core mixing, and duration of burning. The subsequent captures $^{16}\mathrm O(\alpha,\gamma){}^{20}\mathrm{Ne}$ and $^{20}\mathrm{Ne}(\alpha,\gamma){}^{24}\mathrm{Mg}$ are generally far less important under ordinary core-helium-burning conditions. Carbon capture, by contrast, is central to the composition and energy generation.

```{figure} _static/_chapter10/fig35_helium_abundances.png
:width: 93%
:align: center
:name: fig_ch10_helium_abundances
:alt: Example of the changing central abundances and internal burning regions in a 5M_odot model

**Figure 35** Example of the changing central abundances and internal burning regions in a $5M_\odot$ model. Helium declines while carbon and then oxygen accumulate.
```

:::{note}
A final carbon-to-oxygen ratio near $0.3$ is an illustrative model value. A ratio by mass and a ratio by number are different, and the final fractions vary with the reaction rates, stellar mass, and mixing prescription.
:::

#### Pulsational instabilities

When a track crosses the **instability strip**, some layers can drive radial oscillations. In a partially ionized layer, compression can increase opacity and impede the outgoing radiative flux. The resulting heat storage helps the layer do work as it expands. If the net work over a cycle exceeds damping, the oscillation grows. Radius, radial velocity, luminosity, and colour vary through the cycle, with different phases. **RR Lyrae** are low-mass horizontal-branch stars in the strip. **Classical Cepheids** are more massive and can cross the strip during a blue loop as well as during earlier evolution.[^ch10_pulsation]

```{figure} _static/_chapter10/fig36_radial_pulsations.png
:width: 44%
:align: center
:name: fig_ch10_radial_pulsations
:alt: Changes in luminosity, colour, radial velocity, and stellar radius through a cycle of radial pulsation.

**Figure 36** Changes in luminosity, colour, radial velocity, and stellar radius through a cycle of radial pulsation.
```

```{figure} _static/_chapter10/fig37_instability_strip.png
:width: 60%
:align: center
:name: fig_ch10_instability_strip
:alt: Pulsating variables in the HR diagram

**Figure 37** Pulsating variables in the HR diagram. Cepheids and RR Lyrae occupy different luminosity ranges along the classical instability strip.
```

#### The asymptotic giant branch

After central helium exhaustion a carbon–oxygen core remains. Helium burns in a shell around it, and the track moves to lower effective temperature and higher luminosity. This is the **asymptotic giant branch** (AGB). During the early AGB, expansion of the layers above the helium shell can temporarily weaken or extinguish hydrogen-shell burning. It can resume as the structure readjusts. The star then has an inner helium-burning shell and an outer hydrogen-burning shell.[^ch10_agb]

```{figure} _static/_chapter10/fig38_early_agb.png
:width: 68%
:align: center
:name: fig_ch10_early_agb
:alt: Late evolution of a 5M_odot model towards the AGB

**Figure 38** Late evolution of a $5M_\odot$ model towards the AGB. The horizontal excursions at higher effective temperature occur during earlier phases of evolution.
```

For most of the time between pulses, the hydrogen shell supplies the luminosity and deposits helium beneath it. When enough helium has accumulated, the thin helium shell can ignite unstably in a **thermal pulse**. A pulse produces convection between the shells, expands the overlying layers, and can temporarily turn off the hydrogen shell. After the pulse subsides, hydrogen burning can resume. This pattern recurs during the **thermally pulsing AGB**. Deep envelope convection after a pulse can bring newly processed material to the surface in the **third dredge-up**. The winds then return part of it to the interstellar medium. Technetium in such a star is evidence of recent production by slow neutron capture. Some AGB models also alter the abundance of magnesium isotopes or produce nitrogen through proton captures at the hot base of the convective envelope.

```{figure} _static/_chapter10/fig39_agb_shells.png
:width: 53%
:align: center
:name: fig_ch10_agb_shells
:alt: AGB structure with a degenerate carbon–oxygen core, two nuclear-burning shells, and a deep convective envelope losing material in a wind.

**Figure 39** AGB structure with a degenerate carbon–oxygen core, two nuclear-burning shells, and a deep convective envelope losing material in a wind.
```

#### White dwarfs and planetary nebulae

As winds remove the envelope, the remnant evolves towards higher effective temperature. If ultraviolet photons from the exposed core reach the ejecta while the gas is still sufficiently dense, they make it glow as a **planetary nebula**. The name reflects the appearance of some of these objects through early telescopes. The nebula is ejected stellar gas. The central remnant becomes a **white dwarf**, supported mainly by electron degeneracy pressure. It retains thin surface layers, typically helium with or without a hydrogen layer, and cools after sustained nuclear burning ends.

```{figure} _static/_chapter10/fig40_planetary_nebulae.png
:width: 91%
:align: center
:name: fig_ch10_planetary_nebulae
:alt: Several planetary nebulae

**Figure 40** Several planetary nebulae. Differences in shape reflect outflow geometry, viewing angle, and interactions in the ejected gas.
```

The **Southern Ring Nebula** (NGC 3132) illustrates the complementary view provided by Webb. Near-infrared imaging shows fine structure in the expanding gas, while mid-infrared imaging makes dust more prominent and helps distinguish the dusty central source.[^ch10_southern_ring]

```{figure} _static/_chapter10/fig41_southern_ring.png
:width: 94%
:align: center
:name: fig_ch10_southern_ring
:alt: NGC 3132 with Webb/NIRCam (left) and Webb/MIRI (right)

**Figure 41** NGC 3132 with Webb/NIRCam (left) and Webb/MIRI (right). Credit NASA, ESA, CSA, and STScI. [NASA image record](https://science.nasa.gov/asset/webb/southern-ring-nebula-sonifications-nircam-and-miri-images-side-by-side/).
```


### Massive stars

Above an initial mass of roughly $8M_\odot$, stars can develop cores large enough to ignite carbon after helium burning. The exact boundary depends on composition, mixing, and mass loss. The appearance of a massive star during this evolution depends strongly on how much of the hydrogen envelope it retains.[^ch10_massive]

#### Core helium burning, blue supergiants, and red supergiants

For some masses, the track crosses the HR diagram rapidly at nearly constant luminosity after central hydrogen exhaustion, evolving from a hot **blue supergiant** towards a cool **red supergiant** around the onset of central helium burning. A short crossing gives relatively few stars in that part of a coeval population. Blue supergiants can also occur in longer-lived evolutionary stages, including a return towards higher temperatures after substantial envelope loss. Winds can move the track or prevent a prolonged red-supergiant phase altogether. Deep in the star, helium burning is producing carbon and oxygen while hydrogen burning continues in a shell where sufficient hydrogen remains.

```{figure} _static/_chapter10/fig42_massive_tracks.png
:width: 71%
:align: center
:name: fig_ch10_massive_tracks
:alt: Model HR tracks for massive stars

**Figure 42** Model HR tracks for massive stars. Blue and red supergiants differ in surface temperature, and uncertain mass loss changes the route between them.
```

#### Luminous blue variables

The **Humphreys–Davidson limit** is an empirical upper luminosity boundary in the HR diagram of luminous stars. Some hot stars near it undergo strong variability and episodes of mass loss. These are **luminous blue variables** (LBVs). In some outbursts the mass-loss rate can exceed $10^{-3}M_\odot\,\mathrm{yr^{-1}}$. The surrounding nebula can preserve a record of the ejected material.[^ch10_lbv]

**Eta Carinae** is a massive binary in the Carina Nebula, a large star-forming H II region. During the Great Eruption it briefly became the second-brightest star in the night sky in 1843. The event ejected much of the material in the bipolar **Homunculus Nebula** seen today.

```{figure} _static/_chapter10/fig43_eta_carinae.png
:width: 94%
:align: center
:name: fig_ch10_eta_carinae
:alt: The Carina Nebula and views of Eta Carinae and the Homunculus, the dusty ejecta around the massive binary

**Figure 43** The Carina Nebula and views of Eta Carinae and the Homunculus, the dusty ejecta around the massive binary. [NASA image context](https://science.nasa.gov/asset/hubble/eta-carinae-the-great-eruption-of-a-massive-star/).
```

#### Wolf–Rayet stars

**Wolf–Rayet** (WR) spectra show strong, broad emission lines formed in dense, fast stellar winds. Many classical massive WR stars are stripped stars burning helium in their cores. Their spectra expose layers with nitrogen enrichment from hydrogen burning in the WN sequence or carbon and oxygen enrichment from helium burning in the WC and WO sequences. A wind can interact with previously ejected material to produce a circumstellar nebula. Some very massive hydrogen-rich WN stars still burn hydrogen in their cores. The luminosities of WR stars overlap those of LBVs. In an AGB star the helium-burning region is a shell, whereas in a classical stripped WR star helium can still be burning in the centre.

```{figure} _static/_chapter10/fig44_wolf_rayet_nebulae.png
:width: 94%
:align: center
:name: fig_ch10_wolf_rayet_nebulae
:alt: Nebulae around stars with Wolf–Rayet spectra

**Figure 44** Nebulae around stars with Wolf–Rayet spectra. Stellar winds and earlier mass loss shape the surrounding material.
```

#### Carbon burning and later stages

After central helium exhaustion, the carbon–oxygen core of a sufficiently massive star contracts and heats. Carbon fusion can start when the core exceeds roughly $1.05$–$1.1M_\odot$, with the threshold depending on the core's composition and thermal history. For stars that proceed through the full sequence, neon, oxygen, and silicon burning follow. Fuel depleted at the centre can still burn in a shell at larger enclosed mass. Carbon burning makes species such as neon, sodium, and magnesium. Neon burning begins with photodisintegration of $^{20}\mathrm{Ne}$ and subsequent alpha captures. Oxygen and silicon burning produce progressively heavier nuclei, with silicon burning ultimately building iron-group material.[^ch10_advanced]

```{figure} _static/_chapter10/fig45_advanced_core_track.png
:width: 60%
:align: center
:name: fig_ch10_advanced_core_track
:alt: Central temperature and density of 15M_odot and 25M_odot models as they progress from hydrogen and helium burning through the advanced stages.

**Figure 45** Central temperature and density of $15M_\odot$ and $25M_\odot$ models as they progress from hydrogen and helium burning through the advanced stages.
```

#### Neutrino losses

Hydrogen burning already produces neutrinos. At temperatures of several $10^8\ \mathrm K$ and above, thermal neutrino production becomes a major energy sink in advanced cores. Processes include electron–positron annihilation, $e^-+e^+\rightarrow\nu+\bar\nu$, and plasmon decay. While the core is transparent to neutrinos, they escape much more rapidly than energy can diffuse out as photons. The loss speeds up contraction between burning stages. During a burning stage, higher temperatures and higher reaction rates are needed to offset the large loss. The core can evolve rapidly while the envelope changes relatively little.

```{figure} _static/_chapter10/fig46_neutrino_losses.png
:width: 66%
:align: center
:name: fig_ch10_neutrino_losses
:alt: Illustrative nuclear heating rates and neutrino cooling as functions of temperature

**Figure 46** Illustrative nuclear heating rates and neutrino cooling as functions of temperature. Intersections indicate where the local rates are comparable for the adopted conditions.
```

:::{note}
The balance $\epsilon_{\rm nuc}\simeq\epsilon_\nu$ describes a core in which nuclear heating and neutrino cooling dominate the local energy budget. Stability against a temperature perturbation also depends on the temperature sensitivity of the rates and the response of the core. Neutrino oscillations, recognised by the 2015 Nobel Prize in Physics awarded to Takaaki Kajita and Arthur B. McDonald, establish differences between squared neutrino masses. Determining the absolute neutrino mass scale requires complementary evidence.[^ch10_neutrinos]
:::

The following $15M_\odot$ example shows how little time is spent in the last stages.[^ch10_burning_example] Temperatures and densities are characteristic central values. The duration of each stage depends on the model and on the definition of ignition and exhaustion. In this example oxygen burning lasts longer than neon burning, while the broad trend is a sharp reduction in lifetime.

| Core-burning stage | $T$ ($10^9\ \mathrm K$) | $\rho$ ($\mathrm{g\,cm^{-3}}$) | Main fuel | Main products | Duration |
| :--- | ---: | ---: | :--- | :--- | ---: |
| Hydrogen | $0.035$ | $5.8$ | H | He | $1.1\times10^7\ \mathrm{yr}$ |
| Helium | $0.18$ | $1.4\times10^3$ | He | C, O | $2.0\times10^6\ \mathrm{yr}$ |
| Carbon | $0.83$ | $2.4\times10^5$ | C | O, Ne | $2.0\times10^3\ \mathrm{yr}$ |
| Neon | $1.6$ | $7.2\times10^6$ | Ne | O, Mg | $0.7\ \mathrm{yr}$ |
| Oxygen | $1.9$ | $6.7\times10^6$ | O, Mg | Si, S | $2.6\ \mathrm{yr}$ |
| Silicon | $3.3$ | $4.3\times10^7$ | Si, S | Fe, Ni | $18\ \mathrm d$ |

Near the lower mass boundary for carbon ignition, **super-AGB** stars can form degenerate oxygen–neon cores. If the envelope is removed before the core attains the conditions for collapse, an oxygen–neon white dwarf is left behind. Some models instead undergo electron-capture collapse and can produce a supernova. Carbon burning followed by an oxygen–neon white dwarf applies to a limited range of initial masses.[^ch10_super_agb]

#### Pre-supernova structure

In a massive star that reaches silicon burning, successive stages produce a layered interior. An iron-group core is surrounded by burning shells, with the products of progressively earlier burning stages towards the outside. The active central region can become smaller in mass during the advanced stages as neutrino cooling grows. The envelope and the position in the HR diagram can remain nearly unchanged because the time left to collapse is short compared with the envelope's thermal timescale. Alpha and neutron captures and associated decays also produce less abundant isotopes, including nuclei in the silicon, sulfur, chlorine, and chromium groups.

```{figure} _static/_chapter10/fig47_presupernova.png
:width: 63%
:align: center
:name: fig_ch10_presupernova
:alt: Schematic layered structure before iron-core collapse

**Figure 47** Schematic layered structure before iron-core collapse. Onion-like shells contain the ashes and fuels of the different nuclear burning stages. Their radial thicknesses are schematic.
```

The binding-energy maximum lies among the iron-group nuclei. In particular, $^{62}\mathrm{Ni}$ has a slightly higher binding energy per nucleon than $^{56}\mathrm{Fe}$. Silicon burning and nuclear statistical equilibrium produce a mixture whose abundances depend on temperature, density, and electron fraction. The iron-group core has no subsequent fusion stage that can supply the energy needed to maintain the star.

#### Core collapse

An exhausted iron-group core is temporarily supported chiefly by the pressure of relativistic degenerate electrons. As the core grows, electron captures such as $e^-+p\rightarrow n+\nu_e$ and captures on nuclei reduce the electron fraction and hence the electron pressure. At the high temperatures and densities attained during collapse, **photodisintegration** of heavy nuclei absorbs energy, for example

$$
{}^{56}\mathrm{Fe}+\gamma\longrightarrow 13\,{}^4\mathrm{He}+4n.
$$

The inner core falls in on a dynamical timescale, of order a tenth of a second in the example below. At nuclear densities the equation of state stiffens, the inner core decelerates and rebounds, and a shock forms as the infalling outer core meets it.[^ch10_collapse]

```{figure} _static/_chapter10/fig48_collapse.png
:width: 66%
:align: center
:name: fig_ch10_collapse
:alt: Core collapse, neutrino trapping, bounce and shock formation, followed by shock stagnation and possible revival by neutrino heating

**Figure 48** Core collapse, neutrino trapping, bounce and shock formation, followed by shock stagnation and possible revival by neutrino heating. The times are illustrative of one model.
```

:::{note}
The prompt shock generally stalls as it dissociates heavy nuclei and loses energy to neutrinos. Neutrino heating behind the stalled shock, assisted by non-spherical flows, can revive the shock and drive an explosion. Some cores form black holes with little or no luminous explosion. A bounce is one stage of the process.
:::

#### Supernovae

A **supernova** is a stellar explosion whose peak luminosity can approach $10^{10}L_\odot$ and temporarily rival or exceed the light of its host galaxy. The spectroscopic classes describe observed lines. The light curves add information about how radiation emerges from the ejecta.[^ch10_sn]

| Type | Characteristic spectrum | Typical origin |
| :--- | :--- | :--- |
| II | Hydrogen lines | Core collapse with hydrogen-rich ejecta |
| Ib | No conspicuous hydrogen lines, prominent helium lines | Core collapse of a stripped star |
| Ic | No conspicuous hydrogen or helium lines | Core collapse of a more strongly stripped star |
| Ia | No hydrogen, prominent Si II near maximum light | Thermonuclear explosion of a white dwarf in a binary channel |

Representative nearby samples give rough fractions of a half for Type II, about a fifth for stripped-envelope events, and about a quarter to a third for Type Ia. The fractions vary with sample definition, host population, and how transitional spectra are grouped. The new point source in the M82 comparison is **SN 2014J**, a Type Ia event.

```{figure} _static/_chapter10/fig49_sn2014j.png
:width: 84%
:align: center
:name: fig_ch10_sn2014j
:alt: M82 before and after the appearance of SN 2014J

**Figure 49** M82 before and after the appearance of SN 2014J. The bright point in the later image illustrates how a nearby supernova stands out against its host.
```

```{figure} _static/_chapter10/fig50_supernova_light_curves.png
:width: 58%
:align: center
:name: fig_ch10_supernova_light_curves
:alt: Representative supernova light curves

**Figure 50** Representative supernova light curves. The Type II-P curve stays relatively flat for a period, while declining events fade more rapidly.
```

#### Light curves and supernova remnants

The early luminosity depends on the explosion, shock heating, and expansion of the ejecta. For a **Type II-P** supernova, hydrogen recombination lowers the opacity as the envelope cools. The photosphere recedes in mass through the expanding envelope, helping sustain a broad plateau. In many supernovae the late radioactive tail is powered by the energy deposited by the chain $^{56}\mathrm{Ni}\rightarrow{}^{56}\mathrm{Co}\rightarrow{}^{56}\mathrm{Fe}$. The deposition becomes less efficient as the ejecta thin out. Interaction with dense circumstellar material can supply additional luminosity in some events.

A **supernova remnant** is the expanding structure left after the explosion. On much longer timescales, shocks heat and accelerate particles as ejecta interact with circumstellar and interstellar gas. The Crab Nebula also receives energy from its central pulsar, which powers a broad synchrotron spectrum. Images at different wavelengths show the nebula's filaments and particle populations at different scales.

```{figure} _static/_chapter10/fig51_crab_multiband.png
:width: 94%
:align: center
:name: fig_ch10_crab_multiband
:alt: The Crab Nebula observed from radio and infrared through visible, ultraviolet, and X-rays

**Figure 51** The Crab Nebula observed from radio and infrared through visible, ultraviolet, and X-rays. The nebula's apparent structure depends on the radiation mechanism and observing band.
```

#### Naked-eye supernovae

- **SN 1006** was an exceptionally bright recorded stellar event, reported by observers in several parts of the world. It could be seen in daylight according to historical accounts.
- **SN 1054** was recorded by Chinese astronomers as a guest star. Its remnant is the **Crab Nebula**.
- **SN 1604**, first observed on 9 October 1604 and known as **Kepler's supernova**, left a Galactic remnant still observable at several wavelengths.
- **SN 1987A** in the Large Magellanic Cloud was visible to the naked eye. Several detectors recorded a burst of neutrinos, providing direct evidence of the rapid energy loss from the collapsing core.[^ch10_historical_sn]

```{figure} _static/_chapter10/fig52_historical_remnants.png
:width: 94%
:align: center
:name: fig_ch10_historical_remnants
:alt: Left to right, the remnants of Kepler's supernova, SN 1054 (the Crab Nebula), and SN 1987A

**Figure 52** Left to right, the remnants of Kepler's supernova, SN 1054 (the Crab Nebula), and SN 1987A. The last image combines ALMA, Hubble, and Chandra observations. [NASA image record](https://science.nasa.gov/missions/webb/nasas-webb-telescope-will-study-an-iconic-supernova/).
```

### Nucleosynthesis

Gas returned by stellar winds and explosions supplies material for later generations of stars. The abundance of an element reflects several processes integrated over the history of a population. Primordial nucleosynthesis made most of the hydrogen and helium and a small amount of lithium. Cosmic-ray fragmentation supplies much of the lithium, beryllium, and boron produced later. Low- and intermediate-mass stars make carbon and many nuclei by slow neutron capture, which they can return in AGB winds and in the material around planetary nebulae. Massive stars supply, among other products, much of the oxygen and other alpha elements. Thermonuclear supernovae from binary evolution contribute substantially to the iron group. Neutron-star mergers are an observed site of rapid neutron-capture nucleosynthesis, with additional sites possible.[^ch10_elements]

```{figure} _static/_chapter10/fig53_element_origins.png
:width: 95%
:align: center
:name: fig_ch10_element_origins
:alt: Multiple production channels contribute to the elements

**Figure 53** Multiple production channels contribute to the elements. The orange category identifies thermonuclear white-dwarf explosions, and the green category identifies neutron-star mergers. Credit Jennifer A. Johnson. Colour shares are schematic and vary with Galactic history. [Johnson, origin of the elements in the Solar System](https://blog.sdss.org/2017/01/09/origin-of-the-elements-in-the-solar-system/).
```

### Evolution in binary systems

Widely separated components can evolve nearly independently. In a close circular binary, the effective potential in the rotating frame combines the gravity of both stars with the centrifugal term. The critical equipotential around each component defines its **Roche lobe**. The lobes touch at the inner Lagrange point, $L_1$.[^ch10_binaries]

- In a **detached binary**, both photospheres lie inside their lobes. Mass transfer by Roche-lobe overflow is absent, although a companion can accrete part of a wind.
- In a **semidetached binary**, one star fills its lobe and can transfer gas through $L_1$.
- In a **contact binary**, both components fill their lobes and share an outer envelope or photospheric equipotential.

```{figure} _static/_chapter10/fig54_roche_lobes.png
:width: 48%
:align: center
:name: fig_ch10_roche_lobes
:alt: Roche geometry for detached, semidetached, and contact binaries

**Figure 54** Roche geometry for detached, semidetached, and contact binaries. In the semidetached case, the donor fills its lobe and gas can stream through the inner Lagrange point.
```

A star can fill its lobe as it becomes a giant, or because the orbit shrinks. The recipient can gain mass and the donor can lose its envelope before completing the evolution expected for an isolated star of the same initial mass. The effect can leave a low-mass helium white dwarf, expose the core of a massive star, or lead to unstable mass transfer and a common-envelope phase.

### Evolution of the core

The final remnant depends on the core mass and structure left after burning and on the interaction with the envelope and any companion. Envelope loss before core collapse usually leaves a **white dwarf**. Its dominant constituents can be helium, carbon and oxygen, or oxygen and neon, depending on which fuel the progenitor last burned. Collapse of a sufficiently massive core can produce a **neutron star** or a **black hole**. Winds, binary interactions, the explosion, and material falling back after the explosion all influence which outcome occurs at a given initial mass. An object born below the threshold for sustained hydrogen burning follows a substellar cooling track. These outcomes connect the nuclear and structural evolution of a star to the compact object it leaves behind.[^ch10_remnants]

[^ch10_structure]: Hanslmeier (2023), *Introduction to Astronomy and Astrophysics*, §§10.1–10.2, pp. 377–393 (PDF pp. 394–410). Karttunen et al. (2017), *Fundamental Astronomy*, §§11.1–11.2 and 12.1, pp. 247–251 and 261–262 (PDF pp. 256–260 and 270–271). Seeds, Backman, and Wegryn (2026), *Foundations of Astronomy*, §11-4, pp. 246–247 (PDF pp. 267–268).

[^ch10_composition]: Barbieri and Bertini (2021), *Fundamentals of Astronomy*, §17.5, pp. 288–290 (PDF pp. 307–309). Hanslmeier (2023), §§11.3–11.4, pp. 419–425 (PDF pp. 436–442).

[^ch10_fusion]: Hanslmeier (2023), §10.3.1, pp. 395–402 (PDF pp. 412–419). Karttunen et al. (2017), §11.3, pp. 252–255 (PDF pp. 261–264). Seeds et al. (2026), §8-3, pp. 172–176 (PDF pp. 193–197).

[^ch10_tracks]: Karttunen et al. (2017), §§11.4 and 12.7, pp. 255–258 and 273–275 (PDF pp. 264–267 and 282–284). Seeds et al. (2026), §12-3, pp. 270–271 (PDF pp. 291–292). [Stothers (1974), examples of nonuniqueness](https://www.giss.nasa.gov/pubs/abs/st05510d.html).

[^ch10_clouds]: Hanslmeier (2023), §§11.1.1–11.1.2, pp. 410–414 (PDF pp. 427–431). Karttunen et al. (2017), §§12.2 and 16.3–16.4, pp. 262–265 and 341–345 (PDF pp. 271–274 and 350–354). Seeds et al. (2026), §§10-2 and 11-1–11-3, pp. 222–225 and 232–245 (PDF pp. 243–246 and 253–266). [Chevance et al. (2020), molecular-cloud lifetimes](https://arxiv.org/abs/1911.03479).

[^ch10_pillars]: [NASA, Pillars of Creation in visible, near-infrared, and mid-infrared images](https://science.nasa.gov/mission/webb/star-lifecycle/).

[^ch10_surveys]: [ESA, Planck's nine observing bands](https://www.esa.int/media/planck-all-sky-frequency-maps-en-375067). [ALMA Observatory, receiver bands](https://www.almaobservatory.org/en/about-alma/how-alma-works/technologies/receivers/).

[^ch10_main_sequence]: Karttunen et al. (2017), §12.3, pp. 265–267 (PDF pp. 274–276). Hanslmeier (2023), §§11.2.1 and 11.3.4, pp. 418 and 422 (PDF pp. 435 and 439). Seeds et al. (2026), §12-1, pp. 256–262 (PDF pp. 277–283). [Pols, ZAMS convection and main-sequence evolution, §9.2 and Fig. 9.8](https://www.astro.ru.nl/~onnop/education/stev_utrecht_notes/chapter9-11.pdf). [Spiegel, Burrows, and Milsom (2011), deuterium ignition](https://doi.org/10.1088/0004-637X/727/1/57).

[^ch10_upper_mass]: [Kalari et al. (2022), mass estimates for the most massive stars in R136](https://doi.org/10.3847/1538-4357/ac8424).

[^ch10_cno]: Hanslmeier (2023), §10.3.1, pp. 397–400 (PDF pp. 414–417). [Bethe and Critchfield (1938), proton combination](https://doi.org/10.1103/PhysRev.54.248). [Bethe (1939), energy production in stars](https://doi.org/10.1103/PhysRev.55.434). [Borexino Collaboration (2020), solar CNO neutrinos](https://doi.org/10.1038/s41586-020-2934-0).

[^ch10_hii]: Hanslmeier (2023), §12.3.2, pp. 468–470 (PDF pp. 485–487). Karttunen et al. (2017), §16.2, pp. 333–341 (PDF pp. 342–350).

[^ch10_giants]: Karttunen et al. (2017), §12.4, pp. 267–269 (PDF pp. 276–278). Hanslmeier (2023), §11.1.4, pp. 415–417 (PDF pp. 432–434). Seeds et al. (2026), §12-2, pp. 263–269 (PDF pp. 284–290). [Pols, post-main-sequence models, Figs. 10.2, 10.3, and 10.5](https://www.astro.ru.nl/~onnop/education/stev_utrecht_notes/chapter9-11.pdf).

[^ch10_red_dwarfs]: [Laughlin, Bodenheimer, and Adams (1997), models near the end of the main sequence](https://doi.org/10.1086/304125). [Brown et al. (2022), low-mass white dwarfs in binaries](https://arxiv.org/abs/2207.02998).

[^ch10_pulsation]: Hanslmeier (2023), §11.8.2, pp. 443–446 (PDF pp. 460–463). Karttunen et al. (2017), §14.2, pp. 297–299 (PDF pp. 306–308). Seeds et al. (2026), §12-4, pp. 271–276 (PDF pp. 292–297).

[^ch10_agb]: Hanslmeier (2023), §§11.2.1 and 11.8.6, pp. 418 and 451–452 (PDF pp. 435 and 468–469). Karttunen et al. (2017), §§12.4–12.5 and 16.5, pp. 267–270 and 345–346 (PDF pp. 276–279 and 354–355). Seeds et al. (2026), §13-1, pp. 282–288 (PDF pp. 303–309). [Pols, AGB structure, thermal pulses, and nucleosynthesis, §11.1](https://www.astro.ru.nl/~onnop/education/stev_utrecht_notes/chapter9-11.pdf).

[^ch10_southern_ring]: [NASA, Webb observations of the Southern Ring Nebula with NIRCam and MIRI](https://science.nasa.gov/asset/webb/southern-ring-nebula-sonifications-nircam-and-miri-images-side-by-side/).

[^ch10_massive]: Hanslmeier (2023), §11.2.2, pp. 418–419 (PDF pp. 435–436). Seeds et al. (2026), §13-3, pp. 292–294 (PDF pp. 313–315). [Pols, evolution of massive stars and stellar winds, §§12.1–12.2](https://www.astro.ru.nl/~onnop/education/stev_utrecht_notes/chapter12-13.pdf).

[^ch10_lbv]: Hanslmeier (2023), §§11.8.4 and 11.9.2, pp. 448–451 and 455–457 (PDF pp. 465–468 and 472–474). [NASA, Eta Carinae and the 1843 eruption](https://science.nasa.gov/missions/hubble/nasas-hubble-space-telescope-resolves-eruption-of-a-massive-star/).

[^ch10_advanced]: Karttunen et al. (2017), §§11.3 and 12.5, pp. 252–255 and 269–270 (PDF pp. 261–264 and 278–279). [Woosley, Heger, and Weaver (2002), evolution and explosion of massive stars](https://doi.org/10.1103/RevModPhys.74.1015). [Pols, advanced burning and neutrino losses, §12.3, Fig. 12.5 and Table 12.1](https://www.astro.ru.nl/~onnop/education/stev_utrecht_notes/chapter12-13.pdf).

[^ch10_neutrinos]: Hanslmeier (2023), §10.3.2, pp. 402–404 (PDF pp. 419–421). [Nobel Prize in Physics 2015, scientific background](https://www.nobelprize.org/uploads/2017/09/advanced-physicsprize2015.pdf).

[^ch10_super_agb]: [Doherty et al. (2015), models of carbon ignition, white-dwarf formation, and electron-capture supernovae](https://arxiv.org/abs/1410.5431).

[^ch10_collapse]: Hanslmeier (2023), §§11.4.1 and 11.5, pp. 423–424 and 429–433 (PDF pp. 440–441 and 446–450). [Janka (2012), core-collapse explosion mechanisms](https://doi.org/10.1146/annurev-nucl-102711-094901).

[^ch10_sn]: Karttunen et al. (2017), §§14.4 and 16.6, pp. 304–308 and 346–349 (PDF pp. 313–317 and 355–358). Seeds et al. (2026), §13-4, pp. 293–302 (PDF pp. 314–323). [Li et al. (2011), nearby supernova fractions in a volume-limited sample](https://arxiv.org/abs/1006.4612). [NASA, SN 2014J in M82](https://science.nasa.gov/asset/hubble/supernova-in-m82/).

[^ch10_historical_sn]: Hanslmeier (2023), §11.5.3, pp. 432–433 (PDF pp. 449–450). [Hirata et al. (1987), neutrinos from SN 1987A](https://doi.org/10.1103/PhysRevLett.58.1490).

[^ch10_elements]: Karttunen et al. (2017), §12.8, pp. 275–278 (PDF pp. 284–287). Hanslmeier (2023), §11.5.2, pp. 431–432 (PDF pp. 448–449). [Watson et al. (2019), strontium in the merger of two neutron stars](https://doi.org/10.1038/s41586-019-1676-3).

[^ch10_binaries]: Karttunen et al. (2017), §12.6, pp. 270–273 (PDF pp. 279–282). Seeds et al. (2026), §13-2, pp. 289–291 (PDF pp. 310–312).

[^ch10_remnants]: Karttunen et al. (2017), §§12.5 and 15.1–15.3, pp. 269–270 and 309–317 (PDF pp. 278–279 and 318–326). Hanslmeier (2023), §§11.3–11.4 and 11.6, pp. 419–429 and 433–439 (PDF pp. 436–446 and 450–456).

[^ch10_transport]: Hanslmeier (2023), §§10.2.1–10.2.2, pp. 387–393 (PDF pp. 404–410). Karttunen et al. (2017), §15.1, pp. 309–311 (PDF pp. 318–320).

[^ch10_pp]: Hanslmeier (2023), §10.3.1, pp. 396–399 (PDF pp. 413–416). Seeds et al. (2026), §8-3, pp. 172–176 (PDF pp. 193–197).

[^ch10_helium]: Hanslmeier (2023), §10.3.1, pp. 400–401 (PDF pp. 417–418). Karttunen et al. (2017), §§11.3 and 12.4, pp. 253–255 and 267–269 (PDF pp. 262–264 and 276–278).

[^ch10_burning_example]: [Pols, Table 12.1, numerical example from Woosley, Heger, and Weaver (2002)](https://www.astro.ru.nl/~onnop/education/stev_utrecht_notes/chapter12-13.pdf).
