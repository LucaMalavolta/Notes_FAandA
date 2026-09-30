"""Reproduce the original Chapter 2 diagrams. Run with Python, NumPy and Matplotlib.
Topic/slide mapping is documented in chapter02_transformation_of_coordinates.md.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

OUT = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN, PURPLE = '#245b91', '#d07823', '#32856b', '#8154a3'
plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'axes.labelsize': 12,
                     'figure.facecolor': 'white', 'axes.spines.top': False,
                     'axes.spines.right': False, 'savefig.dpi': 200,
                     'mathtext.fontset': 'dejavusans'})
PHI = 45.40643

def save(fig, name):
    fig.savefig(OUT / name, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def arrow(ax, xy, color='black', label=None, origin=(0, 0), text_offset=(0, 0)):
    ax.annotate('', xy=xy, xytext=origin,
                arrowprops=dict(arrowstyle='->', lw=2, color=color))
    if label:
        ax.text(xy[0]+text_offset[0], xy[1]+text_offset[1], label,
                color=color, ha='center', va='center')

def flat(ax):
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_xlim(-1.35, 1.4); ax.set_ylim(-1.25, 1.4)

def horiz(delta, hour, phi=PHI):
    p, d, t = np.deg2rad(phi), np.deg2rad(delta), np.deg2rad(hour*15)
    up = np.sin(p)*np.sin(d)+np.cos(p)*np.cos(d)*np.cos(t)
    east = -np.cos(d)*np.sin(t)
    north = np.cos(p)*np.sin(d)-np.sin(p)*np.cos(d)*np.cos(t)
    return np.arcsin(np.clip(up,-1,1)), (np.arctan2(east,north)-np.pi)%(2*np.pi)

# 1. Changing axes, and longitude/latitude as Cartesian components.
fig = plt.figure(figsize=(11,4.8),layout='constrained')
a = fig.add_subplot(121); flat(a)
a.set_title('A fixed point, two sets of axes')
chi=np.deg2rad(30)
for v,lab in [((1.1,0),'$x$'),((0,1.1),'$y$')]:arrow(a,v,BLUE,lab,text_offset=(.07,.06))
for v,lab in [((1.1*np.cos(chi),1.1*np.sin(chi)),"$x'$"),((-1.1*np.sin(chi),1.1*np.cos(chi)),"$y'$")]:arrow(a,v,ORANGE,lab,text_offset=(.05,.08))
a.add_patch(Arc((0,0),.8,.8,theta1=0,theta2=30,color=ORANGE,lw=2));a.text(.45,.12,'$\\chi$',color=ORANGE)
a.plot(.75,.85,'o',color=PURPLE); a.text(.79,.92,'$P$',color=PURPLE)
a.plot([0,.75],[0,.85],color=PURPLE,lw=2);a.text(-.13,-.15,'$O$')
a.text(0,-.62,'Axes rotate by $+\\chi$;\ncomponents transform with $R_z(\\chi)$.',ha='center')
b = fig.add_subplot(122,projection='3d');b.set_title('Longitude and latitude')
L,B=np.deg2rad([38,32]);r=np.array([np.cos(B)*np.cos(L),np.cos(B)*np.sin(L),np.sin(B)])
for v,lab in [(np.array([1.2,0,0]),'$x$'),(np.array([0,1.2,0]),'$y$'),(np.array([0,0,1.2]),'$z$')]:
    b.quiver(0,0,0,*v,color=BLUE,arrow_length_ratio=.08);b.text(*v,lab)
b.plot([0,r[0]],[0,r[1]],[0,r[2]],color=PURPLE,lw=2);b.scatter(*r,color=PURPLE);b.text(*(r+.04),'$P$')
b.plot([r[0],r[0]],[r[1],r[1]],[0,r[2]],'--',color='gray')
b.plot([0,r[0]],[0,r[1]],[0,0],color='gray')
u=np.linspace(0,L,60);b.plot(.4*np.cos(u),.4*np.sin(u),0*u,color=ORANGE,lw=2);b.text(.4,.15,0,'$L$')
u=np.linspace(0,B,60);b.plot(.6*np.cos(u)*np.cos(L),.6*np.cos(u)*np.sin(L),.6*np.sin(u),color=GREEN,lw=2);b.text(.53,.44,.2,'$B$')
b.set(xlim=(0,1.25),ylim=(0,1.25),zlim=(0,1.25));b.set_box_aspect((1,1,1));b.view_init(25,-120);b.set_axis_off()
save(fig,'fig01_rotated_axes.png')

# 2. Equatorial/ecliptic cross-section: looking towards the origin from +x.
fig,a=plt.subplots(figsize=(7,6),layout='constrained');flat(a)
e=np.deg2rad(23.44)
a.add_patch(Circle((0,0),1,fill=False,color='#dddddd'))
for v,lab,c in [((1.12,0),'$y_{eq}$',BLUE),((0,1.12),'$z_{eq}$ (NCP)',BLUE),((1.12*np.cos(e),1.12*np.sin(e)),'$y_{ecl}$',ORANGE),((-1.12*np.sin(e),1.12*np.cos(e)),'$z_{ecl}$ (NEP)',ORANGE)]:arrow(a,v,c,lab,text_offset=(.03,.10))
a.add_patch(Arc((0,0),.9,.9,theta1=0,theta2=23.44,color=ORANGE,lw=2));a.text(.49,.08,'$\\epsilon$')
a.add_patch(Arc((0,0),1.3,1.3,theta1=90,theta2=113.44,color=ORANGE,lw=2));a.text(-.15,.73,'$\\epsilon$')
a.plot(0,0,'o',color='black');a.text(.05,-.17,'$x_{eq}=x_{ecl}$ toward $\\gamma$\n(out of the page)',ha='left')
a.text(0,-.78,'Equatorial to ecliptic: $R_x(+\\epsilon)$\nEcliptic to equatorial: $R_x(-\\epsilon)$',ha='center',linespacing=1.8)
a.set_title('A rotation about the vernal direction')
save(fig,'fig02_equatorial_ecliptic.png')

# 3. Local meridian section; east axis into page.
fig,a=plt.subplots(figsize=(8,6),layout='constrained');flat(a)
p=np.deg2rad(PHI)
a.add_patch(Circle((0,0),1,fill=False,color='#bbbbbb'))
a.plot([-1.15,1.15],[0,0],color=BLUE,lw=2);a.text(-1.2,0,'S',ha='right');a.text(1.2,0,'N')
arrow(a,(0,1.1),BLUE,'Zenith',text_offset=(0,.1))
P=np.array([np.cos(p),np.sin(p)]);Q=np.array([-np.sin(p),np.cos(p)])
arrow(a,tuple(P),PURPLE,'NCP',text_offset=(.13,.08))
a.plot([-P[0],P[0]],[-P[1],P[1]],'--',color=PURPLE)
a.plot([-Q[0],Q[0]],[-Q[1],Q[1]],color=ORANGE,lw=2)
a.text(Q[0]-.06,Q[1]+.08,'Equator',ha='right',color=ORANGE)
a.add_patch(Arc((0,0),.75,.75,theta1=0,theta2=PHI,color=PURPLE,lw=2));a.text(.42,.15,'$\\phi$')
a.add_patch(Arc((0,0),1.25,1.25,theta1=PHI,theta2=90,color=GREEN,lw=2));a.text(.19,.68,'$90°-\\phi$',color=GREEN)
a.text(-.10,-.17,'$O$');a.text(0,-1.2,'The horizon and equator share the East–West line.',ha='center')
a.set_title('The local sky in the meridian plane')
save(fig,'fig03_horizontal_equatorial.png')

# 4. Schematic equatorial clock, using the sidereal times shown in slides 10-12.
fig,axes=plt.subplots(1,3,figsize=(13,4.4),layout='constrained')
alpha=18+38/60+10/3600
for a,st in zip(axes,[18,alpha,20+40/60]):
    flat(a);a.add_patch(Circle((0,0),1,fill=False,color='#bbbbbb'))
    for h in [0,6,12,18]:
        ang=h*np.pi/12;a.text(1.17*np.cos(ang),1.17*np.sin(ang),f'{h} h',ha='center',va='center',fontsize=10)
    ang=alpha*np.pi/12;mer=st*np.pi/12
    arrow(a,(np.cos(ang),np.sin(ang)),PURPLE)
    arrow(a,(.9*np.cos(mer),.9*np.sin(mer)),ORANGE)
    a.plot(np.cos(ang),np.sin(ang),'o',color=PURPLE)
    ts=np.linspace(min(ang,mer),max(ang,mer),50);a.plot(.55*np.cos(ts),.55*np.sin(ts),color=GREEN,lw=2)
    h=st-alpha
    a.set_title(f'$\\Theta$ = {int(st):02d} h {int(round((st%1)*60))%60:02d} min'+(' 10 s' if st==alpha else ''))
    a.text(0,-1.48,f'$t$ = {h:+.3f} h\n'+('Before transit' if h<0 else 'Upper transit' if h==0 else 'After transit'),ha='center')
fig.suptitle('Equator viewed from the North Celestial Pole\nPurple: fixed stellar right ascension; orange: local upper meridian',fontsize=14)
save(fig,'fig04_sidereal_time.png')

# 5. Parallel stellar reference versus changing solar direction, deliberately exaggerated.
fig,axes=plt.subplots(1,3,figsize=(12,4.5),layout='constrained')
for i,a in enumerate(axes):
    a.set_aspect('equal');a.axis('off');a.set_xlim(-1.55,1.55);a.set_ylim(-1.2,1.3)
    a.add_patch(Circle((0,0),.44,color='#dce8f2',ec=BLUE,lw=1.5))
    solar=0 if i==0 else np.deg2rad(25)
    mer=solar if i==2 else 0
    arrow(a,(1.25,0),PURPLE,'Distant star',text_offset=(0,.13))
    arrow(a,(1.25*np.cos(solar),1.25*np.sin(solar)),ORANGE,'Sun',text_offset=(0,.12 if i else -.18))
    arrow(a,(.64*np.cos(mer),.64*np.sin(mer)),BLUE)
    if i==1:
        a.add_patch(Arc((0,0),1.6,1.6,theta1=0,theta2=25,color=ORANGE));a.text(.85,.17,'$\\Delta\\theta$')
    a.set_title(['Initial solar and stellar transit','After one sidereal rotation','After one solar day'][i],fontsize=12)
    a.text(0,-.85,['Both reference directions coincide.','The star has returned;\nthe Sun is still east of the meridian.','An additional rotation brings\nthe Sun back to the meridian.'][i],ha='center',fontsize=11)
fig.suptitle('Why the solar day is longer\nChanging solar direction exaggerated; blue arrow marks the local meridian',fontsize=14)
save(fig,'fig05_solar_sidereal_day.png')

# 6. Diurnal paths, including one never-rising star.
fig=plt.figure(figsize=(12,5.3),layout='constrained');a=fig.add_subplot(121);b=fig.add_subplot(122,projection='polar')
hours=np.linspace(-12,12,2401)
for d,c in [(-60,BLUE),(0,ORANGE),(20,GREEN),(60,PURPLE)]:
    alt,az=horiz(d,hours);a.plot(hours,np.rad2deg(alt),color=c,label=f'$\\delta={d}°$')
    mask=alt>=0;b.plot(az,np.where(mask,90-np.rad2deg(alt),np.nan),color=c,lw=2)
a.axhline(0,color='black',lw=1);a.set(xlim=(-12,12),ylim=(-90,90),xlabel='Hour angle (sidereal hours)',ylabel='Altitude (degrees)',title='A full sidereal day');a.grid(alpha=.2);a.legend(ncol=2,fontsize=10)
b.set_theta_zero_location('S');b.set_theta_direction(-1);b.set_ylim(0,90);b.set_yticks([30,60,90],['60°','30°','0°']);b.set_xticks(np.deg2rad([0,90,180,270]),['S','W','N','E']);b.set_title('Visible paths above the horizon',pad=22);b.set_rlabel_position(135)
fig.suptitle(f'Diurnal motion at Padova ($\\phi={PHI:.2f}°$)',fontsize=15)
save(fig,'fig06_diurnal_paths.png')

# 7. Visibility as a function of latitude and declination.
fig,a=plt.subplots(figsize=(9,6),layout='constrained')
p=np.linspace(-89.99,89.99,500);d=np.linspace(-89.99,89.99,500);P,D=np.meshgrid(p,d)
upper=90-np.abs(P-D);lower=np.abs(P+D)-90
kind=np.where(lower>0,2,np.where(upper<0,0,1))
from matplotlib.colors import ListedColormap
a.pcolormesh(P,D,kind,cmap=ListedColormap(['#d4d8df','#dfefe9','#e4d7ef']),shading='auto')
for sign in [-1,1]:a.plot(p,sign*(90-np.abs(p)),color='white',lw=1.5)
a.text(48,64,'Always above',ha='center',color=PURPLE);a.text(-48,-64,'Always above',ha='center',color=PURPLE)
a.text(-48,64,'Never rises',ha='center');a.text(48,-64,'Never rises',ha='center');a.text(0,0,'Rises and sets',ha='center')
a.axvline(PHI,color=BLUE,ls='--',lw=1.3);a.text(PHI+2,-5,'Padova',rotation=90,color=BLUE)
a.set(xlim=(-90,90),ylim=(-90,90),xlabel='Observer latitude $\\phi$ (degrees)',ylabel='Stellar declination $\\delta$ (degrees)',title='Geometric visibility in both hemispheres');a.set_xticks(np.arange(-90,91,30));a.set_yticks(np.arange(-90,91,30))
save(fig,'fig07_visibility.png')

# 8. Sun tracks and geometric daylight length.
fig,axes=plt.subplots(1,2,figsize=(12,5),layout='constrained')
for d,c,lab in [(23.44,ORANGE,'June solstice'),(0,GREEN,'Equinoxes'),(-23.44,BLUE,'December solstice')]:
    h=np.linspace(-12,12,1500);alt,az=horiz(d,h);good=alt>=0
    solar_A = (np.rad2deg(az[good])+180)%360-180
    axes[0].plot(solar_A,np.rad2deg(alt[good]),color=c,lw=2,label=lab)
axes[0].set(xlim=(-180,180),ylim=(0,90),xlabel='Azimuth from South through West (degrees)',ylabel='Solar altitude (degrees)',title='Daily paths at Padova');axes[0].set_xticks([-180,-90,0,90,180],['N\n180','E\n270','S\n0','W\n90','N\n180']);axes[0].legend(fontsize=10);axes[0].grid(alpha=.2)
lam=np.linspace(0,360,721);dec=np.arcsin(np.sin(np.deg2rad(23.44))*np.sin(np.deg2rad(lam)))
t0=np.arccos(-np.tan(np.deg2rad(PHI))*np.tan(dec));day=24*t0/np.pi
axes[1].plot(lam,day,color=PURPLE,lw=2);axes[1].set(xlim=(0,360),ylim=(7,17),xlabel='Solar ecliptic longitude (degrees)',ylabel='Approximate daylight (mean solar hours)',title='Annual variation of daylight');axes[1].set_xticks([0,90,180,270,360]);axes[1].grid(alpha=.2)
save(fig,'fig08_solar_paths.png')

# 9. Coordinate rates near an almost zenith transit (no exact singular point plotted).
fig,axes=plt.subplots(1,3,figsize=(14,4.8),layout='constrained')
h=np.linspace(-1,1,4001);p=np.deg2rad(PHI)
for d,c in [(20,BLUE),(44,ORANGE),(46,PURPLE)]:
    alt,az=horiz(d,h);adot=-15*np.cos(p)*np.sin(az);Adot=15*(np.sin(p)+np.cos(p)*np.cos(az)*np.tan(alt))
    for ax,y in zip(axes,[np.rad2deg(alt),adot,Adot]):ax.plot(h,y,color=c,label=f'$\\delta={d}°$',lw=1.7)
for ax,title,ylab in zip(axes,['Altitude near transit','Altitude rate','Azimuth rate'],['Altitude (degrees)','Degrees per sidereal hour','Degrees per sidereal hour']):
    ax.set(xlabel='Hour angle (sidereal hours)',ylabel=ylab,title=title,xlim=(-1,1));ax.grid(alpha=.2)
axes[0].legend(fontsize=10);axes[1].axhline(0,color='gray',lw=.6);axes[2].axhline(0,color='gray',lw=.6)
fig.suptitle(f'Coordinate rates at Padova ($\\phi={PHI:.2f}°$); positive azimuth is South through West',fontsize=14)
save(fig,'fig09_tracking_rates.png')
print('Generated',len(list(OUT.glob('fig*.png'))),'PNG figures')
