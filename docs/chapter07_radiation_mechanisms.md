(chapter07_radiation_mechanisms)=

# Radiation Mechanisms

:::{danger}
This page still needs substantial revision to match the content presented during the lectures
:::

> {sub-ref}`today` | {sub-ref}`wordcount-minutes` min read

Stars have colours. The composite image of a crowded stellar field in [Figure 1](fig01_radiation_stellar_colours) highlights differences from blue-white to orange. A star's visible colour depends on how its radiation is distributed across the visible spectrum. Temperature has a strong effect on this distribution, while atoms and molecules imprint signatures at particular wavelengths. To interpret those signatures, we start from the properties of light, consider how matter emits and absorbs it, and then follow the radiation as it travels through a medium.

```{figure} _static/_chapter07/fig01_stellar_colours.png
:width: 82%
:align: center
:name: fig01_radiation_stellar_colours

**Figure 1** The globular cluster NGC 6362 in a composite of ultraviolet, visible, and infrared observations. Credit ESA/Hubble & NASA. [Image record](https://esahubble.org/images/potw1244a/).
```

## The quantum nature of light

An electromagnetic wave transports energy through oscillating electric and magnetic fields. In a plane wave in vacuum the two fields are perpendicular to each other and to the direction of propagation ([Figure 2](fig02_radiation_electromagnetic_wave)). The frequency $\nu$ counts the oscillations per second, and the wavelength $\lambda$ is the distance over which the phase repeats. In vacuum they are related by

$$
c=\lambda\nu,
\qquad
c=299\,792\,458\ \mathrm{m\,s^{-1}}.
$$

Light exchanges energy with matter in discrete packets called **photons**. For example, a photon absorbed in a silicon detector can generate an electron–hole pair. The detector collects the photoelectrons in a potential well, where the accumulated charge provides a measure of the light received ([Figure 3](fig03_radiation_photon_detection)). The wave description accounts for propagation and interference, while the photon description accounts for the discrete exchanges of energy in detection and atomic transitions.[^ch07_light]

```{figure} _static/_chapter07/fig02_electromagnetic_wave.png
:width: 66%
:align: center
:name: fig02_radiation_electromagnetic_wave

**Figure 2** Electric and magnetic fields in a plane electromagnetic wave in vacuum. The wavelength $\lambda$ spans one full spatial cycle.
```

```{figure} _static/_chapter07/fig03_photon_detection.png
:width: 56%
:align: center
:name: fig03_radiation_photon_detection

**Figure 3** Photon detection in silicon. An electric potential confines the photoelectrons in a well until their charge is read out.
```

A photon has zero rest mass and electric charge, carries momentum, and has two independent transverse polarization states. Its energy and momentum magnitude are

$$
\boxed{E=h\nu=\frac{hc}{\lambda}},
\qquad
p=\frac{E}{c}=\frac{h}{\lambda},
$$

where $h=6.62607015\times10^{-34}\ \mathrm{J\,s}$ is the exact SI value of the Planck constant. Frequency is measured in hertz, with $1\ \mathrm{Hz}=1\ \mathrm{s^{-1}}$. Besides the nanometre, astronomers have traditionally used the ångström, $1\ \text{Å}=0.1\ \mathrm{nm}=10^{-10}\ \mathrm{m}$.[^ch07_constants]

## The electromagnetic spectrum

The **electromagnetic spectrum** is the range of wavelengths or frequencies that radiation can occupy. In order of increasing frequency and photon energy, it includes radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, and gamma rays. Visible light, roughly $400$–$750\ \mathrm{nm}$, occupies a small part of this range ([Figure 4](fig04_radiation_electromagnetic_spectrum)). Band boundaries are conventional, and broad regions are often subdivided, as in the near and far infrared or the extreme ultraviolet.[^ch07_spectrum]

```{figure} _static/_chapter07/fig04_electromagnetic_spectrum.png
:width: 87%
:align: center
:name: fig04_radiation_electromagnetic_spectrum

**Figure 4** Regions of the electromagnetic spectrum. Frequency and photon energy increase as wavelength decreases.
```

Warm bodies often radiate strongly in the infrared, and infrared radiation absorbed by the skin can be felt as warmth. Absorption of radiation at other wavelengths can also heat matter. At high photon energies an absorbed photon can remove a bound electron. Extreme ultraviolet, X-rays, and gamma rays include **ionizing radiation**, with the threshold for a particular process set by the binding energy of the atom or molecule concerned.

## Atomic structure and energy levels

A nucleus contains $Z$ protons and $N$ neutrons. The **atomic number** $Z$ specifies the element, and the **mass number** is $A=Z+N$. A proton has charge $+e$, a neutron has zero charge, and the electron has charge $-e$. A neutral atom therefore contains $Z$ electrons. For example, the carbon-12 atom in [Figure 6](fig06_radiation_carbon_atom) has six protons, six neutrons, and six electrons.

The quantum states of an electron are described by wavefunctions. Their squared magnitudes give probability densities, with different spatial patterns for different states ([Figure 5](fig05_radiation_hydrogen_orbitals)). For spectroscopy, the **Bohr model** offers a simple representation of the discrete energy levels of hydrogen. It depicts the states as orbits indexed by the principal quantum number $n=1,2,3,\ldots$. The orbits in [Figure 7](fig07_radiation_bohr_transition) label the energies involved in a transition. The level spacing of a many-electron atom requires a more detailed quantum description.[^ch07_atom]

```{figure} _static/_chapter07/fig05_hydrogen_orbitals.png
:width: 53%
:align: center
:name: fig05_radiation_hydrogen_orbitals

**Figure 5** Spatial patterns associated with hydrogen orbitals. Different quantum states give different distributions. Credit PoorLeno. [Original image](https://commons.wikimedia.org/wiki/File:Hydrogen_Density_Plots.png).
```

```{figure} _static/_chapter07/fig06_carbon_atom.png
:width: 40%
:align: center
:name: fig06_radiation_carbon_atom

**Figure 6** Schematic carbon-12 atom. The nucleus has six protons and six neutrons, and the neutral atom has six electrons.
```

```{figure} _static/_chapter07/fig07_bohr_transition.png
:width: 48%
:align: center
:name: fig07_radiation_bohr_transition

**Figure 7** A downward transition between two energy levels in the Bohr representation. The emitted photon's energy equals the separation between the levels.
```

Take the zero of energy at the threshold where the electron is free and at rest relative to the ion. Bound hydrogen levels then have negative energies, approximately

$$
E_n=-\frac{13.6\ \mathrm{eV}}{n^2}.
$$

The lowest level, $n=1$, is the **ground state**. Higher bound levels are **excited states**, and their spacing decreases towards the ionization threshold, $E=0$. The energy required to ionize ground-state hydrogen is approximately $13.6\ \mathrm{eV}$. A transition between two levels separated by an energy $|\Delta E|$ involves a photon of frequency $\nu=|\Delta E|/h$ if the exchange is radiative. For a given upper level, the largest energy drop is to the ground state.[^ch07_hydrogen]

The spectral series of hydrogen group transitions by their lower level ([Figure 8](fig08_radiation_hydrogen_series)). The **Lyman series** terminates at $n=1$ and lies in the ultraviolet. The **Balmer series**, ending at $n=2$, includes several prominent visible lines. In particular, the $3\to2$ transition emits H$\alpha$ near $656\ \mathrm{nm}$, in the red. The **Paschen**, **Brackett**, and **Pfund** series end at $n=3$, $4$, and $5$, respectively, and lie in the infrared. Within each series the lines converge towards the wavelength corresponding to ionization from its lower level.

```{figure} _static/_chapter07/fig08_hydrogen_spectral_series.png
:width: 62%
:align: center
:name: fig08_radiation_hydrogen_series

**Figure 8** The Lyman, Balmer, Paschen, Brackett, and Pfund series of hydrogen. The arrows group downward transitions that share the same lower level.
```

## Transitions between energy levels

Radiative processes can be classified by whether the electron is bound or free at the start and end of the interaction. A **bound–bound** transition connects two discrete levels. A **bound–free** or **free–bound** transition connects a bound level to an unbound state. In a **free–free** transition the electron stays unbound. The energy available to a free electron is continuous above the threshold.

### Bound–bound transitions

Let the lower and upper levels have energies $E_1$ and $E_2$, with $E_2>E_1$. The same separation $E_2-E_1=h\nu$ determines the photon frequency for all three processes in [Figure 9](fig09_radiation_bound_bound).[^ch07_lines]

- **Absorption.** An atom in the lower state absorbs a photon near the transition frequency and moves to the upper state.
- **Spontaneous emission.** An excited atom can drop to the lower level and emit a photon. Its phase and direction are not fixed by any incident photon. Excitation can have occurred by another process, such as a collision between particles in a hot gas.
- **Stimulated emission.** An incident photon at the transition frequency can induce an excited atom to decay. The added photon occupies the same radiation mode, with the same frequency, direction, and polarization. The resulting emission is coherent with the incident radiation.

```{figure} _static/_chapter07/fig09_bound_bound_transitions.png
:width: 76%
:align: center
:name: fig09_radiation_bound_bound

**Figure 9** Absorption, spontaneous emission, and stimulated emission between two bound levels. The incident photon in the stimulated process remains in the outgoing beam.
```

### Ionization, recombination, and free–free radiation

In **photoionization**, an atom absorbs a photon with enough energy to release a bound electron ([Figure 10](fig10_radiation_photoionization)). For an initial level of energy $E_n<0$, the binding energy is $\chi_n=|E_n|$. Neglecting the small recoil of the residual ion gives the outgoing electron's kinetic energy,

$$
K_{\rm e}\simeq h\nu-\chi_n,
\qquad
h\nu\geq\chi_n.
$$

For a nonrelativistic electron, $p_{\rm e}=\sqrt{2m_{\rm e}K_{\rm e}}$. The ion also recoils to conserve momentum. The photon frequency can vary continuously above the threshold, and the probability of absorption depends on frequency.

```{figure} _static/_chapter07/fig10_photoionization.png
:width: 51%
:align: center
:name: fig10_radiation_photoionization

**Figure 10** Photoionization. The atom absorbs a photon and releases an electron, leaving a positively charged ion.
```

The inverse process is **radiative recombination**. A free electron is captured into a bound level of an ion and emits a photon. If the captured electron initially has kinetic energy $K_{\rm e}$ far from the ion, the photon carries energy $h\nu\simeq K_{\rm e}+\chi_n$, with a small recoil correction. Captures into a given level produce a continuum with an edge at the binding energy, and subsequent transitions between bound levels can add spectral lines ([Figure 11](fig11_radiation_recombination)).

```{figure} _static/_chapter07/fig11_radiative_recombination.png
:width: 37%
:align: center
:name: fig11_radiation_recombination

**Figure 11** Capture of a free electron by a xenon ion, with emission of a photon.
```

In **free–free emission**, an electron accelerated in the electric field of an ion radiates while remaining unbound ([Figure 12](fig12_radiation_free_free)). The process is called **bremsstrahlung**, or braking radiation. A plasma with a thermal distribution of electron velocities produces a broad continuum. It is an important source of X-rays in very hot, ionized gas. For example, at $T=10^7\ \mathrm{K}$, $kT\simeq0.86\ \mathrm{keV}$, which sets the scale for the exponential decline of thermal bremsstrahlung at high photon energies.[^ch07_continua]

```{figure} _static/_chapter07/fig12_free_free_emission.png
:width: 41%
:align: center
:name: fig12_radiation_free_free

**Figure 12** Free–free emission. The ion deflects a passing electron, which loses energy by emitting a photon and remains unbound.
```

### Scattering

**Scattering** redirects radiation through interaction with matter. Some regimes are approximately elastic, so the outgoing photon has nearly the same wavelength in the scatterer's rest frame. Rayleigh scattering applies to particles much smaller than the wavelength, as with atmospheric molecules in visible light. It is more efficient at short visible wavelengths, giving the daytime sky its blue colour ([Figure 13](fig13_radiation_atmospheric_scattering)). Mie theory describes scattering by spherical particles, and is especially useful for particles comparable in size to the wavelength. Thomson scattering is the low-photon-energy limit for a free electron at rest. At larger photon energies, **Compton scattering** can transfer a significant fraction of the photon's energy to the electron.

```{figure} _static/_chapter07/fig13_atmospheric_scattering.png
:width: 51%
:align: center
:name: fig13_radiation_atmospheric_scattering

**Figure 13** Scattering of sunlight by the Earth's atmosphere. Scattered light can reach an observer from directions away from the Sun.
```

## Continuous, absorption, and emission spectra

Consider three arrangements involving a source of white light and hydrogen gas ([Figures 14](fig14_radiation_spectral_geometry) and [15](fig15_radiation_spectra)). The comparison concerns the spectrum measured along the beam leaving the apparatus.[^ch07_spectra]

1. **Continuous spectrum.** A hot, opaque source, such as a heated solid or a sufficiently opaque gas, produces radiation over a broad range of wavelengths. A smooth continuum may vary strongly in intensity across that range.
2. **Absorption spectrum.** Place cooler, relatively dilute hydrogen gas between the white-light source and the observer. Bound–bound absorption removes photons from the beam around characteristic wavelengths, producing dark lines superposed on the continuum.
3. **Emission spectrum.** Observe a hot, relatively dilute hydrogen gas against a dark background. Collisions populate excited levels, and radiative decay produces bright lines at characteristic wavelengths. With hydrogen in both experiments, the allowed line wavelengths are shared by emission and absorption.

```{figure} _static/_chapter07/fig14_spectral_formation_geometry.png
:width: 75%
:align: center
:name: fig14_radiation_spectral_geometry

**Figure 14** Three observing arrangements. A white-light source is seen directly in A, through cool hydrogen in B, and replaced by hot hydrogen in C. A dispersing element separates the outgoing light by wavelength.
```

```{figure} _static/_chapter07/fig15_continuous_absorption_emission.png
:width: 88%
:align: center
:name: fig15_radiation_spectra

**Figure 15** Schematic appearance of a continuous spectrum, an absorption-line spectrum, and an emission-line spectrum. The line positions and widths illustrate the three cases.
```

### The fingerprints of elements

The pattern of an element's spectral lines reflects the energies of its electronic states. Hydrogen, helium, oxygen, neon, and iron therefore show different patterns in [Figure 16](fig16_radiation_element_spectra). An identification is strengthened when several lines match the same element and ionization stage, after allowing for a possible Doppler shift. Relative line strengths also depend on the physical state of the gas because temperature and density affect which levels and ions are populated.

```{figure} _static/_chapter07/fig16_element_spectra.png
:width: 82%
:align: center
:name: fig16_radiation_element_spectra

**Figure 16** Characteristic spectra of hydrogen, helium, oxygen, neon, and iron. The distribution of lines provides a way to identify each element.
```

## Molecular spectra

Molecules have internal motions in addition to electronic excitation. Their nuclei can rotate together and vibrate relative to one another. In a typical molecule, adjacent rotational levels are closer in energy than adjacent vibrational levels, which in turn are closer than the electronic levels. Bending and symmetric or asymmetric stretching are examples of vibrational motions ([Figure 17](fig17_radiation_molecular_motion)).[^ch07_molecules]

```{figure} _static/_chapter07/fig17_molecular_motion.png
:width: 89%
:align: center
:name: fig17_radiation_molecular_motion

**Figure 17** Examples of molecular rotation, bending, and stretching. Different motions have different characteristic energy scales.
```

Each electronic state has vibrational levels, and each vibrational level has rotational structure ([Figure 18](fig18_radiation_molecular_levels)). Pure rotational lines are often found at microwave or far-infrared wavelengths, vibrational transitions in the infrared, and electronic transitions in the visible or ultraviolet. A transition can change more than one type of motion, subject to quantum selection rules. Many allowed transitions can therefore cluster into a **molecular band**. A spectrometer of sufficient resolving power separates individual lines, while modest resolution shows the broader band envelope ([Figure 19](fig19_radiation_molecular_band)).

```{figure} _static/_chapter07/fig18_molecular_energy_levels.png
:width: 58%
:align: center
:name: fig18_radiation_molecular_levels

**Figure 18** Molecular potential-energy curves and examples of electronic, vibrational, and rotational transitions. The horizontal coordinate is the separation between the nuclei.
```

```{figure} _static/_chapter07/fig19_molecular_band.png
:width: 63%
:align: center
:name: fig19_radiation_molecular_band

**Figure 19** Reflectance across the atmospheric oxygen A-band near $760\ \mathrm{nm}$. The black trace shows individual lines at $0.005\ \mathrm{nm}$ resolution. The red trace shows the same band at the resolution of the SCIAMACHY spectrometer. [Van Diedenhoven et al. (2005), Figure 1](https://acp.copernicus.org/articles/5/2109/2005/).
```

## How continuous spectra arise

A continuum can arise from the distribution of free-electron energies. In free–free emission both the initial and final electron energies range continuously. In radiative recombination, a continuous range of incident electron energies feeds a discrete set of bound levels, producing a continuum above each corresponding emission edge. Photoionization produces continuous **absorption** above each threshold. Individual photons in all these processes still carry the energy $h\nu$.[^ch07_continua]

Compton scattering redistributes photon energies across a range of frequencies. An energetic photon incident on a free electron initially at rest loses energy to electron recoil, and its wavelength increases by

$$
\lambda'-\lambda=\frac{h}{m_{\rm e}c}(1-\cos\theta),
$$

where $\theta$ is the photon scattering angle ([Figure 20](fig20_radiation_compton)). Energetic electrons can transfer energy to lower-energy photons by **inverse Compton scattering**. The range of scattering angles and particle energies can reshape a radiation spectrum.[^ch07_compton]

```{figure} _static/_chapter07/fig20_compton_scattering.png
:width: 53%
:align: center
:name: fig20_radiation_compton

**Figure 20** Photoionization (left) and Compton scattering (right). In the right-hand example a scattered X-ray photon leaves with a longer wavelength, and the electron is ejected.
```

A spectrum can also look nearly continuous when many broadened lines overlap or the instrument cannot resolve them. The **Doppler effect** spreads their frequencies because the emitting or absorbing particles have different velocities along the line of sight. In a dense gas, frequent collisions perturb the radiating atoms and broaden their lines. Either effect can contribute to a **pseudo-continuum** under suitable conditions. A real continuum can coexist with such features. The deuterium lamp in [Figure 21](fig21_radiation_deuterium) shows a molecular continuum, a collection of lines in the Fulcher-$\alpha$ band, and discrete atomic lines. Its shape is set by the emitting species and the detector response. A blackbody continuum, by comparison, has a specific distribution fixed by temperature.[^ch07_deuterium]

```{figure} _static/_chapter07/fig21_deuterium_spectrum.png
:width: 77%
:align: center
:name: fig21_radiation_deuterium

**Figure 21** Spectrum of a deuterium lamp, with a molecular continuum, the Fulcher-$\alpha$ molecular band, and the atomic D$\alpha$ and D$\beta$ lines. The vertical scale is in detector counts. Credit Deglr6328, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). [Original measurement](https://commons.wikimedia.org/wiki/File:Deuterium_lamp_1.png).
```

## Blackbody radiation

A **blackbody** absorbs all incident electromagnetic radiation, at every wavelength and angle of incidence. Its equilibrium emission is set by its temperature. An absorbed photon deposits energy in the material, which can subsequently radiate at other frequencies. If the blackbody reaches a steady state through radiative exchange alone, the total emitted power balances the total absorbed power.[^ch07_blackbody]

A small opening in an opaque cavity provides an approximation to a blackbody ([Figure 22](fig22_radiation_blackbody_cavity)). A ray that enters through the opening generally strikes the walls many times before it has a chance to escape. Even walls that absorb only a fraction of the radiation at each encounter can absorb nearly all the incident energy after many encounters. With the cavity walls held at a common temperature, the radiation escaping through the opening samples the equilibrium radiation inside.

```{figure} _static/_chapter07/fig22_blackbody_cavity.png
:width: 47%
:align: center
:name: fig22_radiation_blackbody_cavity

**Figure 22** A cavity with a small opening approximates a blackbody. Repeated encounters with the walls make the opening a highly efficient absorber. [OpenStax, *University Physics*, Vol. 3, Figure 6.2](https://openstax.org/books/university-physics-volume-3/pages/6-1-blackbody-radiation).
```

### Planck's law

Let $I_\nu$ be the **specific intensity**, or spectral radiance, at frequency $\nu$. The energy crossing an area $dA$ in time $dt$, within the frequency interval $d\nu$ and the solid angle $d\Omega$ around a direction at angle $\theta$ to the surface normal, is

$$
dE=I_\nu\cos\theta\,dA\,d\Omega\,d\nu\,dt.
$$

For a blackbody at absolute temperature $T$, the specific intensity is independent of direction in the outward hemisphere. Its value is the Planck function,

$$
\boxed{
B_\nu(T)=\frac{2h\nu^3}{c^2}
\frac{1}{\exp\!\left(h\nu/kT\right)-1}
},
$$

where $k=1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$ is the Boltzmann constant. The units of $B_\nu$ are $\mathrm{W\,m^{-2}\,sr^{-1}\,Hz^{-1}}$. Since $B_\nu\,|d\nu|=B_\lambda\,|d\lambda|$ for corresponding spectral intervals,

$$
\boxed{
B_\lambda(T)=B_\nu(T)\frac{c}{\lambda^2}
=\frac{2hc^2}{\lambda^5}
\frac{1}{\exp\!\left(hc/\lambda kT\right)-1}
},
\qquad \nu=\frac{c}{\lambda}.
$$

The wavelength form has units $\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ when the wavelength is measured in metres. The factor $c/\lambda^2$ accounts for the unequal widths of the corresponding frequency and wavelength intervals. The curves in [Figure 23](fig23_radiation_planck_curves) illustrate the effect of temperature. At long wavelengths, classical theory gives the **Rayleigh–Jeans limit**, $B_\nu\simeq 2kT\nu^2/c^2$ for $h\nu\ll kT$. Extrapolating this approximation to high frequencies would give an unbounded integrated radiance. The exponential term in Planck's law suppresses the short-wavelength contribution.[^ch07_blackbody]

```{figure} _static/_chapter07/fig23_planck_curves.png
:width: 67%
:align: center
:name: fig23_radiation_planck_curves

**Figure 23** Planck spectra at $3000$, $4000$, and $5000\ \mathrm{K}$, expressed per unit wavelength. The classical curve at $5000\ \mathrm{K}$ approaches the Planck curve towards longer wavelengths and rises steeply towards the ultraviolet. Credit Darth Kule. [Original plot](https://commons.wikimedia.org/wiki/File:Black_body.svg).
```

### The Stefan–Boltzmann law

Integrating the spectral radiance gives the **bolometric radiance**,

$$
B(T)=\int_0^\infty B_\nu(T)\,d\nu
=\int_0^\infty B_\lambda(T)\,d\lambda
=\frac{2\pi^4k^4}{15c^2h^3}\,T^4.
$$

The last equality follows by setting $x=h\nu/(kT)$ and using $\int_0^\infty x^3/(e^x-1)\,dx=\pi^4/15$. The **emitted flux** $F$ measures the power leaving a unit area of the surface. Integrating over the outward hemisphere includes the projected-area factor $\cos\theta$, so

$$
F=\int_{\rm hemisphere}B(T)\cos\theta\,d\Omega=\pi B(T).
$$

This gives the **Stefan–Boltzmann law**,

$$
\boxed{F=\sigma T^4},
\qquad
\sigma=\frac{2\pi^5 k^4}{15c^2h^3}
\simeq5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}.
$$

The flux $F$ is measured in $\mathrm{W\,m^{-2}}$. Doubling the temperature increases the emitted power per unit area by a factor of 16.[^ch07_constants]

### Wien's displacement law

Increasing the temperature raises the spectral radiance at every fixed wavelength and shifts the maximum of $B_\lambda$ towards shorter wavelengths ([Figure 24](fig24_radiation_wien)). The location of that maximum is given by **Wien's displacement law**,

$$
\boxed{\lambda_{\max}T=b},
\qquad
b\simeq2.89777\times10^{-3}\ \mathrm{m\,K}.
$$

For the Sun, the widely used value $T\simeq5778\ \mathrm{K}$ gives $\lambda_{\max}\simeq502\ \mathrm{nm}$, in the visible. The nominal solar effective temperature adopted by the International Astronomical Union is $5772\ \mathrm{K}$, which gives the same result at this precision. Wien's constant here refers to a spectrum per unit **wavelength**. For a spectrum per unit **frequency**, taking the maximum of $B_\nu$ gives a different location because the two densities differ by the factor $c/\lambda^2$.[^ch07_wien]

```{figure} _static/_chapter07/fig24_wien_displacement.png
:width: 70%
:align: center
:name: fig24_radiation_wien

**Figure 24** The maxima of the wavelength spectra shift towards shorter wavelengths as the temperature increases. The horizontal scale is in nanometres, and the shaded strip marks visible light.
```

On logarithmic axes the locus of maxima is a straight line ([Figure 25](fig25_radiation_planck_log)). At a peak, $\lambda_{\max}T=b$, so the exponential factor in $B_\lambda$ is the same for each curve. The peak radiance consequently scales as $\lambda_{\max}^{-5}$, and the wavelength-dependent surface flux has the same scaling. A human body with a surface temperature of order $300\ \mathrm{K}$ has a thermal peak near $9.7\ \mathrm{\mu m}$, far beyond the visible band. An infrared camera detects this emission even in the absence of visible illumination.[^ch07_thermal_imaging]

```{figure} _static/_chapter07/fig25_blackbody_logarithmic.png
:width: 73%
:align: center
:name: fig25_radiation_planck_log

**Figure 25** Blackbody spectra on logarithmic axes. The ordinate gives spectral power per unit emitting area and wavelength, integrated over the outward hemisphere. The dashed line joins the peaks. Credit HighTemplar. [Original plot](https://commons.wikimedia.org/wiki/File:Planck_law_log_log_scale.png).
```

## The colours of stars

**Orion** contains stars of markedly different colours in the same part of the sky ([Figure 26](fig26_radiation_orion_photo)). Betelgeuse ($\alpha$ Orionis) is a red supergiant with a representative effective temperature of about $3500\ \mathrm{K}$. Rigel ($\beta$ Orionis) is a blue-white supergiant, here illustrated with $11\,000\ \mathrm{K}$. Saiph ($\kappa$ Orionis), a hotter blue supergiant, has a model estimate of $26\,500\ \mathrm{K}$. These values illustrate the temperature differences among the three stars. Estimates for an individual star depend on the observations and atmosphere model used.[^ch07_orion]

```{figure} _static/_chapter07/fig26_orion_photograph.png
:width: 78%
:align: center
:name: fig26_radiation_orion_photo

**Figure 26** The constellation Orion. Orange-red Betelgeuse is above and to the left of the Belt in this image. Rigel and Saiph lie below the Belt.
```

The chart in [Figure 27](fig27_radiation_orion_chart) identifies the stars. A blackbody curve at Betelgeuse's illustrative temperature peaks near $830\ \mathrm{nm}$, so its visible light is weighted towards the red. At the temperatures used for Rigel and Saiph, the respective blackbody peaks are near $263$ and $109\ \mathrm{nm}$, in the ultraviolet. Both stars still emit visible light over a broad range of wavelengths, with a greater short-to-long wavelength ratio than Betelgeuse. Colour therefore depends on the relative strength of different parts of the visible spectrum, even when the maximum lies outside it ([Figure 28](fig28_radiation_stellar_temperature_colours)).

```{figure} _static/_chapter07/fig27_orion_chart.png
:width: 42%
:align: center
:name: fig27_radiation_orion_chart

**Figure 27** A chart of Orion identifying Betelgeuse, Rigel, and Saiph. The label at the upper left refers to Betelgeuse. Credit © 2015 GMystic.com.
```

```{figure} _static/_chapter07/fig28_stellar_temperature_colours.png
:width: 60%
:align: center
:name: fig28_radiation_stellar_temperature_colours

**Figure 28** Thermal spectra for stars of different temperatures and a human body. The coloured discs illustrate the appearance of stars at three representative temperatures.
```

## Departures from a blackbody spectrum

A blackbody is a first approximation to a stellar continuum. A photosphere has a temperature gradient, and its atoms, ions, and molecules absorb and emit at wavelength-dependent rates. The opacity helps determine from which depth the emerging radiation comes at each wavelength. Where the opacity rises in a spectral line, the radiation generally emerges from a shallower layer. A line can appear in absorption if this layer is cooler than the layers producing the nearby continuum.[^ch07_stellar_spectra]

The solar irradiance in [Figure 29](fig29_radiation_solar_spectrum) broadly resembles a thermal spectrum but differs from any single Planck curve. The first-light solar observation with the APOGEE near-infrared spectrograph resolves individual absorption features ([Figure 30](fig30_radiation_solar_lines)). Its horizontal coordinate is detector pixel number. Some features come from absorption by molecules in the Earth's atmosphere. The two gaps around pixels $2100$ and $4400$ occur where the instrument switches between detectors.[^ch07_apogee]

```{figure} _static/_chapter07/fig29_solar_spectrum.png
:width: 76%
:align: center
:name: fig29_radiation_solar_spectrum

**Figure 29** Solar spectral irradiance and an illustrative blackbody reference curve. The reference temperature marked in the figure belongs to that comparison curve.
```

```{figure} _static/_chapter07/fig30_solar_absorption_lines.png
:width: 87%
:align: center
:name: fig30_radiation_solar_lines

**Figure 30** First-light solar spectrum from APOGEE, shown as detector counts versus pixel number. The infrared spectrum contains many narrow absorption features. Credit APOGEE/SDSS.
```

## Definitions of temperature

In astrophysics, temperatures can be inferred from total emitted power, radiance at one frequency, particle speeds, or population ratios. They describe distinct measurements and can take different values in an atmosphere.[^ch07_temperatures]

### Effective temperature

The **effective temperature** $T_{\rm eff}$ is the temperature of a blackbody emitting the same bolometric flux $F_{\rm bol}$ per unit surface area as the star,

$$
\boxed{F_{\rm bol}=\sigma T_{\rm eff}^4}.
$$

For a spherical star of radius $R$, its luminosity is $L=4\pi R^2\sigma T_{\rm eff}^4$. The effective temperature characterizes the total power even if the observed spectrum differs substantially from the Planck distribution. [Figure 31](fig31_radiation_solar_bolometric_irradiance) compares two spectra normalized to have equal wavelength integrals. The plotted irradiance is measured outside the Earth's atmosphere at the Earth's orbital distance. To relate it to the solar surface flux one must account for geometrical dilution.

```{figure} _static/_chapter07/fig31_solar_bolometric_irradiance.png
:width: 74%
:align: center
:name: fig31_radiation_solar_bolometric_irradiance

**Figure 31** Extraterrestrial solar spectral irradiance and a blackbody curve with the same integrated irradiance. The curves use historical reference values of $5777\ \mathrm{K}$ and $1367\ \mathrm{W\,m^{-2}}$. Credit Sch, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). [Original plot](https://commons.wikimedia.org/wiki/File:EffectiveTemperature_300dpi_e.png).
```

### Brightness temperature

The **brightness temperature** $T_{\rm b}(\nu)$ is the temperature a blackbody would need to have to reproduce the measured specific intensity at frequency $\nu$,

$$
I_\nu=B_\nu\bigl(T_{\rm b}(\nu)\bigr).
$$

One can define it equivalently using $I_\lambda$ at the corresponding wavelength. In radio astronomy the Rayleigh–Jeans approximation often gives $T_{\rm b}\simeq c^2 I_\nu/(2k\nu^2)$. A stellar flux density measured at Earth combines radiation over the apparent solid angle of the star. Recovering a brightness temperature from it also requires information about that solid angle. A non-Planckian spectrum generally gives a different brightness temperature at each frequency.

### Kinetic, excitation, and ionization temperatures

The **kinetic temperature** $T_{\rm K}$ of a nonrelativistic gas is related to the mean translational kinetic energy of its particles. In three dimensions,

$$
\frac{1}{2}m\langle v^2\rangle=\frac{3}{2}kT_{\rm K},
$$

where the speeds are measured relative to the mean motion of the gas. The mean squared speed $\langle v^2\rangle$ determines the energy.

The **excitation temperature** $T_{\rm exc}$ describes the ratio of the populations $n_2$ and $n_1$ of two energy levels in the same ionization stage. Using the form of the Boltzmann distribution,

$$
\frac{n_2}{n_1}=\frac{g_2}{g_1}
\exp\!\left[-\frac{E_2-E_1}{kT_{\rm exc}}\right],
$$

where $g_1$ and $g_2$ are the statistical weights of the levels. The **ionization temperature** $T_{\rm ion}$ is obtained by comparing populations of successive ionization stages with the **Saha equation**. At a specified electron density, the temperature determines the equilibrium ionization ratio for a given element. The ratio also depends on the ionization energy and the internal states of the two stages.

In complete thermodynamic equilibrium, the gas, atomic populations, and radiation field share the same temperature. **Local thermodynamic equilibrium** (LTE) is a statement about the local state of the material. Its collisions and other interactions can maintain populations consistent with the local kinetic temperature even when the radiation crosses layers at different temperatures. The effective temperature of a star characterizes the total surface flux, and its brightness temperatures characterize the emerging radiation at individual frequencies.[^ch07_populations]

## The basic equation of radiative transfer

The radiation received by an observer depends on what the medium along the ray absorbs and emits. Consider a cylinder of length $dr$ and cross-sectional area $dA$ perpendicular to the ray ([Figure 32](fig32_radiation_transfer_element)). Here the coordinate $r$ increases along the direction of propagation. The specific intensity $I_\nu$ describes the beam within the frequency interval $d\nu$ and the solid angle $d\omega$.[^ch07_transfer]

```{figure} _static/_chapter07/fig32_radiative_transfer_element.png
:width: 49%
:align: center
:name: fig32_radiation_transfer_element

**Figure 32** A volume element along a ray. Radiation propagates through the cylindrical element within the solid angle $d\omega$.
```

Let $\alpha_\nu$ be the absorption coefficient per unit length, in $\mathrm{m^{-1}}$, and let $j_\nu$ be the emission coefficient per unit volume, frequency, and solid angle, in $\mathrm{W\,m^{-3}\,Hz^{-1}\,sr^{-1}}$. In time $dt$, the contributions from absorption and emission are

$$
\begin{aligned}
dE_{\rm abs} &=\alpha_\nu I_\nu\,dr\,dA\,d\nu\,d\omega\,dt,\\
dE_{\rm em}  &=j_\nu\,dr\,dA\,d\nu\,d\omega\,dt.
\end{aligned}
$$

Substituting these in $dE=dE_{\rm em}-dE_{\rm abs}$ gives

$$
\boxed{\frac{dI_\nu}{dr}=-\alpha_\nu I_\nu+j_\nu}.
$$

If scattering matters, the loss coefficient must include scattering out of the beam, and the source term must account for scattering into it. For the absorption and emission case, define the **source function** $S_\nu$ and the **optical depth** measured from the point $r_0$ where the ray enters the medium,

$$
S_\nu=\frac{j_\nu}{\alpha_\nu},
\qquad
d\tau_\nu=\alpha_\nu\,dr,
\qquad
\tau_\nu(r)=\int_{r_0}^{r}\alpha_\nu(r')\,dr'.
$$

The source function has the units of specific intensity, while optical depth is dimensionless. Wherever $\alpha_\nu>0$, the transfer equation becomes

$$
\boxed{\frac{dI_\nu}{d\tau_\nu}=-I_\nu+S_\nu}.
$$

### The formal solution and optical depth

Let $I_\nu(0)$ be the incident background intensity. Write the equation as $dI_\nu/d\tau_\nu+I_\nu=S_\nu$ and multiply by $e^{\tau_\nu}$. The left-hand side is then the derivative of $e^{\tau_\nu}I_\nu$. Integrating gives

$$
\boxed{
I_\nu(\tau_\nu)=I_\nu(0)e^{-\tau_\nu}
+\int_0^{\tau_\nu} S_\nu(t)e^{-(\tau_\nu-t)}\,dt
}.
$$

The first term is the attenuated background. The second term adds up contributions from the medium, each attenuated over the remaining path to the observer. In a uniform slab with constant $S_\nu$, the result reduces to

$$
I_\nu(\tau_\nu)=I_\nu(0)e^{-\tau_\nu}
+S_\nu\bigl(1-e^{-\tau_\nu}\bigr).
$$

- **Optically thin, $\tau_\nu\ll1$.** To first order, $I_\nu\simeq I_\nu(0)+\tau_\nu[S_\nu-I_\nu(0)]$. If there is a bright background and the slab emits little, the background dominates with a small, potentially wavelength-dependent attenuation. If there is no background, the emission of the slab is the whole signal, even when the optical depth is small.
- **Optically thick, $\tau_\nu\gg1$.** The incident background is exponentially suppressed. With constant $S_\nu$, the emerging intensity approaches $S_\nu$. With a varying source function, the main contribution comes from a layer within roughly one optical depth of the observer-facing surface. Optical thickness alone gives no information about whether the medium is in thermodynamic equilibrium.

Fog over the Golden Gate Bridge provides a visible-light example ([Figure 33](fig33_radiation_bridge_fog)). Lights along a nearly clear line of sight remain distinct, whereas denser fog obscures them and adds diffuse light by scattering. The distance to a light and the amount of fog along the ray both affect its visibility.

```{figure} _static/_chapter07/fig33_bridge_in_fog.png
:width: 82%
:align: center
:name: fig33_radiation_bridge_fog

**Figure 33** The Golden Gate Bridge in fog. Direct light is increasingly obscured along paths with greater optical depth.
```

### Balance, absorption, and emission along a ray

The transfer equation shows how the intensity changes wherever the opacity is positive.

- **$I_\nu=S_\nu$.** The gain and loss terms balance, so the local derivative is zero. In a transparent path the derivative is also zero because there is no appreciable interaction. This is how the continuum in case A of [Figure 14](fig14_radiation_spectral_geometry) reaches the observer unchanged.
- **$I_\nu>S_\nu$.** The intensity decreases along the ray. In case B, a cooler gas in front of a bright continuum has $S_\nu<I_\nu$ in the line. The increase in opacity at the line frequency makes the attenuation stronger there.
- **$I_\nu<S_\nu$.** The intensity increases along the ray. This occurs at the line frequencies in case C, where the hot gas has little background to compete with its emission. A thin gas can produce an emission line even while the emerging intensity remains well below $S_\nu$.

### The source function in thermal equilibrium

In thermodynamic equilibrium, detailed balance gives an isotropic Planck radiation field and a thermal source function. With LTE populations and thermal emission and absorption, **Kirchhoff's law** gives

$$
\boxed{
j_\nu=\alpha_\nu B_\nu(T_{\rm K}),
\qquad
S_\nu=B_\nu(T_{\rm K})
}.
$$

This relation can hold locally even if the ray intensity differs from the local Planck function. If scattering contributes appreciably, the total source function also depends on the radiation incident from other directions. Outside LTE, a positive source function can be expressed as $S_\nu=B_\nu(T_{\rm S})$ at a given frequency, thereby defining a **source-function temperature** $T_{\rm S}$. For an isolated bound–bound line with matching emission and absorption profiles, the two level populations give $S_{\nu_0}=B_{\nu_0}(T_{\rm exc})$ at the line centre $\nu_0$. The excitation temperature then gives the line source function even if it differs from the kinetic temperature of the gas.[^ch07_source_function]

## References

- **Barbieri, C., and Bertini, I. (2021)**, *Fundamentals of Astronomy*, 2nd ed., §§16.4 and 16.11, printed pp. 252–254 and 268–270 (PDF pp. 271–273 and 287–289), and §§17.2–17.4, printed pp. 277–287 (PDF pp. 296–306).
- **Hanslmeier, A. (2023)**, *Introduction to Astronomy and Astrophysics*, §§5.6.1–5.6.3, printed pp. 147–152 (PDF pp. 166–171), §8.4, printed pp. 317–318 (PDF pp. 334–335), and §§9.2–9.5, printed pp. 345–364 (PDF pp. 361–380).
- **Karttunen, H., et al. (eds., 2017)**, *Fundamental Astronomy*, 6th ed., Chapter 5, printed pp. 103–118 (PDF pp. 115–130).
- **Seeds, M. A., and Backman, D. E. (2026)**, *Foundations of Astronomy*, 15th ed., §6-1 and §§7-1–7-3. The examples of Orion, the Sun, and a human body are in §7-2, printed pp. 140–143 (PDF pp. 161–164).
- **Condon, J. J., and Ransom, S. M. (2016)**, *Essential Radio Astronomy*, Chapters 2, 4, and 7. [NRAO online edition](https://www.cv.nrao.edu/~sransom/web/).

[^ch07_light]: Seeds and Backman (2026), §6-1, printed pp. 108–110 (PDF pp. 129–131). For the silicon detector in Figure 3, see [Florida State University, Anatomy of a Charge-Coupled Device](https://micro.magnet.fsu.edu/primer/digitalimaging/concepts/ccdanatomy.html).

[^ch07_constants]: [NIST, 2022 CODATA recommended values](https://www.physics.nist.gov/cuu/pdf/wall_2022.pdf), for $c$, $h$, $k$, the Stefan–Boltzmann constant, and the wavelength form of Wien's constant.

[^ch07_spectrum]: Hanslmeier (2023), §5.6.1, printed pp. 147–148 (PDF pp. 166–167). [NASA Science, The Electromagnetic Spectrum](https://science.nasa.gov/asset/webb/the-electromagnetic-spectrum-with-hubble-webb-and-spitzer-highlights/).

[^ch07_atom]: Karttunen et al. (2017), §§5.1–5.2, printed pp. 103–107 (PDF pp. 115–119), for the Bohr model and hydrogen energy levels.

[^ch07_hydrogen]: Karttunen et al. (2017), §5.2, printed pp. 104–107 (PDF pp. 116–119). [NIST, Atomic Data for Hydrogen](https://physics.nist.gov/PhysRefData/Handbook/Tables/hydrogentable1_a.htm) gives the ground-state ionization energy of $13.598433\ \mathrm{eV}$ and links to observed wavelengths.

[^ch07_lines]: Karttunen et al. (2017), §§5.1–5.4, printed pp. 103–111 (PDF pp. 115–123). Barbieri and Bertini (2021), §§17.2–17.3, printed pp. 277–285 (PDF pp. 296–304), discuss line formation and the processes connecting discrete states.

[^ch07_continua]: Karttunen et al. (2017), §5.6, printed p. 111 (PDF p. 123), and Hanslmeier (2023), §9.4, printed pp. 357–358 (PDF pp. 373–374). For the thermal free–free spectrum see [Condon and Ransom, Free–Free Radiation](https://www.cv.nrao.edu/~sransom/web/Ch4.html).

[^ch07_spectra]: Seeds and Backman (2026), §7-3 and the diagrams on PDF pp. 166–167. Hanslmeier (2023), §5.6.3, printed pp. 150–152 (PDF pp. 169–171).

[^ch07_molecules]: Karttunen et al. (2017), §5.5, printed p. 111 (PDF p. 123), for rotational, vibrational, and electronic transitions. See also [Condon and Ransom, Spectral Lines](https://www.cv.nrao.edu/~sransom/web/Ch7.html).

[^ch07_compton]: [Compton, A. H. (1923), A Quantum Theory of the Scattering of X-rays by Light Elements](https://journals.aps.org/pr/abstract/10.1103/PhysRev.21.483). For scattering in astrophysical media, see Hanslmeier (2023), §9.4.2, printed pp. 357–358 (PDF pp. 373–374).

[^ch07_deuterium]: Hanslmeier (2023), §9.5, printed pp. 361–364 (PDF pp. 377–380), for line broadening. See [Deglr6328, Deuterium lamp spectrum and measurement notes](https://commons.wikimedia.org/wiki/File:Deuterium_lamp_1.png) for the plot, its detector response, and saturation of the strongest features.

[^ch07_blackbody]: Karttunen et al. (2017), §5.7, printed pp. 111–114 (PDF pp. 123–126). Barbieri and Bertini (2021), §§16.4 and 16.11, printed pp. 252–254 and 268–270 (PDF pp. 271–273 and 287–289).

[^ch07_wien]: Barbieri and Bertini (2021), §16.4, printed pp. 252–254 (PDF pp. 271–273), for the $5778\ \mathrm{K}$ solar temperature example and the two forms of the displacement law. [IAU 2015 Resolution B3](https://arxiv.org/abs/1510.07674) adopts nominal values of $5772\ \mathrm{K}$ and $1361\ \mathrm{W\,m^{-2}}$ for solar effective temperature and total solar irradiance, respectively.

[^ch07_thermal_imaging]: Seeds and Backman (2026), §7-2, printed p. 143 (PDF p. 164), uses $310\ \mathrm{K}$ as a representative body temperature in the same infrared imaging example. [NASA Science, Infrared Waves](https://science.nasa.gov/ems/07_infraredwaves/).

[^ch07_orion]: Seeds and Backman (2026), §7-2, printed p. 140 (PDF p. 161), contrasts Betelgeuse and Rigel. The illustrative temperatures of the three stars are tabulated in [NASA Space Math, Sensors and the Electromagnetic Spectrum, Table 24](https://spacemath.gsfc.nasa.gov/Sensor/SensorsBook.pdf). See also the atmosphere analyses by [Lobel and Dupree (2000), Betelgeuse](https://simbad.idia.ac.za/simbad/sim-ref?bibcode=2000ApJ...545..454L), [Przybilla et al. (2006), Rigel](https://www.aanda.org/articles/aa/pdf/2006/03/aa3832-05.pdf), and [Crowther et al. (2006), Saiph, Table 3](https://www.aanda.org/articles/aa/pdf/2006/04/aa3685-05.pdf). The Rigel analysis derives $12\,000\pm200\ \mathrm{K}$.

[^ch07_stellar_spectra]: Hanslmeier (2023), §§9.3–9.4, printed pp. 349–358 (PDF pp. 365–374), for formation of continuum and lines in a stellar atmosphere.

[^ch07_apogee]: [SDSS, APOGEE observes the Sun](https://sdss3.wordpress.com/2011/01/22/apogee-observes-the-sun/), for the original first-light infrared spectrum.

[^ch07_temperatures]: Karttunen et al. (2017), §5.8, printed pp. 114–116 (PDF pp. 126–128), and Hanslmeier (2023), §8.4, printed pp. 317–318 (PDF pp. 334–335). See [Condon and Ransom, Radiation Fundamentals](https://www.cv.nrao.edu/~sransom/web/Ch2.html) for the radio definition of brightness temperature.

[^ch07_populations]: Hanslmeier (2023), §9.2, printed pp. 345–349 (PDF pp. 361–365), and Barbieri and Bertini (2021), §§17.3–17.4, printed pp. 281–287 (PDF pp. 300–306), for statistical equilibrium, excitation, and ionization.

[^ch07_transfer]: Karttunen et al. (2017), §5.10, printed pp. 117–118 (PDF pp. 129–130), and Hanslmeier (2023), §9.3, printed pp. 349–356 (PDF pp. 365–372). Here optical depth increases in the direction of propagation. An atmospheric depth coordinate may instead increase inwards from the surface.

[^ch07_source_function]: Hanslmeier (2023), §9.3, printed pp. 349–356 (PDF pp. 365–372), and [Condon and Ransom, Spectral Lines](https://www.cv.nrao.edu/~sransom/web/Ch7.html), for the relation between a line source function and its excitation temperature.
